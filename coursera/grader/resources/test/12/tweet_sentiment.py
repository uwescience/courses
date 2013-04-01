import json
import sys

def decode_json(stream_data):
    decoder = json.JSONDecoder()
    messages = map(decoder.decode, stream_data)
    return messages

def process_sentiment(sentiment):
    split_sentiment = sentiment.split()
    score = split_sentiment.pop()
    text = ' '.join(split_sentiment)
    return int(score), text

def map_sentiments(afin):
    sentiments = {}
    sentiment_count = 0

    for sentiment in afin: 
        score, text = process_sentiment(sentiment)
        sentiments[text] = score
        sentiment_count = sentiment_count + 1
    
    return sentiments

def parse_tweets(stream_data):
    messages_json = decode_json(stream_data)
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
        
def main():
    base_sentiments = map_sentiments(open(sys.argv[1]))
    tweets = parse_tweets(open(sys.argv[2]))
    for tweet in tweets:
        print compute_tweet_sentiment(base_sentiments, tweet)

if __name__ == '__main__':
    main()
