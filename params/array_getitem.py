from arraybase import ArrayMixin, _IntTuple, _IntOrIntTuple
import functools as ft
import weakref

_CACHE = weakref.WeakValueDictionary()
class ArrayGetItem(ArrayMixin):
    def __init__(self, values: _IntOrIntTuple) -> None:
        dims = self.dims
        size = ft.reduce(int.__mul__, dims, 1)
        if dims and len(values) != size:
            raise ValueError()

        if not dims:
            if isinstance(values, tuple):
                if len(values) != 1:
                    raise ValueError()
            elif not isinstance(values, int):
                raise TypeError(f'{dims}, {values}')
            else:
                values = values,
        self.values = values

    def __class_getitem__(cls, dims):
        if hasattr(cls, 'dims'):
            raise TypeError(f'{cls} is already bound to {cls.dims}')
        if not isinstance(dims, tuple):
            if not isinstance(dims, int):
                raise TypeError()
            dims = dims,

        try:
            return _CACHE[dims]
        except KeyError:
            pass

        T = type(cls)(f"ArrayGetItem[{dims}]", (ArrayGetItem,), dict(dims=dims))
        return T

    @classmethod
    def _mkArray(cls, dims: _IntTuple, values: _IntTuple) -> 'ArrayParam':
        return ArrayGetItem[dims](values)

Scalar = ArrayGetItem[()]
