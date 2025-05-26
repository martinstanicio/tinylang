# TINY

Si bien se especifica a continuación la gramática en la notación usual $G = \left< VN, VT, P, S \right>$, detallando cada una de los 4 elementos de la gramática, se hacen las siguientes aclaraciones para que puedan leer la gramática más fácilmente desde las producciones si lo desean:

- El símbolo inicial o distinguido es $program$.
- Los terminales comienzan con minúsculas.
- Los no terminales comienzan en mayúsculas, pudiendo contener mayúsculas intermedias para aclarar su significado, y se escriben en itálica.
- Terminales y no Terminales se hallan separados por espacios en blanco para claridad de la gramática.

## No terminales

```math
VN = \set{
  TCode,
  Body,
  DecVarList,
  DecVar,
  DecVarBody,
  Statement,
  StatementList,
  StatementBody,
  Goto,
  Assignment,
  Op,
  MatOp,
  BoolOp,
  Lvalue,
  Rvalue,
  Conditional,
  CompExpr,
  CompOp
}
```

## Terminales

```math
VT = \set{
  program,
  var,
  int,
  bool,
  true,
  false,
  begin,
  end,
  if,
  else,
  not,
  goto,
  let,
  and,
  or,
  id,
  num,
  .,
  ;,
  :,
  \dots,
  =,
  (,
  ),
  +,
  -,
  *,
  ==,
  <>,
  <,
  >,
  <=,
  >=
}
```

## Símbolo distinguido

```math
S = TCode
```

## Producciones

```math
P = \left\{
  \begin{array}{l}
    TCode \to \text{program id .} \space Body \\
    Body \to \text{begin} \space StatementList \space \text{end} | \text{var} \space DecVar \space DecVarList \space \text{begin} \space StatementList \space \text{end} \\
    DecVarList \to DecVarList \space DecVar | \lambda \\
    DecVar \to \text{id :} \space DecVarBody \\
    DecVarBody \to \text{int} \left( \text{num} \dots \text{num} \right) \text{= num ;} | \text{bool = true ;} | \text{bool = false ;} \\
    StatementList \to StatementList Statement | \lambda \\
    Statement \to \text{id :} \space StatementBody | StatementBody \\
    StatementBody \to Assignment | Conditional | Goto \\
    Goto \to \text{goto id ;} \\
    Assignment \to \text{let} \space Lvalue \space  \text{=} \space Rvalue \space \text{;} | \text{let} \space Lvalue \space \text{=} \space Rvalue \space Op \space Rvalue \space \text{;} | \text{let} \space Lvalue \space \text{=} \space \text{not} \space Rvalue \space \text{;} \\
    Op \to MatOp | BoolOp \\
    MatOp \to \text{+} | \text{-} | \text{*} \\
    BoolOp \to \text{or} | \text{and} \\
    Lvalue \to \text{id} \\
    Rvalue \to \text{id} | \text{num} | \text{true} | \text{false} \\
    Conditional \to \text{if} \space CompExpr \space \text{goto id ; else goto id ;} | \text{if} \space CompExpr \space \text{goto id ;} \\
    CompExpre \to Rvalue \space CompOp \space Rvalue \\
    CompOp \to| \text{==} | \text{<>} | \text{<} | \text{>} | \text{<=} | \text{>=} \\
  \end{array}
\right\}
```
