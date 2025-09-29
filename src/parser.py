from typing import List

from .util import Token


class ParseError(Exception):
    pass


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens + [("EOF", "#")]
        self.i = 0
        self.producciones: List[str] = []

    def token_actual(self):
        return self.tokens[self.i]

    def token_siguiente(self):
        return self.tokens[self.i + 1]

    def consumir(self, tipo_token_esperado: str):
        tipo_token, _ = self.token_actual()

        if tipo_token != tipo_token_esperado:
            raise ParseError(
                f"Se esperaba {tipo_token_esperado} pero se encontró {tipo_token} en posición {self.i}"
            )

        self.i += 1

    def parse(self):
        self.producciones.clear()
        self.i = 0

        self.TCode()
        return self.producciones

    # TCode -> program id . Body
    def TCode(self):
        raise NotImplementedError

    # Body -> begin StatementList end
    # Body -> var DecVar DecVarList begin StatementList end
    def Body(self):
        raise NotImplementedError

    # DecVarList -> DecVar DecVarList
    # DecVarList -> λ
    def DecVarList(self):
        raise NotImplementedError

    # DecVar -> id : DecVarBody ;
    def DecVar(self):
        raise NotImplementedError

    # DecVarBody -> int ( num ... num ) = num
    # DecVarBody -> bool = DecVarBody'
    def DecVarBody(self):
        raise NotImplementedError

    # DecVarBody' -> true
    # DecVarBody' -> false
    def DecVarBodyP(self):
        raise NotImplementedError

    # StatementList -> Statement StatementList
    # StatementList -> λ
    def StatementList(self):
        raise NotImplementedError

    # Statement -> id : StatementBody
    # Statement -> StatementBody
    def Statement(self):
        raise NotImplementedError

    # StatementBody -> Assignment
    # StatementBody -> Conditional
    # StatementBody -> Goto
    def StatementBody(self):
        raise NotImplementedError

    # Goto -> goto id ;
    def Goto(self):
        raise NotImplementedError

    # Assignment -> let Lvalue = Assignment' ;
    def Assignment(self):
        raise NotImplementedError

    # Assignment' -> Rvalue Assignment''
    # Assignment' -> not Rvalue
    def AssignmentP(self):
        raise NotImplementedError

    # Assignment'' -> Op Rvalue
    # Assignment'' -> λ
    def AssignmentPP(self):
        raise NotImplementedError

    # Op -> MatOp
    # Op -> BoolOp
    def Op(self):
        raise NotImplementedError

    # MatOp -> +
    # MatOp -> -
    # MatOp -> *
    def MatOp(self):
        raise NotImplementedError

    # BoolOp -> or
    # BoolOp -> and
    def BoolOp(self):
        raise NotImplementedError

    # Lvalue -> id
    def Lvalue(self):
        raise NotImplementedError

    # Rvalue -> id
    # Rvalue -> num
    # Rvalue -> true
    # Rvalue -> false
    def Rvalue(self):
        raise NotImplementedError

    # Conditional -> if CompExpr Goto Conditional'
    def Conditional(self):
        raise NotImplementedError

    # Conditional' -> else Goto
    # Conditional' -> λ
    def ConditionalP(self):
        raise NotImplementedError

    # CompExpr -> Rvalue CompOp Rvalue
    def CompExpr(self):
        raise NotImplementedError

    # CompOp -> ==
    # CompOp -> <>
    # CompOp -> <
    # CompOp -> >
    # CompOp -> <=
    # CompOp -> >=
    def CompOp(self):
        raise NotImplementedError


def parser(tokens):
    p = Parser(tokens)
    return p.parse()
