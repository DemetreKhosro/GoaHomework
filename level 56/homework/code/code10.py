'''https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python'''
# Find the capitals

def capitals(word):
    result = []
    capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 0
    for char in word:
        if char in capital:
            result.append(i)
        i += 1
    return result