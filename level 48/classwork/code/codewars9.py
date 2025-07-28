'''https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python'''
# Regex validate PIN code

def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        digit = '0123456789'
        for char in pin:
            if char not in digit:
                return False
        return True
    return False