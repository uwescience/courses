# RESOURCE_HOME := The directory with grading resources (scripts, answers, etc.)
override RESOURCE_HOME:=$(shell realpath $(RESOURCE_HOME))
lib = "../../../resources/lib"
db = "bin/matrix.db"

compile:
	cp $(lib)/matrix.db $(db)
	cp $(RESOURCE_HOME)/insert.txt bin/
	cp $(RESOURCE_HOME)/mult_soln.txt bin/
	sqlite3 -csv $(db) < src/mult.sql > bin/stdn.txt

run:
	sqlite3 $(db) < bin/insert.txt
	python2.7 $(RESOURCE_HOME)/mult_grader.py $(db) > out/tests.log
	
