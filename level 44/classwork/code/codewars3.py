'''https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python'''
# Complementary DNA

def DNA_strand(dna):
    complement = ''
    for acid in dna:
        if acid == 'A':
            complement += 'T'
        elif acid == 'T':
            complement += 'A'
        elif acid == 'C':
            complement += 'G'
        elif acid == 'G':
            complement += 'C'
    return complement