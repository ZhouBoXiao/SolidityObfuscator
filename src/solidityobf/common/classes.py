class Selfsmallprinter():
    def smallprint(self):
        return ("%s" % str(self)).replace("\n", "")


class Onelineisstr():
    def oneline_str(self):
        return ("%s" % str(self)).replace("\n", "")


class Textsmallprinter():
    def smallprint(self):
        return "%s" % self


class Nonesmallprinter():
    def smallprint(self):
        return ""


class Getliner():
    def getLine(self):
        return self.line


def through_exp(arg, condition):
    if isinstance(arg, Expr):
        if len(arg.exprs) == 1:
            return through_exp(arg.exprs[0], condition)
        else:
            return False
    # if isinstance(arg, MemberExpr):
    #     if len(arg.suffix_list) == 0:
    #         return through_exp(arg.expr, condition)
    #     else:
    #         return False
    return condition(arg)


def cleaner(obj):
    if getattr(obj, "getChildren"):
        for c in list(obj.getChildren()):
            cleaner(c)
            c.parent = None


class Expr(object, Selfsmallprinter, Getliner):
    text = "Expr"
    parent = None
    operator = ""
    line = -1
    exprs = []

    def __init__(self, exprs=[]):
        self.exprs = exprs[:]
        for i in range(len(self.exprs)):
            if (not isinstance(self.exprs[i], str)) and (not isinstance(self.exprs[i], unicode)):
                self.exprs[i].parent = self

    def insert(self, index=0, value=None):
        self.exprs.insert(index, value)
        value.parent = self

    def replace(self, index=0, value=None):
        self.exprs[index] = value
        value.parent = self

    def index(self, item):
        return self.exprs.index(item)

    def replace_item(self, item, value):
        index = self.index(item)
        self.exprs[index] = value
        value.parent = self

    def replace_expr(self, efrom=None, value=None):
        index = self.exprs.index(efrom)
        self.exprs[index] = value
        value.parent = self

    def __str__(self):
        if len(self.exprs) == 0:
            return ""
        pb, pe = "", ""
        # if len(self.exprs) != 1 and not isinstance(self.parent, Statements):
        #     pb, pe = "(", ")"
        # expr = []
        # for e in self.exprs:
        #     if e == "-":
        #         expr.append(" - ")
        #     else:
        #         expr.append(e)
        return pb + "".join(map(format, self.exprs)) + pe

    def oneline_str(self):
        if len(self.exprs) == 0:
            return ""
        pb, pe = "", ""
        # if len(self.exprs) != 1 and not isinstance(self.parent, Statements):
        #     pb, pe = "(", ")"
        expr = []
        for e in self.exprs:
            if "oneline_str" in dir(e):
                expr.append(e.oneline_str())
            else:
                expr.append(e)
        # for e in self.exprs:
        #     if e == "-":
        #         expr.append(" - ")
        #     else:
        #         if "oneline_str" in dir(e):
        #             expr.append(e.oneline_str())
        #         else:
        #             expr.append(e)
        return pb + "".join(map(format, expr)) + pe

    def getChildren(self):
        return filter(lambda x: type(x) != str and type(x) != unicode, self.exprs)


# class Var(object, Selfsmallprinter, Getliner):
#     text = "Var"
#     parent = None
#     args_dec_list = []  # VarDeclaration()
#     line = -1
#
#     def __init__(self, args_dec_list=[]):
#         self.args_dec_list = args_dec_list[:]
#         for l in self.args_dec_list:
#             l.parent = self
#
#     def __str__(self):
#         if self.args_dec_list is not []:
#             return "var " + ",".join(map(lambda x: "%s" % x, self.args_dec_list))
#         return ""
#
#     def oneline_str(self):
#         if self.args_dec_list is not []:
#             return "var " + ",".join(map(lambda x: "%s" % x.oneline_str(), self.args_dec_list))
#         return ""
#
#     def insert(self, index=0, value=None):
#         self.args_dec_list.insert(index, value)
#         value.parent = self
#
#     def replace(self, index=0, value=None):
#         self.args_dec_list[index] = value
#         value.parent = self
#
#     def getChildren(self):
#         return self.args_dec_list



# class Address(object, Selfsmallprinter, Getliner):
#     text = "Address"
#     parent = None
#     args_dec_list = []  # VarDeclaration()
#     line = -1
#
#     def __init__(self, args_dec_list=[]):
#         self.args_dec_list = args_dec_list[:]
#         for l in self.args_dec_list:
#             l.parent = self
#
#     def __str__(self):
#         if self.args_dec_list is not []:
#             return "address " + ",".join(map(lambda x: "%s" % x, self.args_dec_list))  # +";"
#         return ""
#
#     def oneline_str(self):
#         if self.args_dec_list is not []:
#             return "address " + ",".join(map(lambda x: "%s" % x.oneline_str(), self.args_dec_list))  # +";"
#         return ""
#
#     def insert(self, index=0, value=None):
#         self.args_dec_list.insert(index, value)
#         value.parent = self
#
#     def replace(self, index=0, value=None):
#         self.args_dec_list[index] = value
#         value.parent = self
#
#     def getChildren(self):
#         return self.args_dec_list
#
#
# class Bool(object, Selfsmallprinter, Getliner):
#     text = "Bool"
#     parent = None
#     args_dec_list = []  # VarDeclaration()
#     line = -1
#
#     def __init__(self, args_dec_list=[]):
#         self.args_dec_list = args_dec_list[:]
#         for l in self.args_dec_list:
#             l.parent = self
#
#     def __str__(self):
#         if self.args_dec_list is not []:
#             return "bool " + ",".join(map(lambda x: "%s" % x, self.args_dec_list))  # +";"
#         return ""
#
#     def oneline_str(self):
#         if self.args_dec_list is not []:
#             return "bool " + ",".join(map(lambda x: "%s" % x.oneline_str(), self.args_dec_list))  # +";"
#         return ""
#
#     def insert(self, index=0, value=None):
#         self.args_dec_list.insert(index, value)
#         value.parent = self
#
#     def replace(self, index=0, value=None):
#         self.args_dec_list[index] = value
#         value.parent = self
#
#     def getChildren(self):
#         return self.args_dec_list
#
#
# class Int(object, Selfsmallprinter, Getliner):
#     text = "Int"
#     parent = None
#     args_dec_list = []  # VarDeclaration()
#     line = -1
#
#     def __init__(self, args_dec_list=[]):
#         self.args_dec_list = args_dec_list[:]
#         for l in self.args_dec_list:
#             l.parent = self
#
#     def __str__(self):
#         if self.args_dec_list is not []:
#             return "int " + ",".join(map(lambda x: "%s" % x, self.args_dec_list))  # +";"
#         return ""
#
#     def oneline_str(self):
#         if self.args_dec_list is not []:
#             return "int " + ",".join(map(lambda x: "%s" % x.oneline_str(), self.args_dec_list))  # +";"
#         return ""
#
#     def insert(self, index=0, value=None):
#         self.args_dec_list.insert(index, value)
#         value.parent = self
#
#     def replace(self, index=0, value=None):
#         self.args_dec_list[index] = value
#         value.parent = self
#
#     def getChildren(self):
#         return self.args_dec_list
#
#
# class Uint(object, Selfsmallprinter, Getliner):
#     text = "Uint"
#     parent = None
#     args_dec_list = []  # VarDeclaration()
#     line = -1
#
#     def __init__(self, args_dec_list=[]):
#         self.args_dec_list = args_dec_list[:]
#         for l in self.args_dec_list:
#             l.parent = self
#
#     def __str__(self):
#         if self.args_dec_list is not []:
#             return "uint " + ",".join(map(lambda x: "%s" % x, self.args_dec_list))  # +";"
#         return ""
#
#     def oneline_str(self):
#         if self.args_dec_list is not []:
#             return "uint " + ",".join(map(lambda x: "%s" % x.oneline_str(), self.args_dec_list))  # +";"
#         return ""
#
#     def insert(self, index=0, value=None):
#         self.args_dec_list.insert(index, value)
#         value.parent = self
#
#     def replace(self, index=0, value=None):
#         self.args_dec_list[index] = value
#         value.parent = self
#
#     def getChildren(self):
#         return self.args_dec_list


