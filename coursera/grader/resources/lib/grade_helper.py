import sys

def fail(feedback):
    print '0;' + feedback 
    sys.exit()    

def success():
    print '1;Good Job!'

def parse_str_float_line(line):
    parts = line.split()
    if len(parts) != 2:
        fail('Formatting error: ' + line)

    try:
       float(parts[1]) 
    except ValueError:
        fail('value is not parseable as float: ' + line)
        
    return parts[0].decode('utf-8'), float(parts[1])
    
def parse_str_float_lines(in_file):
    lines = in_file.readlines()
    parsed_pairs = map(parse_str_float_line, lines)
    return dict(parsed_pairs)

def check_terms(student, solution):
    for term in solution:
        if term not in student:
            fail(term + ' has no computed value')

def parse_state(state_file):
    state = state_file.readlines()
    if len(state) != 1:
        fail('Input contains multiple lines')

    state_code = state[0].strip()

    if len(state_code) != 2:
        fail(state_code + ' is not a 2 character state abbreviation')

    return state_code

def parse_top_ten_line(line):
    parts = line.split()
    if len(parts) != 2:
        fail('Formatting error: ' + line)

    try:
        int(parts[1])
    except ValueError:
        fail('Value is not an integer: ' + line)

    return parts[0], int(parts[1])

def parse_top_ten_file(top_file):
    lines = top_file.readlines()
    if len(lines) != 10:
        fail('There are not exactly ten values in your solution.')
    parsed_pairs = map(parse_top_ten_line, lines)
    top_ten = dict(parsed_pairs)
    return top_ten
