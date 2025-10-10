'''https://www.codewars.com/kata/556deca17c58da83c00002db/train/python'''
# Tribonacci Sequence

def tribonacci(signature, n):
    sequence = signature[:]
    for i in range(3, n):
        sequence.append(sequence[-3] + sequence[-2] + sequence[-1])
    return sequence[:n]