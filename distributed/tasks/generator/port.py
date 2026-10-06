from component import GrammarComponent

pcfg_template = """
    PORT             -> VALID_PORT [{p_valid}] | INVALID_PORT [{p_invalid}] | 'NULL' [{p_null}]

    VALID_PORT       -> 'ASCII_DIGITS' [{valid_1d}] | 'ASCII_DIGITS' 'ASCII_DIGITS' [{valid_2d}] | 'ASCII_DIGITS' 'ASCII_DIGITS' 'ASCII_DIGITS' [{valid_3d}] | 'ASCII_DIGITS' 'ASCII_DIGITS' 'ASCII_DIGITS' 'ASCII_DIGITS' [{valid_4d}]

    INVALID_PORT     -> INVALID_PORT_CHAR INVALID_PORT_TAIL [{inv_start_char}] | 'ASCII_DIGITS' INVALID_PORT [{inv_start_valid}] | OVERFLOW_PORT [{inv_overflow}]

    OVERFLOW_PORT    -> 'ASCII_DIGITS' 'ASCII_DIGITS' 'ASCII_DIGITS' 'ASCII_DIGITS' 'ASCII_DIGITS' 'ASCII_DIGITS' DIGIT_RECURSE [{overflow_start}]
    DIGIT_RECURSE    -> 'ASCII_DIGITS' DIGIT_RECURSE [{valid_recurse}] | 'ASCII_DIGITS' [{valid_stop}]

    INVALID_PORT_TAIL -> ANY_CHAR INVALID_PORT_TAIL [{inv_recurse}] | 'NULL' [{inv_stop}]

    INVALID_PORT_CHAR -> 'ASCII_LETTERS' [{inv_char_letters}] | 'ASCII_WHITESPACE' [{inv_char_whitespace}] | 'ASCII_SPECIAL' [{inv_char_special}] | 'ASCII_CONTROL' [{inv_char_control}] | 'UNICODE_VALID' [{inv_char_unicode}] | 'UNICODE_DISALLOWED' [{inv_char_disallowed}] | 'UNICODE_UNASSIGNED' [{inv_char_unassigned}] | 'UNICODE_RESERVED' [{inv_char_reserved}]

    ANY_CHAR         -> 'ASCII_DIGITS' [{any_digits}] | INVALID_PORT_CHAR [{any_invalid}]
"""

DEFAULT_WEIGHTS = {
    "p_valid": { "weight": 0.5, "grouping": "PORT" },
    "p_invalid": { "weight": 0.4, "grouping": "PORT" },
    "p_null": { "weight": 0.1, "grouping": "PORT" },

    "valid_1d": { "weight": 0.25, "grouping": "VALID_PORT" },
    "valid_2d": { "weight": 0.25, "grouping": "VALID_PORT" },
    "valid_3d": { "weight": 0.25, "grouping": "VALID_PORT" },
    "valid_4d": { "weight": 0.25, "grouping": "VALID_PORT" },

    "valid_recurse": { "weight": 0.7, "grouping": "DIGIT_RECURSE" },
    "valid_stop": { "weight": 0.3, "grouping": "DIGIT_RECURSE" },

    "inv_start_char": { "weight": 0.5, "grouping": "INVALID_PORT" },
    "inv_start_valid": { "weight": 0.4, "grouping": "INVALID_PORT" },
    "inv_overflow": { "weight": 0.1, "grouping": "INVALID_PORT" },

    "overflow_start": { "weight": 1.0, "grouping": "OVERFLOW_PORT" },

    "inv_recurse": { "weight": 0.7, "grouping": "INVALID_PORT_TAIL" },
    "inv_stop": { "weight": 0.3, "grouping": "INVALID_PORT_TAIL" },

    "inv_char_letters": { "weight": 0.15, "grouping": "INVALID_PORT_CHAR" },
    "inv_char_whitespace": { "weight": 0.15, "grouping": "INVALID_PORT_CHAR" },
    "inv_char_special": { "weight": 0.2, "grouping": "INVALID_PORT_CHAR" },
    "inv_char_control": { "weight": 0.1, "grouping": "INVALID_PORT_CHAR" },
    "inv_char_unicode": { "weight": 0.1, "grouping": "INVALID_PORT_CHAR" },
    "inv_char_disallowed": { "weight": 0.1, "grouping": "INVALID_PORT_CHAR" },
    "inv_char_unassigned": { "weight": 0.1, "grouping": "INVALID_PORT_CHAR" },
    "inv_char_reserved": { "weight": 0.1, "grouping": "INVALID_PORT_CHAR" },

    "any_digits": { "weight": 0.3, "grouping": "ANY_CHAR" },
    "any_invalid": { "weight": 0.7, "grouping": "ANY_CHAR" },
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
