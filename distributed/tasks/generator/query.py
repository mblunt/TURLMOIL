from component import GrammarComponent

# Formalisms for keys, like {VALID_CHAR}={VALID_CHAR}&{VALID_CHAR}={VALID_CHAR}

pcfg_template = """
    QUERY            -> VALID_QUERY [{p_valid}] | INVALID_QUERY [{p_invalid}] | 'NULL' [{p_null}]

    VALID_QUERY      -> PARAM [{param}] | PARAM '&' VALID_QUERY [{param_recurse}] | 'NULL' [{param_stop}]
    PARAM -> KEY '=' VALUE  [{key_value_pair}] | KEY [{key_only}]
    KEY -> VALID_QUERY_CHAR KEY_TAIL [1.0]
    KEY_TAIL -> VALID_QUERY_CHAR KEY_TAIL [{key_recurse}] | 'NULL' [{key_stop}]
    VALUE -> VALID_QUERY_CHAR VALUE_TAIL [1.0]
    VALUE_TAIL -> VALID_QUERY_CHAR VALUE_TAIL [{value_recurse}] | 'NULL' [{value_stop}]

    VALID_QUERY_CHAR -> 'ASCII_LETTERS' [{valid_char_letters}] | 'ASCII_DIGITS' [{valid_char_digits}] | 'QUERY_SPECIAL' [{valid_char_query_special}]

    INVALID_QUERY    -> INVALID_QUERY_CHAR INVALID_QUERY_TAIL [{inv_start_char}] | VALID_QUERY_CHAR INVALID_QUERY [{inv_start_valid}]
    INVALID_QUERY_TAIL -> ANY_CHAR INVALID_QUERY_TAIL [{inv_recurse}] | 'NULL' [{inv_stop}]
    INVALID_QUERY_CHAR -> '#' [{inv_char_hash}] | 'UNICODE_VALID' [{inv_char_unicode}] | 'ASCII_WHITESPACE' [{inv_char_whitespace}] | 'ASCII_CONTROL' [{inv_char_control}] | 'UNICODE_DISALLOWED' [{inv_char_disallowed}] | 'UNICODE_UNASSIGNED' [{inv_char_unassigned}] | 'UNICODE_RESERVED' [{inv_char_reserved}]

    ANY_CHAR         -> VALID_QUERY_CHAR [{any_valid}] | INVALID_QUERY_CHAR [{any_invalid}]
"""

DEFAULT_WEIGHTS = {
    "p_valid": { "weight": 0.6, "grouping": "QUERY" },
    "p_invalid": { "weight": 0.3, "grouping": "QUERY" },
    "p_null": { "weight": 0.1, "grouping": "QUERY" },

    "param": { "weight": 0.4, "grouping": "VALID_QUERY" },
    "param_recurse": { "weight": 0.5, "grouping": "VALID_QUERY" },
    "param_stop": { "weight": 0.1, "grouping": "VALID_QUERY" },

    "key_value_pair": { "weight": 0.7, "grouping": "PARAM" },
    "key_only": { "weight": 0.3, "grouping": "PARAM" },

    "value_recurse": { "weight": 0.8, "grouping": "VALUE_TAIL" },
    "value_stop": { "weight": 0.2, "grouping": "VALUE_TAIL" },

    "key_recurse": { "weight": 0.8, "grouping": "KEY_TAIL" },
    "key_stop": { "weight": 0.2, "grouping": "KEY_TAIL" },

    "valid_char_letters": { "weight": 0.3, "grouping": "VALID_QUERY_CHAR" },
    "valid_char_digits": { "weight": 0.3, "grouping": "VALID_QUERY_CHAR" },
    "valid_char_query_special": { "weight": 0.4, "grouping": "VALID_QUERY_CHAR" },

    "inv_start_char": { "weight": 0.5, "grouping": "INVALID_QUERY" },
    "inv_start_valid": { "weight": 0.5, "grouping": "INVALID_QUERY" },

    "inv_recurse": { "weight": 0.8, "grouping": "INVALID_QUERY_TAIL" },
    "inv_stop": { "weight": 0.2, "grouping": "INVALID_QUERY_TAIL" },

    "inv_char_unicode": { "weight": 0.1, "grouping": "INVALID_QUERY_CHAR" },
    "inv_char_hash": { "weight": 0.2, "grouping": "INVALID_QUERY_CHAR" },
    "inv_char_whitespace": { "weight": 0.2, "grouping": "INVALID_QUERY_CHAR" },
    "inv_char_control": { "weight": 0.1, "grouping": "INVALID_QUERY_CHAR" },
    "inv_char_disallowed": { "weight": 0.2, "grouping": "INVALID_QUERY_CHAR" },
    "inv_char_unassigned": { "weight": 0.1, "grouping": "INVALID_QUERY_CHAR" },
    "inv_char_reserved": { "weight": 0.1, "grouping": "INVALID_QUERY_CHAR" },

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
