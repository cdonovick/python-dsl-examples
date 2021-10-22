import typing as tp

import libcst as cst

from ast_tools.passes import Pass
from ast_tools.stack import SymbolTable

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

class IfInliner(cst.CSTTransformer):
    def visit_If(self, original_node: cst.If) -> tp.Optional[bool]:
        return False

    def leave_If(self,
            original_node: cst.If,
            update_node: cst.If
            ) -> tp.Union[
                    cst.If,
                    cst.RemovalSentinel,
                    cst.FlattenSentinel[cst.BaseStatement]
                ]:
        if isinstance(update_node.test, cst.Name):
            if update_node.test.value == 'True':
                new_body = update_node.body.visit(self)
                return cst.FlattenSentinel(new_body.body)
            elif update_node.test.value == 'False':
                if update_node.orelse is None:
                    return cst.RemoveFromParent()
                elif isinstance(update_node.orelse, cst.If):
                    return update_node.orelse.visit(self)
                else:
                    new_body = update_node.orelse.body.visit(self)
                    return cst.FlattenSentinel(new_body.body)
        new_body = update_node.body.visit(self)
        if update_node.orelse is None:
            new_orelse = None
        else:
            new_orelse = update_node.orelse.visit(self)

        return update_node.with_changes(body=new_body, orelse=new_orelse)

class example_pass(Pass):
    def rewrite(self,
            tree: cst.CSTNode,
            env: SymbolTable,
            metadata: tp.MutableMapping) -> tp.Tuple[cst.CSTNode, SymbolTable, tp.MutableMapping]:
        transformer = IfInliner()
        visitor = MethodCounter()

        new_tree = tree.visit(transformer)
        new_tree.visit(visitor)
        metadata['method_count'] = visitor.count
        return new_tree, env, metadata
