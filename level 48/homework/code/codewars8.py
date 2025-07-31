'''https://www.codewars.com/kata/56606694ec01347ce800001b/train/python'''
# Is this a triangle?

def is_triangle(a, b, c):
    if a + b <= c:
        return False
    elif b + c <= a:
        return False
    elif a + c <= b:
        return False
    elif a + b > c:
        return True
    elif b + c > a:
        return True
    elif a + c > b:
        return True