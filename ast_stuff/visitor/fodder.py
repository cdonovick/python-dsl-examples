def f():
    def local_func(): pass

    class LocalClass:
        def __init__(self):
            def super_local_func(): pass

class S:
    def __init__(self):
        def local_func(): pass


    if True:
        def method(self): pass # impl 1
    else:
        def method(self): pass # impl 2


class S:
    def method(self):
        class LocalClass:
            def __init__(self): pass
