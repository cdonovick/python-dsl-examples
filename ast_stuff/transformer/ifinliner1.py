import typing as tp
import libcst as cst

class IfInliner(cst.CSTTransformer):
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
                return cst.FlattenSentinel(update_node.body.body)
            elif update_node.test.value == 'False':
                if update_node.orelse is None:
                    return cst.RemoveFromParent()
                elif isinstance(update_node.orelse, cst.If):
                    return cst.FlattenSentinel(update_node.orelse.body.body)
                else:
                    assert isinstance(update_node.orelse, cst.Else)
                    return cst.FlattenSentinel(update_node.orelse.body.body)
        return update_node



