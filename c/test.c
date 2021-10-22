#include "lib.h"
#include "test.h"

int main(void)
{
	Test t;
	t.x = 0xdeadbeaf;
	t.y = 0;
	t.z = -1;

	size_t sizes[6] = {sizeof(int), 0, sizeof(int), 0, sizeof(short), 0};
	int rval = print_buf(6, sizes, (byte*) &t);

	return rval;
}
