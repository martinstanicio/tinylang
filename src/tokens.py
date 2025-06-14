from string import ascii_letters, digits

from .afd import AFD

PROGRAM = AFD(
    token="PROGRAM",
    delta={
        0: {"p": 1},
        1: {"r": 2},
        2: {"o": 3},
        3: {"g": 4},
        4: {"r": 5},
        5: {"a": 6},
        6: {"m": 7},
    },
    estados_finales=[7],
)
VAR = AFD(
    token="VAR", delta={0: {"v": 1}, 1: {"a": 2}, 2: {"r": 3}}, estados_finales=[3]
)
INT = AFD(
    token="INT", delta={0: {"i": 1}, 1: {"n": 2}, 2: {"t": 3}}, estados_finales=[3]
)
BOOL = AFD(
    token="BOOL",
    delta={0: {"b": 1}, 1: {"o": 2}, 2: {"o": 3}, 3: {"l": 4}},
    estados_finales=[4],
)
TRUE = AFD(
    token="TRUE",
    delta={0: {"t": 1}, 1: {"r": 2}, 2: {"u": 3}, 3: {"e": 4}},
    estados_finales=[4],
)
FALSE = AFD(
    token="FALSE",
    delta={0: {"f": 1}, 1: {"a": 2}, 2: {"l": 3}, 3: {"s": 4}, 4: {"e": 5}},
    estados_finales=[5],
)
BEGIN = AFD(
    token="BEGIN",
    delta={0: {"b": 1}, 1: {"e": 2}, 2: {"g": 3}, 3: {"i": 4}, 4: {"n": 5}},
    estados_finales=[5],
)
END = AFD(
    token="END", delta={0: {"e": 1}, 1: {"n": 2}, 2: {"d": 3}}, estados_finales=[3]
)
IF = AFD(token="IF", delta={0: {"i": 1}, 1: {"f": 2}}, estados_finales=[2])
ELSE = AFD(
    token="ELSE",
    delta={0: {"e": 1}, 1: {"l": 2}, 2: {"s": 3}, 3: {"e": 4}},
    estados_finales=[4],
)
NOT = AFD(
    token="NOT", delta={0: {"n": 1}, 1: {"o": 2}, 2: {"t": 3}}, estados_finales=[3]
)
GOTO = AFD(
    token="GOTO",
    delta={0: {"g": 1}, 1: {"o": 2}, 2: {"t": 3}, 3: {"o": 4}},
    estados_finales=[4],
)
LET = AFD(
    token="LET", delta={0: {"l": 1}, 1: {"e": 2}, 2: {"t": 3}}, estados_finales=[3]
)
AND = AFD(
    token="AND", delta={0: {"a": 1}, 1: {"n": 2}, 2: {"d": 3}}, estados_finales=[3]
)
OR = AFD(token="OR", delta={0: {"o": 1}, 1: {"r": 2}}, estados_finales=[2])
DOT = AFD(token="DOT", delta={0: {".": 1}}, estados_finales=[1])
SEMICOLON = AFD(token="SEMICOLON", delta={0: {";": 1}}, estados_finales=[1])
COLON = AFD(token="COLON", delta={0: {":": 1}}, estados_finales=[1])
ELLIPSIS = AFD(
    token="ELLIPSIS", delta={0: {".": 1}, 1: {".": 2}, 2: {".": 3}}, estados_finales=[3]
)
ASSIGN = AFD(token="ASSIGN", delta={0: {"=": 1}}, estados_finales=[1])
LPAREN = AFD(token="LPAREN", delta={0: {"(": 1}}, estados_finales=[1])
RPAREN = AFD(token="RPAREN", delta={0: {")": 1}}, estados_finales=[1])
PLUS = AFD(token="PLUS", delta={0: {"+": 1}}, estados_finales=[1])
MINUS = AFD(token="MINUS", delta={0: {"-": 1}}, estados_finales=[1])
ASTERISK = AFD(token="ASTERISK", delta={0: {"*": 1}}, estados_finales=[1])
EQUAL = AFD(token="EQUAL", delta={0: {"=": 1}, 1: {"=": 2}}, estados_finales=[2])
NOT_EQUAL = AFD(
    token="NOT_EQUAL", delta={0: {"<": 1}, 1: {">": 2}}, estados_finales=[2]
)
LESS_THAN = AFD(token="LESS_THAN", delta={0: {"<": 1}}, estados_finales=[1])
GREATER_THAN = AFD(token="GREATER_THAN", delta={0: {">": 1}}, estados_finales=[1])
LESS_EQUAL = AFD(
    token="LESS_EQUAL", delta={0: {"<": 1}, 1: {"=": 2}}, estados_finales=[2]
)
GREATER_EQUAL = AFD(
    token="GREATER_EQUAL", delta={0: {">": 1}, 1: {"=": 2}}, estados_finales=[2]
)
ID = AFD(
    token="ID",
    delta={
        0: {letter: 1 for letter in ascii_letters},
        1: {char: 1 for char in ascii_letters + digits},
    },
    estados_finales=[1],
)
NUMBER = AFD(
    token="NUMBER",
    delta={
        0: {digit: 2 for digit in digits} | {"-": 1},
        1: {digit: 2 for digit in digits},
        2: {digit: 2 for digit in digits},
    },
    estados_finales=[2],
)
WHITESPACE = AFD(
    token="WHITESPACE",
    delta={0: {" ": 1, "\t": 1, "\n": 1}, 1: {" ": 1, "\t": 1, "\n": 1}},
    estados_finales=[1],
)


# La prioridad de los tokens se define por el orden en que aparecen en la lista.
# Si un lexema puede ser reconocido como más de un token, se tomará el primero de la lista.
tokens = [
    PROGRAM,
    VAR,
    INT,
    BOOL,
    TRUE,
    FALSE,
    BEGIN,
    END,
    IF,
    ELSE,
    NOT,
    GOTO,
    LET,
    AND,
    OR,
    DOT,
    SEMICOLON,
    COLON,
    ELLIPSIS,
    ASSIGN,
    LPAREN,
    RPAREN,
    PLUS,
    MINUS,
    ASTERISK,
    EQUAL,
    NOT_EQUAL,
    LESS_THAN,
    GREATER_THAN,
    LESS_EQUAL,
    GREATER_EQUAL,
    ID,
    NUMBER,
    WHITESPACE,
]
