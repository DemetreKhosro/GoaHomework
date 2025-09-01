'''https://www.codewars.com/kata/526c7363236867513f0005ca/train/python'''
# Leap Years

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False