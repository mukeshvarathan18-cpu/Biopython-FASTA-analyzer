# Biopython-FASTA-analyzer
Bioinformatics tool for analyzing DNA sequences from FASTA files using Biopython

# Description
This project is a basic bioinformatics tool developed using Biopython to analyze DNA sequences from FASTA files. It reads sequence data and performs multiple biological analyses such as GC content calculation, reverse complement generation, and DNA to protein translation.

# Features
•	Reads FASTA files using Biopython (SeqIO)
•	Calculates sequence length
•	Computes GC content (%)
•	Generates reverse complement of DNA
•	Translates DNA sequence into protein
•	Handles partial codons by trimming sequence length

# Methodology
•	FASTA files are parsed using SeqIO.parse(), which returns SeqRecord objects.
•	The DNA sequence is extracted as a Seq object for biological operations.
•	GC content is calculated using base counting.
•	Reverse complement is generated using base pairing rules.
•	Translation is performed by converting codons (triplets) into amino acids using the genetic code.
•	Sequences are trimmed to ensure length is divisible by 3 to avoid partial codon errors.

# Tools & Libraries
•	Python 3
•	Biopython

# How to Run
Python file.py
Enter the FASTA file path when prompted.
Input
A FASTA file containing DNA sequences.
Example:
>seq1
ATGTACGCTAATGCGGAAT

# Output
•	Sequence ID
•	Length of sequence
•	GC content (%)
•	Reverse complement
•	Protein sequence

# Key Learning Outcomes
•	Understanding biological sequence representation using Seq objects
•	Parsing biological data formats (FASTA)
•	Applying sequence-level bioinformatics analysis
•	Handling issues like partial codons during translation
