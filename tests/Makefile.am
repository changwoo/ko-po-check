TESTS = $(srcdir)/kpc-test

dist-hook:
	for X in $(srcdir)/test-*.po $(srcdir)/test-*.out; do \
	  install -m644 $$X $(distdir); \
	done
