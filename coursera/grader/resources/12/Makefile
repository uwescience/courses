# RESOURCE_HOME := The directory with grading resources (scripts, answers, etc.)
override RESOURCE_HOME:=$(shell realpath $(RESOURCE_HOME))
res_base = "../../../resources"
afinn = "$(res_base)/lib/AFINN-111.txt"
tweets = "$(res_base)/lib/tweets.txt"

compile:
	python2.7 src/tweet_sentiment.py $(afinn) $(tweets) > bin/scores.txt

run:
	python $(RESOURCE_HOME)/tweet_sentiment_grader.py $(afinn) $(tweets) bin/scores.txt > out/tests.log
