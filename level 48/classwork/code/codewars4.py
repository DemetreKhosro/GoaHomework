'''https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python'''
# Mumbling

def accum(st):
    res = ''
    for index, char in enumerate(st):
        string = (index + 1) * char
        res += string.capitalize() + '-'
    return res[:-1]