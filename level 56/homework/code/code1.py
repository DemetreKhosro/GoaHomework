'''https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python'''
# Beginner - Reduce but Grow

def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result