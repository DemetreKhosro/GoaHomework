'''https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python'''
# Fake Binary

def fake_bin(x):
    result = ''
    for char in x:
        if int(char) < 5:
            result += '0'
        else:
            result += '1'
    return result
