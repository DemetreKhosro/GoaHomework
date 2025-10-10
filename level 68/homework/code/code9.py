'''https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python'''
# Find the unique number

def find_uniq(arr):
    if arr[0] == arr[1] or arr[0] == arr[2]:
        common = arr[0]
    else:
        common = arr[1]
        
    for num in arr:
        if num != common:
            return num