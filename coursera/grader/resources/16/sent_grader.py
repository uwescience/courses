import json
import sys

sys.path.append('../lib/')

import parse_afinn
import grade_helper

def is_tweet_positive(sentiments, tweet):
    parts = tweet.split()
    scored_parts = filter(lambda x : x in sentiments, parts)
    positive_parts = filter(lambda x : sentiments[x] > 0, scored_parts)
    return any(positive_parts)

def get_positive_dict(sentiments, tweets):
    dict_pairs = map(lambda x: (x, is_tweet_positive(sentiments, x)), tweets)
    return dict(dict_pairs)

def is_tweet_negative(sentiments, tweet):
    parts = tweet.split()
    scored_parts = filter(lambda x : x in sentiments, parts)
    negative_parts = filter(lambda x : sentiments[x] < 0, scored_parts)
    return any(negative_parts)

def get_negative_dict(sentiments, tweets):
    dict_pairs = map(lambda x: (x, is_tweet_negative(sentiments, x)), tweets)
    return dict(dict_pairs)

def get_term_tweet_dict(tweet):
    result = dict()
    parts = tweet.split()
    for part in parts:
        result.setdefault(part, [])
        result[part].append(tweet)

    return result

#Computes the sentiment for a list of tweets
def compute_sentiment(positive_tweet_dict, negative_tweet_dict,
        tweets):

    positive_tweets = list(filter(lambda tweet : positive_tweet_dict[tweet], tweets))
    negative_tweets = list(filter(lambda tweet : negative_tweet_dict[tweet], tweets))

    positive_tweet_count = len(positive_tweets)
    negative_tweet_count = len(negative_tweets) 
    if negative_tweet_count == 0:
        negative_tweet_count = 1
    
    sentiment = (1.0 * positive_tweet_count) / negative_tweet_count

    return sentiment

def parse_tweets(tweet_file):
    decoder = json.JSONDecoder()
    messages = map(decoder.decode, tweet_file)
    return filter(lambda x : u'id_str' in x, messages)

def get_term_sentiments(sentiments, tweet_file):
    tweets_json = parse_tweets(tweet_file)
    tweets_text = map(lambda x: x[u'text'], tweets_json)

    term_tweet_dict = {}
    term_dicts = map(get_term_tweet_dict, tweets_text)
    for i_dict in term_dicts:
        for term in i_dict:
            term_tweet_dict.setdefault(term, [])
            term_tweet_dict[term].extend(i_dict[term])

    negative_tweet_dict = get_negative_dict(sentiments, tweets_text)
    positive_tweet_dict = get_positive_dict(sentiments, tweets_text)
    
    computed_sentiments = {}
    for term in term_tweet_dict:
        tweets_for_term = term_tweet_dict[term]
        computed_sentiments[term] = compute_sentiment(positive_tweet_dict,
            negative_tweet_dict, tweets_for_term)

    return computed_sentiments

def grade(student, solution):
    sorted_solution = sorted(solution.items(), key=lambda x : x[1])
    soln_min_term = sorted_solution[0][0]
    soln_max_term = sorted_solution[len(sorted_solution) - 1][0]
    mid_sent = 1.0 * (solution[soln_min_term] + solution[soln_max_term]) / 2
    sorted_by_dist_from_mid = sorted(solution.items(), key=lambda x : abs(x[1] - mid_sent))
    soln_mid_term = sorted_by_dist_from_mid[0][0]
    student_max_sent = student[soln_max_term]
    student_mid_sent = student[soln_mid_term]
    student_min_sent = student[soln_min_term]

    if not (student_max_sent >= student_mid_sent):
        grade_helper.fail(soln_mid_term + '(' + str(student_mid_sent) + ') has a greater sentiment score than ' + soln_max_term + '(' + str(student_max_sent) + ')')

    if not (student_mid_sent >= student_min_sent):
        grade_helper.fail(soln_min_term + '(' + str(student_min_sent) + ') has a greater sentiment score than ' + soln_mid_term + '(' + str(student_mid_sent) + ')')

    grade_helper.success()
    
def main():
    pre_sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    student_sent_file = open(sys.argv[3])

    pre_sent = parse_afinn.parse_sentiment_file(pre_sent_file)
    solution_sentiments = get_term_sentiments(pre_sent, tweet_file)
    student_sentiments = grade_helper.parse_str_float_lines(student_sent_file)

    grade_helper.check_terms(student_sentiments, solution_sentiments)
    grade(student_sentiments, solution_sentiments)
    
if __name__ == '__main__':
    main()
