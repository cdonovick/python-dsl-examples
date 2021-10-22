import cffi
import _lib.lib as lib

ffi = cffi.FFI()

with open('test.h.pre', 'r') as f:
    ffi.cdef(f.read())

with open('lib.h.pre', 'r') as f:
    ffi.cdef(f.read())

def get_field_size(ptr, field):
    ptr_t = ffi.typeof(ptr)
    t =  ptr_t.item
    fields = dict(t.fields)
    try:
        field_obj = fields[field]
    except KeyError:
        raise ValueError(f'{t} has no field {field}')
    field_t = field_obj.type
    return ffi.sizeof(field_t)

def get_field_sizes(ptr):
    ptr_t = ffi.typeof(ptr)
    t =  ptr_t.item
    sizes = {}
    for field_name, field_obj in t.fields:
        sizes[field_name] = ffi.sizeof(field_obj.type)

    return sizes

test = ffi.new('Test *', [0xdeadbeaf, 0, -1])
field_sizes = get_field_sizes(test)
sizes = ffi.new('size_t[6]', [field_sizes['x'], 0, field_sizes['y'], 0, field_sizes['z'], 0])
res = lib.print_buf(6, sizes, ffi.cast('byte *', test))

print(f'lib returned {res}')
