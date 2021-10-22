SRC=lib.c
OBJ=$(SRC:.c=.o)
LIB=libtest.so
TEST=test.c
BIN=test
HEADERS=lib.h test.h
PREPROCESSED=$(HEADERS:.h=.h.pre)
CFLAGS += -std=c99

.PHONY: all
all: $(BIN) $(LIB)


.PHONY: bin
bin: $(BIN)

$(BIN): $(TEST) $(SRC)
	$(CC) $(CFLAGS) $(LDFLAGS) $? -o $@

.PHONY: lib
lib: $(LIB)

$(LIB): LDFLAGS += -shared
$(LIB): $(OBJ)
	$(CC) $(LDFLAGS) $? -o $@

%.o: CFLAGS += -fPIC
%.o: %.c
	$(CC) -c $(CFLAGS) $? -o $@

.PHONY: cffi
cffi: $(PREPROCESSED) $(LIB)
	python3 cffi_compile.py

%.h.pre: %.h
	$(CC) -ansi -E -P $? > $@

.PHONY: clean
clean:
	rm -f $(OBJ) $(BIN) $(LIB) $(PREPROCESSED) _lib*
