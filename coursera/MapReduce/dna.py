import sys
import json
import MapReduce

def mapper(mr, dataline):
    pair = json.loads(dataline)
    seq_id = pair[0]
    seq = pair[1]
    trim_seq = seq[-10:]
    mr.emit_intermediate(trim_seq, seq_id)

def reducer(mr, trim_seq, seq_ids):
    mr.emit(trim_seq)

def main():
    dna = open(sys.argv[1])
    MapReduce.execute(dna, mapper, reducer)

if __name__ == '__main__':
    main()
