class ArrayMixin:
    @staticmethod
    def _validate_TN(T, N):
        if not isinstance(N, int):
            raise TypeError()
        if N < 0:
            raise ValueError()
        if not isinstance(T, type):
            raise TypeError()

    def _validate_vals(self, vals):
        if not len(vals) == self.N:
            raise ValueError()
        for v in vals:
            if not isinstance(v, self.T):
                raise TypeError(f'{v} is not a {self.T}')

    def __getitem__(self, idx):
        return self.vals[idx]

    def __setitem__(self, idx, v):
        if not isinstance(v, self.T):
            raise TypeError()
        self.vals[idx] = v

    def __repr__(self):
        return type(self).__name__ + f'({self.vals})'
