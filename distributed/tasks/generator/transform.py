"""Post-hoc URL transformations for differential fuzzing."""

import random
import re

_GROUP = "TRANSFORMATION"

TRANSFORMATIONS = [
    "URL_ENCODING",
    "MULTIPLE_URL_ENCODING",
    "SLASH_NORMALIZATION",
    "DOT_NORMALIZATION",
    "PUNYCODE",
    "OVERLONG_UTF8",
    "LABEL_NORMALIZATION",
    "SLASH_SWITCHING",
    "NULL_INJECTION",
    "DUPLICATE_COMPONENT",
    "DUPLICATE_KEYS_VALUES",
    "SUBSTRING_REINSERTION",
    "NONE",
]

_N = len(TRANSFORMATIONS)
DEFAULT_WEIGHTS = {t: {"weight": 1.0 / _N, "group": _GROUP} for t in TRANSFORMATIONS}


def _url_encode(url: str) -> str:
    # Percent-encode ~30% of ASCII characters. Parsers disagree on whether to
    # decode before splitting on delimiters (%2F, %40, %3F, %23 etc.) or after,
    # causing host/path/query boundaries to land in different places.
    out = []
    for ch in url:
        if ch.isascii() and ch != '%' and random.random() < 0.3:
            out.append(f'%{ord(ch):02X}')
        else:
            out.append(ch)
    return ''.join(out)


def _multiple_url_encode(url: str) -> str:
    # Double (or triple) percent-encode: the first pass encodes chars, the
    # second encodes the resulting % signs to %25. Parsers that decode in a
    # loop (e.g. nginx %25xx → %xx → char) will resolve to different values
    # than single-pass parsers, opening path-traversal and SSRF bypass vectors.
    encoded = _url_encode(url)
    if random.random() < 0.25:
        encoded = _url_encode(encoded)
    return encoded.replace('%', '%25')


def _slash_normalize(url: str) -> str:
    # Inject excess or mixed slashes. Many parsers collapse repeated slashes
    # (http:////host → http://host) but disagree on where — browsers strip them
    # from the authority, proxies may leave them in the path, causing the
    # apparent host to differ between client and server (SSRF, open-redirect).
    # Variants: extra slashes after ://, doubled interior slash, /\ mix, // prefix.
    variant = random.randint(0, 3)
    if variant == 0:
        extra = '/' * random.randint(2, 5)
        return url.replace('://', '://' + extra, 1)
    elif variant == 1:
        return re.sub(r'(?<=[^/])/(?=[^/])', '//', url, count=random.randint(1, 2))
    elif variant == 2:
        return url.replace('/', '/\\', random.randint(1, 2))
    else:
        return '//' + url


def _dot_normalize(url: str) -> str:
    # Insert dot-segment traversal sequences (/../, /./, /.., /..., /.) into
    # the path. Parsers that resolve dot segments before access control checks
    # (RFC 3986 §5.2) will see a different effective path than those that pass
    # raw paths to the filesystem or downstream service — classic path traversal.
    segs = ['/../', '/./', '/..', '/...', '/.']
    seg = random.choice(segs)
    m = re.search(r'(?<=[:/])/[^?#]*', url)
    if m:
        insert_pos = m.start() + random.randint(0, m.end() - m.start())
        return url[:insert_pos] + seg + url[insert_pos:]
    return url + seg


def _punycode(url: str) -> str:
    # Convert unicode hostname labels to ACE/Punycode (xn--...). Parsers that
    # compare hostnames as raw strings will not match the unicode and punycode
    # forms, so allowlist/blocklist checks on one form bypass the other.
    # Only applied when the host actually contains non-ASCII (no-op otherwise).
    m = re.search(r'(://)(?:[^@]*@)?([^/:?#]+)', url)
    if not m:
        return url
    host = m.group(2)
    if not any(ord(c) > 127 for c in host):
        return url
    try:
        labels = host.split('.')
        encoded = '.'.join(
            lbl.encode('idna').decode('ascii') if any(ord(c) > 127 for c in lbl) else lbl
            for lbl in labels
        )
        start = m.start(2)
        return url[:start] + encoded + url[start + len(host):]
    except (UnicodeError, UnicodeDecodeError):
        return url


def _overlong_utf8(url: str) -> str:
    # Re-encode ~15% of ASCII bytes as two-byte overlong UTF-8 sequences
    # (e.g. '/' → 0xC0 0xAF). These are invalid per RFC 3629 but parsers
    # implemented in C that walk raw bytes (rather than decoding first) may
    # accept them, allowing delimiter characters like / ? # @ to slip through
    # validation that operates on the decoded form.
    out = []
    for ch in url:
        cp = ord(ch)
        if ch.isascii() and cp > 0 and random.random() < 0.15:
            out.append(bytes([0xC0 | (cp >> 6), 0x80 | (cp & 0x3F)]).decode('latin-1'))
        else:
            out.append(ch)
    return ''.join(out)


