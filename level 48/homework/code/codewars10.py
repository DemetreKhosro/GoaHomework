'''https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python'''
# Ones and Zeros

def binary_array_to_number(arr):
    total = 0
    for num in arr:
        total = total * 2
        total = total + num
    return total