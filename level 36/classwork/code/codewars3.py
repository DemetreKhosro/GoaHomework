'''https://www.codewars.com/kata/65128732b5aff40032a3d8f0/train/python'''
# Neutralisation

def neutralise(s1, s2):
    result = ''
    for num in range(len(s1)):
        if s1[num] == s2[num]:
            result += s1[num]
        else:
            result += '0'
    return result