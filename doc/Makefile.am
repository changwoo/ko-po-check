doc = ko-po-check
xml = $(doc).xml
entities = spelling-rule.xml

EXTRA_DIST = $(xml) $(entities)

all: html
html: $(doc).xml $(entities)
	db2html $(doc).xml

clean:
	rm -r $(doc) $(doc).junk
