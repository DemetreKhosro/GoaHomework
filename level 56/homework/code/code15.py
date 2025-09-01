'''https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python'''
# Detecet Pangram

def is_pangram(st):
    st = st.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in st:
            return False
    return True