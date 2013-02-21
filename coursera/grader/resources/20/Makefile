# RESOURCE_HOME := The directory with grading resources (scripts, answers, etc.)
override RESOURCE_HOME:=$(shell realpath $(RESOURCE_HOME))
res_base = '../../../resources'
tweets = "$(res_base)/lib/tweets.txt"

compile:
	python src/top_ten.py $(tweets) > out/top_ten.txt

run:
	python $(RESOURCE_HOME)/top_ten_grader.py $(tweets) out/top_ten.txt > out/tests.log
