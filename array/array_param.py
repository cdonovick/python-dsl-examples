from array_mix import ArrayMixin

class Array(ArrayMixin):
    def __init__(self, T, N, vals):
        self._validate_TN(T, N)
        self.T = T
        self.N = N
        self._validate_vals(vals)
        self.vals = vals


if __name__ == '__main__':
    a = Array(int, 5, list(range(5)))
    b = Array(str, 3, 'abc')

    assert type(a) is type(b) is Array
    print(type(a))

    try:
        a[0] = b[0]
    except TypeError:
        print('raised TypeError')
    else:
        print('did not raise')

