# RESOURCE_HOME := The directory with grading resources (scripts, answers, etc.)
override RESOURCE_HOME:=$(shell realpath $(RESOURCE_HOME))
lib = "../../../resources/lib"
db = "bin/reuters.db"

compile:
	cp $(lib)/reuters.db $(db)
	cp $(RESOURCE_HOME)/insert.txt bin/
	cp $(RESOURCE_HOME)/tf-idf_soln.txt bin/
	python2.7 src/tf-idf.py $(db) > bin/stdn.txt

run:
	sqlite3 $(db) < bin/insert.txt
	python2.7 $(RESOURCE_HOME)/tfidf_grader.py $(db) > out/tests.log
	rm $(db)
