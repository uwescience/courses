def process_sentiment(sentiment):
    parts = sentiment.split()
    score = parts.pop()
    phrase = ' '.join(parts)
    return phrase, int(score)

def parse_sentiment_file(sent_file):
    sentiment_pairs = map(process_sentiment, sent_file)
    return dict(sentiment_pairs)
