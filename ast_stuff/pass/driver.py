import inspect

from ast_tools.passes import apply_passes
from example_pass import example_pass

@apply_passes([example_pass()], metadata_attr='metadata')
class T:
    if False:
        def __init__(self):
            print('version 1')
    else:
        def __init__(self):
            print('version 2')

print(T.metadata)
