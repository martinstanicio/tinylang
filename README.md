# Tinylang

Implementación en Python de un analizador lexicográfico (lexer) y analizador sintáctico (parser), para el lenguaje de programación [TINY](docs/tiny.md).

El lexer toma como entrada código fuente escrito en [TINY](docs/tiny.md), y produce como salida una lista de tokens de forma `(tipo_token, lexema)`. El listado de tokens, REGEX y AFD utilizados se encuentra en [regexp-afd](docs/regexp-afd.md).
