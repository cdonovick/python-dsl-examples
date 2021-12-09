from array_mix import ArrayMixin

class ArrayMeta(type):
    _cache = {}
    def __new__(mcs, name, bases, namespace):
        N = namespace.get('N', None)
        T = namespace.get('T', None)

        # Make sure we aren't trying to change N or T
        base_N = None
        base_T = None
        for base in bases:
            if isinstance(base, mcs):
                base_N = getattr(base, 'N', base_N)
                base_T = getattr(base, 'T', base_T)

        if base_N is not None and N is not None:
            raise TypeError('redefinition of N is not allowed')
        if base_T is not None and T is not None:
            raise TypeError('redefinition of T is not allowed')

        if N is None:
            N = base_N
        if T is None:
            T = base_T

        try:
            return mcs._cache[T, N]
        except KeyError:
            pass

        if N is not None and T is not None:
            ArrayMixin._validate_TN(T, N)
            namespace['T'] = T
            namespace['N'] = N
            name = f'Array[{T.__name__}, {N}]'
            NBase = mcs('', (), {'N': N})
            TBase = mcs('', (), {'T': T})

            if NBase not in bases:
                bases = *bases, NBase
            if TBase not in bases:
                bases = *bases, TBase

        elif N is not None:
            name = f'Array[..., {N}]'
        elif T is not None:
            name = f'Array[{T.__name__}, ...]'

        namespace['__qualname__'] = name
        cls = super().__new__(mcs, name, bases, namespace)
        mcs._cache[T, N] = cls
        return cls

    def __call__(cls, vals):
        if not hasattr(cls, 'T') or not hasattr(cls, 'N'):
            raise TypeError('cannot instance incomplete type')
        ArrayMixin._validate_vals(cls, vals)
        return super().__call__(vals)

class Array(ArrayMixin, metaclass=ArrayMeta):
    def __init__(self, vals):
        self.vals = vals

if __name__ == '__main__':
    class ArrayOfInt(Array):
        T = int

    class ArrayOf5(Array):
        N = 5

    class ArrayOf3Str(Array):
        T = str
        N = 3

    class ArrayOf5Int(ArrayOfInt, ArrayOf5): pass
    class ArrayOf5Int_2(ArrayOfInt):
        N = 5

    assert ArrayOf5Int is ArrayOf5Int_2
    assert issubclass(ArrayOf5Int, ArrayOf5)
    assert issubclass(ArrayOf5Int, ArrayOfInt)


#    class OverWritten(ArrayOf3Str):
#        N = 4

    print(ArrayOfInt)
    print(ArrayOf3Str)

#    ArrayOfInt([])
    print(ArrayOf5Int([1,2,3,4,5]))
