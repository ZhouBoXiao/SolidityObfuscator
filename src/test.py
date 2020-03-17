
# -*- coding: UTF-8 -*-
import os
import sys
from antlr4 import *

from solidityobf.common.convert import convert1
from solidityobf.parser.MyVisitor import MyVisitor
from solidityobf.parser.SolidityLexer import SolidityLexer
from solidityobf.parser.SolidityParser import SolidityParser
from solidityobf.parser.SolidityListener import SolidityListener
from solidityobf.parser.SolidityVisitor import SolidityVisitor
from solidityobf.pyminifier import pyminify
from solidityobf.transformations.add_dummy_exprs import add_dummy_exprs
from solidityobf.transformations.add_dummy_variables import add_dummy_variables
from solidityobf.transformations.add_if_statement import add_if_statement
from solidityobf.transformations.add_if_statement_2 import add_if_statement_2
from solidityobf.transformations.aggregate_data import aggregate_data
from solidityobf.transformations.duplicate_function import duplicate_function
from solidityobf.transformations.modify_control_flow_1 import modify_control_flow_1
from solidityobf.transformations.modify_data_flow_1 import modify_data_flow_1
from solidityobf.transformations.modify_data_flow_2 import modify_data_flow_2
from solidityobf.transformations.remove_empty_statement import remove_empty_statement
from solidityobf.transformations.rename_variables import rename_variables


def main(argv):
    # path = "testsuite/testcases/47_array_passer.sol"
    path = argv[1]

    d = convert1(path, 2)
    #for _ in range(10):


    # d = modify_data_flow_1(d, 2)
    # d = modify_data_flow_2(d, 2)
    # d = add_if_statement(d, 2)
    # d = add_if_statement_2(d, 2)
    # d = aggregate_data(d, 2)
    # d = modify_control_flow_1(d, 2)
    # d = add_dummy_exprs(d, 2)

    d = add_dummy_variables(d, 2)
    d = add_dummy_exprs(d, 2)
    d = add_if_statement(d, 2)
    d = add_if_statement_2(d, 2)
    d = modify_data_flow_1(d, 2)
    d = modify_data_flow_2(d, 2)
    # d = duplicate_function(d, 2)
    d = modify_control_flow_1(d, 2)
    print d
    # d = rename_variables(c, 2)
    d = remove_empty_statement(d, 2)
    outfile = path.split('.sol')[0] + '_obf.sol'
    try:
        with open(outfile, 'w') as f:
            f.write(str(d))
            f.close()
    except IOError:
        print "Error: don't found file!"

    options = {'obf_functions': False, 'obf_import_methods': False, 'pyz': None, 'nominify': False,
               'obf_classes': False, 'tabs': False, 'replacement_length': '5', 'bzip2': False, 'destdir': './minified',
               'prepend': None, 'obf_variables': False, 'outfile': outfile, 'obf_builtins': False, 'obfuscate': True,
               'gzip': False, 'use_nonlatin': False}
    pyminify(options, outfile)




if __name__ == '__main__':
    main(sys.argv)