def _label_normalize(url: str) -> str:
    # Replace ASCII dots in the hostname with UTS #46 alternative label
    # separators (U+3002 IDEOGRAPHIC FULL STOP, U+FF0E FULLWIDTH FULL STOP,
    # U+FF61 HALFWIDTH IDEOGRAPHIC FULL STOP). Browsers and IDNA-aware parsers
    # normalise these to '.', while parsers doing a raw byte comparison will
    # see a completely different host string — bypassing host-based ACLs.
    alt_dots = ['\u3002', '\uFF0E', '\uFF61']
    m = re.search(r'(://)(?:[^@]*@)?([^/:?#]+)', url)
    if not m:
        return url
    host_start, host_end = m.start(2), m.end(2)
    host = url[host_start:host_end]
    dot_count = host.count('.')
    if dot_count == 0:
        return url
    host = host.replace('.', random.choice(alt_dots), random.randint(1, dot_count))
    return url[:host_start] + host + url[host_end:]


def _slash_switch(url: str) -> str:
    # Replace forward slashes in the path with backslashes. Windows-native
    # parsers and IIS normalise \ to / before routing; POSIX parsers treat \
    # as a literal path character. A parser that normalises will resolve the
    # request to a different resource than one that does not, enabling
    # path-confusion attacks and WAF bypasses.
    m = re.search(r'://[^/?#]*(.*)', url, re.DOTALL)
    if not m:
        return url.replace('/', '\\', random.randint(1, 3))
    path_start = m.start(1)
    path_part = url[path_start:]
    count = random.randint(1, max(1, path_part.count('/')))
    return url[:path_start] + path_part.replace('/', '\\', count)


def _null_inject(url: str) -> str:
    # Insert 1–3 null bytes (\x00) at random positions. C-string parsers
    # (curl, many CGI stacks) truncate at the first null, so the effective URL
    # they see may be a strict prefix of the full string. Higher-level parsers
    # that treat the URL as a length-delimited byte sequence see the full string,
    # causing host/path disagreement and potential null-byte injection crashes.
    chars = list(url)
    for _ in range(random.randint(1, 3)):
        chars.insert(random.randint(0, len(chars)), '\x00')
    return ''.join(chars)


def _duplicate_component(url: str) -> str:
    # Inject a second scheme+authority after the first (e.g. http://ftp://host/path).
    # Parsers that stop at the first :// see the outer scheme/host; parsers that
    # re-scan or follow redirects may pick up the inner one. This is the classic
    # "scheme confusion" vector that tricks proxies into forwarding to a different
    # host than the one the security layer validated.
    m = re.match(r'([a-zA-Z][a-zA-Z0-9+\-.]*)(://)', url)
    if not m:
        return url
    extra = random.choice(['http', 'ftp', 'https', 'file', m.group(1)])
    return url[:m.end()] + extra + '://' + url[m.end():]


def _substring_reinsertion(url: str) -> str:
    # Cut a random-length slice from a random position and paste it back at a
    # different random position. Moves structural characters (://, @, ?, #, /)
    # out of their expected positions, causing parsers that rely on delimiter
    # order or fixed-offset scanning to misidentify component boundaries entirely.
    if len(url) < 4:
        return url
    start = random.randint(0, len(url) - 2)
    length = random.randint(1, max(1, len(url) - start))
    chunk = url[start:start + length]
    remaining = url[:start] + url[start + length:]
    insert_at = random.randint(0, len(remaining))
    return remaining[:insert_at] + chunk + remaining[insert_at:]


def _duplicate_keys_values(url: str) -> str:
    # Duplicate a random query parameter so the same key appears twice
    # (e.g. ?a=1&b=2&a=1). Parsers disagree on which occurrence wins: some
    # take the first, some the last, some concatenate. This causes the
    # application layer and any security middleware to observe different values
    # for the same parameter, enabling parameter pollution bypasses.
    m = re.search(r'\?([^#]*)', url)
    if not m or not m.group(1):
        return url
    pairs = m.group(1).split('&')
    pairs.append(random.choice(pairs))
    random.shuffle(pairs)
    return url[:m.start(1)] + '&'.join(pairs) + url[m.end(1):]


_TRANSFORM_FNS = {
    "URL_ENCODING":          _url_encode,
    "MULTIPLE_URL_ENCODING": _multiple_url_encode,
    "SLASH_NORMALIZATION":   _slash_normalize,
    "DOT_NORMALIZATION":     _dot_normalize,
    "PUNYCODE":              _punycode,
    "OVERLONG_UTF8":         _overlong_utf8,
    "LABEL_NORMALIZATION":   _label_normalize,
    "SLASH_SWITCHING":       _slash_switch,
    "NULL_INJECTION":        _null_inject,
    "DUPLICATE_COMPONENT":   _duplicate_component,
    "DUPLICATE_KEYS_VALUES":  _duplicate_keys_values,
    "SUBSTRING_REINSERTION":  _substring_reinsertion,
    "NONE":                   lambda url: url,
}


def generate_with_choice(weights=None):
    """Select a transformation using probability weights.

    weights: dict mapping transformation name to {"weight": float, "group": str}
             as returned by _logits_to_probs in generator.py. Pass None for uniform.

    Returns:
        (transform_fn, chosen_key, group)
    """
    w = weights or {}
    keys = list(_TRANSFORM_FNS.keys())
    probs = [w.get(k, {}).get("weight", 1.0 / len(keys)) for k in keys]
    total = sum(probs)
    probs = [p / total for p in probs]
    chosen = random.choices(keys, weights=probs, k=1)[0]
    return _TRANSFORM_FNS[chosen], chosen, _GROUP


def serialize_weights(_weights=None):
    """Return default weight dict for seeding into ParserWeights."""
    return {k: {"weight": v["weight"], "group": _GROUP} for k, v in DEFAULT_WEIGHTS.items()}
