import MapReduce
import json
import sys

#Dataline contains a json formatted key value pair associating a book to 
#a list of words
def mapper(mr, dataline):
    pairs = json.loads(dataline, encoding='latin-1')
    for book in pairs:
        for word in pairs[book]:
            mr.emit_intermediate(word, book)

def reducer(mr, word, books):
    mr.emit({word : list(set(books))})

def main():
    MapReduce.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()