class Statements(object, Textsmallprinter, Getliner):
    text = "Statements"
    parent = None
    statements_list = []
    line = -1

    def __init__(self, l=[]):
        self.statements_list = l[:]
        for s in self.statements_list:
            s.parent = self

    def oneline_str(self):
        string = ""
        for s in self.statements_list:
            if not through_exp(s, lambda x: x.__class__ in [Statements, Function, If, For, While]):
                string += format(s.oneline_str()) + ";"
            else:
                string += format(s.oneline_str()) + ""
        ret = ""
        if self.parent.__class__ in [Program] and string.strip() != "":
            ret = string
        else:
            ret = "{" + string + "}"
        return ret

    def __str__(self, INDENT="  "):
        string = ""
        for s in self.statements_list:
            if not through_exp(s, lambda x: x.__class__ in [Statements, Function, If, For, While]):
                if format(s).strip() != "":
                    string += format(s) + ";\n"
            else:
                string += format(s) + ""
        ret = ""
        string = "\n".join(map(lambda x: INDENT + format(x), string.splitlines()))
        if self.parent.__class__ in [Program] and string.strip() != "":
            ret = string
        else:
            ret = "{\n" + string + "\n}\n"
        return ret

    def insert(self, index=0, value=None):
        self.statements_list.insert(index, value)
        value.parent = self

    def remove(self, index=0):
        del self.statements_list[index]

    def append(self, value):
        self.statements_list.append(value)
        value.parent = self

    def append_list(self, value):
        for v in value:
            self.append(v)

    def replace(self, index=0, value=Expr()):
        self.statements_list[index] = value
        value.parent = self

    def index(self, item):
        return self.statements_list.index(item)

    def replace_item(self, item, value):
        index = self.statements_list.index(item)
        self.statements_list[index] = value
        value.parent = self

    def replaceall(self, value=[]):
        self.statements_list = []
        for v in value:
            self.append(v)

    def getChildren(self):
        return self.statements_list


class Listarguments(object, Selfsmallprinter, Getliner):
    text = "Listarguments"
    args_list = []  # [Var()]
    parent = None
    line = -1

    def __init__(self, args_list=[]):
        if len(args_list) > 0:
            self.args_list = args_list[:]
            for l in args_list:
                l.parent = self

    def __str__(self):
        return "(" + ",".join(map(lambda x: "%s" % str(x), self.args_list)) + ")"

    def oneline_str(self):
        return "(" + ",".join(map(lambda x: "%s" % x.oneline_str(), self.args_list)) + ")"

    def insert(self, index=0, value=None):
        self.args_list.insert(index, value)
        value.parent = self

    def replace(self, index=0, value=None):
        self.args_list[index] = value
        value.parent = self

    def replace_item(self, item, value):
        index = self.args_list.index(item)
        self.args_list[index] = value
        value.parent = self

    def getChildren(self):
        return self.args_list


class Ident(object, Selfsmallprinter, Getliner, Onelineisstr):
    text = "Ident"
    parent = None
    assigned = False
    name = ""
    line = -1

    def __init__(self, name="", assigned=False):
        self.assigned = assigned
        self.name = name

    def __str__(self):
        return "%s" % (str(self.name))

    def getChildren(self):
        return []

# class IntDeclaration(object, Textsmallprinter, Getliner):
#     text = "IntDeclaration"
#     parent = None
#     var = None  # Ident()
#     keywords = []
#     line = -1
#     expr = None
#     dummy = False
#
#     def __init__(self, keywords=[], var=Ident(), expr=None):
#         self.keywords = keywords[:]
#         self.var = var
#         self.var.parent = self
#         self.expr = expr
#         if self.expr is not None:
#             self.expr.parent = self
#
#     def replace_expr(self, expr):
#         self.expr = expr
#         if self.expr is not None:
#             self.expr.parent = self
#
#     def replace_item(self, dummy, item):
#         self.replace_expr(item)
#
#     def __str__(self):
#         if self.expr is not None:
#             e = str(self.expr)
#             if len(self.keywords) > 0:
#                 str = "int" #+ str(self.var) + " = " + e
#                 for keyword in self.keywords:
#                     str = keyword + " "
#                 str += str(self.var) + " = " + e
#             else:
#                 return "int" + str(self.var) + " = " + e
#         elif len(self.keywords) > 0:
#             str = "int"
#             for keyword in self.keywords:
#                 str = keyword + " "
#             return str + "%s" % (self.var)
#         return "int %s" % (self.var)
#
#     def getChildren(self):
#         if self.expr is not None:
#             return [self.var, self.expr]
#         return [self.var]
#
#     def oneline_str(self):
#         if self.expr is not None:
#             e = self.expr.oneline_str()
#             if len(self.keywords) > 0:
#                 str = "int" #+ str(self.var) + " = " + e
#                 for keyword in self.keywords:
#                     str = keyword + " "
#                 str += str(self.var) + " = " + e
#             else:
#                 return "int" + str(self.var) + " = " + e
#         elif len(self.keywords) > 0:
#             str = "int"
#             for keyword in self.keywords:
#                 str = keyword + " "
#             return str + "%s" % (self.var)
#         return "int %s" % (self.var)


# class AddressDeclaration(object, Textsmallprinter, Getliner):
#     text = "AddressDeclaration"
#     parent = None
#     keywords = []
#     var = None  # Ident()
#     line = -1
#     expr = None
#     dummy = False
#
#     def __init__(self, keywords=[], var=Ident(), expr=None):
#         self.keywords = keywords[:]
#         self.var = var
#         self.var.parent = self
#         self.expr = expr
#         if self.expr is not None:
#             self.expr.parent = self
#
#     def replace_expr(self, expr):
#         self.expr = expr
#         if self.expr is not None:
#             self.expr.parent = self
#
#     def replace_item(self, dummy, item):
#         self.replace_expr(item)
#
#     def __str__(self):
#         if self.expr is not None:
#             e = str(self.expr)
#             if len(self.keywords) > 0:
#                 str = "int"  # + str(self.var) + " = " + e
#                 for keyword in self.keywords:
#                     str = keyword + " "
#                 str += str(self.var) + " = " + e
#             else:
#                 return "int" + str(self.var) + " = " + e
#         elif len(self.keywords) > 0:
#             str = "int"
#             for keyword in self.keywords:
#                 str = keyword + " "
#             return str + "%s" % (self.var)
#         return "int %s" % (self.var)
#
#     def getChildren(self):
#         if self.expr is not None:
#             return [self.var, self.expr]
#         return [self.var]
#
#     def oneline_str(self):
#         if self.expr is not None:
#             e = self.expr.oneline_str()
#             if len(self.keywords) > 0:
#                 str = "address"  # + str(self.var) + " = " + e
#                 for keyword in self.keywords:
#                     str = keyword + " "
#                 str += str(self.var) + " = " + e
#             else:
#                 return "address" + str(self.var) + " = " + e
#         elif len(self.keywords) > 0:
#             str = "address"
#             for keyword in self.keywords:
#                 str = keyword + " "
#             return str + "%s" % (self.var)
#         return "address %s" % (self.var)


class MemberExpr(object, Textsmallprinter, Getliner):
    text = "MemberExpr"
    parent = None
    suffix_list = []
    expr = None
    name = ""
    line = -1

    def __init__(self, expr=Expr(), suffix_list=[]):
        self.expr = expr
        self.expr.parent = self
        self.suffix_list = suffix_list[:]
        for s in self.suffix_list:
            s.parent = self

    def __str__(self):
        return "%s" % (self.expr) + "".join(map(format, self.suffix_list))

    def oneline_str(self):
        return "%s" % (self.expr.oneline_str()) + "".join(map(lambda x: x.oneline_str(), self.suffix_list))

    def getChildren(self):
        return [self.expr] + self.suffix_list

class Suffix(object, Nonesmallprinter, Getliner):
    text = "Suffix"
    parent = None
    suffix = None
    name = ""
    line = -1

    def __init__(self, suffix):
        self.suffix = suffix
        suffix.parent = self

    def __str__(self):
        return "%s" % self.suffix

    def oneline_str(self):
        return self.suffix.oneline_str()

    def getChildren(self):
        return [self.suffix]


class PropertyGet(object, Getliner):
    text = "PropertyGet"
    parent = None
    statements = None
    name = None
    line = -1

    def __init__(self, name, statements):
        self.name = name
        self.name.parent = self
        self.statements = statements
        self.statements.parent = self

    def __str__(self):
        return "get %s() {%s}" % (self.name, self.statements)

    def oneline_str(self):
        return "get %s() {%s}" % (self.name.oneline_str(), self.statements.oneline_str())

    def getChildren(self):
        return [self.name, self.statements]


class PropertySet(object, Getliner):
    text = "PropertySet"
    parent = None
    statements = None
    name = None
    ident = None
    line = -1

    def __init__(self, name, ident, statements):
        self.name = name
        self.name.parent = self
        self.ident = ident
        self.ident.parent = self
        self.statements = statements
        self.statements.parent = self

    def __str__(self):
        return "set %s(%s) {%s}" % (self.name, self.ident, self.statements)

    def oneline_str(self):
        return "set %s(%s) {%s}" % (self.name.oneline_str(), self.ident.oneline_str(), self.statements.oneline_str())

    def getChildren(self):
        return [self.name, self.ident, self.statements]


class Throw(object, Textsmallprinter, Getliner):
    text = "Throw"
    parent = None
    line = -1

    def __str__(self):
        return "throw"

    def oneline_str(self):
        return "throw"

    def getChildren(self):
        return []


