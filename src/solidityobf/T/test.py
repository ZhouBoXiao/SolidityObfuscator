# from solidityobf.common.convert import convert
# from solidityobf.transformations.add_if_statement import add_if_statement
#
# if __name__ == "__main__":
#     # input = sys.stdin.read()
#     # if len (sys.argv) >1:
#     #     prg = sys.argv[1]
#     # else:
#     #     sys.exit()
#
#     prg = 'D:\\PycharmProjects\\JShadobf\\testsuite\prgms\\alert.js'
#     c = convert(prg)
#     for _ in range(10):
#         d = add_if_statement(c)
#     #print d
#     output = format(d)
#     with open("res.js", "w") as f:
#         f.write(output)
#         f.close()

import sys

import antlr3

from solLexer import solLexer
from solParser import solParser

def main(argv):
    char_stream = antlr3.ANTLRFileStream(argv[1], encoding='utf-8')
    lexer = solLexer(char_stream)
    tokens = antlr3.CommonTokenStream(lexer)
    pp = solParser(tokens)
    prgm = pp.sourceUnit()
    tree = prgm.tree

    print()


if __name__ == '__main__':
    main(sys.argv)
