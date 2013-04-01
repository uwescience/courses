# RESOURCE_HOME := The directory with grading resources (scripts, answers, etc.)
override RESOURCE_HOME:=$(shell realpath $(RESOURCE_HOME))

compile:

run:
	python output_parser.py src/output.txt > out/tests.log
