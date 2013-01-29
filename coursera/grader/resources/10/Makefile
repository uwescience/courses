# RESOURCE_HOME := The directory with grading resources (scripts, answers, etc.)
override RESOURCE_HOME:=$(shell realpath $(RESOURCE_HOME))

# Don't do anything
compile:

run:
	python $(RESOURCE_HOME)/grader.py > out/test.log
