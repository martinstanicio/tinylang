# Tinylang

Implementación en Python de un analizador lexicográfico (lexer) y analizador sintáctico (parser) para el lenguaje de programación [TINY](docs/tiny.md).

El **analizador lexicográfico (lexer)** toma como entrada código fuente escrito en [TINY](docs/tiny.md) y produce como salida una lista de tokens de forma `(tipo_token, lexema)`.
Luego, el **analizador sintáctico (parser)** procesa la secuencia de tokens generada por el lexer y calcula la derivación desde el símbolo distinguido para la cadena, es decir, qué producciones se deben utilizar para pasar del símbolo distinguido a la cadena final.

> [!important]
> El listado de tokens, expresiones regulares y AFD utilizados se encuentra en [regexp-afd](docs/regexp-afd.md).

## Estructura del proyecto

```text
tinylang/
├── docs/
│   ├── regexp-afd.md  # Tokens, REGEXs y AFDs utilizados
│   └── tiny.md        # Definición de la gramática del lenguaje TINY
├── src/
│   ├── __init__.py
│   ├── afd.py
│   ├── lexer.py
│   ├── parser.py
│   ├── tokens.py
│   └── util.py
├── tiny/              # Archivos de prueba en lenguaje TINY
│   └── ...
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Ejecutar el analizador completo

Para procesar todos los archivos de prueba y generar un reporte completo:

```bash
uv run main.py
```

Este comando:

1. Lee todos los archivos `.tiny` del directorio `tiny/`
2. Ejecuta el lexer en cada archivo
3. Si no hay errores léxicos, ejecuta el parser
4. Genera un archivo `dist/output.md` con los resultados
