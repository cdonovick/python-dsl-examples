import typing as tp
import libcst as cst

class FunCounter(cst.CSTVisitor):
    count: int

    def __init__(self):
        self.count = 0

    def visit_FunctionDef(self,
            node: cst.FunctionDef) -> tp.Optional[bool]:
        self.count += 1

    def visit_ClassDef(self,
            node : cst.ClassDef) -> tp.Optional[bool]:
        return False
