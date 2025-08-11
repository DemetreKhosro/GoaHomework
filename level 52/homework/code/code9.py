'''https://www.codewars.com/kata/57f609022f4d534f05000024/train/python'''
# Find the stray number

def stray(arr):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]