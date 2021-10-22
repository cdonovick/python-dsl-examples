import cffi
import os

ffi = cffi.FFI()

with open('lib.h.pre', 'r') as f:
    ffi.cdef(f.read())

ffi.set_source('_lib',
        '#include "lib.h"',
        libraries=['test'],
        library_dirs=[os.path.dirname(__file__)],
)

ffi.compile()
