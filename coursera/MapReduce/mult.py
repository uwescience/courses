import sys
import json
import MapReduce

i_range = 10
j_range = 10

# record = (matrix, i, j, value)
def mapper(mr, dataline):
    global i_range
    global j_range

    record = json.loads(dataline)
    if record[0] == 'a':
        i = record[1]
        for j in range(j_range + 1):
            mr.emit_intermediate((i, j), record)
    elif record[0] == 'b':
        j = record[2]
        for i in range(i_range + 1):
            mr.emit_intermediate((i, j), record)
    else:
        raise Exception

# key should be the target bucket, values should be a list of records
def reducer(mr, key, values):
    values = list(values)
    a_rows = filter(lambda x : x[0] == 'a', values)
    b_rows = filter(lambda x : x[0] == 'b', values)

    result = 0
    for a in a_rows:
        for b in b_rows:
            if a[2] == b[1]:
                result = result + a[3] * b[3]

    mr.emit((key[0], key[1], result))

def main():
    records_file = open(sys.argv[1])
    MapReduce.execute(records_file, mapper, reducer)

if __name__ == '__main__':
    main()
