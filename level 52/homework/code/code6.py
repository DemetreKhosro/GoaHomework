'''https://www.codewars.com/kata/57a4d500e298a7952100035d/train/python'''
# Hex to Decimal

def hex_to_dec(s):

    hex_digit_values = {
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15
    }
    
    hex_digits = "abcdef"
    total = 0
    length = len(s)
    s = s[::-1]
    for index in range(length):
        digit = s[index]
        if digit in hex_digits:
            value = hex_digit_values[digit]
            total += value * (16 ** index)
        else:
            total += int(digit) * (16 ** index)
    return total