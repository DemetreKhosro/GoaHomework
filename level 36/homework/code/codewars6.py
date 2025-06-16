'''https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1/train/python'''
# Indexed capitalization

def capitalize(s, ind):
    result = ''
    character = 0
    for char in s:
        if character in ind:
            result += char.upper()
        else:
            result += char
        character += 1
    return result