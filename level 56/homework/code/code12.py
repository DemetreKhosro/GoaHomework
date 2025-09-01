'''https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python'''
# Find the words

def vowel_indices(word):
    vowels = 'aeiouyAEIOUY'
    result = []
    index = 1
    for char in word:
        if char in vowels:
            result.append(index)
        index += 1
    return result