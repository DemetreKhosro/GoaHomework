'''https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python'''
# Split Strings

def solution(s):
    s = s + '_' * (len(s) % 2)
    return [s[i:i+2] for i in range(0, len(s), 2)]