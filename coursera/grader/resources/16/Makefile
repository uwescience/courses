# RESOURCE_HOME := The directory with grading resources (scripts, answers, etc.)
override RESOURCE_HOME:=$(shell realpath $(RESOURCE_HOME))
res_base = '../../../resources'
afinn = "$(res_base)/lib/AFINN-111.txt"
tweets = "$(res_base)/lib/tweets.txt"

compile:
	python src/sent.py $(afinn) $(tweets) > bin/sent.txt

run:
	python $(RESOURCE_HOME)/sent_grader.py $(afinn) $(tweets) bin/sent.txt > out/tests.log
