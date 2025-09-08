'''https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python'''
# Find the middle element

def gimme(input_array):
    a, b, c = input_array
    if (b <= a <= c) or (c <= a <= b):
        return 0
    elif (a <= b <= c) or (c <= b <= a):
        return 1
    else:
        return 2