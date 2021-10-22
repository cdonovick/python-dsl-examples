import ctypes

lib = ctypes.cdll.LoadLibrary('./libtest.so')

class Test(ctypes.Structure):
    _fields_ = [
                ('x', ctypes.c_uint),
                ('y', ctypes.c_uint),
                ('z', ctypes.c_short),
    ]


test = Test(0xdeadbeaf, 0, -1)

sizes = (ctypes.c_size_t * 6)(ctypes.sizeof(ctypes.c_int), 0, ctypes.sizeof(ctypes.c_int), 0, ctypes.sizeof(ctypes.c_short), 0)

res = lib.print_buf(ctypes.c_size_t(6), sizes, ctypes.pointer(test))


print(f'lib returned {res}')
