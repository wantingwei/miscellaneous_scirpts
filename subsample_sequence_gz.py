import sys
import gzip
from random import sample
from Bio import SeqIO

def detect_format(filename):
    if filename.endswith('.fasta') or filename.endswith('.fa'):
        return 'fasta'
    elif filename.endswith('.fastq') or filename.endswith('.fq'):
        return 'fastq'
    elif filename.endswith('.fasta.gz') or filename.endswith('.fa.gz'):
        return 'fasta'
    elif filename.endswith('.fastq.gz') or filename.endswith('.fq.gz'):
        return 'fastq'
    else:
        raise ValueError("Unsupported file format")

def open_file(filename):
    return gzip.open(filename, 'rt') if filename.endswith('.gz') else open(filename, 'r')

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 subsample_sequences.py <input_file> <num_seqs> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    num_seqs = int(sys.argv[2])
    output_file = sys.argv[3]

    seq_format = detect_format(input_file)

    with open_file(input_file) as handle:
        seqs = list(SeqIO.parse(handle, seq_format))

    if num_seqs > len(seqs):
        print(f"Requested {num_seqs} sequences, but only {len(seqs)} available.")
        sys.exit(1)

    subsample = sample(seqs, num_seqs)

    with open(output_file, 'w') as out_handle:
        SeqIO.write(subsample, out_handle, seq_format)

if __name__ == '__main__':
    main()

