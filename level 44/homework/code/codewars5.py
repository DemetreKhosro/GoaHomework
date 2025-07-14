'''https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python'''
# Convert number to reversed array of digits

def digitize(n):
    result = []
    for digit in str(n):
        result.insert(0, int(digit))
    return result