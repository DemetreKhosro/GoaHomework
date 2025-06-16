'''https://www.codewars.com/kata/57aa218e72292d98d500240f/train/python'''
# Heron's formula

import math

def heron(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area