import typing as tp
import libcst as cst
import sys
from ifinliner1 import IfInliner as IfInliner_v1
from ifinliner2 import IfInliner as IfInliner_v2

assert len(sys.argv) == 3
srcs = [
'''
if True:
    code_point_1
else:
    code_point_2
''',
'''
if False:
    code_point_1
else:
    code_point_2
''',
'''
if True:
    code_point_1
elif True:
    code_point_2
else:
    code_point_3
''',
'''
if False:
    code_point_1
elif True:
    code_point_2
else:
    code_point_3
''',
'''
if False:
    code_point_1
elif False:
    code_point_2
else:
    code_point_3
'''
]



if sys.argv[1] == '1':
    transformer = IfInliner_v1()
else:
    assert sys.argv[1] == '2'
    transformer = IfInliner_v2()
src = srcs[int(sys.argv[2])]

tree = cst.parse_module(src)
new_tree = tree.visit(transformer)
print(new_tree.code)
