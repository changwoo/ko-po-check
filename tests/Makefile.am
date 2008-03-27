TESTS = \
	test-00001.test \
	test-00002.test \
	test-00003.test \
	test-00004.test \
	test-00005.test \
	test-00006.test \
	test-00007.test \
	test-00008.test \
	test-00009.test \
	test-00010.test \
	test-00011.test \
	test-00012.test

TESTS_ENVIRONMENT =

EXTRA_DIST = $(TESTS)

dist-hook:
	for X in $(srcdir)/test-*.po $(srcdir)/test-*.out; do \
	  install -m644 $$X $(distdir); \
	done
