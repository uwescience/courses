import sys
import MapReduce
from Bio import SeqIO

def data(file_handle):
    results = {}
    base_dict = SeqIO.to_dict(SeqIO.parse(file_handle, 'fasta'))

    for key in base_dict:
        results[key] = base_dict[key].seq

    return results

def mapper(mr, seq_id, seq):
    trim_seq = seq[-10:]
    mr.emit_intermediate(trim_seq, seq_id)

def reducer(mr, trim_seq, seq_ids):
    mr.emit(trim_seq.tostring())

def main():
    dna_file_handle = open(sys.argv[1])
    MapReduce.execute(data(dna_file_handle), mapper, reducer)

if __name__ == '__main__':
    main()
