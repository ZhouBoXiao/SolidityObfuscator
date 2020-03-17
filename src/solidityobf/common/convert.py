import sys
# from antlr4 import *
# from antlr4.InputStream import InputStream
import antlr3
from antlr4 import FileStream
import antlr4

from solidityobf.common.colors import RED
from solidityobf.common.classes import Statements, Program, VarDeclaration, Ident, \
    Return, \
    Function, Listarguments, If, For, \
    While, DoWhile, Throw, \
    Break, Continue, Number, \
    Ternary, String, Assignment, \
    Expr, New, Ltrue, Lfalse, Index, \
    Functioncall, Contract, Returns, ModifierList, Address, Int, Uint, \
    ArrayDeclaration, StateVariableDeclaration, StateArrayDeclaration, Emit, Inheritance, StructDefinition, \
    EventDefinition, Modifier, EnumDefinition, UsingForDeclaration, ConstructorDefinition, ModifierInvocation, Property
# from solidityobf.parser.SolidityLexer import SolidityLexer
# from solidityobf.parser.SolidityParser import SolidityParser
# from solidityobf.parser.SolidityListener import SolidityListener
from solidityobf.par.solLexer import solLexer
from solidityobf.par.solParser import solParser
from solidityobf.parser.JavaScriptLexer import JavaScriptLexer
from solidityobf.parser.JavaScriptParser import JavaScriptParser
from solidityobf.parser.SolidityLexer import SolidityLexer
from solidityobf.parser.SolidityListener import SolidityListener
from solidityobf.parser.SolidityParser import SolidityParser


def statement_convertor(t):
    if not isinstance(t, Statements):
        t = Statements([t])
    return t

def getTypeName(tree):
    return tree.children[0].children[0].symbol.text


def convert1(path, verbose=0):
    input_stream = FileStream(path)
    lexer = SolidityLexer(input_stream)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = SolidityParser(token_stream)
    program = parser.sourceUnit()
    # contract = program.contractDefinition()
    # listener = SolidityListener()
    # walker = ParseTreeWalker()
    # walker.walk(listener, program)

    # print('result_stack=', listener.stack)
    return convertTree(program, verbose)