class ArrayDeclaration(object, Textsmallprinter, Getliner):
    text = "ArrayDeclaration"
    parent = None
    var = ""  # Ident()
    line = -1
    elist = []
    dummy = False
    typeName = ""
    keywords = []
    expr = None

    def __init__(self, typeName="", keywords=[], var=Ident(), elist=[], expr=None):
        self.typeName = typeName
        self.keywords = keywords[:]
        if expr is not None:
            self.expr = expr
            self.expr.parent = self
        if var is not None:
            self.var = var
            self.var.parent = self
        self.elist = elist[:]
        for s in self.elist:
            s.parent = self

    def replace_ident(self, ident):
        self.var = ident
        self.var.parent = self

    def __str__(self):
        ret = self.typeName
        for e in self.elist:
            ret += '[' + str(e) + ']'
        if self.expr is not None:
            ret += " %s %s=%s" % (" ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var), str(self.expr))
        else:
            ret += " %s %s" % (" ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var))
        return ret

    def oneline_str(self):
        ret = self.typeName
        for e in self.elist:
            ret += '[' + e.oneline_str() + ']'
        if self.expr is not None:
            ret += " %s %s=%s" % (
            " ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var), self.expr.oneline_str())
        else:
            ret += " %s %s" % (" ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var))
        return ret

    def getChildren(self):
        p = []
        # if self.elist is not None:
        #     p.append(self.elist)
        # if len(self.keywords) > 0:
        #     p.append(self.keywords)
        if self.var != "":
            p.append(self.var)
        if self.expr is not None:
            p.append(self.expr)
        return p


class StateArrayDeclaration(object, Textsmallprinter, Getliner):
    text = "StateArrayDeclaration"
    parent = None
    var = None  # Ident()
    line = -1
    elist = []
    dummy = False
    typeName = ""
    keywords = []
    expr = None

    def __init__(self, typeName="", keywords=[], var=Ident(), elist=[], expr=None):
        self.typeName = typeName
        self.keywords = keywords[:]
        self.var = var
        if expr is not None:
            self.expr = expr
            self.expr.parent = self
        self.var.parent = self
        self.elist = elist[:]
        for s in self.elist:
            s.parent = self

    def replace_ident(self, ident):
        self.var = ident
        self.var.parent = self

    def __str__(self):
        ret = self.typeName
        for e in self.elist:
            ret += '[' + str(e) + ']'
        if self.expr is not None:
            ret += " %s %s=%s;\n" % (" ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var), str(self.expr))
        else:
            ret += " %s %s;\n" % (" ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var))
        return ret

    def oneline_str(self):
        ret = self.typeName
        for e in self.elist:
            ret += '[' + e.oneline_str() + ']'
        if self.expr is not None:
            ret += " %s %s=%s;" % (" ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var), self.expr.oneline_str())
        else:
            ret += " %s %s;" % (" ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var))
        return ret

    def getChildren(self):
        p = []
        # if self.elist is not None:
        #     p.append(self.elist)
        # if len(self.keywords) > 0:
        #     p.append(self.keywords)
        if self.var is not None:
            p.append(self.var)
        if self.expr is not None:
            p.append(self.expr)
        return p


class VarDeclaration(object, Textsmallprinter, Getliner):
    text = "VarDeclaration"
    parent = None
    var = None  # Ident()
    line = -1
    expr = None
    dummy = False
    typeName = None
    keywords = []

    def __init__(self, typeName, keywords, var=Ident(), expr=None):
        self.typeName = typeName
        self.keywords = keywords[:]
        if var is not None:
            self.var = var
            self.var.parent = self
        self.text = str(typeName)
        if expr is not None:
            self.expr = expr
            self.expr.parent = self

    def replace_ident(self, ident):
        self.var = ident
        self.var.parent = self

    def replace_expr(self, expr):
        self.expr = expr
        if self.expr is not None:
            self.expr.parent = self

    def replace_item(self, dummy, item):
        self.replace_expr(item)

    def __str__(self):
        if self.var is None:
            self.var = ""
        if self.expr is not None:
            ret = "%s %s %s=%s" % (
                self.text, " ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var), str(self.expr))
            return ret
        else:
            ret = "%s %s %s" % (self.text, " ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var))
            return ret

    def oneline_str(self):
        if self.var is None:
            self.var = ""
        if self.expr is not None:
            ret = "%s %s %s=%s" % (
                self.text, " ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var), self.expr.oneline_str())
            return ret
        else:
            ret = "%s %s %s" % (self.text, " ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var))
            return ret

    def getChildren(self):
        p = []
        # if len(self.keywords) > 0:
        #     p.append(self.keywords)
        if self.var != "" and self.var is not None:
            p.append(self.var)
        if self.expr is not None:
            p.append(self.expr)
        return p


class StateVariableDeclaration(object, Textsmallprinter, Getliner):
    text = "StateVariableDeclaration"
    parent = None
    var = None  # Ident()
    line = -1
    expr = None
    dummy = False
    typeName = None
    keywords = []

    def __init__(self, typeName, keywords, var=Ident(), expr=None):
        self.typeName = typeName
        self.keywords = keywords[:]
        self.var = var
        self.var.parent = self
        self.text = str(typeName)
        if expr is not None:
            self.expr = expr
            self.expr.parent = self

    def replace_ident(self, ident):
        self.var = ident
        self.var.parent = self

    def replace_expr(self, expr):
        self.expr = expr
        if self.expr is not None:
            self.expr.parent = self

    def replace_item(self, dummy, item):
        self.replace_expr(item)

    def __str__(self):
        if self.expr is not None:
            ret = "%s %s %s=%s;\n" % (
            self.text, " ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var), str(self.expr))
            return ret
        else:
            ret = "%s %s %s;\n" % (self.text, " ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var))
            return ret

    def oneline_str(self):
        if self.expr is not None:
            ret = "%s %s %s=%s;" % (self.text, " ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var), self.expr.oneline_str())
            return ret
        else:
            ret = "%s %s %s;" % (self.text, " ".join(map(lambda x: "%s" % x, self.keywords)), str(self.var))
            return ret

    def getChildren(self):
        p = []
        # if len(self.keywords) > 0:
        #     p.append(self.keywords)
        if self.var is not None:
            p.append(self.var)
        if self.expr is not None:
            p.append(self.expr)
        return p


class Return(object, Selfsmallprinter, Getliner):
    expr = None
    text = "Return"
    parent = None
    line = -1

    def __init__(self, expr=None):
        if expr is not None:
            self.expr = expr
            self.expr.parent = self

    def __str__(self):
        if self.expr is not None:
            return "return %s" % str(self.expr)
        return "return "

    def oneline_str(self):
        if self.expr is not None:
            return "return %s" % (self.expr.oneline_str())
        return "return "

    def getChildren(self):
        if self.expr is not None:
            return [self.expr]
        return []


# class CallExpressionSuffix(object, Selfsmallprinter, Getliner):
#     text = "CallExpressionSuffix"
#     parent = None
#     suffix_list = None
#     line = -1
#
#     def __init__(self, suffix_list=[]):
#         self.suffix_list = suffix_list
#         for s in self.suffix_list:
#             s.parent = self
#
#     def __str__(self):
#         return "".join(map(format, self.suffix_list))
#
#     def oneline_str(self):
#         return "".join(map(lambda x: x.oneline_str(), self.suffix_list))
#
#     def getChildren(self):
#         return self.suffix_list


class Functioncall(object, Selfsmallprinter, Getliner):
    text = "Functioncall"
    parent = None
    args = None
    rest = None
    expr = None
    line = -1

    def __init__(self, expr=Expr(), args=[]):
        self.expr = expr
        self.expr.parent = self
        self.args = args[:]
        for a in self.args:
            a.parent = self

    def __str__(self):
        ret = str(self.expr) + "(" + ",".join(map(lambda x: "%s" % str(x), self.args)) + ")"
        return ret

    def oneline_str(self):
        ret = self.expr.oneline_str() + "(" + ",".join(map(lambda x: "%s" % x.oneline_str(), self.args)) + ")"
        return ret

    def getChildren(self):
        # if self.rest is not None:
        #     return [self.memberexpr, self.args, self.rest]
        return [self.expr] + self.args


class Number(object, Selfsmallprinter, Getliner, Onelineisstr):
    text = "Number"
    parent = None
    value = None
    line = -1

    def __init__(self, value=0.0):
        self.value = value

    def __str__(self):
        return str(self.value)

    def oneline_str(self):
        return str(self.value)

    def getChildren(self):
        return []


# class RegEx(object, Selfsmallprinter, Getliner, Onelineisstr):
#     text = "RegEx"
#     parent = None
#     value = None
#     line = -1
#
#     def __init__(self, value="//"):
#         self.value = value
#
#     def __str__(self):
#         return format(self.value)
#
#     def getChildren(self):
#         return []


# class NaN(object, Selfsmallprinter, Getliner, Onelineisstr):
#     text = "NaN"
#     parent = None
#     value = "NaN"
#     line = -1
#
#     def __str__(self):
#         return format(self.value)
#
#     def getChildren(self):
#         return []


# class This(object, Selfsmallprinter, Getliner, Onelineisstr):
#     text = "This"
#     parent = None
#     value = "this"
#     line = -1
#
#     def __str__(self):
#         return format(self.value)
#
#     def getChildren(self):
#         return []

class List(object, Getliner):
    text = "List"
    parent = None
    value = None
    line = -1

    def __init__(self, value=[]):
        self.value = value[:]
        for v in self.value:
            v.parent = self

    def __str__(self):
        return "[%s]" % ",".join(map(lambda x: "%s" % x, self.value))

    def oneline_str(self):
        return "[%s]" % ",".join(map(lambda x: "%s" % x.oneline_str(), self.value))

    def getChildren(self):
        return self.value

    def insert(self, value, i, item):
        self.value.insert(i, item)
        item.parent = self

    def replace(self, value, i, item):
        self.value[i] = item
        item.parent = self

    def replace_item(self, item, value):
        index = self.value.index(item)
        self.value[index] = value
        value.parent = self

    def smallprint(self):
        return "[%s]" % ",".join(map(lambda x: str(x).replace("\"", ""), self.value))


# class ListCreation(object, Selfsmallprinter, Getliner):
#     text = "List"
#     parent = None
#     expr = None
#     fors = None
#     line = -1
#
#     def __init__(self, expr, fors):
#         self.expr = expr
#         self.fors = fors
#         self.expr.parent = self
#         self.fors.parent = self
#
#     def oneline_str(self):
#         return "[%s %s]" % (self.expr.oneline_str(), self.fors.oneline_str())
#
#     def __str__(self):
#         return "[%s %s]" % (self.expr, self.fors)
#
#     def getChildren(self):
#         return [self.expr, self.fors]

# class ObjectLiteral(object, Getliner):
#     text = "ObjectLiteral"
#     parent = None
#     value = None
#     line = -1
#
#     def __init__(self, value=[]):
#         self.value = value[:]
#         for v in self.value:
#             v.parent = self
#
#     def __str__(self):
#         return "{%s}" % ",".join(map(lambda x: "%s" % x, self.value))
#
#     def getChildren(self):
#         return self.value
#
#     def insert(self, value, i, item):
#         self.value.insert(i, item)
#         item.parent = self
#
#     def replace(self, value, i, item):
#         self.value[i] = item
#         item.parent = self
#
#     def replace_item(self, item, value):
#         index = self.value.index(item)
#         self.value[index] = value
#         value.parent = self
#
#     def oneline_str(self):
#         return "{%s}" % ",".join(map(lambda x: x.oneline_str(), self.value))
#
#     def smallprint(self):
#         return "{%s}" % ",".join(map(lambda x: str(x).replace("\"", ""), self.value))


class String(object, Selfsmallprinter, Getliner, Onelineisstr):
    text = "String"
    parent = None
    value = None
    line = -1

    def __init__(self, value=""):
        self.value = value

    def __str__(self):
        return self.value.encode("utf-8")

    def getChildren(self):
        return []

    def smallprint(self):
        return str(self.value)


class Assignment(object, Selfsmallprinter, Getliner):
    text = "Assignment"
    parent = None
    typeof = ""
    var = None
    expr = None
    line = -1

    def __init__(self, var=Expr(), typeof="=", expr=Expr()):
        self.typeof = typeof
        self.var = var
        self.var.parent = self
        self.expr = expr
        self.expr.parent = self

    def __str__(self):
        return "%s %s %s" % (str(self.var), str(self.typeof), str(self.expr))

    def oneline_str(self):
        return "%s %s %s" % (str(self.var.oneline_str()), str(self.typeof), str(self.expr.oneline_str()))

    def getChildren(self):
        return [self.var, self.expr]


# class Switch(object, Getliner):
#     text = "Switch"
#     parent = None
#     caseblock = []
#     expr = None
#     line = -1
#
#     def __init__(self, expr=Expr(), caseblock=[]):
#         self.caseblock = caseblock[:]
#         for cb in caseblock:
#             cb.parent = self
#         self.expr = expr
#         self.expr.parent = self
#
#     def __str__(self):
#         return "switch (%s) {%s}" % (self.expr, "".join(map(format, self.caseblock)))
#
#     def oneline_str(self):
#         return "switch (%s) {%s}" % (self.expr.oneline_str(), "".join(map(lambda x: x.oneline_str(), self.caseblock)))
#
#     def getChildren(self):
#         return [self.expr] + self.caseblock
#
#     def smallprint(self):
#         return "switch (%s)" % (self.expr)


# class CaseBlock(object, Getliner):
#     text = "CaseBlock"
#     parent = None
#     line = -1
#     statement = None
#     expr = None
#
#     def __init__(self, statement=Statements(), expr=None):
#         self.statement = statement
#         self.statement.parent = self
#         if expr is not None:
#             self.expr = expr
#             self.expr.parent = self
#
#     def __str__(self):
#         if self.expr is not None:
#             return "case %s : %s" % (self.expr, self.statement)
#         return "default : %s" % (self.statement)
#
#     def oneline_str(self):
#         if self.expr is not None:
#             return "case %s : %s" % (self.expr, self.statement.oneline_str())
#         return "default : %s" % (self.statement.oneline_str())
#
#     def getChildren(self):
#         ret = []
#         if self.expr is not None:
#             ret.append(self.expr)
#         return ret + [self.statement]
#
#     def smallprint(self):
#         return "case %s" % (self.expr)


class Break(object, Selfsmallprinter, Getliner, Onelineisstr):
    text = "Break"
    parent = None
    line = -1
    ident = None

    # def __init__(self, ident=None):
    #     if ident is not None:
    #         self.ident = ident
    #         self.ident.parent = self

    def __str__(self):

        return "break"

    def getChildren(self):
        # if self.ident is not None:
        #     return [self.ident]
        return []


class Continue(object, Selfsmallprinter, Getliner, Onelineisstr):
    text = "Continue"
    parent = None
    line = -1
    ident = None

    # def __init__(self, ident=None):
    #     if ident is not None:
    #         self.ident = ident
    #         self.ident.parent = self

    def __str__(self):
        # i = ""
        # if self.ident is not None:
        #     i = format(self.ident)
        return "continue"

    def getChildren(self):
        # if self.ident is not None:
        #     return [self.ident]
        return []


# class Yield(object, Selfsmallprinter, Getliner):
#     text = "Yield"
#     parent = None
#     line = -1
#     expr = None
#
#     def __init__(self, expr):
#         self.expr = expr
#         self.expr.parent = self
#
#     def __str__(self):
#         return "yield " + format(self.expr)
#
#     def oneline_str(self):
#         return "yield %s" % self.expr.oneline_str()
#
#     def getChildren(self):
#         return [self.expr]


# class Let(object, Selfsmallprinter, Getliner):
#     text = "Let"
#     parent = None
#     line = -1
#     vardec = None
#     statement = None
#
#     def __init__(self, vardec, statement=None):
#         self.vardec = vardec
#         self.vardec.parent = self
#         if statement != None:
#             self.statement = statement
#             self.statement.parent = self
#
#     def __str__(self):
#         ret = "let "
#         if self.statement != None:
#             ret += "(" + format(self.vardec) + ")" + format(self.statement)
#         else:
#             ret += format(self.vardec)
#         return ret
#
#     def oneline_str(self):
#         if self.statement != None:
#             return "let (%s) %s" % (self.vardec.oneline_str(), self.statement.oneline_str())
#         return "let %s " % self.vardec.oneline_str()
#
#     def getChildren(self):
#         ret = [self.vardec]
#         if self.statement != None:
#             ret.append(self.statement)
#         return ret


# class ExpressionStatement(object, Selfsmallprinter, Getliner):
#     text = "ExpressionStatement"
#     parent = None
#     operator = ""
#     line = -1
#     exprs = []
#
#     def __init__(self, exprs=[]):
#         self.exprs = exprs[:]
#         for i in range(len(self.exprs)):
#             if type(self.exprs[i]) != str and type(self.exprs[i]) != unicode:
#                 self.exprs[i].parent = self
#
#     def insert(self, index=0, value=Expr()):
#         self.exprs.insert(index, value)
#         value.parent = self
#
#     def replace(self, index=0, value=Expr()):
#         self.exprs[index] = value
#         value.parent = self
#
#     def index(self, item):
#         return self.exprs.index(item)
#
#     def replace_item(self, item, value):
#         index = self.exprs.index(item)
#         self.exprs[index] = value
#         value.parent = self
#
#     def oneline_str(self):
#         return ",".join(map(lambda x: x.oneline_str(), self.exprs))
#
#     def __str__(self):
#         return ",".join(map(format, self.exprs))
#
#     def getChildren(self):
#         return self.exprs  # filter (lambda x : type(x) != str and  type(x) != unicode, self.exprs)


# class Try(object, Selfsmallprinter, Getliner):
#     line = -1
#     parent = None
#     text = "Try"
#     statements = None
#     clause_list = []
#
#     def __init__(self, statements=Statements(), clause_list=None):
#         self.statements = statements
#         self.statements.parent = self
#         self.clause_list = clause_list
#         for c in clause_list:
#             c.parent = self
#
#     def __str__(self):
#         s = "try %s" % self.statements
#         for c in self.clause_list:
#             s += " %s" % c
#         return s
#
#     def oneline_str(self):
#         s = "try %s" % self.statements.oneline_str()
#         for c in self.clause_list:
#             s += " %s" % c.oneline_str()
#         return s
#
#     def getChildren(self):
#         ret = [self.statements] + self.clause_list
#         return ret


# class CatchClause(object, Selfsmallprinter, Getliner):
#     line = -1
#     parent = None
#     text = "CatchClause"
#     statements = None
#     ident = None
#     expr = None
#
#     def __init__(self, ident=Ident(), statements=Statements(), expr=None):
#         self.ident = ident
#         self.ident.parent = self
#         if expr != None:
#             self.expr = expr
#             self.expr.parent = self
#         self.statements = statements
#         self.statements.parent = self
#
#     def __str__(self):
#         ex = ""
#         if self.expr != None:
#             ex = " if %s" % self.expr
#         return "catch (%s%s) %s" % (self.ident, ex, self.statements)
#
#     def oneline_str(self):
#         ex = ""
#         if self.expr != None:
#             ex = " if %s" % self.expr.oneline_str()
#         return "catch (%s%s) %s" % (self.ident, ex, self.statements.oneline_str())
#
#     def getChildren(self):
#         ret = [self.ident, self.statements]
#         if self.expr != None:
#             ret.append(self.expr)
#         return ret


# class FinallyClause(object, Selfsmallprinter, Getliner):
#     line = -1
#     parent = None
#     text = "FinallyClause"
#     statements = None
#
#     def __init__(self, statements=Statements()):
#         self.statements = statements
#         self.statements.parent = self
#
#     def __str__(self):
#         return "finally %s" % self.statements
#
#     def oneline_str(self):
#         return "finally %s" % self.statements.oneline_str()
#
#     def getChildren(self):
#         return [self.statements]


class Ternary(object, Selfsmallprinter, Getliner):
    text = "Ternary"
    parent = None
    expr = None
    exprtrue = None
    exprfalse = None
    line = -1

    def __init__(self, expr=Expr(), exprtrue=None, exprfalse=None):
        self.expr = expr
        self.exprtrue = exprtrue
        self.exprfalse = exprfalse
        self.expr.parent = self
        if self.exprtrue is not None:
            self.exprtrue.parent = self
        if self.exprfalse is not None:
            self.exprfalse.parent = self

    def __str__(self):
        if self.exprtrue is not None:
            return "(%s?%s:%s)" % (self.expr, self.exprtrue, self.exprfalse)
        else:
            return "%s" % self.expr

    def oneline_str(self):
        if self.exprtrue is not None:
            return "(%s?%s:%s)" % (self.expr.oneline_str(), self.exprtrue.oneline_str(), self.exprfalse.oneline_str())
        else:
            return "%s" % self.expr.oneline_str()

    def getChildren(self):
        ret = [self.expr]
        if self.exprtrue is not None:
            ret.append(self.exprtrue)
        if self.exprfalse is not None:
            ret.append(self.exprfalse)
        return ret


# class UnaryExpr(object, Selfsmallprinter, Getliner):
#     text = "UnaryExpr"
#     parent = None
#     typeof = None
#     expr = None
#     line = -1
#
#     def __init__(self, typeof=None, expr=None):
#         self.typeof = typeof
#         self.expr = expr
#         self.expr.parent = self
#
#     def __str__(self):
#         return "%s %s" % (self.typeof, self.expr)
#
#     def oneline_str(self):
#         return "%s %s" % (self.typeof, self.expr.oneline_str())
#
#     def getChildren(self):
#         return [self.expr]

class PropertyName(object, Selfsmallprinter, Getliner):
    text = "PropertyName"
    parent = None
    name = None
    expr = None
    line = -1

    def __init__(self, name=None, expr=None):
        self.name = name
        self.expr = expr
        if self.name is not None:
            self.name.parent = self
        if self.expr is not None:
            self.expr.parent = self

    def __str__(self):
        if self.expr is not None:
            return "%s:%s" % (self.name, self.expr)
        else:
            return "%s" % (self.name)

    def oneline_str(self):
        if self.expr is not None:
            return "%s:%s" % (self.name.oneline_str(), self.expr.oneline_str())
        else:
            return "%s" % (self.name.oneline_str())

    def replace_expr(self, expr):
        self.expr = expr
        if self.expr is not None:
            self.expr.parent = self

    def replace_item(self, dummy, expr):
        self.expr = expr
        self.expr.parent = self

    def getChildren(self):
        if self.expr is not None:
            return [self.name, self.expr]
        return [self.name]

class Property(object, Selfsmallprinter, Getliner):
    text = "Property"
    parent = None
    name = None
    line = -1

    def __init__(self, name=None):
        self.name = name
        if self.name is not None:
            self.name.parent = self

    def __str__(self):
        return ".%s" % str(self.name)

    def oneline_str(self):
        return ".%s" % (self.name.oneline_str())

    def getChildren(self):
        return [self.name]


# class Null(object, Selfsmallprinter, Getliner, Onelineisstr):
#     text = "Null"
#     parent = None
#     line = -1
#
#     def __str__(self):
#         return "null"
#
#     def getChildren(self):
#         return []


class Ltrue(object, Selfsmallprinter, Getliner, Onelineisstr):
    text = "True"
    value = "true"
    parent = None
    line = -1

    def __str__(self):
        return "true"

    def getChildren(self):
        return []


# class Typeof(object, Selfsmallprinter, Getliner, Onelineisstr):
#     text = "Typeof"
#     value = "typeof "
#     parent = None
#     line = -1
#
#     def __str__(self):
#         return "typeof "
#
#     def getChildren(self):
#         return []


# class Void(object, Selfsmallprinter, Getliner, Onelineisstr):
#     text = "Void"
#     value = "void "
#     parent = None
#     line = -1
#
#     def __str__(self):
#         return "void "
#
#     def getChildren(self):
#         return []


class Delete(object, Selfsmallprinter, Getliner, Onelineisstr):
    text = "Delete"
    value = "delete "
    parent = None
    line = -1

    def __str__(self):
        return "delete "

    def getChildren(self):
        return []


# class Each(object, Selfsmallprinter, Getliner, Onelineisstr):
#     text = "Each"
#     parent = None
#     value = "each"
#     line = -1
#
#     def __str__(self):
#         return "each"
#
#     def getChildren(self):
#         return []


class Lfalse(object, Selfsmallprinter, Getliner, Onelineisstr):
    text = "False"
    parent = None
    value = "false"
    line = -1

    def __str__(self):
        return "false"

    def getChildren(self):
        return []


class Index(object, Selfsmallprinter, Getliner):
    text = "Index"
    parent = None
    expr = None
    line = -1

    def __init__(self, expr=Expr()):
        self.expr = expr
        self.expr.parent = self

    def __str__(self):
        return "[%s]" % self.expr

    def oneline_str(self):
        return "[%s]" % (self.expr.oneline_str())

    def getChildren(self):
        ret = [self.expr]
        return ret

    def replace_item(self, dummy, item):
        self.expr = item
        self.expr.parent = self


class New(object, Selfsmallprinter, Getliner):
    text = "New"
    parent = None
    expr = None
    arguments = None
    line = -1

    def __init__(self, expr=Expr(), arguments=None):
        self.expr = expr
        self.expr.parent = self
        self.arguments = arguments
        if arguments is not None:
            self.arguments.parent = self

    def __str__(self):
        if self.arguments is not None:
            return "new %s %s" % (self.expr, self.arguments)
        return "(new %s)" % self.expr

    def oneline_str(self):
        if self.arguments is not None:
            return "new %s %s" % (self.expr.oneline_str(), self.arguments.oneline_str())
        return "(new %s)" % self.expr.oneline_str()

    def getChildren(self):
        if self.arguments is not None:
            return [self.expr, self.arguments]
        return [self.expr]


class While(object, Getliner):
    text = "While"
    parent = None
    predicate = None
    statements = None
    line = -1

    def __init__(self, predicate=Expr(), statements=Statements()):
        self.predicate = predicate
        self.predicate.parent = self
        self.statements = statements
        self.statements.parent = self

    def oneline_str(self):
        return "while(%s)%s" % (self.predicate.oneline_str(), self.statements.oneline_str())

    def __str__(self):
        return "while (%s) %s" % (format(self.predicate), format(self.statements))

    def getChildren(self):
        return [self.predicate, self.statements]

    def smallprint(self):
        return "while (%s)" % self.predicate


class DoWhile(object, Getliner):
    text = "DoWhile"
    parent = None
    predicate = None
    statements = None
    line = -1

    def __init__(self, statements=Statements(), predicate=Expr()):
        self.predicate = predicate
        self.predicate.parent = self
        self.statements = statements
        self.statements.parent = self

    def oneline_str(self):
        return "do %swhile(%s)" % (self.statements.oneline_str(), self.predicate.oneline_str())

    def __str__(self):
        return "do %swhile(%s)" % (self.statements, self.predicate)

    def getChildren(self):
        return [self.predicate, self.statements]

    def smallprint(self):
        return "dowhile (%s)" % self.predicate


class For(object, Getliner):
    text = "For"
    initpart = None
    expr1 = None
    expr2 = None
    statements = None
    line = -1

    def __init__(self, initpart=None, expr1=None, expr2=None, statements=None):
        self.initpart = initpart
        if self.initpart is not None:
            self.initpart.parent = self
        self.expr1 = expr1
        if self.expr1 is not None:
            self.expr1.parent = self
        self.expr2 = expr2
        if self.expr2 is not None:
            self.expr2.parent = self
        self.statements = statements
        if self.statements is not None:
            self.statements.parent = self

    def oneline_str(self):
        ret = "for(%s;%s;%s)%s" % (
        self.initpart.oneline_str(), self.expr1.oneline_str(), self.expr2.oneline_str(), self.statements.oneline_str())
        return ret

    def __str__(self):
        ret = "for (%s;%s;%s)%s" % (self.initpart, self.expr1, self.expr2, self.statements)
        return ret

    def getChildren(self):
        ret = []
        if self.initpart is not None:
            ret.append(self.initpart)
        if self.expr1 is not None:
            ret.append(self.expr1)
        if self.expr2 is not None:
            ret.append(self.expr2)
        if self.statements is not None:
            ret.append(self.statements)
        return ret

    def smallprint(self):
        return "for (%s;%s;%s)" % (self.initpart, self.expr1, self.expr2)


# class ForIn(object, Getliner):
#     text = "ForIn"
#     initpart = None
#     statements = None
#     line = -1
#     each = False
#
#     def __init__(self, initpart=None, statements=None, expr1=None, each=False):
#         self.initpart = initpart
#         self.expr1 = expr1
#         self.expr1.parent = self
#         self.initpart.parent = self
#         self.statements = statements
#         if self.statements is not None:
#             self.statements.parent = self
#
#     def oneline_str(self):
#         s = ""
#         if self.statements is not None:
#             s = self.statements.oneline_str()
#         ret = "for %s(%s in %s) %s" % (
#         "each" if self.each else "", self.initpart.oneline_str(), self.expr1.oneline_str(), s)
#         return ret
#
#     def __str__(self):
#         s = ""
#         if self.statements is not None:
#             s = "%s" % self.statements
#         ret = "for %s(%s in %s) %s" % ("each" if self.each else "", self.initpart, self.expr1, s)
#         return ret
#
#     def getChildren(self):
#         ret = []
#         if self.initpart is not None:
#             ret.append(self.initpart)
#         if self.expr1 is not None:
#             ret.append(self.expr1)
#         if self.statements is not None:
#             ret.append(self.statements)
#         return ret
#
#     def smallprint(self):
#         return "for %s(%s in %s)" % ("each" if self.each else "", self.initpart, self.expr1)


class EmptyStatement(object, Selfsmallprinter, Getliner, Onelineisstr):
    line = -1
    text = "EmptyStatement"
    parent = None

    def __str__(self):
        return ""

    def getChildren(self):
        return []


class If(object, Getliner):
    text = "If"
    parent = None
    exprs = []
    statements = []
    line = -1

    def __init__(self, exprs=[], statements=[]):
        self.exprs = exprs[:]
        for e in self.exprs:
            e.parent = self
        self.statements = statements[:]
        for e in self.statements:
            e.parent = self

    def __str__(self):
        ret = ""
        if len(self.statements) == 1:
            ret = "if(%s)%s" % (format(self.exprs[0]), format(self.statements[0]))
        elif len(self.statements) == 2:
            ret = "if(%s)%selse%s" % (format(self.exprs[0]), format(self.statements[0]), format(self.statements[1]))
        elif len(self.statements) >= 3:
            start = "if(%s)%s" % (format(self.exprs[0]), format(self.statements[0]))
            end = ""
            if len(self.statements) > len(self.exprs):
                end = "else%s" % (format(self.statements[-1]))
            for i in range(1, len(self.exprs)-1):
                ret += "else if(%s)%s" % (format(self.exprs[i]), format(self.statements[i]))
            ret = start + ret + end
        return ret
        # return "if(%s)%selse%s" % (format(self.predicate), format(self.statementstrue), format(self.statementsfalse))

    def oneline_str(self):
        ret = ""
        if len(self.statements) == 1:
            ret = "if(%s)%s" % (self.exprs[0].oneline_str(), self.statements[0].oneline_str())
        elif len(self.statements) == 2:
            ret = "if(%s)%selse%s" % (self.exprs[0].oneline_str(), self.statements[0].oneline_str(), self.statements[1].oneline_str())
        elif len(self.statements) >= 3:
            start = "if(%s)%s" % (self.exprs[0].oneline_str(), self.statements[0].oneline_str())
            end = ""
            if len(self.statements) > len(self.exprs):
                end = "else%s" % (self.statements[-1].oneline_str())
            for i in range(1, len(self.exprs) - 1):
                ret += "else if(%s)%s" % (self.exprs[i].oneline_str(), self.statements[i].oneline_str())
            ret = start + ret + end
        return ret

    def getChildren(self):
        return self.exprs + self.statements

    # def smallprint(self):
    #     if self.statementsfalse is None:
    #         return "if(%s)" % self.predicate
    #     return "if(%s) else" % self.predicate

# class If(object, Getliner):
#     text = "If"
#     parent = None
#     predicate = None
#     statementstrue = None
#     statementsfalse = None
#     line = -1
#
#     def __init__(self, predicate=Expr(), statementstrue=None, statementsfalse=None):
#         self.predicate = predicate
#         self.predicate.parent = self
#         self.statementstrue = statementstrue
#         self.statementstrue.parent = self
#         if statementsfalse is not None:
#             self.statementsfalse = statementsfalse
#             self.statementsfalse.parent = self
#
#     def __str__(self):
#         if self.statementsfalse is None:
#             return "if(%s)%s" % (format(self.predicate), format(self.statementstrue))
#         return "if(%s)%selse%s" % (format(self.predicate), format(self.statementstrue), format(self.statementsfalse))
#
#     def oneline_str(self):
#         if self.statementsfalse is None:
#             return "if(%s)%s" % (self.predicate.oneline_str(), self.statementstrue.oneline_str())
#         return "if(%s)%s else %s" % (
#         self.predicate.oneline_str(), self.statementstrue.oneline_str(), self.statementsfalse.oneline_str())
#
#     def getChildren(self):
#         l = [self.predicate, self.statementstrue]
#         if self.statementsfalse is not None:
#             l.append(self.statementsfalse)
#         return l
#
#     def smallprint(self):
#         if self.statementsfalse is None:
#             return "if(%s)" % self.predicate
#         return "if(%s) else" % self.predicate


class Program(object, Textsmallprinter, Getliner):
    text = "Program"
    parent = None
    line = -1
    list = []

    def __init__(self, list=[]):
        self.list = list[:]
        for l in self.list:
            l.parent = self

    def oneline_str(self):
        ret = "".join(map(lambda x: x.oneline_str(), self.list))
        return ret

    def __str__(self):
        ret = "".join(map(lambda x: str(x), self.list))
        return ret

    def getChildren(self):
        return self.list


class Emit(object, Textsmallprinter, Getliner):
    text = "Emit"
    parent = None
    fcall = None
    line = -1

    def __init__(self, fcall=Functioncall()):
        self.fcall = fcall
        self.fcall.parent = self

    def oneline_str(self):
        return "emit %s" % format(self.fcall.oneline_str())

    def __str__(self):
        return "emit %s" % str(self.fcall)

    def getChildren(self):
        return [self.fcall]


class UsingForDeclaration(object, Textsmallprinter, Getliner):
    text = "UsingForDeclaration"
    parent = None
    line = -1
    ident = None
    type = ""

    def __init__(self, ident=Ident(), type=""):

        self.ident = ident
        self.type = type
        self.ident.parent = self

    def replace_ident(self, ident):
        self.ident = ident
        self.ident.parent = self

    def oneline_str(self):
        ret = "using %s for %s;" % (str(self.ident), self.type)
        return ret

    def __str__(self):
        ret = "using %s for %s;\n" % (str(self.ident), self.type)
        return ret

    def getChildren(self):
        return [self.ident]


class StructDefinition(object, Textsmallprinter, Getliner):
    text = "StructDefinition"
    parent = None
    line = -1
    ident = None
    varlist =[]

    def __init__(self, ident=Ident(), varlist=[]):

        self.ident = ident
        self.varlist = varlist[:]
        self.ident.parent = self
        for l in self.varlist:
            l.parent = self

    def replace_ident(self, ident):
        self.ident = ident
        self.ident.parent = self

    def oneline_str(self):
        ret = "struct %s {%s}" % (str(self.ident), "".join(map(lambda x: x.oneline_str() + ";", self.varlist)))
        return ret

    def __str__(self):
        ret = "struct %s {%s}\n" % (str(self.ident), "".join(map(lambda x: str(x) + ";", self.varlist)))
        return ret

    def getChildren(self):
        return [self.ident] + self.varlist


class EnumDefinition(object, Textsmallprinter, Getliner):
    text = "EnumDefinition"
    parent = None
    line = -1
    ident = None
    idents = []

    def __init__(self, ident=Ident(), idents=[]):

        self.ident = ident
        self.idents = idents[:]
        self.ident.parent = self
        for l in self.idents:
            l.parent = self

    def replace_ident(self, ident):
        self.ident = ident
        self.ident.parent = self

    def oneline_str(self):
        ret = "enum %s {%s}" % (str(self.ident), ",".join(map(lambda x: x.oneline_str(), self.idents)))
        return ret

    def __str__(self):
        ret = "enum %s {%s}\n" % (str(self.ident), ",".join(map(lambda x: str(x), self.idents)))
        return ret

    def getChildren(self):
        return [self.ident] + self.idents


class Inheritance(object, Textsmallprinter, Getliner):
    text = "Inheritance"
    parent = None
    line = -1
    ident = None
    exprs =[]

    def __init__(self, ident=Ident(), exprs=[]):

        self.ident = ident
        self.exprs = exprs[:]
        for e in self.exprs:
            e.parent = self
        self.ident.parent = self

    def replace_ident(self, ident):
        self.ident = ident
        self.ident.parent = self

    def oneline_str(self):
        ret = str(self.ident)
        if len(self.exprs) > 0:
            ret += "(%s)" % (",".join(map(lambda x: x.oneline_str(), self.exprs)))
        return ret

    def __str__(self):
        ret = str(self.ident)
        if len(self.exprs) > 0:
            ret += "(%s)" % (",".join(map(lambda x: str(x), self.exprs)))
        return ret

    def getChildren(self):
        if len(self.exprs) > 0:
            return [self.ident] + self.exprs
        return [self.ident]


class Contract(object, Textsmallprinter, Getliner):
    text = "Contract"
    parent = None
    statements = None
    line = -1
    t = ""
    ident = None
    inheritance = []
    contractpart = []

    def __init__(self, t="contract", ident=Ident(), inheritance=[], contractpart=[]):
        self.t = t
        self.ident = ident
        self.ident.parent = self
        if len(inheritance) > 0:
            self.inheritance = inheritance[:]
            for i in self.inheritance:
                i.parent = self
        if len(contractpart) > 0:
            self.contractpart = contractpart[:]
            for i in self.contractpart:
                i.parent = self

    def replace_ident(self, ident):
        self.ident = ident
        self.ident.parent = self

    def oneline_str(self):
        ret = self.t + " " + str(self.ident)
        if len(self.inheritance) > 0:
            ret += " is " + ",".join(map(lambda x: "%s" % x.oneline_str(), self.inheritance))
        if len(self.contractpart) > 0:
            ret += "{" + "".join(map(lambda x: "%s" % x.oneline_str(), self.contractpart)) + "}"
        return ret

    def __str__(self):
        ret = self.t + " " + str(self.ident)
        if len(self.inheritance) > 0:
            ret += " is " + ",".join(map(lambda x : "%s" % str(x), self.inheritance))
        if len(self.contractpart) > 0:
            ret += "{\n" + "".join(map(lambda x: "%s" % str(x), self.contractpart)) + "}"
        return ret

    def getChildren(self):
        p = [self.ident]
        if len(self.inheritance) > 0:
            p += self.inheritance
        if len(self.contractpart) > 0:
            p += self.contractpart
        return p


# class Block(object, Textsmallprinter, Getliner):
#     text = "Block"
#     parent = None
#     statements = None
#     line = -1
#
#     def __init__(self, statements=Statements()):
#         self.statements = statements
#         self.statements.parent = self
#
#     def oneline_str(self):
#         return format(self.statements.oneline_str())        ###
#
#     def __str__(self):
#         return self.statements.__str__(INDENT="")
#
#     def getChildren(self):
#         return [self.statements]


class Returns(object, Textsmallprinter, Getliner):
    text = "Returns"
    parent = None
    #statements = None
    line = -1
    args = None

    def __init__(self, args=Listarguments()):
        self.args = args
        self.args.parent = self

    def oneline_str(self):
        return "returns %s" % str(self.args.oneline_str())

    def __str__(self):
        return "returns %s" % str(self.args)

    def getChildren(self):
        return [self.args]


class Ufixed(object, Textsmallprinter, Getliner):
    text = "Ufixed"
    parent = None
    line = -1
    args = None
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def getChildren(self):
        return []


class Fixed(object, Textsmallprinter, Getliner):
    text = "Fixed"
    parent = None
    line = -1
    args = None
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def getChildren(self):
        return []


class Byte(object, Textsmallprinter, Getliner):
    text = "Byte"
    parent = None
    line = -1
    args = None
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def getChildren(self):
        return []


class Bool(object, Textsmallprinter, Getliner):
    text = "Bool"
    parent = None
    line = -1
    args = None
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def getChildren(self):
        return []


class Address(object, Textsmallprinter, Getliner):
    text = "Address"
    parent = None
    line = -1
    args = None
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def getChildren(self):
        return []


class Int(object, Textsmallprinter, Getliner):
    text = "Int"
    parent = None
    line = -1
    args = None
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def getChildren(self):
        return []


class Uint(object, Textsmallprinter, Getliner):
    text = "Uint"
    parent = None
    line = -1
    args = None
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def getChildren(self):
        return []


# class Anonymous(object, Textsmallprinter, Getliner):
#     text = "Anonymous"
#     parent = None
#     line = -1
#     args = None
#
#     def __init__(self):
#         self.parent = self
#
#     def oneline_str(self):
#         return "Anonymous"
#
#     def __str__(self):
#         return "Anonymous"
#
#     def getChildren(self):
#         return []


# class External(object, Textsmallprinter, Getliner):
#     text = "External"
#     parent = None
#     line = -1
#     args = None
#
#     def __init__(self):
#         self.parent = self
#
#     def oneline_str(self):
#         return "External"
#
#     def __str__(self):
#         return "External"
#
#     def getChildren(self):
#         return []


# class Indexed(object, Textsmallprinter, Getliner):
#     text = "Indexed"
#     parent = None
#     line = -1
#     args = None
#
#     def __init__(self):
#         self.parent = self
#
#     def oneline_str(self):
#         return "indexed"
#
#     def __str__(self):
#         return "indexed"
#
#     def getChildren(self):
#         return []


# class Public(object, Textsmallprinter, Getliner):
#     text = "Public"
#     parent = None
#     line = -1
#     args = None
#
#     def __init__(self):
#         self.parent = self
#
#     def oneline_str(self):
#         return "public"
#
#     def __str__(self):
#         return "public"
#
#     def getChildren(self):
#         return []
#

# class Internal(object, Textsmallprinter, Getliner):
#     text = "Internal"
#     parent = None
#     line = -1
#     args = None
#
#     def __init__(self):
#         self.parent = self
#
#     def oneline_str(self):
#         return "Internal"
#
#     def __str__(self):
#         return "Internal"
#
#     def getChildren(self):
#         return []


# class Private(object, Textsmallprinter, Getliner):
#     text = "private"
#     parent = None
#     line = -1
#     args = None
#
#     def __init__(self):
#         self.parent = self
#
#     def oneline_str(self):
#         return "Private"
#
#     def __str__(self):
#         return "Private"
#
#     def getChildren(self):
#         return []

#
# class Pure(object, Textsmallprinter, Getliner):
#     text = "Pure"
#     parent = None
#     line = -1
#     args = None
#
#     def __init__(self):
#         self.parent = self
#
#     def oneline_str(self):
#         return "pure"
#
#     def __str__(self):
#         return "pure"
#
#     def getChildren(self):
#         return []


# class Constant(object, Textsmallprinter, Getliner):
#     text = "Constant"
#     parent = None
#     line = -1
#     args = None
#
#     def __init__(self):
#         self.parent = self
#
#     def oneline_str(self):
#         return "constant"
#
#     def __str__(self):
#         return "constant"
#
#     def getChildren(self):
#         return []


# class View(object, Textsmallprinter, Getliner):
#     text = "View"
#     parent = None
#     line = -1
#     args = None
#
#     def __init__(self):
#         self.parent = self
#
#     def oneline_str(self):
#         return "view"
#
#     def __str__(self):
#         return "view"
#
#     def getChildren(self):
#         return []


# class Payable(object, Textsmallprinter, Getliner):
#     text = "Payable"
#     parent = None
#     line = -1
#     args = None
#
#     def __init__(self):
#         self.parent = self
#
#     def oneline_str(self):
#         return "payable"
#
#     def __str__(self):
#         return "payable"
#
#     def getChildren(self):
#         return []

class ModifierInvocation(object, Textsmallprinter, Getliner):
    text = "ModifierInvocation"
    parent = None
    line = -1
    args = None
    ident = None
    exprs = []

    def __init__(self, ident=Ident(), exprs=[]):
        self.ident = ident
        self.ident.parent = self
        self.exprs = exprs[:]
        for i in self.exprs:
            i.parent = self

    def oneline_str(self):
        ret = str(self.ident)
        if len(self.exprs) > 0:
            ret += "(%s)" % (",".join(map(lambda x : "%s" % x.oneline_str(), self.exprs)))
        return ret

    def __str__(self):
        ret = str(self.ident)
        if len(self.exprs) > 0:
            ret += "(%s)" % (",".join(map(lambda x: "%s" % x.oneline_str(), self.exprs)))
        return ret

    def getChildren(self):
        if len(self.exprs) > 0:
            return [self.ident] + self.exprs
        return [self.ident]


class ModifierList(object, Textsmallprinter, Getliner):
    text = "ModifierList"
    parent = None
    line = -1
    args = None
    keywords = []
    mi = []

    def __init__(self, mi=[], keywords=[]):
        self.mi = mi[:]
        for i in self.mi:
            i.parent = self
        self.keywords = keywords[:]

    def oneline_str(self):
        ret = ""
        if len(self.mi) > 0:
            ret += " ".join(map(lambda x: "%s" % x.oneline_str(), self.mi)) + " "
        if len(self.keywords) > 0:
            ret += " ".join(map(lambda x: "%s" % str(x), self.keywords))
        return ret

    def __str__(self):
        ret = ""
        if self.mi is not None:
            ret += " ".join(map(lambda x: "%s" % str(x), self.mi)) + " "
        if len(self.keywords) > 0:
            ret += " ".join(map(lambda x: "%s" % str(x), self.keywords))
        return ret

    def getChildren(self):

        return self.mi


class Modifier(object, Getliner):
    text = "Modifier"
    parent = None
    ident = None
    args_dec = None
    statements = None
    functionexpr = False
    functional = False
    line = -1

    def __init__(self, ident=Ident(), args_dec=Listarguments(), statements=Statements()):
        self.ident = ident
        if ident is not None:
            self.ident.parent = self
        self.statements = statements
        self.statements.parent = self
        self.args_dec = args_dec
        self.args_dec.parent = self

    def oneline_str(self):
        if self.ident is not None:
            return "modifier %s %s %s" % (
            str(self.ident), str(self.args_dec.oneline_str()), str(self.statements.oneline_str()))
        return "modifier %s %s" % (str(self.args_dec.oneline_str()), str(self.statements.oneline_str()))

    def __str__(self):
        ret = ""
        if self.ident is not None:
            ret = "modifier %s %s %s" % (str(self.ident), str(self.args_dec), str(self.statements))
        else:
            ret = "modifier %s %s" % (str(self.args_dec), str(self.statements))
        return ret

    def replace_ident(self, ident):
        self.ident = ident
        self.ident.parent = self

    def getChildren(self):
        if self.ident is not None:
            return [self.ident, self.args_dec, self.statements]
        return [self.args_dec, self.statements]

    def smallprint(self):
        if self.ident is not None:
            return "modifier %s %s" % (self.ident, self.args_dec)
        return "modifier %s" % self.args_dec


class Function(object, Getliner):
    text = "Function"
    parent = None
    ident = None
    args_dec = None
    statements = None
    line = -1
    ml = None
    returns = None

    def __init__(self, ident=None, args_dec=Listarguments(), ml=ModifierList(), returns=None, statements=Statements()):
        if ident is not None:
            self.ident = ident
            self.ident.parent = self
        self.statements = statements
        self.statements.parent = self
        self.args_dec = args_dec
        self.args_dec.parent = self
        if returns is not None:
            self.returns = returns
            self.returns.parent = self
        if ml is not None:
            self.ml = ml
            self.ml.parent = self

    def oneline_str(self):
        if self.ident is not None:
            if self.returns is not None:
                return "function %s %s %s %s %s" % (str(self.ident), str(self.args_dec.oneline_str()),
                        self.ml.oneline_str(), self.returns.oneline_str(), str(self.statements.oneline_str()))
            return "function %s %s %s %s" % (str(self.ident), str(self.args_dec.oneline_str()),
                                                self.ml.oneline_str(), str(self.statements.oneline_str()))
        else:
            if self.returns is not None:
                return "function %s %s %s %s" % (str(self.args_dec.oneline_str()), self.ml.oneline_str(), self.returns.oneline_str(), str(self.statements.oneline_str()))
            return "function %s %s %s" % (str(self.args_dec.oneline_str()), self.ml.oneline_str(), str(self.statements.oneline_str()))

    def __str__(self):
        if self.ident is not None:
            if self.returns is not None:
                return "function %s %s %s %s %s" % (str(self.ident), str(self.args_dec),
                                                    str(self.ml), str(self.returns), str(self.statements))
            return "function %s %s %s %s" % (str(self.ident), str(self.args_dec),
                                             str(self.ml), str(self.statements))
        else:
            if self.returns is not None:
                return "function %s %s %s %s" % (str(self.args_dec), str(self.ml), str(self.returns), str(self.statements))
            return "function %s %s %s" % (str(self.args_dec), str(self.ml), str(self.statements))

    def replace_ident(self, ident):
        self.ident = ident
        self.ident.parent = self

    def getChildren(self):
        ret = []
        if self.ident is not None:
            ret.append(self.ident)
        ret.append(self.args_dec)
        ret.append(self.ml)
        if self.returns is not None:
            ret.append(self.returns)
        ret.append(self.statements)
        return ret

    # def smallprint(self):
    #     if self.ident is not None:
    #         return "function %s %s" % (self.ident, self.args_dec)
    #     return "function %s" % (self.args_dec)


class EventDefinition(object, Getliner):
    text = "Event"
    parent = None
    ident = None
    args_dec = None
    line = -1
    anonymous = ""

    def __init__(self, ident=Ident(), args_dec=Listarguments(), anonymous=""):
        self.ident = ident
        self.ident.parent = self
        self.args_dec = args_dec
        self.args_dec.parent = self
        self.anonymous = anonymous

    def replace_ident(self, ident):
        self.ident = ident
        self.ident.parent = self

    def oneline_str(self):
        if self.anonymous is not None:
            return "event %s %s %s" % (
            str(self.ident), str(self.args_dec.oneline_str()), str(self.anonymous)) + ";"
        return "event %s %s" % (str(self.ident), str(self.args_dec.oneline_str())) + ";"

    def __str__(self):
        ret = ""
        if self.anonymous is not None:
            ret = "event %s %s %s" % (str(self.ident), str(self.args_dec), str(self.anonymous))
        else:
            ret = "event %s %s" % (str(self.ident), str(self.args_dec))
        return ret + ";\n"

    def getChildren(self):
        return [self.ident, self.args_dec]

    def smallprint(self):
        if self.anonymous is not None:
            return "event %s %s %s" % (self.ident, self.args_dec, self.anonymous)
        return "event %s %s" % (self.ident, self.args_dec)


class ConstructorDefinition(object, Textsmallprinter, Getliner):
    text = "ConstructorDefinition"
    parent = None
    line = -1
    statements = None
    ml = None
    args = None

    def __init__(self, args=Listarguments(), ml=ModifierList(), statements=Statements()):
        self.args = args
        self.args.parent = self
        self.ml = ml
        self.ml.parent = self
        self.statements = statements
        self.statements.parent = self

    def replace_ident(self, ident):
        self.ident = ident
        self.ident.parent = self

    def oneline_str(self):
        return "constructor %s %s %s" % (self.args.oneline_str(), self.ml.oneline_str(), self.statements.oneline_str())

    def __str__(self):
        return "constructor %s %s %s" % (str(self.args), str(self.ml), str(self.statements))

    def getChildren(self):
        return [self.args, self.ml, self.statements]