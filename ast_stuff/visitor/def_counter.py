import typing as tp
import libcst as cst

class DefCounter(cst.CSTVisitor):
    count: int

    def __init__(self):
        self.count = 0


    def visit_FunctionDef(self,
            node: cst.FunctionDef) -> tp.Optional[bool]:
        self.count += 1
