# Expresiones regulares y autómatas finitos determinísticos para el lenguaje TINY

La lista de tokens utilizados por el lexer, junto con sus respectivos lexemas válidos, es la siguiente.

- `(PROGRAM, "program")`
- `(VAR, "var")`
- `(INT, "int")`
- `(BOOL, "bool")`
- `(TRUE, "true")`
- `(FALSE, "false")`
- `(BEGIN, "begin")`
- `(END, "end")`
- `(IF, "if")`
- `(ELSE, "else")`
- `(NOT, "not")`
- `(GOTO, "goto")`
- `(LET, "let")`
- `(AND, "and")`
- `(OR, "or")`
- `(DOT, ".")`
- `(SEMICOLON, ";")`
- `(COLON, ":")`
- `(ELLIPSIS, "...")`
- `(ASSIGN, "=")`
- `(LPAREN, "(")`
- `(RPAREN, ")")`
- `(PLUS, "+")`
- `(MINUS, "-")`
- `(ASTERISK, "*")`
- `(EQUAL, "==")`
- `(NOT_EQUAL, "<>")`
- `(LESS_THAN, "<")`
- `(GREATER_THAN, ">")`
- `(LESS_EQUAL, "<=")`
- `(GREATER_EQUAL, ">=")`
- `(ID, id)` (A-Z, a-z y 0-9, pero no puede comenzar con un número)
- `(NUMBER, num)` (solo se considera el conjunto $\mathbb{Z}$)
- `(WHITESPACE, " " | "\t" | "\n")`

> [!warning]
> El token `WHITESPACE` se utiliza internamente por cuestiones de legibilidad del código fuente y facilidad de desarrollo (del lexer). No forma parte de la gramática, ni de la salida del lexer.

A continuación, se encuentran detallados cada uno de ellos, incluyendo su expresión regular y autómata finito determinístico (AFD) correspondiente.

> [!note]
> Se utiliza $\beta$ como cadena en blanco, y $\lambda$ como cadena vacía.

## PROGRAM

```math
\text{"program"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3(("q3"))
    q4(("q4"))
    q5(("q5"))
    q6(("q6"))
    q7((("q7")))
    T(("T"))

    q0 -- "p" --> q1 -- "r" --> q2 -- "o" --> q3 -- "g" --> q4 -- "r" --> q5 -- "a" --> q6 -- "m" --> q7
    q0 & q1 & q2 & q3 & q4 & q5 & q6 & q7 & T -- "..." --> T
```

## VAR

```math
\text{"var"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3((("q3")))
    T(("T"))

    q0 -- "v" --> q1 -- "a" --> q2 -- "r" --> q3
    q0 & q1 & q2 & q3 & T -- "..." --> T
```

## INT

```math
\text{"int"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3((("q3")))
    T(("T"))

    q0 -- "i" --> q1 -- "n" --> q2 -- "t" --> q3
    q0 & q1 & q2 & q3 & T -- "..." --> T
```

## BOOL

```math
\text{"bool"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3(("q3"))
    q4((("q4")))
    T(("T"))

    q0 -- "b" --> q1 -- "o" --> q2 -- "o" --> q3 -- "l" --> q4
    q0 & q1 & q2 & q3 & q4 & T -- "..." --> T
```

## TRUE

```math
\text{"true"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3(("q3"))
    q4((("q4")))
    T(("T"))

    q0 -- "t" --> q1 -- "r" --> q2 -- "u" --> q3 -- "e" --> q4
    q0 & q1 & q2 & q3 & q4 & T -- "..." --> T
```

## FALSE

```math
\text{"false"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3(("q3"))
    q4(("q4"))
    q5((("q5")))
    T(("T"))

    q0 -- "f" --> q1 -- "a" --> q2 -- "l" --> q3 -- "s" --> q4 -- "e" --> q5
    q0 & q1 & q2 & q3 & q4 & q5 & T -- "..." --> T
```

## BEGIN

```math
\text{"begin"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3(("q3"))
    q4(("q4"))
    q5((("q5")))
    T(("T"))

    q0 -- "b" --> q1 -- "e" --> q2 -- "g" --> q3 -- "i" --> q4 -- "n" --> q5
    q0 & q1 & q2 & q3 & q4 & q5 & T -- "..." --> T
```

## END

```math
\text{"end"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3((("q3")))
    T(("T"))

    q0 -- "e" --> q1 -- "n" --> q2 -- "d" --> q3
    q0 & q1 & q2 & q3 & T -- "..." --> T
```

## IF

```math
\text{"if"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2((("q2")))
    T(("T"))

    q0 -- "i" --> q1 -- "f" --> q2
    q0 & q1 & q2 & T -- "..." --> T
```

## ELSE

```math
\text{"else"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3(("q3"))
    q4((("q4")))
    T(("T"))

    q0 -- "e" --> q1 -- "l" --> q2 -- "s" --> q3 -- "e" --> q4
    q0 & q1 & q2 & q3 & q4 & T -- "..." --> T
```

