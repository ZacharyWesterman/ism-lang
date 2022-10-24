
CC = clang++

DSYMUTIL_MAYBE = true
LLVM_SYM_PATH = /usr/bin/llvm-symbolizer

CFLAGS_LLVM_SYM =
ifeq ($(shell test -e $(LLVM_SYM_PATH) && echo 'yes'), yes)
	CFLAGS_LLVM_SYM = -D__HAS_LLVM_SYMBOLIZER__ -D__LLVM_SYMBOLIZER_PATH__=$(LLVM_SYM_PATH)
endif
CFLAGS = -I./gen -I./include -g -ggdb -g3 -std=c++17 -fno-omit-frame-pointer $(CFLAGS_LLVM_SYM) $(CFLAGS_EXTRA)

LFLAGS = -ltcmalloc -lunwind -ldl

ism: ism_main.cpp gen/ism__gen.hpp
	$(CC) $(CFLAGS) $(LFLAGS) $< -o $@

gen/ism__gen.hpp: ism.lang
	langcc -h $< gen

clean:
	rm -rf build gen

.PHONY: clean
