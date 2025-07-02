'''https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python'''
# Shortest Word

def find_short(s):
    s = s.split(' ')
    length = map(len, s)
    return min(length)