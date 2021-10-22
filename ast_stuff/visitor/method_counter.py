import typing as tp
import libcst as cst

class MethodCounter(cst.CSTVisitor):
    count: int
    path: tp.List[tp.Union[cst.FunctionDef, cst.ClassDef]]

    def __init__(self):
        self.count = 0
        self.path = []


    def visit_FunctionDef(self,
            node: cst.FunctionDef) -> tp.Optional[bool]:
        if self.path and isinstance(self.path[-1], cst.ClassDef):
            self.count += 1
        self.path.append(node)

    def leave_FunctionDef(self, node: cst.FunctionDef) -> None:
        self.path.pop()

    def visit_ClassDef(self,
            node : cst.ClassDef) -> tp.Optional[bool]:
        self.path.append(node)

    def leave_ClassDef(self, node: cst.FunctionDef) -> None:
        self.path.pop()
