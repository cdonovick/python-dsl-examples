from abc import ABCMeta, abstractmethod
import functools as ft
import operator
import typing as tp


_IntTuple = tp.Tuple[int, ...]
_IntOrIntTuple = tp.Union[int, _IntTuple]


class ArrayMixin:
    dims: _IntTuple
    values: _IntTuple

    @classmethod
    def _mkArray(cls, dims: _IntTuple, values: _IntTuple) -> 'ArrayMixin': pass

    def __neg__(self):
        return self._mkArray(self.dims, *(-elem for elem in self.values))

    def __pow__(self, power: int):
        if not isinstance(power, int):
            return NotImplemented
        return self._mkArray(self.dims, *(elem**power for elem in self.values))

    def __add__(self, other: 'ArrayMixin') -> 'ArrayMixin':
        if not isinstance(other, ArrayMixin) or self.dims != other.dims:
            return NotImplemented
        return self._mkArray(self.dims, *(x + y for x, y in zip(self.values, other.values)))

    def __sub__(self, other: 'ArrayMixin') -> 'ArrayMixin':
        if not isinstance(other, ArrayMixin) or self.dims != other.dims:
            return NotImplemented
        return self._mkArray(self.dims, *(x - y for x, y in zip(self.values, other.values)))

    def reduce(self) -> 'ArrayMixin':
        def _reduce(dims: _IntTuple, values: _IntTuple) -> tp.Iterator[int]:
            if len(dims) == 1:
                yield sum(values)
            else:
                dim = dims[0]
                n = len(values)
                assert n % dim == 0
                stride = n // dim
                for i in range(dims[0]):
                    yield from _reduce(dims[1:], values[stride*i : stride*(i+1)])

        if not self.dims:
            raise TypeError()

        new_dims = self.dims[:-1]
        return self._mkArray(new_dims, tuple(_reduce(self.dims, self.values)))

    def __repr__(self) -> str:
        def _repr(dims: _IntTuple, values: _IntTuple) -> tp.Iterator[str]:
            if not dims:
                assert len(values) == 1
                yield repr(values[0])
            else:
                dim = dims[0]
                n = len(values)
                assert n % dim == 0
                stride = n // dim
                for i in range(dims[0]):
                    yield '['
                    yield from _repr(dims[1:], values[stride*i : stride*(i+1)])
                    yield ']'
        return '[' + ''.join(_repr(self.dims, self.values)) + ']'
