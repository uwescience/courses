DOCUMENT=section10-similar-items
SOURCES=Realmakefile $(DOCUMENT).tex versions.sty

all: blank solution
blank: $(DOCUMENT)-blank.pdf
solution: $(DOCUMENT)-solution.pdf

$(DOCUMENT)-blank.pdf: $(SOURCES)
	make -f Realmakefile
	mv $(DOCUMENT).pdf $@

$(DOCUMENT)-solution.pdf: $(SOURCES)
	make -f Realmakefile SOL=
	mv $(DOCUMENT).pdf $@

clean: Realmakefile
	make -f Realmakefile clean
