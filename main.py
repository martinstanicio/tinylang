import os
import pprint

from src import ParseError, lexer, parser


def main() -> None:
    tiny_path = "./tiny"
    output_path = "./dist"
    output_file = "output.md"

    tiny_files = sorted(os.listdir(tiny_path))

    output = "# Tinylang\n"

    for i, filename in enumerate(tiny_files):
        with open(os.path.join(tiny_path, filename)) as file:
            tiny = file.read()

            output += f"\n## Programa {i + 1}\n\n```text\n{tiny}```\n"

            lexer_output = lexer(tiny)
            lexer_has_errored = "ERROR" in [token[0] for token in lexer_output]

            output += f"\n### Salida del lexer\n\n```python\n{pprint.pformat(lexer_output)}\n```\n"

            if not lexer_has_errored:
                parser_output = ""

                try:
                    parser_output = parser(lexer_output)
                except ParseError as e:
                    parser_output = str(e)

                output += f"\n### Salida del parser\n\n```python\n{pprint.pformat(parser_output)}\n```\n"

    os.makedirs(output_path, exist_ok=True)
    with open(os.path.join(output_path, output_file), "w") as file:
        file.write(output)


if __name__ == "__main__":
    main()
