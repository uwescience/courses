# RESOURCE_HOME := The directory with grading resources (scripts, answers, etc.)
override RESOURCE_HOME:=$(shell realpath $(RESOURCE_HOME))
lib = "../../../resources/lib"
db = "bin/matrix.db"
mode = ".mode csv\n"
stdn = ".import bin/stdn.txt stdn\n"
soln = ".import $(RESOURCE_HOME)/mult_soln.txt c"

compile:
	cp $(lib)/matrix.db $(db)
	sqlite3 -csv $(db) < src/mult.sql > bin/stdn.txt

run:
	echo $(mode)$(stdn)$(soln) | sqlite3 $(db)
	python2.7 $(RESOURCE_HOME)/mult_grader.py $(db) > out/tests.log
	
