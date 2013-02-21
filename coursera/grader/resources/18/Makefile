# RESOURCE_HOME := The directory with grading resources (scripts, answers, etc.)
override RESOURCE_HOME:=$(shell realpath $(RESOURCE_HOME))
res_base = '../../../resources'
afinn = "$(res_base)/lib/AFINN-111.txt"
tweets = "$(res_base)/lib/tweets.txt"

compile:
	python src/hap.py $(afinn) $(tweets) > bin/hap.txt

run:
	python $(RESOURCE_HOME)/happiest_state_grader.py $(afinn) $(tweets) bin/hap.txt > out/tests.log
