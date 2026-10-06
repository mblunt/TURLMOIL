from component import GrammarComponent

pcfg_template = """
    PATH             -> VALID_PATH [{p_valid}] | INVALID_PATH [{p_invalid}] | 'NULL' [{p_null}]

    VALID_PATH       -> VALID_PATH_CHAR VALID_PATH_TAIL [1.0]
    VALID_PATH_TAIL  -> VALID_PATH_CHAR VALID_PATH_TAIL [{valid_recurse}] | 'NULL' [{valid_stop}]
    VALID_PATH_CHAR  -> 'ASCII_LETTERS' [{valid_char_letters}] | 'ASCII_DIGITS' [{valid_char_digits}] |  'PATH_SPECIAL' [{valid_char_path_special}]

    INVALID_PATH     -> INVALID_PATH_CHAR INVALID_PATH_TAIL [{inv_start_char}] | VALID_PATH_CHAR INVALID_PATH [{inv_start_valid}]
    INVALID_PATH_TAIL -> ANY_CHAR INVALID_PATH_TAIL [{inv_recurse}] | 'NULL' [{inv_stop}]
    INVALID_PATH_CHAR -> 'UNICODE_VALID' [{inv_char_unicode}] | 'ASCII_CONTROL' [{inv_char_control}] | 'PATH_FORBIDDEN' [{inv_char_forbidden}] | 'ASCII_WHITESPACE' [{inv_char_whitespace}] | 'UNICODE_DISALLOWED' [{inv_char_disallowed}] | 'UNICODE_UNASSIGNED' [{inv_char_unassigned}] | 'UNICODE_RESERVED' [{inv_char_reserved}]

    ANY_CHAR         -> VALID_PATH_CHAR [{any_valid}] | INVALID_PATH_CHAR [{any_invalid}]
"""

DEFAULT_WEIGHTS = {
    "p_valid": { "weight": 0.6, "grouping": "PATH" },
    "p_invalid": { "weight": 0.3, "grouping": "PATH" },
    "p_null": { "weight": 0.1, "grouping": "PATH" },

    "valid_recurse": { "weight": 0.99, "grouping": "VALID_PATH_TAIL" },
    "valid_stop": { "weight": 0.01, "grouping": "VALID_PATH_TAIL" },

    "valid_char_letters": { "weight": 0.45, "grouping": "VALID_PATH_CHAR" },
    "valid_char_digits": { "weight": 0.45, "grouping": "VALID_PATH_CHAR" },
    "valid_char_path_special": { "weight": 0.1, "grouping": "VALID_PATH_CHAR" },

    "inv_start_char": { "weight": 0.5, "grouping": "INVALID_PATH" },
    "inv_start_valid": { "weight": 0.5, "grouping": "INVALID_PATH" },

    "inv_recurse": { "weight": 0.8, "grouping": "INVALID_PATH_TAIL" },
    "inv_stop": { "weight": 0.2, "grouping": "INVALID_PATH_TAIL" },

    "inv_char_control": { "weight": 0.1, "grouping": "INVALID_PATH_CHAR" },
    "inv_char_unicode": { "weight": 0.1, "grouping": "INVALID_PATH_CHAR" },
    "inv_char_forbidden": { "weight": 0.1, "grouping": "INVALID_PATH_CHAR" },
    "inv_char_whitespace": { "weight": 0.2, "grouping": "INVALID_PATH_CHAR" },
    "inv_char_disallowed": { "weight": 0.2, "grouping": "INVALID_PATH_CHAR" },
    "inv_char_unassigned": { "weight": 0.15, "grouping": "INVALID_PATH_CHAR" },
    "inv_char_reserved": { "weight": 0.15, "grouping": "INVALID_PATH_CHAR" },

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
