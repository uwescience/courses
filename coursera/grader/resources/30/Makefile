# RESOURCE_HOME := The directory with grading resources (scripts, answers, etc.)
override RESOURCE_HOME:=$(shell realpath $(RESOURCE_HOME))
lib = "../../../resources/lib"
db = "bin/reuters.db"
mode = ".mode csv\n"
stdn = ".import bin/stdn.txt stdn\n"
soln = ".import $(RESOURCE_HOME)/tf-idf_soln.txt tfidf"

compile:
	cp $(lib)/reuters.db $(db)
	python2.7 src/tf-idf.py $(db) > bin/stdn.txt

run:
	echo $(mode)$(stdn)$(soln) | sqlite3 $(db)
	python2.7 $(RESOURCE_HOME)/tfidf_grader.py $(db) > out/tests.log
	rm $(db)
