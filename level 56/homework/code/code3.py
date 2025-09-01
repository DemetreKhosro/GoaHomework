'''https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python'''
# Sum without highest and lowest number

def sum_array(arr):
    if not arr or len(arr) < 3:
        return 0
    sorted_arr = sorted(arr)
    return sum(sorted_arr[1:-1])