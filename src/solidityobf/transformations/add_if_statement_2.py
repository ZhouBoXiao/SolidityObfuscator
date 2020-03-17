from solidityobf.common.classes import Number, Expr, Statements, EmptyStatement, If
from solidityobf.common import *
from solidityobf.common.common import deepcopy,check_tree, solidityobf_random, is_functioncall_inside, is_function_inside
from solidityobf.common.tree_walker import walker
from solidityobf.transformations.common import NUMBERMAX, count_object, shouldi, genPredicate


def add_if_statement_2(program_tree, verbose=0, numbermax=NUMBERMAX):
    if verbose > 1:
        print "apply add_if_statement transformation", "with", numbermax
    p = deepcopy(program_tree)
    arg = {"numbermax":numbermax}
    arg["size"] = count_object(p, [Statements])
    walker(p, postfunction=add_if_statement_2_func_post, arg=arg)
    return p


def add_if_statement_2_func_post(program, arg):
    if program.__class__ == Statements:   
        if shouldi(arg=arg) :#and not is_function_inside(program):
            o = program.statements_list
            if len(o) > 0:
                ifrom = solidityobf_random.randint(0, len(o) - 1)
                ito = solidityobf_random.randint(ifrom, len(o))
                s1 = deepcopy(o[ifrom:ito])
                s2 = deepcopy(o[ifrom:ito])
                for i in range(len(s2), 0, -1):
                    if solidityobf_random.randint(0, 4) == 0:
                        del s2[i-1]
                flipcoin = solidityobf_random.randint(0, 1)
                if not flipcoin:
                    s1, s2 = s2, s1
                if not flipcoin:
                    ie = If([genPredicate(program, flipcoin)], [Statements([EmptyStatement()]), Statements(s2)])
                else:
                    ie = If([genPredicate(program, flipcoin)], [Statements(s1), Statements([EmptyStatement()])])
                program.replaceall(o[:ifrom])
                program.append(ie)
                program.append_list(o[ito:])
    return [], arg
