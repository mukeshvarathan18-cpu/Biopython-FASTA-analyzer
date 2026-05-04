#------------------------------
### BASICS OF BIOPYTHON
# ------------------------------

# Bio --> main Biopython package
# Seq --> Which represents the biological sequences

from Bio.Seq import Seq
dna = Seq("ATGTACGCGCGCAATCAT") # Seq() --> biological object
print(dna)
#----------------------------------
# Length calculation
#----------------------------------
# len() --> Explains the total length of dna

print(len(dna)) # Output --> total length of DNA

#----------------------------------
# GC count 
#----------------------------------
# dna.count("G") --> Counts the total number of "G" in DNA sequence
# dna.count("C") --> Counts the total number of "C" in DNA sequence
# dna.count()/ len(dna) * 100 --> counts in percentage

gc = (dna.count("G") + dna.count("C")) / len(dna) * 100
print(gc) # Output --> GC count in percentage

#-------------------------------------
# Reverse complement
#-------------------------------------
# dna.reverse_complement() --> complement to given DNA sequence
# Example : A > T -- T > A -- G > C -- C > G --
rc = dna.reverse_complement()
print(rc) # Output = Whole sequence complement occurs

#-------------------------------------
# Translation DNA --> PROTEIN
#-------------------------------------
# dna.translate() --> 3 nucleotides of sequence codes as protein
protein = dna.translate()
print(protein)

#-------------------------------------
# Reading the FASTA files
#-------------------------------------
# SeqIO --> Sequence input and output handler (Reading the biological data file formats)
# SeqIO reads FASTA files
from Bio import SeqIO
for record in SeqIO.parse("C:/Users/HP/Downloads/fasta1.fasta", "fasta"):
    print(record.id)
    seq = record.seq

    # -------------------------------
    # length calculation
    # -------------------------------
    print(len(seq))

    # ------------------------------
    # GC Content Calculation
    # ------------------------------
    # seq.count("G") counts number of Guanine bases
    # seq.count("C") counts number of Cytosine bases
    # GC% = (G + C) / total length × 100
    gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    print(gc)
    
    
    # ------------------------------
    # Reverse Complement
    # ------------------------------
    # These represents the antiparllel DNA strands
    print(seq.reverse_complement())
    
    
    # ------------------------------
    # Translation (DNA → Protein)
    # ------------------------------
    # if the codon is not properly arranged means then biopython will shows warning, so that we need to justify the length of DNA properly then only we'll get the proper translation process
    # here :len(seq) - total length of DNA STRAND
    # While len(seq) % 3 divides the total sequneces which able to divisible by 3, the remaining nucleotides are removed
    # for example: if DNA total strand length is 19, it means it does translate properly, if i dividing it by 3 then i'll get 18 as my new length of the DNA strand now it's able to translate without any warning

    
    seq = seq[:len(seq) - len(seq) % 3]
    print(seq.translate())