from component import GrammarComponent

pcfg_template = """
    PASSWORD         -> VALID_PASSWORD [{p_valid}] | INVALID_PASSWORD [{p_invalid}] | 'NULL' [{p_null}]

    VALID_PASSWORD   -> VALID_PASS_CHAR VALID_PASS_TAIL [1.0]
    VALID_PASS_TAIL  -> VALID_PASS_CHAR VALID_PASS_TAIL [{valid_recurse}] | 'NULL' [{valid_stop}]
    VALID_PASS_CHAR  -> 'ASCII_LETTERS' [{valid_char_letters}] | 'ASCII_DIGITS' [{valid_char_digits}] | 

    INVALID_PASSWORD -> INVALID_PASS_CHAR INVALID_PASS_TAIL [{inv_start_char}] | VALID_PASS_CHAR INVALID_PASSWORD [{inv_start_valid}]
    INVALID_PASS_TAIL -> ANY_CHAR INVALID_PASS_TAIL [{inv_recurse}] | 'NULL' [{inv_stop}]
    INVALID_PASS_CHAR -> '@' [{inv_char_at}] | 'ASCII_SPECIAL' [{inv_char_special}] | 'UNICODE_VALID' [{inv_char_unicode}] | 'ASCII_WHITESPACE' [{inv_char_whitespace}] | 'ASCII_CONTROL' [{inv_char_control}] | 'UNICODE_DISALLOWED' [{inv_char_disallowed}] | 'UNICODE_UNASSIGNED' [{inv_char_unassigned}] | 'UNICODE_RESERVED' [{inv_char_reserved}]

    ANY_CHAR         -> VALID_PASS_CHAR [{any_valid}] | INVALID_PASS_CHAR [{any_invalid}]
"""

DEFAULT_WEIGHTS = {
    "p_valid": { "weight": 0.6, "grouping": "PASSWORD" },
    "p_invalid": { "weight": 0.3, "grouping": "PASSWORD" },
    "p_null": { "weight": 0.1, "grouping": "PASSWORD" },

    "valid_recurse": { "weight": 0.8, "grouping": "VALID_PASS_TAIL" },
    "valid_stop": { "weight": 0.2, "grouping": "VALID_PASS_TAIL" },

    "valid_char_letters": { "weight": 0.5, "grouping": "VALID_PASS_CHAR" },
    "valid_char_digits": { "weight": 0.5, "grouping": "VALID_PASS_CHAR" },

    "inv_start_char": { "weight": 0.5, "grouping": "INVALID_PASSWORD" },
    "inv_start_valid": { "weight": 0.5, "grouping": "INVALID_PASSWORD" },

    "inv_recurse": { "weight": 0.8, "grouping": "INVALID_PASS_TAIL" },
    "inv_stop": { "weight": 0.2, "grouping": "INVALID_PASS_TAIL" },

    "inv_char_at": { "weight": 0.1, "grouping": "INVALID_PASS_CHAR" },
    "inv_char_special": { "weight": 0.1, "grouping": "INVALID_PASS_CHAR" },
    "inv_char_unicode": { "weight": 0.1, "grouping": "INVALID_PASS_CHAR" },
    "inv_char_whitespace": { "weight": 0.1, "grouping": "INVALID_PASS_CHAR" },
    "inv_char_control": { "weight": 0.1, "grouping": "INVALID_PASS_CHAR" },
    "inv_char_disallowed": { "weight": 0.2, "grouping": "INVALID_PASS_CHAR" },
    "inv_char_unassigned": { "weight": 0.15, "grouping": "INVALID_PASS_CHAR" },
    "inv_char_reserved": { "weight": 0.15, "grouping": "INVALID_PASS_CHAR" },

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
