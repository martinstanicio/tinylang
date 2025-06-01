import os
from pprint import pp as prettyprint

from src.lexer import lexer


def main() -> None:
    tiny_path = "./tiny"

    for filename in os.listdir(tiny_path):
        full_file_path = os.path.join(tiny_path, filename)

        if not os.path.isfile(full_file_path):
            continue

        print("\n\n\n", end="")
        print("==========", end="")
        print("\n\n\n", end="")

        with open(full_file_path) as file:
            tiny = file.read()
            tokens = lexer(tiny)

            print(tiny)
            prettyprint(tokens)


if __name__ == "__main__":
    main()
