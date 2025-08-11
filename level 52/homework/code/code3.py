'''https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python'''
# Count of positives / sum of negatives

def count_positives_sum_negatives(arr):
    positive_counter = 0
    negative_counter = 0
    if not arr:
        return []
    for num in arr:
        if num > 0:
            positive_counter += 1
        elif num < 0:
            negative_counter += num
    return [positive_counter, negative_counter]