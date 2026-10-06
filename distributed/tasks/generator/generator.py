import math
import sys
import os
import logging

logger = logging.getLogger(__name__)

# Allow this module to be imported from outside its directory while keeping
# the local component imports resolvable.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from scheme import generate as generate_scheme, generate_with_choice as generate_scheme_with_choice, serialize_weights as serialize_scheme_weights
from schemeauthdelim import generate as generate_scheme_auth_delim, generate_with_choice as generate_scheme_auth_delim_with_choice, serialize_weights as serialize_scheme_auth_delim_weights
from username import generate as generate_username, generate_with_choice as generate_username_with_choice, serialize_weights as serialize_username_weights
from userpassdelim import generate as generate_userpass_delim, generate_with_choice as generate_userpass_delim_with_choice, serialize_weights as serialize_userpass_delim_weights
from password import generate as generate_password, generate_with_choice as generate_password_with_choice, serialize_weights as serialize_password_weights
from userinfohostdelim import generate as generate_userinfo_host_delim, generate_with_choice as generate_userinfo_host_delim_with_choice, serialize_weights as serialize_userinfo_host_delim_weights
from host import generate as generate_host, generate_with_choice as generate_host_with_choice, serialize_weights as serialize_host_weights
from hostportdelim import generate as generate_host_port_delim, generate_with_choice as generate_host_port_delim_with_choice, serialize_weights as serialize_host_port_delim_weights
from port import generate as generate_port, generate_with_choice as generate_port_with_choice, serialize_weights as serialize_port_weights
from authpathdelim import generate as generate_auth_path_delim, generate_with_choice as generate_auth_path_delim_with_choice, serialize_weights as serialize_auth_path_delim_weights
from path import generate as generate_path, generate_with_choice as generate_path_with_choice, serialize_weights as serialize_path_weights
from pathquerydelim import generate as generate_path_query_delim, generate_with_choice as generate_path_query_delim_with_choice, serialize_weights as serialize_path_query_delim_weights
from query import generate as generate_query, generate_with_choice as generate_query_with_choice, serialize_weights as serialize_query_weights
from queryfragdelim import generate as generate_query_frag_delim, generate_with_choice as generate_query_frag_delim_with_choice, serialize_weights as serialize_query_frag_delim_weights
from fragment import generate as generate_fragment, generate_with_choice as generate_fragment_with_choice, serialize_weights as serialize_fragment_weights
import transform


_COMPONENTS_WITH_CHOICE = [
    ("scheme",            generate_scheme_with_choice),
    ("schemeauthdelim",   generate_scheme_auth_delim_with_choice),
    ("username",          generate_username_with_choice),
    ("userpassdelim",     generate_userpass_delim_with_choice),
    ("password",          generate_password_with_choice),
    ("userinfohostdelim", generate_userinfo_host_delim_with_choice),
    ("host",              generate_host_with_choice),
    ("hostportdelim",     generate_host_port_delim_with_choice),
    ("port",              generate_port_with_choice),
    ("authpathdelim",     generate_auth_path_delim_with_choice),
    ("path",              generate_path_with_choice),
    ("pathquerydelim",    generate_path_query_delim_with_choice),
    ("query",             generate_query_with_choice),
    ("queryfragdelim",    generate_query_frag_delim_with_choice),
    ("fragment",          generate_fragment_with_choice),
]


def _logits_to_probs(logits_dict: dict) -> dict:
    """Convert a logit-parameterised weight dict to a probability weight dict.

    ParserWeights stores logits so REINFORCE can update in unconstrained space.
    Generation requires probabilities, so softmax is applied per group here.

    Input:  {"p_valid": {"logit": 0.0, "group": "SCHEME"}, ...}
    Output: {"p_valid": {"weight": 0.5, "group": "SCHEME"}, ...}
    """
    groups: dict[str, list[str]] = {}
    for key, spec in logits_dict.items():
        g = spec["group"]
        groups.setdefault(g, []).append(key)

    result = {}
    for group, keys in groups.items():
        logits = [logits_dict[k]["logit"] for k in keys]
        max_l = max(logits)  # numerical stability
        exp_l = [math.exp(l - max_l) for l in logits]
        total = sum(exp_l)
        for key, e in zip(keys, exp_l):
            result[key] = {"weight": e / total, "group": group}
    return result


