# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python
# The observed PIN

def get_pins(observed):
    adjacent = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9', '0'],
        '9': ['9', '6', '8']
    }

    from itertools import product  


    combinations = [adjacent[digit] for digit in observed]


    possible_pins = [''.join(pin) for pin in product(*combinations)]

    return possible_pins