def convertTree(tree, verbose=0):
    # global type
    p = []
    if type(tree).__name__ == "TerminalNodeImpl":
        if tree.symbol.text == "<EOF>":
            return
    # if tree.symbol.text in ('{', '}', ';'):
    #     return p
    # else:
    #     return tree.symbol.text
    children = tree.children

    # if verbose > 3:
    #     print tree.getLine(), ":", type(tree).__name__
    # type(tree).__name__

    if type(tree).__name__ == "SourceUnitContext":
        p = Program([convertTree(c, verbose) for c in children[:-1]])
        # print p.oneline_str()
    elif type(tree).__name__ == "PragmaDirective":
        pass
    elif type(tree).__name__ == "ImportDirectiveContext":
        pass
    elif type(tree).__name__ == "ContractDefinitionContext":
        t = children[0].symbol.text  # contract | library  | interface
        l = []  # contratPart
        i = None  # identifier
        inheritance = []
        for c in children:
            if type(c).__name__ == "ContractPartContext":
                l.append(convertTree(c.children[0], verbose))
            elif type(c).__name__ == "IdentifierContext":
                i = convertTree(c, verbose)
            elif type(c).__name__ == "InheritanceSpecifierContext":
                inheritance.append(convertTree(c, verbose))
        p = Contract(t, i, inheritance, l)

    elif type(tree).__name__ == "InheritanceSpecifierContext":
        i = convertTree(children[0].children[0])
        l = []
        for c in children:
            if type(c).__name__ == "ExpressionContext":
                l.append(convertTree(c, verbose))
        p = Inheritance(i, l)

    # elif type(tree).__name__ == "ContractPartContext":
    #     o = [convertTree(c, verbose) for c in children]
    #     p = ContractPart(o)
    # if type(tree).__name__ == "SimpleStatementContext":
    #     o = [convertTree(c, verbose) for c in children]
    #     p = SimpleStatement(o)
    elif type(tree).__name__ == "VariableDeclarationStatementContext":
        typeName = None
        i = None
        keywords = []
        e = None
        for c in children:
            if type(c).__name__ == "ExpressionContext":
                e = convertTree(c, verbose)
        for c in children[0].children:
            if type(c).__name__ == "IdentifierContext":
                i = convertTree(c, verbose)
            elif type(c).__name__ == "StorageLocationContext":
                keywords.append(c.children[0].symbol.text)
        if len(children[0].children[0].children) == 2:
            elist = []
            t = None

            if type(children[0].children[0].children[1]).__name__ == "ArrayContext":
                # t = getTypeName(children[0].children[0].children[0])
                cc = children[0].children[0].children[0]
                while type(cc).__name__ != "TerminalNodeImpl":
                    cc = cc.children[0]
                t = cc.symbol.text
                for c in children[0].children[1].children:
                    if type(c).__name__ == "ExpressionContext":
                        elist.append(convertTree(c, verbose))
            p = ArrayDeclaration(t, keywords, i, elist, e)
        else:
            cc = children[0].children[0]
            while type(cc).__name__ != "TerminalNodeImpl":
                cc = cc.children[0]
            t = cc.symbol.text
            p = VarDeclaration(t, keywords, i, e)
        # for c in children:
        #     if type(c).__name__ == "VariableDeclarationContext":
        #         for cc in c.children:
        #             if type(cc).__name__ == "TypeNameContext":
        #                 typeName = getTypeName(cc)
        #             elif type(cc).__name__ == "StorageLocationContext":
        #                 keywords.append(cc.children[0].symbol.text)
        #             elif type(cc).__name__ == "IdentifierContext":
        #                 i = convertTree(cc, verbose)
        # p = VarDeclaration(typeName, keywords, i, e)

    elif type(tree).__name__ == "StatementContext":
        if type(children[0]).__name__ == "SimpleStatementContext":
            p = convertTree(children[0].children[0], verbose)
        else:
            p = convertTree(children[0])
    # if type(tree).__name__ == "ExpressionContext":
    elif type(tree).__name__ == "ExpressionStatementContext":
        p = convertTree(children[0], verbose)
    # #if type(tree).__name__ == "ExpressionContext":

    elif type(tree).__name__ == "StateVariableDeclarationContext":
        keywords = []
        i = None
        e = None
        elist = []
        t = ""
        for c in children:
            if type(c).__name__ == "IdentifierContext":
                i = convertTree(c, verbose)
            elif type(c).__name__ == "TerminalNodeImpl" and c.symbol.text in (
                    "public", "internal", "private", "constant"):
                keywords.append(c.symbol.text)
            elif type(c).__name__ == "ExpressionContext":
                e = convertTree(c, verbose)
        if len(children[0].children) >= 2:
            if type(children[0].children[1]).__name__ == "ArrayContext":
                cc = children[0].children[0].children[0]
                while type(cc).__name__ != "TerminalNodeImpl":
                    cc = cc.children[0]
                t = cc.symbol.text
                for c in children[0].children[1].children:
                    if type(c).__name__ == "ExpressionContext":
                        elist.append(convertTree(c, verbose))
            p = StateArrayDeclaration(t, keywords, i, elist, e)
            # print p.b()
        else:
            t = getTypeName(children[0])
            p = StateVariableDeclaration(t, keywords, i, e)

    elif type(tree).__name__ == "UsingForDeclarationContext":
        i = convertTree(children[1], verbose)
        if type(children[3]).__name__ == "TypeNameContext":
            t = convertTree(children[3].children[0].children[0], verbose)
        elif children[3].symbol.text == "*":
            t = Ident("*")
        p = UsingForDeclaration(i, t)

    elif type(tree).__name__ == "StructDefinitionContext":
        i = convertTree(children[1], verbose)
        l = [convertTree(c, verbose) for c in children if type(c).__name__ == "VariableDeclarationContext"]
        p = StructDefinition(i, l)

    elif type(tree).__name__ == "EventDefinitionContext":
        i = convertTree(children[1], verbose)  # identifier
        params = [convertTree(c, verbose) for c in children[2].children if type(c).__name__ == "EventParameterContext"]
        a = None
        if children[3].symbol.text == "anonymous":
            a = "anonymous"
        l = Listarguments(params)
        p = EventDefinition(i, l, a)

    elif type(tree).__name__ == "EventParameterContext":
        typeName = None
        i = None
        keywords = []

        for c in children:
            if type(c).__name__ == "TypeNameContext":
                typeName = getTypeName(c)
            elif type(c).__name__ == "TerminalNodeImpl":
                keywords.append(c.symbol.text)
            elif type(c).__name__ == "IdentifierContext":
                i = convertTree(c, verbose)
        p = VarDeclaration(typeName, keywords, i)

    elif type(tree).__name__ == "ConstructorDefinitionContext":
        keywords = []
        params = []
        params = [convertTree(c, verbose) for c in children[1].children if type(c).__name__ == "ParameterContext"]
        # for c in children[1].children:
        #     if type(c).__name__ == "ParameterContext":
        #         params.append(convertTree(c, verbose))
        mis = []
        for c in children[2].children:
            if type(c).__name__ == "TerminalNodeImpl":
                keywords.append(c.symbol.text)
            elif type(c).__name__ == "StateMutabilityContext":
                keywords.append(c.children[0].symbol.text)
            elif type(c).__name__ == "ModifierInvocationContext":
                mis.append(convertTree(c, verbose))
        ml = ModifierList(mis, keywords)
        s = convertTree(children[3], verbose)
        p = ConstructorDefinition(Listarguments(params), ml, s)

    elif type(tree).__name__ == "EnumDefinitionContext":
        i = convertTree(children[1], verbose)
        l = [convertTree(c.children[0], verbose) for c in children if type(c).__name__ == "EnumValueContext"]
        p = EnumDefinition(i, l)

    elif type(tree).__name__ == "ModifierDefinitionContext":
        i = None  # identifier
        s = None  # statement
        l = None  # parameterList
        params = []
        i = convertTree(children[1], verbose)
        if type(children[2]).__name__ == "BlockContext":
            s = statement_convertor(convertTree(children[2], verbose))
        elif type(children[3]).__name__ == "BlockContext":
            s = convertTree(children[3], verbose)
            l = convertTree(children[2], verbose)
            # params = [convertTree(c, verbose) for c in children[2].children if type(c).__name__ == "ParameterContext"]
            # l = Listarguments(params)
        p = Modifier(i, l, s)

    elif type(tree).__name__ == "PrimaryExpressionContext":
        if len(children) == 1:
            p = convertTree(children[0], verbose)
        elif type(children[0]).__name__ in ("IdentifierContext", "elementaryTypeNameExpressionContext"):
            if children[1].chilren[0].symbol.text == "[" and children[2].chilren[0].symbol.text == "]":
                p = [convertTree(children[0]), '[', ']']
            else:
                p = convertTree(children[0])

    elif type(tree).__name__ == "ExpressionContext":
        l = []
        typeof = ""
        if len(children) == 1:
            p = convertTree(children[0], verbose)
        elif len(children) == 2:
            for c in children:
                if type(c).__name__ == "TerminalNodeImpl":
                    if c.symbol.text in ('++', '--', '+', '-', 'after', 'delete', '!', '~'):
                        l.append(c.symbol.text)
                elif type(c).__name__ == "ExpressionContext":
                    l.append(convertTree(c, verbose))
            p = Expr(l)

        elif len(children) == 3:
            if type(children[0]).__name__ == "TerminalNodeImpl" and type(children[2]).__name__ == "TerminalNodeImpl":
                if children[0].symbol.text == '(' and children[2].symbol.text == ')':
                    l = ['(', convertTree(children[1], verbose), ')']
                    p = Expr(l)
            else:
                for c in children:
                    if type(c).__name__ == "TerminalNodeImpl":
                        # if c.symbol.text in ('=', '|=', '^=', '&=', '<<=', '>>=', '+=', '-=', '*=', '/=', '%='):
                        #     typeof = c.symbol.text

                        if c.symbol.text in ('=', '|=', '^=', '&=', '<<=', '>>=', '+=', '-=', '*=', '/=', '%=',
                                             '**', '*', '/', '%', '+', '-', '<<', '>>', '&', '^', '|', '>', '<',
                                             '<=', '>=', '==', '!=', '&&', '||', '(', ')', '.'):
                            l.append(c.symbol.text)
                    elif type(c).__name__ == "ExpressionContext":
                        l.append(convertTree(c, verbose))
                    elif type(c).__name__ == "IdentifierContext":
                        l.append(convertTree(c, verbose))
                if l[1] in ('=', '|=', '^=', '&=', '<<=', '>>=', '+=', '-=', '*=', '/=', '%='):
                    p = Assignment(l[0], l[1], l[2])
                elif l[1] == '.':
                    lis = [l[0], Property(l[2])]
                    p = Expr(lis)
                else:
                    p = Expr(l)
        elif len(children) == 4:
            if type(children[1]).__name__ == "TerminalNodeImpl" and type(children[3]).__name__ == "TerminalNodeImpl":
                if children[1].symbol.text == '[' and children[3].symbol.text == ']':
                    l = [convertTree(children[0]), '[', convertTree(children[2], verbose), ']']
                    p = Expr(l)
                elif children[1].symbol.text == '(' and children[3].symbol.text == ')':
                    # l = [convertTree(children[0]), '(', convertTree(children[2], verbose), ')']
                    # p = Expr(l)
                    e = convertTree(children[0], verbose)
                    p = Functioncall(e, convertTree(children[2]))
        elif len(children) == 5:
            l = [convertTree(c, verbose) for c in children if type(c).__name__ == "ExpressionContext"]
            Ternary(l[0], l[1], l[2])
        # for c in children:
        #     conv = convertTree(c, verbose)
        #     if conv == []:
        #         if c.symbol.text not in ('{', '}', ';', 'EOF'):
        #             l.append(c.symbol.text)
        #
        #     else:
        #         l.append(conv)
        # if len(l) == 0:
        #     p = Expr()
        # elif len(l) == 1:
        #     if isinstance(l[0], Expr):
        #         p = l[0]
        #     else:
        #         p = Expr(l)
        # elif len(l) == 3:
        #     if type(children[1]).__name__ == "TerminalNodeImpl":
        #         if children[1].symbol.text in ('=', '|=', '^=', '&=', '<<=', '>>=', '+=', '-=', '*=', '/=', '%='):
        #             v = convertTree(children[0], verbose)
        #             t = children[1].symbol.text
        #             e = convertTree(children[2], verbose)
        #             p = Assignment(v, t, e)
        # else:
        #     if l[1] == ",":
        #         p = Statements([l[i] for i in range(0, len(l) + 1, 2)])
        #     else:
        #         p = Expr(l)
    # elif type(tree).__name__ == "VarDeclaration":
    #     if len(children) > 1:
    #         p = VarDeclaration(convertTree(children[0], verbose), convertTree(children[1],verbose))
    #     else:
    #         p = VarDeclaration(convertTree(children[0], verbose))
    elif type(tree).__name__ == "IdentifierContext":
        p = Ident(children[0].symbol.text)
    # elif type(tree).__name__ == "Suffix":
    #     p = Suffix(convertTree(children[0], verbose))
    # elif type(tree).__name__ == "MemberExpr":
    #     if len(children) > 1:
    #         p = MemberExpr(convertTree(children[0], verbose), map(convertTree,children[1:]))
    #     else:
    #         p = convertTree(children[0], verbose)
    elif type(tree).__name__ == "ReturnStatementContext":
        e = None
        if len(children) == 3:
            e = convertTree(children[1], verbose)
        p = Return(e)
    # elif type(tree).__name__ == "ObjectLiteral" :
    #     o = [convertTree(c, verbose) for c in children]
    #     p = ObjectLiteral(o)
    # elif type(tree).__name__ == "PropertyGet":
    #     if children[0].text != "get":
    #         print "error expecting get"
    #         sys.exit(1)
    #     n = convertTree(children[1], verbose)
    #     b = convertTree(children[2], verbose)
    #     p = PropertyGet(n, b)
    # elif type(tree).__name__ == "PropertySet":
    #     if children[0].text != "set":
    #         print "error expecting set"
    #         sys.exit(1)
    #     n = convertTree(children[1], verbose)
    #     i = convertTree(children[2], verbose)
    #     b = convertTree(children[3], verbose)
    #     p = PropertySet(n, i, b)
    elif type(tree).__name__ == "BlockContext":
        # p = Statements(filter(lambda x: x != [], map(lambda x: convertTree(x, verbose), children[1:-1])))
        l = []
        for c in children:
            if type(c).__name__ == "StatementContext":
                l.append(convertTree(c, verbose))
        p = Statements(l)

    elif type(tree).__name__ == "ParameterListContext":
        params = [convertTree(c, verbose) for c in children if type(c).__name__ == "ParameterContext"]
        p = Listarguments(params)
    elif type(tree).__name__ == "ParameterContext":
        typeName = None
        i = None
        keywords = []
        for c in children:
            if type(c).__name__ == "StorageLocationContext":
                keywords.append(c.children[0].symbol.text)
            elif type(c).__name__ == "IdentifierContext":
                i = convertTree(c, verbose)
        if len(children[0].children) == 2:
            elist = []
            t = None
            if type(children[0].children[1]).__name__ == "ArrayContext":
                cc = children[0].children[0]
                while type(cc).__name__ != "TerminalNodeImpl":
                    cc = cc.children[0]
                t = cc.symbol.text
                for c in children[0].children[1].children:
                    if type(c).__name__ == "ExpressionContext":
                        elist.append(convertTree(c, verbose))
            p = ArrayDeclaration(t, keywords, i, elist)
        else:
            for c in children:
                if type(c).__name__ == "TypeNameContext":
                    typeName = getTypeName(c)
            p = VarDeclaration(typeName, keywords, i)

    elif type(tree).__name__ == "VariableDeclarationContext":
        typeName = None
        i = None
        keywords = []
        e = None
        for c in children:
            if type(c).__name__ == "StorageLocationContext":
                keywords.append(c.children[0].symbol.text)
            elif type(c).__name__ == "IdentifierContext":
                i = convertTree(c, verbose)
        if len(children[0].children) == 2:
            elist = []
            t = None
            if type(children[0].children[1]).__name__ == "ArrayContext":
                t = getTypeName(children[0].children[0].children[0])
                for c in children[0].children[1].children:
                    if type(c).__name__ == "ExpressionContext":
                        elist.append(convertTree(c, verbose))
            p = ArrayDeclaration(t, keywords, i, elist)
        else:
            typeName = getTypeName(children[0])
            p = VarDeclaration(typeName, keywords, i)

    elif type(tree).__name__ == "ForStatementContext":
        # if type(children[2].chilren[0]).__name__ == "variableDeclarationContext":
        i = convertTree(children[2].children[0], verbose)
        e1 = convertTree(children[3], verbose)
        e2 = convertTree(children[4], verbose)
        s = statement_convertor(convertTree(children[6], verbose))
        p = For(i, e1, e2, s)
    # if type(tree).__name__ == "TypeNameContext":
    # for c in children:
    #     if type(c).__name__ == "ElementaryTypeNameContext":
    #         p = func(c.children[0].symbol.text)
    elif type(tree).__name__ == "FunctionDefinitionContext":
        # a = convertTree(children[1], verbose)
        # s = statement_convertor(convertTree(children[1], verbose))
        i = None  # identifier
        s = None  # statement
        r = None  # returns
        ml = None  # ModifierList
        l = None  #
        params = None
        # if len(children) == 3:
        #    i = convertTree(children[2], verbose)
        i = convertTree(children[1], verbose)
        if type(children[4]).__name__ == "BlockContext":
            s = statement_convertor(convertTree(children[4], verbose))
        elif type(children[5]).__name__ == "BlockContext":
            s = statement_convertor(convertTree(children[5], verbose))
        if type(children[4]).__name__ == "ReturnParametersContext":
            # params = [convertTree(c, verbose) for c in children[4].children[1].children if type(c).__name__ == "ParameterContext"]
            l = convertTree(children[4].children[1], verbose)
            r = Returns(l)
        if type(children[3]).__name__ == "ModifierListContext":
            ml = convertTree(children[3], verbose)
        if type(children[2]).__name__ == "ParameterListContext":
            params = convertTree(children[2], verbose)
            # params = [convertTree(c, verbose) for c in children[2].children if type(c).__name__ == "ParameterContext"]
            # l = Listarguments(params)
        p = Function(i, params, ml, r, s)
        # print p.oneline_str()
    elif type(tree).__name__ == "ModifierListContext":
        mis, keywords = [], []
        if children is not None:
            for c in children:
                if type(c).__name__ == "TerminalNodeImpl":
                    keywords.append(c.symbol.text)
                elif type(c).__name__ == "StateMutabilityContext":
                    keywords.append(c.children[0].symbol.text)
                elif type(c).__name__ == "ModifierInvocationContext":
                    mis.append(convertTree(c, verbose))
        p = ModifierList(mis, keywords)
    # elif type(tree).__name__ == "EventParameterListContext":
    #     pass
    # elif type(tree).__name__ == "EventParameterContext":
    #     pass
    # elif type(tree).__name__ == "UserDefinedTypeNameContext":
    #     pass
    # elif type(tree).__name__ == "UserDefinedTypeNameContext":
    #     pass
    elif type(tree).__name__ == "EmitStatementContext":
        p = Emit(convertTree(children[1]))

    elif type(tree).__name__ == "FunctionCallContext":
        e = convertTree(children[0], verbose)
        p = Functioncall(e, convertTree(children[2]))

    elif type(tree).__name__ == "ExpressionListContext":
        p = [convertTree(c, verbose) for c in children if type(c).__name__ == "ExpressionContext"]
        # for c in children:
        #     if type(c).__name__ == "ExpressionContext":
        #         p.append(convertTree(c, verbose))
    elif type(tree).__name__ == "FunctionCallArgumentsContext":
        if type(children[0]).__name__ == "ExpressionListContext":
            p = convertTree(children[0], verbose)

    elif type(tree).__name__ == "ModifierInvocationContext":
        if len(children) == 1:
            p = convertTree(children[0], verbose)
        else:
            i, exprs = None, None
            for c in children:
                if type(c).__name__ == "IdentifierContext":
                    i = convertTree(c, verbose)
                elif type(c).__name__ == "ExpressionListContext":
                    exprs = convertTree(c, verbose)
            p = ModifierInvocation(i, exprs)

    # elif type(tree).__name__ == "VariableStatement":
    #     p = convertTree(children[0], verbose)
    # elif type(tree).__name__ == "Var":
    #     p = Var(map(lambda x:convertTree(x, verbose), children))
    # elif type(tree).__name__ == "Listarguments":
    #     p = Listarguments(map(lambda x:convertTree(x, verbose), children))
    # elif type(tree).__name__ == "Statements":
    #     s = map(lambda x: convertTree(x, verbose), children)
    #     s = filter(lambda x: x != [], s)
    #     p = Statements(s)
    #     for i in s:
    #         if i.parent != p:
    #             print RED, "error"
    #             sys.exit(1)
    # if type(tree).__name__ == "EmptyStatement":
    #     p = EmptyStatement()
    elif type(tree).__name__ == "IfStatementContext":
        # p = convertTree(children[2], verbose)
        # tt = convertTree(children[4], verbose)
        # t = statement_convertor(tt)
        # f = None
        # if len(children) == 7:
        #     f = statement_convertor(convertTree(children[6], verbose))
        # p = If(p, t, f)
        exprs, s = [], []
        for c in children:
            if type(c).__name__ == "ExpressionContext":
                exprs.append(convertTree(c, verbose))
            elif type(c).__name__ == "StatementContext":
                s.append(statement_convertor(convertTree(c, verbose)))
        # ss = statement_convertor(s)
        p = If(exprs, s)
        #print p
    # if type(tree).__name__ == "Yield":
    #     e = convertTree(children[0], verbose)
    #     p = Yield(e)
    # if type(tree).__name__ == "Let":
    #     v = convertTree(children[0], verbose)
    #     t =
    #
    #
    #
    #     if len(children) == 2:
    #         tt = convertTree(children[1], verbose)
    #         t = statement_convertor(tt)
    #     p = Let(v, t)

    # if type(tree).__name__ == "each":
    #     p = Each()
    # if type(tree).__name__ == "ForIn":
    #     i = convertTree(children[0], verbose)
    #     e1 = convertTree(children[1], verbose)
    #     each = children[2]
    #     s = None
    #     if len(children) == 4:
    #         s = convertTree(children[3], verbose)
    #     print each
    #     if len(each.getChildren()) == 0:
    #         each = False
    #     elif each.getChildren()[0].text == "each":
    #         each = True
    #     else:
    #         print "%d:error: for cannot be followed by %s" %(each.getLine(), each.getChildren()[0].text)
    #         sys.exit(0)
    #     if s is not None:
    #         s = statement_convertor(s)
    #     p = ForIn(i, s, e1, each)
    # elif type(tree).__name__ == "Try":
    #     s = convertTree(children[0], verbose)
    #     rest = map(lambda x: convertTree(x, verbose), children[1:])
    #     t = statement_convertor(s)
    #     p = Try(t, rest)
    elif type(tree).__name__ == "WhileStatementContext":
        p = convertTree(children[2], verbose)
        t = statement_convertor(convertTree(children[4].children[0], verbose))
        p = While(p, t)
    elif type(tree).__name__ == "DoWhileStatementContext":
        p = statement_convertor(convertTree(children[1].children[0], verbose))
        t = convertTree(children[4], verbose)
        p = DoWhile(p, t)
    # if type(tree).__name__ == "Switch":
    #     e = convertTree(children[0], verbose)
    #     cb = map(lambda x: convertTree(x, verbose), children[1:])
    #     p = Switch(e, cb)
    # if type(tree).__name__ == "Throw":
    #     e = convertTree(children[0], verbose)
    #     p = Throw(e)
    # if type(tree).__name__ == "CatchClause":
    #     i = convertTree(children[0], verbose)
    #     e = statement_convertor(convertTree(children[1], verbose))
    #     ex = None
    #     if len(children) == 3:
    #         ex = convertTree(children[2], verbose)
    #     p = CatchClause(i, e, ex)
    # if type(tree).__name__ == "FinallyClause":
    #     e = statement_convertor(convertTree(children[0], verbose))
    #     p = FinallyClause(e)
    # if type(tree).__name__ == "CaseClause":
    #     e = convertTree(children[0], verbose)
    #     cc = Statements(filter(lambda x: x != [], map(lambda x: convertTree(x, verbose), children[1:])))
    #     p = CaseBlock(cc, e)
    # if type(tree).__name__ == "DefaultBlock":
    #     cc = Statements(filter(lambda x: x != [], map(lambda x: convertTree(x, verbose), children[:])))
    #     p = CaseBlock(cc)
    elif type(tree).__name__ == "BreakStatementContext":
        p = Break()

    elif type(tree).__name__ == "ThrowStatementContext":
        p = Throw()

    elif type(tree).__name__ == "ContinueStatementContext":
        p = Continue()

    elif type(tree).__name__ == "BooleanLiteralContext":
        if children[0].symbol.text == "true":
            p = Ltrue()
        else:
            p = Lfalse()
    elif type(tree).__name__ == "HexLiteralContext":
        pass
    elif type(tree).__name__ == "StringLiteralContext":
        p = String(children[0].symbol.text)

    elif type(tree).__name__ == "NumberLiteralContext":
        p = Number(children[0].symbol.text)

    # elif type(tree).__name__ == "UnaryExpr":
    #     c1 = convertTree(children[1], verbose)
    #     p = UnaryExpr(children[0].text, c1)
    # elif type(tree).__name__ == "PropertyName":
    #     if len(children) == 2:
    #         c1 = convertTree(children[1], verbose)
    #         c0 = convertTree(children[0], verbose)
    #         p = PropertyName(c0, c1)
    #     else:
    #         p = PropertyName(convertTree(children[0], verbose))
    # elif type(tree).__name__ == "Property":
    #     p = Property(convertTree(children[0], verbose))
    elif type(tree).__name__ == "Zero":
        p = Number(0)
    elif type(tree).__name__ == "Ternary":
        if len(children) == 3:
            p = Ternary(convertTree(children[0], verbose), convertTree(children[1], verbose),
                        convertTree(children[2], verbose))
        else:
            p = convertTree(children[0], verbose)

    # elif type(tree).__name__ == "RegEx":
    #     p = RegEx(children[0].text)
    # elif type(tree).__name__ == "List":
    #     p = List([convertTree(c, verbose) for c in children])
    # elif type(tree).__name__ == "ListCreation":
    #     e = convertTree(children[0], verbose)
    #     f = convertTree(children[1], verbose)
    #     p = ListCreation(e, f)

    # elif type(tree).__name__ == "Assignment":
    #     v = convertTree(children[0],verbose)
    #     t = children[1].text
    #     e = convertTree(children[2],verbose)
    #     p = Assignment(v,t,e)

    # elif type(tree).__name__ == "This":
    #     p = This()

    elif type(tree).__name__ == "New":
        e = convertTree(children[0], verbose)
        a = None
        if len(children) == 2:
            a = convertTree(children[1], verbose)
        p = New(e, a)
    # elif type(tree).__name__ == "Null":
    #     p = Null()
    # elif type(tree).__name__ == "Ltrue":
    #     p = Ltrue()
    # elif type(tree).__name__ == "Lfalse":
    #     p = Lfalse()
    elif type(tree).__name__ == "Index":
        p = Index(convertTree(children[0], verbose))
    # elif type(tree).__name__ == "Functioncall":
    #     i, a, r = None, None, None
    #     if len(children) == 1:
    #         p = convertTree(children[0], verbose)
    #     else:
    #         i = convertTree(children[0], verbose)
    #         a = convertTree(children[1], verbose)
    #         r = None
    #         if len (children) > 2:
    #             r = CallExpressionSuffix(map(convertTree, children[2:]))
    #     p = Functioncall(i, a, r)

    # if p is not []:
    #     p.line = tree.getLine()
    return p