def generate_n(n):
    '''
    Generate n URLs based on the weights in the database.

    :param n: Number of URLs to generate
    '''
    from core.database import get_session
    from core.models import ParserWeights, ParseJob, JobStatus
    from tasks.parse_url import parse_all

    # 1. Fetch the singleton weights row and convert logits → probabilities
    with get_session() as session:
        weights_row = ParserWeights.get(session)
        if weights_row is None:
            logger.info("No ParserWeights singleton found — seeding with default logits")
            default_w = _serialize_weights()
            seed = {
                component: {
                    k: {"logit": math.log(max(v["weight"], 1e-9)), "group": v["group"]}
                    for k, v in keys.items()
                }
                for component, keys in default_w.items()
            }
            ParserWeights.upsert(session, **seed)
            session.commit()
            prob_weights = {}
        else:
            if weights_row.transformation is None:
                transform_default = transform.serialize_weights()
                weights_row.transformation = {
                    k: {"logit": math.log(max(v["weight"], 1e-9)), "group": v["group"]}
                    for k, v in transform_default.items()
                }
                from sqlalchemy.orm.attributes import flag_modified
                flag_modified(weights_row, "transformation")
                session.commit()

            prob_weights = {
                "scheme":            _logits_to_probs(weights_row.scheme)            if weights_row.scheme            else {},
                "schemeauthdelim":   _logits_to_probs(weights_row.schemeauthdelim)   if weights_row.schemeauthdelim   else {},
                "username":          _logits_to_probs(weights_row.username)          if weights_row.username          else {},
                "userpassdelim":     _logits_to_probs(weights_row.userpassdelim)     if weights_row.userpassdelim     else {},
                "password":          _logits_to_probs(weights_row.password)          if weights_row.password          else {},
                "userinfohostdelim": _logits_to_probs(weights_row.userinfohostdelim) if weights_row.userinfohostdelim else {},
                "host":              _logits_to_probs(weights_row.host)              if weights_row.host              else {},
                "hostportdelim":     _logits_to_probs(weights_row.hostportdelim)     if weights_row.hostportdelim     else {},
                "port":              _logits_to_probs(weights_row.port)              if weights_row.port              else {},
                "authpathdelim":     _logits_to_probs(weights_row.authpathdelim)     if weights_row.authpathdelim     else {},
                "path":              _logits_to_probs(weights_row.path)              if weights_row.path              else {},
                "pathquerydelim":    _logits_to_probs(weights_row.pathquerydelim)    if weights_row.pathquerydelim    else {},
                "query":             _logits_to_probs(weights_row.query)             if weights_row.query             else {},
                "queryfragdelim":    _logits_to_probs(weights_row.queryfragdelim)    if weights_row.queryfragdelim    else {},
                "fragment":          _logits_to_probs(weights_row.fragment)          if weights_row.fragment          else {},
                "transformation":    _logits_to_probs(weights_row.transformation)    if weights_row.transformation    else {},
            }

    # 2. Generate n URLs, recording per-component choices for REINFORCE
    results = [_generate_with_choices(prob_weights) for _ in range(n)]

    # 3. Create jobs (with choices attached) and dispatch parsing.
    #    Choices are stored on the job so the feedback task can read them
    #    by job_id without coupling parse_url to REINFORCE concerns.
    job_ids = []
    for url, choices in results:
        transform_fn, transform_key, transform_group = transform.generate_with_choice(
            prob_weights.get("transformation")
        )
        url = transform_fn(url)
        choices["transformation"] = {"chosen": transform_key, "group": transform_group}
        db_url = url.replace("\x00", "\\x00")  # postgres rejects NUL bytes; store escaped
        with get_session() as session:
            job = ParseJob(
                url=db_url,
                status=JobStatus.PENDING.value,
                generation_choices=choices,
            )
            session.add(job)
            session.flush()
            job_id = job.id
        parse_all.delay(job_id)
        job_ids.append(job_id)

    return job_ids


def _generate_with_choices(weights=None):
    """Generate a URL and return the per-component branch choices.

    Returns:
        (url_string, choices) where choices maps component name to
        {"chosen": key, "group": group_name} for use in REINFORCE.
    """
    w = weights or {}
    parts = []
    choices = {}

    for name, gen_fn in _COMPONENTS_WITH_CHOICE:
        string, chosen_key, group = gen_fn(w.get(name))
        parts.append(string)
        choices[name] = {"chosen": chosen_key, "group": group}

    return "".join(parts), choices


def _generate(weights=None):
    w = weights or {}
    return (
        generate_scheme(w.get("scheme")) +
        generate_scheme_auth_delim(w.get("schemeauthdelim")) +
        generate_username(w.get("username")) +
        generate_userpass_delim(w.get("userpassdelim")) +
        generate_password(w.get("password")) +
        generate_userinfo_host_delim(w.get("userinfohostdelim")) +
        generate_host(w.get("host")) +
        generate_host_port_delim(w.get("hostportdelim")) +
        generate_port(w.get("port")) +
        generate_auth_path_delim(w.get("authpathdelim")) +
        generate_path(w.get("path")) +
        generate_path_query_delim(w.get("pathquerydelim")) +
        generate_query(w.get("query")) +
        generate_query_frag_delim(w.get("queryfragdelim")) +
        generate_fragment(w.get("fragment"))
    )

def _generate_valid():
    weights = {"p_valid": 1, "p_null": 0, "p_invalid": 0}
    return (
        generate_scheme(weights) +
        generate_scheme_auth_delim(weights) +
        generate_username(weights) +
        generate_userpass_delim(weights) +
        generate_password(weights) +
        generate_userinfo_host_delim(weights) +
        generate_host(weights) +
        generate_host_port_delim(weights) +
        generate_port(weights) +
        generate_auth_path_delim(weights) +
        generate_path(weights) +
        generate_path_query_delim(weights) +
        generate_query(weights) +
        generate_query_frag_delim(weights) +
        generate_fragment(weights)
    )

def _serialize_weights(weights=None):
    return {
        "scheme": serialize_scheme_weights(weights),
        "schemeauthdelim": serialize_scheme_auth_delim_weights(weights),
        "username": serialize_username_weights(weights),
        "userpassdelim": serialize_userpass_delim_weights(weights),
        "password": serialize_password_weights(weights),
        "userinfohostdelim": serialize_userinfo_host_delim_weights(weights),
        "host": serialize_host_weights(weights),
        "hostportdelim": serialize_host_port_delim_weights(weights),
        "port": serialize_port_weights(weights),
        "authpathdelim": serialize_auth_path_delim_weights(weights),
        "path": serialize_path_weights(weights),
        "pathquerydelim": serialize_path_query_delim_weights(weights),
        "query": serialize_query_weights(weights),
        "queryfragdelim": serialize_query_frag_delim_weights(weights),
        "fragment": serialize_fragment_weights(weights),
        "transformation": transform.serialize_weights(),
    }

if __name__ == "__main__":
    for _ in range(5):
        print(_generate_valid())

    print("Serialized valid weights:")
    weights = {"p_valid": 1, "p_null": 0, "p_invalid": 0}
    print(_serialize_weights(weights))