## NOT

```math
\text{"not"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3((("q3")))
    T(("T"))

    q0 -- "n" --> q1 -- "o" --> q2 -- "t" --> q3
    q0 & q1 & q2 & q3 & T -- "..." --> T
```

## GOTO

```math
\text{"goto"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3(("q3"))
    q4((("q4")))
    T(("T"))

    q0 -- "g" --> q1 -- "o" --> q2 -- "t" --> q3 -- "o" --> q4
    q0 & q1 & q2 & q3 & q4 & T -- "..." --> T
```

## LET

```math
\text{"let"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3((("q3")))
    T(("T"))

    q0 -- "l" --> q1 -- "e" --> q2 -- "t" --> q3
    q0 & q1 & q2 & q3 & T -- "..." --> T
```

## AND

```math
\text{"and"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3((("q3")))
    T(("T"))

    q0 -- "a" --> q1 -- "n" --> q2 -- "d" --> q3
    q0 & q1 & q2 & q3 & T -- "..." --> T
```

## OR

```math
\text{"or"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2((("q2")))
    T(("T"))

    q0 -- "o" --> q1 -- "r" --> q2
    q0 & q1 & q2 & T -- "..." --> T
```

## DOT

```math
\text{"."}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 -- "." --> q1
    q0 & q1 & T -- "..." --> T
```

## SEMICOLON

```math
\text{";"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 -- ";" --> q1
    q0 & q1 & T -- "..." --> T
```

## COLON

```math
\text{":"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 -- ":" --> q1
    q0 & q1 & T -- "..." --> T
```

## ELLIPSIS

```math
\text{"} \dots \text{"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2(("q2"))
    q3((("q3")))
    T(("T"))

    q0 -- "." --> q1 -- "." --> q2 -- "." --> q3
    q0 & q1 & q2 & q3 & T -- "..." --> T
```

## ASSIGN

```math
\text{"="}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 -- "=" --> q1
    q0 & q1 & T -- "..." --> T
```

## LPAREN

```math
\text{"} \left( \right. \text{"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 -- "(" --> q1
    q0 & q1 & T -- "..." --> T
```

## RPAREN

```math
\text{"} \left. \right) \text{"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 -- ")" --> q1
    q0 & q1 & T -- "..." --> T
```

## PLUS

```math
\text{"+"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 -- "\+" --> q1
    q0 & q1 & T -- "..." --> T
```

## MINUS

```math
\text{"-"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 -- "\-" --> q1
    q0 & q1 & T -- "..." --> T
```

## ASTERISK

```math
\text{"*"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 -- "\*" --> q1
    q0 & q1 & T -- "..." --> T
```

## EQUAL

```math
\text{"=="}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2((("q2")))
    T(("T"))

    q0 -- "=" --> q1 -- "=" --> q2
    q0 & q1 & q2 & T -- "..." --> T
```

## NOT_EQUAL

```math
\text{"<>"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2((("q2")))
    T(("T"))

    q0 -- "\<" --> q1 -- "\>" --> q2
    q0 & q1 & q2 & T -- "..." --> T
```

## LESS_THAN

```math
\text{"<"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 -- "\<" --> q1
    q0 & q1 & T -- "..." --> T
```

## GREATER_THAN

```math
\text{">"}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 -- "\>" --> q1
    q0 & q1 & T -- "..." --> T
```

## LESS_EQUAL

```math
\text{"<="}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2((("q2")))
    T(("T"))

    q0 -- "\<" --> q1 -- "=" --> q2
    q0 & q1 & q2 & T -- "..." --> T
```

## GREATER_EQUAL

```math
\text{">="}
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2((("q2")))
    T(("T"))

    q0 -- "\>" --> q1 -- "=" --> q2
    q0 & q1 & q2 & T -- "..." --> T
```

## ID

```math
\left( \text{"A"} + ... + \text{"Z"} + \text{"a"} + ... + \text{"z"} \right) \left( \text{"A"} + ... + \text{"Z"} + \text{"a"} + ... + \text{"z"} + 0 + ... + 9 \right)^*
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 -- "A-Z, a-z" --> q1
    q1 -- "A-Z, a-z, 0-9" --> q1
    q0 & q1 & T -- "..." --> T
```

## NUMBER

```math
\left( \text{"-"} + \lambda \right) \left( 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 \right)^+
```

```mermaid
flowchart LR
    q0(("q0"))
    q1(("q1"))
    q2((("q2")))
    T(("T"))

    q0 -- "\-" --> q1
    q0 & q1 & q2 -- "0-9" --> q2
    q0 & q1 & q2 & T -- "..." --> T
```

## WHITESPACE

```math
\left( \beta + \text{"\\t"} + \text{"\\n"} \right)^+
```

```mermaid
flowchart LR
    q0(("q0"))
    q1((("q1")))
    T(("T"))

    q0 & q1 -- "β, \t, \n" --> q1
    q0 & q1 & T -- "..." --> T
```
