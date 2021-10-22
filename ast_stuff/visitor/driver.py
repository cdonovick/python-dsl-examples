import typing as tp
import libcst as cst
import sys
from def_counter import DefCounter
from fun_counter import FunCounter
from method_counter import MethodCounter

assert len(sys.argv) == 2

with open('fodder.py', 'r') as f:
    src = f.read()

tree = cst.parse_module(src)
if sys.argv[1] == 'def':
    visitor = DefCounter()
elif sys.argv[1] == 'fun':
    visitor = FunCounter()
else:
    assert sys.argv[1] == 'meth'
    visitor = MethodCounter()

tree.visit(visitor)

print(visitor.count)
