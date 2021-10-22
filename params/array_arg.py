from arraybase import ArrayMixin, _IntTuple, _IntOrIntTuple
import functools as ft


class ArrayParam(ArrayMixin):
    def __init__(self, dims: _IntTuple, values: _IntOrIntTuple) -> None:
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
        self.dims = dims
        self.values = values

    @classmethod
    def _mkArray(cls, dims: _IntTuple, values: _IntTuple) -> 'ArrayParam':
        return cls(dims, values)

class Scalar(ArrayParam):
    def __init__(self, value: int):
        super().__init__((), value)

