from component import GrammarComponent

pcfg_template = """
    SCHEME -> VALID_SCHEME [{p_valid}] | INVALID_SCHEME [{p_invalid}] | 'NULL' [{p_null}]

    VALID_SCHEME -> 'COMMON_SCHEMES' [{schemes_common}] | 'KNOWN_SCHEMES' [{schemes_uncommon}]

    INVALID_SCHEME -> INVALID_CHAR INVALID_TAIL [{inv_char}] | KNOWN_SCHEMES INVALID_TAIL [{inv_known}] | ASCII_LETTERS INVALID_SCHEME [{inv_letter}]
    INVALID_TAIL -> ANY_CHAR INVALID_TAIL [{inv2_recurse}] | KNOWN_SCHEMES INVALID_TAIL [{inv2_tail_known}] | 'NULL' [{inv2_stop}]

    VALID_CHAR -> 'ASCII_LETTERS' [{valid3_char_letters}] | 'ASCII_DIGITS' [{valid3_char_digits}]
    INVALID_CHAR -> 'ASCII_SPECIAL' [{inv3_char_special}] | 'UNICODE_VALID' [{inv3_char_unicode}] | 'ASCII_WHITESPACE' [{inv3_char_whitespace}] | 'ASCII_CONTROL' [{inv3_char_control}] | 'UNICODE_DISALLOWED' [{inv3_char_disallowed}] | 'UNICODE_UNASSIGNED' [{inv3_char_unassigned}] | 'UNICODE_RESERVED' [{inv3_char_reserved}]
    ANY_CHAR -> VALID_CHAR [{any_valid}] | INVALID_CHAR [{any_invalid}]

    ASCII_LETTERS -> 'ASCII_LETTERS' [1.0]
"""

DEFAULT_WEIGHTS = {
    "p_valid": { "weight": 0.45, "grouping": "SCHEME" },
    "p_invalid": { "weight": 0.45, "grouping": "SCHEME" },
    "p_null": { "weight": 0.1, "grouping": "SCHEME" },

    "inv_char": { "weight": 0.4, "grouping": "INVALID_SCHEME" },
    "inv_known": { "weight": 0.3, "grouping": "INVALID_SCHEME" },
    "inv_letter": { "weight": 0.3, "grouping": "INVALID_SCHEME" },

    "inv2_recurse": { "weight": 0.45, "grouping": "INVALID_TAIL" },
    "inv2_tail_known": { "weight": 0.45, "grouping": "INVALID_TAIL" },
    "inv2_stop": { "weight": 0.1, "grouping": "INVALID_TAIL" },

    "valid3_char_letters": { "weight": 0.8, "grouping": "VALID_CHAR" },
    "valid3_char_digits": { "weight": 0.2, "grouping": "VALID_CHAR" },

    "inv3_char_special": { "weight": 0.25, "grouping": "INVALID_CHAR" },
    "inv3_char_unicode": { "weight": 0.25, "grouping": "INVALID_CHAR" },
    "inv3_char_whitespace": { "weight": 0.1, "grouping": "INVALID_CHAR" },
    "inv3_char_control": { "weight": 0.1, "grouping": "INVALID_CHAR" },
    "inv3_char_disallowed": { "weight": 0.1, "grouping": "INVALID_CHAR" },
    "inv3_char_unassigned": { "weight": 0.1, "grouping": "INVALID_CHAR" },
    "inv3_char_reserved": { "weight": 0.1, "grouping": "INVALID_CHAR" },

    "any_valid": { "weight": 0.5, "grouping": "ANY_CHAR" },
    "any_invalid": { "weight": 0.5, "grouping": "ANY_CHAR" },

    "schemes_common": { "weight": 0.8, "grouping": "VALID_SCHEME" },
    "schemes_uncommon": { "weight": 0.2, "grouping": "VALID_SCHEME" },
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
