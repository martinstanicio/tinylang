import os
import sys
import unittest

# Agregar el directorio padre al path para poder importar el módulo src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import lexer


def gen_tiny(tokens: list[tuple[str, str]]):
    return "".join([lexema for (_, lexema) in tokens])


class LexerTest(unittest.TestCase):
    def test_keywords(self):
        tokens_esperados = [
            ("PROGRAM", "program"),
            ("WHITESPACE", "\n"),
            ("VAR", "var"),
            ("WHITESPACE", "\n"),
            ("INT", "int"),
            ("WHITESPACE", "\n"),
            ("BOOL", "bool"),
            ("WHITESPACE", "\n"),
            ("TRUE", "true"),
            ("WHITESPACE", "\n"),
            ("FALSE", "false"),
            ("WHITESPACE", "\n"),
            ("BEGIN", "begin"),
            ("WHITESPACE", "\n"),
            ("END", "end"),
            ("WHITESPACE", "\n"),
            ("IF", "if"),
            ("WHITESPACE", "\n"),
            ("ELSE", "else"),
            ("WHITESPACE", "\n"),
            ("NOT", "not"),
            ("WHITESPACE", "\n"),
            ("GOTO", "goto"),
            ("WHITESPACE", "\n"),
            ("LET", "let"),
            ("WHITESPACE", "\n"),
            ("AND", "and"),
            ("WHITESPACE", "\n"),
            ("OR", "or"),
            ("WHITESPACE", "\n"),
        ]
        tiny = gen_tiny(tokens_esperados)
        tokens = lexer(tiny)
        self.assertEqual(tokens, tokens_esperados)

    def test_identifier(self):
        tokens_esperados = [
            ("ID", "abc"),
            ("WHITESPACE", "\n"),
            ("ID", "XYZ"),
            ("WHITESPACE", "\n"),
            ("ID", "x1"),
            ("WHITESPACE", "\n"),
            # "1x" no es un identificador válido
            ("NUMBER", "1"),
            ("ID", "x"),
            ("WHITESPACE", "\n"),
        ]
        tiny = gen_tiny(tokens_esperados)
        tokens = lexer(tiny)
        self.assertEqual(tokens, tokens_esperados)

    def test_number(self):
        tokens_esperados = [
            ("NUMBER", "42"),
            ("WHITESPACE", " "),
            ("NUMBER", "-10"),
            ("WHITESPACE", " "),
            ("NUMBER", "0"),
            ("WHITESPACE", " "),
        ]
        tiny = gen_tiny(tokens_esperados)
        tokens = lexer(tiny)
        self.assertEqual(tokens, tokens_esperados)

    def test_whitespace(self):
        tokens_esperados = [("WHITESPACE", " \t\n")]
        tiny = gen_tiny(tokens_esperados)
        tokens = lexer(tiny)
        self.assertEqual(tokens, tokens_esperados)

    def test_symbols(self):
        tokens_esperados = [
            ("DOT", "."),
            ("SEMICOLON", ";"),
            ("COLON", ":"),
            ("LPAREN", "("),
            ("RPAREN", ")"),
            ("ELLIPSIS", "..."),
            ("DOT", "."),
        ]
        tiny = gen_tiny(tokens_esperados)
        tokens = lexer(tiny)
        self.assertEqual(tokens, tokens_esperados)

    def test_arithmetic_ops(self):
        tokens_esperados = [
            ("PLUS", "+"),
            ("MINUS", "-"),
            ("ASTERISK", "*"),
        ]
        tiny = gen_tiny(tokens_esperados)
        tokens = lexer(tiny)
        self.assertEqual(tokens, tokens_esperados)

    def test_comparison_ops(self):
        tokens_esperados = [
            ("EQUAL", "=="),
            ("NOT_EQUAL", "<>"),
            ("LESS_THAN", "<"),
            ("LESS_EQUAL", "<="),
            ("GREATER_THAN", ">"),
            ("GREATER_EQUAL", ">="),
        ]
        tiny = gen_tiny(tokens_esperados)
        tokens = lexer(tiny)
        self.assertEqual(tokens, tokens_esperados)

    def test_invalid_character(self):
        tokens_esperados = [
            ("ERROR", "@"),
            ("ERROR", "$"),
            ("ERROR", "?"),
        ]
        tiny = gen_tiny(tokens_esperados)
        tokens = lexer(tiny)
        self.assertEqual(tokens, tokens_esperados)

    def test_mixed_valid_and_invalid(self):
        tokens_esperados = [
            ("LET", "let"),
            ("WHITESPACE", " "),
            ("ERROR", "$"),
            ("ID", "abc"),
        ]
        tiny = gen_tiny(tokens_esperados)
        tokens = lexer(tiny)
        self.assertEqual(tokens, tokens_esperados)


if __name__ == "__main__":
    unittest.main()
