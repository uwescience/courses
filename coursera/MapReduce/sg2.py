import sys
import MapReduce
import json

def mapper(mr, dataline):
    friendship = json.loads(dataline)
    mr.emit_intermediate(friendship[0], friendship[1])
    mr.emit_intermediate(friendship[1], friendship[0])

def reducer(mr, person, friend_list):
    counts = {}
    for friend in friend_list:
        counts.setdefault(friend, 0)
        counts[friend] = counts[friend] + 1

    nonsym = filter(lambda x : counts[x] == 1, counts.keys())

    for i in nonsym:
        mr.emit((person, i))

def main():
    persons = open(sys.argv[1])
    MapReduce.execute(persons, mapper, reducer)

if __name__ == '__main__':
    main()
