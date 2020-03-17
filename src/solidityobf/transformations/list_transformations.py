'''
Created on Oct 24, 2016

@author: benoit
'''
from solidityobf.transformations.rename_variables import rename_variables
from solidityobf.transformations.add_dummy_variables import add_dummy_variables
from solidityobf.transformations.add_dummy_exprs import add_dummy_exprs
from solidityobf.transformations.add_if_statement import add_if_statement
from solidityobf.transformations.add_if_statement_2 import add_if_statement_2
from solidityobf.transformations.modify_data_flow_1 import modify_data_flow_1
from solidityobf.transformations.modify_data_flow_2 import modify_data_flow_2
from solidityobf.transformations.modify_control_flow_1 import modify_control_flow_1
from solidityobf.transformations.change_str import change_str
from solidityobf.transformations.change_list import change_list
from solidityobf.transformations.aggregate_data import aggregate_data
from solidityobf.transformations.duplicate_function import duplicate_function
from solidityobf.transformations.outlining import outlining
from solidityobf.transformations.evalification import evalification
from solidityobf.transformations.simplify_if import simplify_if
from solidityobf.transformations.remove_empty_statement import remove_empty_statement
TRANSFORMATIONS = [rename_variables,
                   add_dummy_variables,
                   add_dummy_exprs,
                   add_if_statement,
                   add_if_statement_2,
                   modify_data_flow_1,
                   modify_data_flow_2,
                   modify_control_flow_1,
                   change_str,
                   change_list,
                   aggregate_data,
                   duplicate_function,
                   outlining,
                   evalification,

                   simplify_if,
                   remove_empty_statement,
                   ]
