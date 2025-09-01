'''https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/python'''
# Array plus array

def array_plus_array(arr1,arr2):
    sum1 = 0
    sum2 = 0
    for num in arr1:
        sum1 += num
    for num in arr2:
        sum2 += num
    return sum1 + sum2