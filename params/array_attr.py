from arraybase import ArrayMixin, _IntTuple, _IntOrIntTuple
import functools as ft


class ArrayAttr(ArrayMixin):
    def __init__(self, values: _IntOrIntTuple) -> None:
        dims = self.dims
        size = ft.reduce(int.__mul__, dims, 1)
        if dims and len(values) != size:
            raise ValueError()

        if not dims:
            if isinstance(values, tuple):
                if len(values) != 1:
                    raise ValueError()
                values = values[0]
            if not isinstance(values, int):
                raise TypeError(f'{dims}, {values}')
            values = (values,)
        self.values = values

    @classmethod
    def _mkArray(cls, dims: _IntTuple, values: _IntTuple) -> 'ArrayParam':
        Array = type(cls)('ArrayT', (ArrayAttr,), dict(dims=dims))
        return Array(values)

class Scalar(ArrayAttr):
    dims = ()
