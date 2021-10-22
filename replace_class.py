class A:
    def __call__(self):
        print('calling an A')

def new_call(self):
    print('calling new_call')


a = A()
b = A()
c = A()

b.__call__ = new_call
c.__class__ = type('AWithNewCall', (A,), dict(__call__=new_call))

a()
b()
c()
