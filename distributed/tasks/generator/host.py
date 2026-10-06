from component import GrammarComponent

# TODO: IPv6 and IPv4

pcfg_template = """
    HOST             -> VALID_HOST [{p_valid}] | INVALID_HOST [{p_invalid}] | 'NULL' [{p_null}]

    IP_ADDRESS       -> VALID_IP [{p_valid_ip}] | INVALID_IP [{p_invalid_ip}]
    VALID_IP         -> IPV4 [{valid_ipv4}] | '[' IPV6 ']' [{valid_ipv6}]
    IPV4             -> DIGITS '.' DIGITS '.' DIGITS '.' DIGITS [1.0]
    IPV6             -> HEXDIGITS ':' HEXDIGITS ':' HEXDIGITS ':' HEXDIGITS ':' HEXDIGITS ':' HEXDIGITS ':' HEXDIGITS ':' HEXDIGITS [1.0]
    DIGITS           -> 'ASCII_DIGITS' [{digits}] | 'ASCII_DIGITS' 'ASCII_DIGITS' [{digits_2}]
    HEXDIGITS        -> 'HEXDIGIT' [{hexdigits}] | 'HEXDIGIT' 'HEXDIGIT' [{hexdigits_2}]
    INVALID_IP       -> INVALID_IP_CHAR INVALID_IP_TAIL [1.0]
    INVALID_IP_TAIL -> INVALID_IP_CHAR INVALID_IP_TAIL [{inv_ip_recurse}] | 'NULL' [{inv_ip_stop}]
    INVALID_IP_CHAR -> 'ASCII_WHITESPACE' [{inv_ip_whitespace}] | 'ASCII_CONTROL' [{inv_ip_control}] | 'UNICODE_VALID' [{inv_ip_unicode}] | 'UNICODE_DISALLOWED' [{inv_ip_disallowed}] | 'UNICODE_UNASSIGNED' [{inv_ip_unassigned}] | 'UNICODE_RESERVED' [{inv_ip_reserved}]

    VALID_HOST       -> VALID_HOST_CHAR VALID_HOST_TAIL [{valid_host}] | VALID_IP [{valid_ip_host}]
    VALID_HOST_TAIL  -> VALID_HOST_CHAR VALID_HOST_TAIL [{valid_recurse}] | 'NULL' [{valid_stop}]
    VALID_HOST_CHAR  -> 'ASCII_LETTERS' [{valid_char_letters}] | 'ASCII_DIGITS' [{valid_char_digits}] | 'HOST_SPECIAL' [{valid_char_host_special}] 

    INVALID_HOST     -> INVALID_HOST_CHAR INVALID_HOST_TAIL [{inv_start_char}] | VALID_HOST_CHAR INVALID_HOST [{inv_start_valid}]
    INVALID_HOST_TAIL -> ANY_CHAR INVALID_HOST_TAIL [{inv_recurse}] | 'NULL' [{inv_stop}]
    INVALID_HOST_CHAR -> 'UNICODE_VALID' [{inv_char_unicode}] | 'ASCII_WHITESPACE' [{inv_char_whitespace}] | 'ASCII_CONTROL' [{inv_char_control}] | 'UNICODE_DISALLOWED' [{inv_char_disallowed}] | 'UNICODE_UNASSIGNED' [{inv_char_unassigned}] | 'UNICODE_RESERVED' [{inv_char_reserved}]

    ANY_CHAR         -> VALID_HOST_CHAR [{any_valid}] | INVALID_HOST_CHAR [{any_invalid}]
"""

DEFAULT_WEIGHTS = {
    "p_valid": { "weight": 0.6, "grouping": "HOST" },
    "p_invalid": { "weight": 0.3, "grouping": "HOST" },
    "p_null": { "weight": 0.1, "grouping": "HOST" },

    "valid_ip_host": { "weight": 0.5, "grouping": "VALID_HOST" },
    "valid_host": { "weight": 0.5, "grouping": "VALID_HOST" },

    "valid_recurse": { "weight": 0.95, "grouping": "VALID_HOST_TAIL" },
    "valid_stop": { "weight": 0.05, "grouping": "VALID_HOST_TAIL" },

    "valid_char_letters": { "weight": 0.4, "grouping": "VALID_HOST_CHAR" },
    "valid_char_digits": { "weight": 0.4, "grouping": "VALID_HOST_CHAR" },
    "valid_char_host_special": { "weight": 0.2, "grouping": "VALID_HOST_CHAR" },

    "p_valid_ip": { "weight": 0.9, "grouping": "IP_ADDRESS" },
    "p_invalid_ip": { "weight": 0.1, "grouping": "IP_ADDRESS" },

    "valid_ipv4": { "weight": 0.5, "grouping": "VALID_IP" },
    "valid_ipv6": { "weight": 0.5, "grouping": "VALID_IP" },

    "inv_ip_whitespace": { "weight": 0.2, "grouping": "INVALID_IP_CHAR" },
    "inv_ip_control": { "weight": 0.2, "grouping": "INVALID_IP_CHAR" },
    "inv_ip_unicode": { "weight": 0.3, "grouping": "INVALID_IP_CHAR" },
    "inv_ip_disallowed": { "weight": 0.1, "grouping": "INVALID_IP_CHAR" },
    "inv_ip_unassigned": { "weight": 0.1, "grouping": "INVALID_IP_CHAR" },
    "inv_ip_reserved": { "weight": 0.1, "grouping": "INVALID_IP_CHAR" },

    "inv_ip_recurse": { "weight": 0.8, "grouping": "INVALID_IP_TAIL" },
    "inv_ip_stop": { "weight": 0.2, "grouping": "INVALID_IP_TAIL" },

    "digits": { "weight": 0.3, "grouping": "DIGITS" },
    "digits_2": { "weight": 0.7, "grouping": "DIGITS" },

    "hexdigits": { "weight": 0.4, "grouping": "HEXDIGITS" },
    "hexdigits_2": { "weight": 0.6, "grouping": "HEXDIGITS" },

    "inv_start_char": { "weight": 0.5, "grouping": "INVALID_HOST" },
    "inv_start_valid": { "weight": 0.5, "grouping": "INVALID_HOST" },
    
    "inv_recurse": { "weight": 0.8, "grouping": "INVALID_HOST_TAIL" },
    "inv_stop": { "weight": 0.2, "grouping": "INVALID_HOST_TAIL" },
    
    "inv_char_whitespace": { "weight": 0.2, "grouping": "INVALID_HOST_CHAR" },
    "inv_char_control": { "weight": 0.2, "grouping": "INVALID_HOST_CHAR" },
    "inv_char_disallowed": { "weight": 0.1, "grouping": "INVALID_HOST_CHAR" },
    "inv_char_unassigned": { "weight": 0.1, "grouping": "INVALID_HOST_CHAR" },
    "inv_char_reserved": { "weight": 0.1, "grouping": "INVALID_HOST_CHAR" },
    "inv_char_unicode": { "weight": 0.3, "grouping": "INVALID_HOST_CHAR" },
    
    "any_valid": { "weight": 0.5, "grouping": "ANY_CHAR" },
    "any_invalid": { "weight": 0.5, "grouping": "ANY_CHAR" },
}

component = GrammarComponent(pcfg_template, DEFAULT_WEIGHTS)


def generate(weights=None):
    return component.generate(weights=weights)

def generate_with_choice(weights=None):
    return component.generate_with_choice(weights=weights)

def serialize_weights(weights=None):
    return component.serialize_weights(weights)


if __name__ == "__main__":
    for _ in range(10):
        print(generate())
