import typing as tp
import libcst as cst

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
