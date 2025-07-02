'''https://www.codewars.com/kata/515e271a311df0350d00000f/train/python'''
# Square(n) Sum

def square_sum(numbers):
    result = 0
    for num in numbers:
        result += num ** 2
    return result