from util import ESTADO_FINAL, ESTADO_NO_FINAL, ESTADO_TRAMPA


class AFD:
    def __init__(
        self,
        token: str,
        delta: dict[int, dict[str, int]],
        estados_finales: list[int],
        estado_inicial: int = 0,
    ):
        self.token = token
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales
        self.delta = delta
        self.estado = estado_inicial

    def __str__(self):
        return self.token

    def eval(self, lexema: str):
        self.estado = self.estado_inicial

        for caracter in lexema:
            if caracter not in self.delta.get(self.estado, dict()).keys():
                self.estado = -1
                break

            self.estado = self.delta[self.estado][caracter]

        if self.estado == -1:
            return ESTADO_TRAMPA

        return ESTADO_FINAL if self.estado in self.estados_finales else ESTADO_NO_FINAL
