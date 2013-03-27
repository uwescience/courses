import json
import sys
sys.path.append('../../../resources/lib')
import grade_helper

def get_term_count_dict(tweet):
    result = dict()
    parts = tweet.split()
    for part in parts:
        result.setdefault(part, 0)
        result[part] = result[part] + 1

    return result

def generate_histogram(term_counts):
    hist = {}

    for term in term_counts:
        freq = 1.0 * term_counts[term] / len(term_counts)
        hist[term] = freq
        
    return hist

#Returns the term that has the frequency closest to the average of the
#maximum and minimum frequencies
def mid_freq_term(hist, min_term, max_term):
    ideal_mid_freq = 1.0 * (hist[max_term] - hist[min_term]) / 2
    return min(hist.items(), key=lambda x : abs(x[1] - ideal_mid_freq))[0]

def compute_soln_freq(stream_data):
    total_terms = 0

    decoder = json.JSONDecoder()
    messages = map(decoder.decode, stream_data)
    tweets = filter(lambda x : u'id_str' in x, messages)
    tweets = map(lambda x : x[u'text'], tweets)
    
    term_counts = {}
    term_count_dicts = map(get_term_count_dict, tweets)
    for term_dict in term_count_dicts:
        for term in term_dict:
            term_counts.setdefault(term, 0)
            term_counts[term] = term_counts[term] + term_dict[term]

    return generate_histogram(term_counts)

def grade(stdn, soln):
    soln_min_term = min(soln.items(), key=lambda x: x[1])[0]
    soln_max_term = max(soln.items(), key=lambda x: x[1])[0]
    soln_mid_term = mid_freq_term(soln, soln_min_term, soln_max_term)
    stdn_min_score = stdn[soln_min_term]
    stdn_mid_score = stdn[soln_mid_term]
    stdn_max_score = stdn[soln_max_term]

    if not (stdn_max_score >= stdn_mid_score):
        grade_helper.fail(soln_mid_term + '(' + str(stdn_mid_score) + ') has a greater frequency than ' + soln_max_term + '(' + str(stdn_max_score) + ')')

    if not (stdn_mid_score >= stdn_min_score):
        grade_helper.fail(soln_min_term + '(' + str(stdn_min_score) + ') has a greater frequency than ' + soln_mid_term + '(' + str(stdn_mid_score) + ')')

    grade_helper.success()

def main():
    tweet_file = open(sys.argv[1])
    stdn_freq_file = open(sys.argv[2])
    stdn_freq = grade_helper.parse_str_float_lines(stdn_freq_file)
    soln_freq = compute_soln_freq(tweet_file)
    grade_helper.check_terms(stdn_freq, soln_freq)
    grade(stdn_freq, soln_freq)

if __name__ == '__main__':
    main()
