#ifndef LIB_H
#define LIB_H
#include "stdint.h"
#include "stddef.h"

typedef uint8_t byte;

int print_bufs(size_t n, size_t* sizes, byte* buf, char* sep);
int print_buf(size_t n, size_t* sizes, byte* buf);

#endif
