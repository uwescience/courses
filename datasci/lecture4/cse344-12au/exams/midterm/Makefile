REPORT=midterm
SRCS=$(wildcard *.tex)
LATEX=pdflatex "\def\includedsol{${SOL}} \input{${REPORT}}"
LATEX_SOL=${LATEX}

all: $(REPORT).pdf

$(REPORT).pdf: $(SRCS) 
	make makesol SOL=solution
	make makesol SOL=whitespace

makesol:
	$(LATEX_SOL)
	$(LATEX_SOL)
	$(LATEX_SOL)
	cp $(REPORT).pdf $(REPORT)-$(SOL).pdf


clean:
	rm -f *.dvi *.aux *.log *.blg *.bbl $(REPORT).ps $(REPORT).pdf
	make cleansol SOL=solution
	make cleansol SOL=whitespace

cleansol:
	rm -f $(REPORT)-$(SOL).ps $(REPORT)-$(SOL).pdf
