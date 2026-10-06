import random
from nltk import PCFG

def generate_sample(grammar, symbol, TERMINAL_MAP, depth=0, max_depth=20):
    # Quoted terminal: NLTK gives us a plain Python str
    if isinstance(symbol, str):
        if symbol not in TERMINAL_MAP:
            return symbol
        return str(random.choice(TERMINAL_MAP[symbol]))

    # Unquoted nonterminal: NLTK gives us a Nonterminal object.
    # Some grammar rules use bare names (e.g. KNOWN_SCHEMES) that are
    # intentionally resolved via the terminal map rather than grammar rules.
    symbol_str = str(symbol)
    if symbol_str in TERMINAL_MAP:
        return str(random.choice(TERMINAL_MAP[symbol_str]))

    productions = grammar.productions(lhs=symbol)

    # Safety: missing productions or recursion too deep
    if not productions or depth > max_depth:
        return ""

    probs = [p.prob() for p in productions]
    chosen_production = random.choices(productions, weights=probs)[0]

    # recurse on the right-hand side of the chosen production
    return "".join(generate_sample(grammar, s, TERMINAL_MAP, depth + 1, max_depth) for s in chosen_production.rhs())