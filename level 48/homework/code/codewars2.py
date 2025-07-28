'''https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python'''
# Calculate average

def find_average(numbers):
    # stops function if list is empty
    if not numbers:
        return 0
    # start of function if list not empty
    nums = 0
    sum = 0
    for num in numbers:
        nums += 1
        sum += num
    return sum / nums