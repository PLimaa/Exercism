def to_rna(dna_strand):
    dna = "GCTA"
    rna = "CGAU"
    rna_strand = ""
    for nucleotide in dna_strand:
        if nucleotide.isalpha():
            rna_strand += rna[dna.index(nucleotide)]
        else:
            rna_strand += nucleotide
    return rna_strand  
