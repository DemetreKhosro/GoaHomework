'''https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python'''
# Number of People in the Bus

def number(bus_stops):
    return sum(on - off for on, off in bus_stops)