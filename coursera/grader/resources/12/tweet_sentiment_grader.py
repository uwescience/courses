import json
import sys

sys.path.append('../../../resources/lib/')

import parse_afinn
import grade_helper

def parse_tweets(stream_data):
    decoder = json.JSONDecoder()
    messages_json = map(decoder.decode, stream_data)
    tweets = filter(lambda x : u'id_str' in x, messages_json)
    return map(lambda x : x[u'text'], tweets)
    
#in: tweets to booleans maps, and list of tweets
def compute_tweet_sentiment(sentiments, tweet):
    parts = tweet.split()
    scored_parts = filter(lambda x : x in sentiments, parts)
    scores = map(lambda x : sentiments[x], scored_parts)
    sentiment = 0
    for score in scores:
        sentiment = sentiment + score
    return sentiment

def parse(score_file):
    scores = []
    for score_line in score_file:
        try:
            score = float(score_line)
        except:
            grade_helper.fail('parsing error, line should be a number: ' + score_line)
        
        scores.append(score)
    return scores

def grade(soln, stdn):
    if len(soln) != len(stdn):
        grade_helper.fail('Expected ' + str(len(soln)) + ' scores')

    for i in range(len(soln)):
        soln_score = soln[i]
        stdn_score = stdn[i]
        if soln_score != stdn_score:
            grade_helper.fail('Expected ' + str(soln_score) + ' for tweet #' + str(i) + ' got: ' + str(stdn_score))

    grade_helper.success()
        
def main():
    base_sentiments = parse_afinn.parse_sentiment_file(open(sys.argv[1]))
    tweets = parse_tweets(open(sys.argv[2]))
    student_scores = parse(open(sys.argv[3]))

    solution_scores = []

    for tweet in tweets:
        solution_scores.append(compute_tweet_sentiment(base_sentiments, tweet))

    grade(solution_scores, student_scores)

if __name__ == '__main__':
    main()
