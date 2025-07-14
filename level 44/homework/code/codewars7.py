'''https://www.codewars.com/kata/56747fd5cb988479af000028/train/python'''
# Get the Middle Character

def get_middle(s):
    length = len(s)
    middle_index = length // 2
    if length % 2 == 0:
        return s[middle_index - 1:middle_index + 1]
    else:
        return s[middle_index]