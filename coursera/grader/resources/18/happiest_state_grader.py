import json
import sys

sys.path.append('../../../resources/lib/')
import parse_afinn
import grade_helper

sys.path.append('../../../resources/16/')
import sent_grader

def parse_tweets(tweet_file):
    decoder = json.JSONDecoder()
    messages = map(decoder.decode, tweet_file)
    return filter(lambda x : u'id_str' in x, messages)

def is_in_us(tweet):
    place = tweet[u'place']
    return place[u'country_code'] == u'US'

def has_state(tweet):
    place = tweet[u'place']
    full_name = place[u'full_name']
    state = full_name.split().pop()
    return len(state) == 2 and state != u'US'

def assoc_states_with_tweets(tweet):
    place = tweet[u'place']
    full_name = place[u'full_name']
    state = full_name.split().pop()
    return (state, tweet)

def create_state_tweet_dict(assoc_tuples):
    assoc = {}
    for state, tweet in assoc_tuples:
        if state not in assoc:
            assoc[state] = []
        assoc[state].append(tweet)
    return assoc

def score_tweet(tweet, computed_sentiments):
    text = tweet[u'text']
    parts = text.split()
    scored_parts = map(lambda x: computed_sentiments[x], parts)
    return sum(scored_parts)

def score_tweets(tweets, computed_sentiments):
    sum_score = 0

    for tweet in tweets:
        score = score_tweet(tweet, computed_sentiments)
        sum_score = sum_score + score

    return sum_score
    
def create_state_score_dict(state_tweet_dict, computed_sentiments):
    assoc = {}

    for state in state_tweet_dict:
        tweets = state_tweet_dict[state]
        score = score_tweets(tweets, computed_sentiments)
        assoc[state] = score

    return assoc
        
def compute_happiest(sentiments, tweets):
    placed_tweets = filter(lambda x : x[u'place'] is not None, tweets)
    us_tweets = list(filter(is_in_us, placed_tweets))
    state_tweets = filter(has_state, us_tweets)

    state_tweet_tuples = map(assoc_states_with_tweets, state_tweets)
    state_tweet_dict = create_state_tweet_dict(state_tweet_tuples)
    state_score_dict = create_state_score_dict(state_tweet_dict, sentiments)

    happiest = max(state_score_dict.items(), key=lambda pair : pair[1])

    return happiest[0]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hap_file = open(sys.argv[3])
    pre_comp_sent = parse_afinn.parse_sentiment_file(sent_file)
    sentiments = sent_grader.get_term_sentiments(pre_comp_sent, tweet_file)
    stdn_hap_state = grade_helper.parse_state(hap_file)

    tweet_file.seek(0)
    soln_hap_state = compute_happiest(sentiments, parse_tweets(tweet_file))

    if stdn_hap_state.lower() != soln_hap_state.lower():
        grade_helper.fail('Student solution returns ' + stdn_hap_state + ' while grader solution returns ' + soln_hap_state)
    else:
        grade_helper.success()
    
if __name__ == '__main__':
    main()
