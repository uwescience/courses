import sys
import json
import MapReduce


def mapper(mr, dataline):
    friendship = json.loads(dataline)
    mr.emit_intermediate(friendship[0], friendship[1])

def reducer(mr, person, friends):
    friend_set = set(friends)
    mr.emit({person : len(friends)})

def main():
    friendships = open(sys.argv[1])
    MapReduce.execute(friendships, mapper, reducer)

if __name__ == '__main__':
    main()
