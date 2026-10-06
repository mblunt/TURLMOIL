from component import GrammarComponent

pcfg_template = """
    DELIM -> VALID_DELIM [{p_valid}] | INVALID_DELIM [{p_invalid}] | 'NULL' [{p_null}]
    VALID_DELIM -> "://" [1.0]
    INVALID_DELIM -> ANY_CHAR INVALID_DELIM [{inv_recurse}] | 'NULL' [{inv_stop}]
    ANY_CHAR -> 'ASCII_DIGITS' [{any_digits}] | 'ASCII_LETTERS' [{any_letters}] | 'ASCII_WHITESPACE' [{any_whitespace}] | 'ASCII_SPECIAL' [{any_special}] | 'ASCII_CONTROL' [{any_control}] | 'UNICODE_VALID' [{any_unicode}] | 'UNICODE_DISALLOWED' [{any_disallowed}] | 'UNICODE_UNASSIGNED' [{any_unassigned}] | 'UNICODE_RESERVED' [{any_reserved}]
"""

DEFAULT_WEIGHTS = {
    "p_valid": { "weight": 0.9, "grouping": "DELIM" },
    "p_invalid": { "weight": 0.05, "grouping": "DELIM" },
    "p_null": { "weight": 0.05, "grouping": "DELIM" },

    "inv_recurse": { "weight": 0.9, "grouping": "INVALID_DELIM" },
    "inv_stop": { "weight": 0.1, "grouping": "INVALID_DELIM" },

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
