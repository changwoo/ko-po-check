all:

.PHONY: all test

test:
	@echo testing....
	for T in *.test; do \
	    echo $$T...; \
	    ./$$T || exit 1; \
	done
