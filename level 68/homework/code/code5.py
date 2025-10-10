'''https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python'''
# Remove duplicate words

def remove_duplicate_words(s):
    words = set()
    result = []
    for word in s.split():
        if word not in words:
            words.add(word)
            result.append(word)
    return ' '.join(result)