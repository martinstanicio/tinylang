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
                f"Se esperaba {tipo_token_esperado}, pero se encontró {tipo_token} en posición {self.i}"
            )

        self.i += 1

    def parse(self):
        self.producciones.clear()
        self.i = 0

        self.TCode()
        return self.producciones

    # TCode -> program id . Body
    def TCode(self):
        self.producciones.append("TCode -> program id . Body")
        self.consumir("PROGRAM")
        self.consumir("ID")
        self.consumir("DOT")
        self.Body()

    # Body -> begin StatementList end
    # Body -> var DecVar DecVarList begin StatementList end
    def Body(self):
        tipo_token, _ = self.token_actual()

        match tipo_token:
            case "BEGIN":
                self.producciones.append("Body -> begin StatementList end")
            case "VAR":
                self.producciones.append(
                    "Body -> var DecVar DecVarList begin StatementList end"
                )
                self.consumir("VAR")
                self.DecVar()
                self.DecVarList()
            case _:
                raise ParseError(
                    f"Body: se esperaba BEGIN, o VAR, pero se obtuvo {tipo_token}"
                )

        self.consumir("BEGIN")
        self.StatementList()
        self.consumir("END")

    # DecVarList -> DecVar DecVarList
    # DecVarList -> λ
    def DecVarList(self):
        tipo_token, _ = self.token_actual()

        if tipo_token == "ID":
            self.producciones.append("DecVarList -> DecVar DecVarList")
            self.DecVar()
            self.DecVarList()
        else:
            self.producciones.append("DecVarList -> λ")

    # DecVar -> id : DecVarBody ;
    def DecVar(self):
        self.producciones.append("DecVar -> id : DecVarBody ;")
        self.consumir("ID")
        self.consumir("COLON")
        self.DecVarBody()
        self.consumir("SEMICOLON")

    # DecVarBody -> int ( num ... num ) = num
    # DecVarBody -> bool = DecVarBody'
    def DecVarBody(self):
        tipo_token, _ = self.token_actual()

        match tipo_token:
            case "INT":
                self.producciones.append("DecVarBody -> int ( num ... num ) = num")
                self.consumir("INT")
                self.consumir("LPAREN")
                self.consumir("NUMBER")
                self.consumir("ELLIPSIS")
                self.consumir("NUMBER")
                self.consumir("RPAREN")
                self.consumir("ASSIGN")
                self.consumir("NUMBER")
            case "BOOL":
                self.producciones.append("DecVarBody -> bool = DecVarBody'")
                self.consumir("BOOL")
                self.consumir("ASSIGN")
                self.DecVarBodyP()
            case _:
                raise ParseError(
                    f"DecVarBody: se esperaba INT, o BOOL, pero se obtuvo {tipo_token}"
                )

    # DecVarBody' -> true
    # DecVarBody' -> false
    def DecVarBodyP(self):
        tipo_token, _ = self.token_actual()

        match tipo_token:
            case "TRUE":
                self.producciones.append("DecVarBody' -> true")
                self.consumir("TRUE")
            case "FALSE":
                self.producciones.append("DecVarBody' -> false")
                self.consumir("FALSE")
            case _:
                raise ParseError(
                    f"DecVarBodyP: se esperaba TRUE, o FALSE, pero se obtuvo {tipo_token}"
                )

    # StatementList -> Statement StatementList
    # StatementList -> λ
    def StatementList(self):
        tipo_token, _ = self.token_actual()

        if tipo_token in ["ID", "LET", "IF", "GOTO"]:
            self.producciones.append("StatementList -> Statement StatementList")
            self.Statement()
            self.StatementList()
        else:
            self.producciones.append("StatementList -> λ")

    # Statement -> id : StatementBody
    # Statement -> StatementBody
    def Statement(self):
        tipo_token, _ = self.token_actual()

        if tipo_token == "ID":
            self.producciones.append("Statement -> id : StatementBody")
            self.consumir("ID")
            self.consumir("COLON")
        else:
            self.producciones.append("Statement -> StatementBody")

        self.StatementBody()

    # StatementBody -> Assignment
    # StatementBody -> Conditional
    # StatementBody -> Goto
    def StatementBody(self):
        tipo_token, _ = self.token_actual()

        match tipo_token:
            case "LET":
                self.producciones.append("StatementBody -> Assignment")
                self.Assignment()
            case "IF":
                self.producciones.append("StatementBody -> Conditional")
                self.Conditional()
            case "GOTO":
                self.producciones.append("StatementBody -> Goto")
                self.Goto()
            case _:
                raise ParseError(
                    f"StatementBody: se esperaba LET, IF, o GOTO, pero se obtuvo {tipo_token}"
                )

    # Goto -> goto id ;
    def Goto(self):
        self.producciones.append("Goto -> goto id ;")
        self.consumir("GOTO")
        self.consumir("ID")
        self.consumir("SEMICOLON")

    # Assignment -> let Lvalue = Assignment' ;
    def Assignment(self):
        self.producciones.append("Assignment -> let Lvalue = Assignment' ;")
        self.consumir("LET")
        self.Lvalue()
        self.consumir("ASSIGN")
        self.AssignmentP()
        self.consumir("SEMICOLON")

    # Assignment' -> Rvalue Assignment''
    # Assignment' -> not Rvalue
    def AssignmentP(self):
        tipo_token, _ = self.token_actual()

        match tipo_token:
            case "ID" | "NUMBER" | "TRUE" | "FALSE":
                self.producciones.append("Assignment' -> Rvalue Assignment''")
                self.Rvalue()
                self.AssignmentPP()
            case "NOT":
                self.producciones.append("Assignment' -> not Rvalue")
                self.consumir("NOT")
                self.Rvalue()
            case _:
                raise ParseError(
                    f"AssignmentP: se esperaba ID, NUMBER, TRUE, FALSE, o NOT, pero se obtuvo {tipo_token}"
                )

    # Assignment'' -> Op Rvalue
    # Assignment'' -> λ
    def AssignmentPP(self):
        tipo_token, _ = self.token_actual()

        if tipo_token in ["PLUS", "MINUS", "ASTERISK", "OR", "AND"]:
            self.producciones.append("Assignment'' -> Op Rvalue")
            self.Op()
            self.Rvalue()
        else:
            self.producciones.append("Assignment'' -> λ")

    # Op -> MatOp
    # Op -> BoolOp
    def Op(self):
        tipo_token, _ = self.token_actual()

        match tipo_token:
            case "PLUS" | "MINUS" | "ASTERISK":
                self.producciones.append("Op -> MatOp")
                self.MatOp()
            case "OR" | "AND":
                self.producciones.append("Op -> BoolOp")
                self.BoolOp()
            case _:
                raise ParseError(
                    f"Op: se esperaba PLUS, MINUS, ASTERISK, OR, o AND, pero se obtuvo {tipo_token}"
                )

    # MatOp -> +
    # MatOp -> -
    # MatOp -> *
    def MatOp(self):
        tipo_token, _ = self.token_actual()

        match tipo_token:
            case "PLUS":
                self.producciones.append("MatOp -> +")
                self.consumir("PLUS")
            case "MINUS":
                self.producciones.append("MatOp -> -")
                self.consumir("MINUS")
            case "ASTERISK":
                self.producciones.append("MatOp -> *")
                self.consumir("ASTERISK")
            case _:
                raise ParseError(
                    f"MatOp: se esperaba PLUS, MINUS, o ASTERISK, pero se obtuvo {tipo_token}"
                )

    # BoolOp -> or
    # BoolOp -> and
    def BoolOp(self):
        tipo_token, _ = self.token_actual()

        match tipo_token:
            case "OR":
                self.producciones.append("BoolOp -> +")
                self.consumir("OR")
            case "AND":
                self.producciones.append("BoolOp -> -")
                self.consumir("AND")
            case _:
                raise ParseError(
                    f"BoolOp: se esperaba OR, o AND, pero se obtuvo {tipo_token}"
                )

    # Lvalue -> id
    def Lvalue(self):
        self.producciones.append("Lvalue -> id")
        self.consumir("ID")

    # Rvalue -> id
    # Rvalue -> num
    # Rvalue -> true
    # Rvalue -> false
    def Rvalue(self):
        tipo_token, _ = self.token_actual()

        match tipo_token:
            case "ID":
                self.producciones.append("Rvalue -> id")
                self.consumir("ID")
            case "NUMBER":
                self.producciones.append("Rvalue -> num")
                self.consumir("NUMBER")
            case "TRUE":
                self.producciones.append("Rvalue -> true")
                self.consumir("TRUE")
            case "FALSE":
                self.producciones.append("Rvalue -> false")
                self.consumir("FALSE")
            case _:
                raise ParseError(
                    f"Rvalue: se esperaba ID, NUMBER, TRUE, o FALSE, pero se obtuvo {tipo_token}"
                )

    # Conditional -> if CompExpr Goto Conditional'
    def Conditional(self):
        self.producciones.append("Conditional -> if CompExpr Goto Conditional'")
        self.consumir("IF")
        self.CompExpr()
        self.Goto()
        self.ConditionalP()

    # Conditional' -> else Goto
    # Conditional' -> λ
    def ConditionalP(self):
        tipo_token, _ = self.token_actual()

        if tipo_token == "ELSE":
            self.producciones.append("Conditional' -> else Goto")
            self.consumir("ELSE")
            self.Goto()
        else:
            self.producciones.append("Conditional' -> λ")

    # CompExpr -> Rvalue CompOp Rvalue
    def CompExpr(self):
        self.producciones.append("CompExpr -> Rvalue CompOp Rvalue")
        self.Rvalue()
        self.CompOp()
        self.Rvalue()

    # CompOp -> ==
    # CompOp -> <>
    # CompOp -> <
    # CompOp -> >
    # CompOp -> <=
    # CompOp -> >=
    def CompOp(self):
        tipo_token, _ = self.token_actual()

        match tipo_token:
            case "EQUAL":
                self.producciones.append("CompOp -> ==")
                self.consumir("EQUAL")
            case "NOT_EQUAL":
                self.producciones.append("CompOp -> <>")
                self.consumir("NOT_EQUAL")
            case "LESS_THAN":
                self.producciones.append("CompOp -> <")
                self.consumir("LESS_THAN")
            case "GREATER_THAN":
                self.producciones.append("CompOp -> >")
                self.consumir("GREATER_THAN")
            case "LESS_EQUAL":
                self.producciones.append("CompOp -> <=")
                self.consumir("LESS_EQUAL")
            case "GREATER_EQUAL":
                self.producciones.append("CompOp -> >=")
                self.consumir("GREATER_EQUAL")
            case _:
                raise ParseError(
                    f"CompOp: se esperaba EQUAL, NOT_EQUAL, LESS_THAN, GREATER_THAN, LESS_EQUAL, o GREATER_EQUAL, pero se obtuvo {tipo_token}"
                )


def parser(tokens):
    p = Parser(tokens)
    return p.parse()
