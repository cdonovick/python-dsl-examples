from array_mix import ArrayMixin


_cache = {}
class Array(ArrayMixin):
    def __init__(self, vals):
        N = getattr(self, 'N', ...)
        T = getattr(self, 'T', ...)
        if T is ... or N is ...:
            raise TypeError('cannot instance incomplete type')
        self._validate_vals(vals)
        self.vals = vals

    def __class_getitem__(cls, TN):
        mcs = type(cls)
        T, N = TN

        base_N = getattr(cls, 'N', ...)
        base_T = getattr(cls, 'T', ...)

        if base_N is not ... and N is not ...:
            raise TypeError('redefinition of N is not allowed')
        if base_T is not ... and T is not ...:
            raise TypeError('redefinition of T is not allowed')

        if N is ...:
            N = base_N
        if T is ...:
            T = base_T

        if N is T is ...:
            return cls

        try:
            return _cache[T, N]
        except KeyError:
            pass

        if N is not ... and T is not ...:
            ArrayMixin._validate_TN(T, N)
            name = f'Array[{T.__name__}, {N}]'
            NBase = Array[..., N]
            TBase = Array[T, ...]
            bases = TBase, NBase,
        elif N is not ...:
            name = f'Array[..., {N}]'
            bases = Array,
        elif T is not ...:
            name = f'Array[{T.__name__}, ...]'
            bases = Array,
        else:
            return cls

        cls = mcs(name, bases, {'N': N, 'T': T})
        _cache[T, N] = cls
        return cls

if __name__ == '__main__':
    ArrayOfInt = Array[int, ...]
    ArrayOf5 = Array[..., 5]
    ArrayOf3Str = Array[str, 3]
    ArrayOf5Int = ArrayOfInt[..., 5]
    ArrayOf5Int_2 = ArrayOf5[int, ...]

    assert ArrayOf5Int is ArrayOf5Int_2 is Array[int, 5]
    assert issubclass(ArrayOf5Int, ArrayOf5)
    assert issubclass(ArrayOf5Int, ArrayOfInt)


#   OverWritten = ArrayOf3Str[int, ...]

    print(ArrayOfInt)
    print(ArrayOf3Str)

#    ArrayOfInt([])
    print(Array[int, 5]([1,2,3,4,5]))

