from solidityobf.common.classes import If
from solidityobf.common.common import *
from solidityobf.common.common import deepcopy
from solidityobf.common.tree_walker import walker
from solidityobf.transformations.common import NUMBERMAX


def simplify_if(program_tree, verbose=False, numbermax=NUMBERMAX):
    if verbose:
        print "apply simplify_if transformation"
    p = deepcopy(program_tree)
    walker(p, simplify_if_func, arg=[])
    return p


def simplify_if_func(program, arg):
    if isinstance(program, If):
        try:
            res = eval(str(program.predicate))
            if res:
                i = program.parent.statements_list.index(program)
                program.parent.statements_list[i] = program.statementstrue
                program.statementstrue.parent = program.parent
            else: 
                i = program.parent.statements_list.index(program)
                if program.statementsfalse is not None:
                    program.parent.statements_list[i] = program.statementsfalse
                    program.statementsfalse.parent = program.parent
                else:
                    del program.parent.statements_list[i] 
        except Exception: 
            pass
    return [], arg
