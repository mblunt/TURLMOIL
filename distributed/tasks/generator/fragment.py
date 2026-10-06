from component import GrammarComponent

pcfg_template = """
    FRAGMENT         -> VALID_FRAGMENT [{p_valid}] | INVALID_FRAGMENT [{p_invalid}] | 'NULL' [{p_null}]

    VALID_FRAGMENT   -> FRAG_CHAR FRAG_TAIL [1.0]
    FRAG_TAIL        -> FRAG_CHAR FRAG_TAIL [{frag_recurse}] | 'NULL' [{frag_stop}]

    INVALID_FRAGMENT -> INVALID_FRAG_CHAR INVALID_FRAG_TAIL [1.0]
    INVALID_FRAG_TAIL -> INVALID_FRAG_CHAR INVALID_FRAG_TAIL [{inv_frag_recurse}] | 'ASCII_WHITESPACE' [{inv_frag_whitespace}] | 'NULL' [{inv_frag_stop}]

    FRAG_CHAR        -> 'ASCII_LETTERS' [{frag_char_letters}] | 'ASCII_DIGITS' [{frag_char_digits}] | 'ASCII_SPECIAL' [{frag_char_special}] 
    INVALID_FRAG_CHAR -> 'ASCII_CONTROL' [{invfrag_char_control}] | 'UNICODE_VALID' [{invfrag_char_unicode}] | 'UNICODE_DISALLOWED' [{invfrag_char_disallowed}] | 'UNICODE_UNASSIGNED' [{invfrag_char_unassigned}] | 'UNICODE_RESERVED' [{invfrag_char_reserved}]
"""

DEFAULT_WEIGHTS = {
    "p_valid": { "weight": 0.7, "grouping": "FRAGMENT" },
    "p_invalid": { "weight": 0.2, "grouping": "FRAGMENT" },
    "p_null": { "weight": 0.1, "grouping": "FRAGMENT" },

    "frag_recurse": { "weight": 0.7, "grouping": "FRAG_TAIL" },
    "frag_stop": { "weight": 0.3, "grouping": "FRAG_TAIL" },

    "inv_frag_recurse": { "weight": 0.6, "grouping": "INVALID_FRAG_TAIL" },
    "inv_frag_whitespace": { "weight": 0.2, "grouping": "INVALID_FRAG_TAIL" },
    "inv_frag_stop": { "weight": 0.2, "grouping": "INVALID_FRAG_TAIL" },

    "frag_char_letters": { "weight": 0.4, "grouping": "FRAG_CHAR" },
    "frag_char_digits": { "weight": 0.4, "grouping": "FRAG_CHAR" },
    "frag_char_special": { "weight": 0.2, "grouping": "FRAG_CHAR" },

    "invfrag_char_control": { "weight": 0.375, "grouping": "INVALID_FRAG_CHAR" },
    "invfrag_char_unicode": { "weight": 0.375, "grouping": "INVALID_FRAG_CHAR" },
    "invfrag_char_disallowed": { "weight": 0.05, "grouping": "INVALID_FRAG_CHAR" },
    "invfrag_char_unassigned": { "weight": 0.05, "grouping": "INVALID_FRAG_CHAR" },
    "invfrag_char_reserved": { "weight": 0.15, "grouping": "INVALID_FRAG_CHAR" },
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
