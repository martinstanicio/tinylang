from .tokens import tokens as AFDS
from .util import ESTADO_FINAL, ESTADO_TRAMPA


def lexer(tiny: str, *, debug: bool = False) -> list:
    tokens = []
    posicion = 0

    while posicion < len(tiny):
        comienzo_lexema = posicion

        lexema = ""
        lexema_con_un_caracter_mas = ""

        posibles_tokens = []
        posibles_tokens_con_un_caracter_mas = []

        lexema_invalido = False

        while not lexema_invalido and posicion <= len(tiny):
            lexema = tiny[comienzo_lexema:posicion]
            lexema_con_un_caracter_mas = tiny[comienzo_lexema : posicion + 1]

            posibles_tokens = posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas = []

            lexema_invalido = True

            for afd in AFDS:
                estado = afd.eval(lexema_con_un_caracter_mas)

                if estado == ESTADO_FINAL:
                    posibles_tokens_con_un_caracter_mas.append(str(afd))

                # mientras alguno de los afds no esté en un estado trampa, aún
                # existe la posibilidad de que el lexema sea aceptado
                if estado != ESTADO_TRAMPA:
                    lexema_invalido = False

            posicion += 1

        if len(posibles_tokens) == 0:
            tokens.append(("ERROR", lexema_con_un_caracter_mas))
            continue

        posicion -= 1
        tokens.append((posibles_tokens[0], lexema))

    if debug: return tokens

    tokens_sin_whitespace = list(filter(lambda t: t[0] != "WHITESPACE", tokens))
    return tokens_sin_whitespace
