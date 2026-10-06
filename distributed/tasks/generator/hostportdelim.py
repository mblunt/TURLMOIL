from component import GrammarComponent

pcfg_template = """
    HOST_PORT_DELIM    -> VALID_DELIM [{p_valid}] | INVALID_DELIM [{p_invalid}] | 'NULL' [{p_null}]

    VALID_DELIM        -> ':' [{valid_colon}] | 'NULL' [{valid_null}]

    INVALID_DELIM      -> INVALID_DELIM_CHAR INVALID_DELIM_TAIL [1.0]
    INVALID_DELIM_TAIL -> ANY_CHAR INVALID_DELIM_TAIL [{inv_recurse}] | 'NULL' [{inv_stop}]

    INVALID_DELIM_CHAR -> 'ASCII_DIGITS' [{inv_char_digits}] | 'ASCII_LETTERS' [{inv_char_letters}] | 'ASCII_WHITESPACE' [{inv_char_whitespace}] | 'ASCII_SPECIAL' [{inv_char_special}] | 'ASCII_CONTROL' [{inv_char_control}] | 'UNICODE_VALID' [{inv_char_unicode}] | 'UNICODE_DISALLOWED' [{inv_char_disallowed}] | 'UNICODE_UNASSIGNED' [{inv_char_unassigned}] | 'UNICODE_RESERVED' [{inv_char_reserved}]

    ANY_CHAR           -> 'ASCII_DIGITS' [{any_digits}] | 'ASCII_LETTERS' [{any_letters}] | 'ASCII_WHITESPACE' [{any_whitespace}] | 'ASCII_SPECIAL' [{any_special}] | 'ASCII_CONTROL' [{any_control}] | 'UNICODE_VALID' [{any_unicode}] | 'UNICODE_DISALLOWED' [{any_disallowed}] | 'UNICODE_UNASSIGNED' [{any_unassigned}] | 'UNICODE_RESERVED' [{any_reserved}]
"""

DEFAULT_WEIGHTS = {
    "p_valid": { "weight": 0.6, "grouping": "HOST_PORT_DELIM" },
    "p_invalid": { "weight": 0.3, "grouping": "HOST_PORT_DELIM" },
    "p_null": { "weight": 0.1, "grouping": "HOST_PORT_DELIM" },

    "valid_colon": { "weight": 0.9, "grouping": "VALID_DELIM" },
    "valid_null": { "weight": 0.1, "grouping": "VALID_DELIM" },

    "inv_recurse": { "weight": 0.8, "grouping": "INVALID_DELIM_TAIL" },
    "inv_stop": { "weight": 0.2, "grouping": "INVALID_DELIM_TAIL" },

    "inv_char_digits": { "weight": 0.1, "grouping": "INVALID_DELIM_CHAR" },
    "inv_char_letters": { "weight": 0.1, "grouping": "INVALID_DELIM_CHAR" },
    "inv_char_whitespace": { "weight": 0.1, "grouping": "INVALID_DELIM_CHAR" },
    "inv_char_special": { "weight": 0.2, "grouping": "INVALID_DELIM_CHAR" },
    "inv_char_control": { "weight": 0.1, "grouping": "INVALID_DELIM_CHAR" },
    "inv_char_unicode": { "weight": 0.1, "grouping": "INVALID_DELIM_CHAR" },
    "inv_char_disallowed": { "weight": 0.1, "grouping": "INVALID_DELIM_CHAR" },
    "inv_char_unassigned": { "weight": 0.1, "grouping": "INVALID_DELIM_CHAR" },
    "inv_char_reserved": { "weight": 0.1, "grouping": "INVALID_DELIM_CHAR" },

    "any_digits": { "weight": 0.1, "grouping": "ANY_CHAR" },
    "any_letters": { "weight": 0.1, "grouping": "ANY_CHAR" },
    "any_whitespace": { "weight": 0.1, "grouping": "ANY_CHAR" },
    "any_special": { "weight": 0.2, "grouping": "ANY_CHAR" },
    "any_control": { "weight": 0.1, "grouping": "ANY_CHAR" },
    "any_unicode": { "weight": 0.1, "grouping": "ANY_CHAR" },
    "any_disallowed": { "weight": 0.1, "grouping": "ANY_CHAR" },
    "any_unassigned": { "weight": 0.1, "grouping": "ANY_CHAR" },
    "any_reserved": { "weight": 0.1, "grouping": "ANY_CHAR" },
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
