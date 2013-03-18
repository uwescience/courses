import json
import sys

sys.path.append('../../../resources/lib/')

import grade_helper

def decode_json(stream_data):
    decoder = json.JSONDecoder()
    messages = map(decoder.decode, stream_data)
    return messages
    
def get_tweets(stream_data):
    messages_json = decode_json(stream_data)
    tweets = filter(lambda x : u'id_str' in x, messages_json)
    return tweets

def generate_tag_counts(tag_list):
    counts = {}

    for tag in tag_list:
        if tag not in counts:
            counts[tag] = 0
        counts[tag] = counts[tag] + 1

    return counts

def get_top_ten(tweets):
    entities = map(lambda x : x[u'entities'], tweets)
    hash_tag_lists = map(lambda x : x[u'hashtags'], entities)
    
    hash_tags = []
    for tag_list in hash_tag_lists:
        hash_tags = hash_tags + tag_list
    
    text_tag_list = map(lambda x : x[u'text'], hash_tags)

    counts = generate_tag_counts(text_tag_list)

    reverse_sorted_counts = sorted(counts.items(), key=lambda x : x[1], reverse=True)
    return dict(reverse_sorted_counts[:10])

def grade(stdn_ten, soln_ten):
    sort_stdn = sorted(stdn_ten.items(), key=lambda x : x[1], reverse=True) 
    sort_soln = sorted(soln_ten.items(), key=lambda x : x[1], reverse=True)
    for i in range(len(sort_soln)):
        stdn_val = sort_stdn[i][1]
        soln_val = sort_soln[i][1]
        if stdn_val != soln_val:
            grade_helper.fail('Expected a count of ' + str(soln_val) + ' at rank ' + str(i) + ', got ' + str(stdn_val))

    grade_helper.success()
        
def main():
    tweet_file = open(sys.argv[1])
    top_file = open(sys.argv[2])
    stdn_ten = grade_helper.parse_top_ten_file(top_file)

    tweets = get_tweets(tweet_file)
    soln_ten = get_top_ten(tweets)
    grade(stdn_ten, soln_ten)

if __name__ == '__main__':
    main()
