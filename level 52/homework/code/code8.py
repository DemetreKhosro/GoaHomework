'''https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python'''
# Remove the minimum

def remove_smallest(numbers):
    if not numbers:
        return []
    min_num = min(numbers)
    index = numbers.index(min_num)
    return numbers[:index] + numbers[index+1:]