'''https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python'''
# Exes and Ohs

def xo(s):
    s = s.lower()
    x = s.count('x')
    o = s.count('o')
    return x == o