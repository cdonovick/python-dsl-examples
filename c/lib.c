#include "lib.h"
#include "inttypes.h"
#include "stdio.h"

int print_bufs(size_t n, size_t* sizes, byte* buf, char* sep) {
	byte* ptr = buf;
	for (size_t i = 0; i < n; ++i) {
		switch (sizes[i]) {
			case 0:
				printf("%s", sep);
				break;
			case 1:
				printf("%" PRIx8, *((uint8_t*) ptr));
				break;
			case 2:
				printf("%" PRIx16, *((uint16_t*) ptr));
				break;
			case 4:
				printf("%" PRIx32, *((uint32_t*) ptr));
				break;
			case 8:
				printf("%" PRIx64, *((uint64_t*) ptr));
				break;
			default:
				printf("error\n");
				return 1;
		}
		ptr = ptr + sizes[i];
	}
	return 0;

}

int print_buf(size_t n, size_t* sizes, byte* buf) {
	return print_bufs(n, sizes, buf, "\n");
}

