'''https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python'''
# Vowel Count

def get_count(sentence):
    vowels = "aeiou"
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count +=1
    return vowel_count