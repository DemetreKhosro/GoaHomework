'''https://www.codewars.com/kata/54edbc7200b811e956000556/train/python'''
# Counting sheep...

def count_sheeps(sheep):
    sheep_counter = 0
    for sheep in sheep:
        if sheep == True:
            sheep_counter += 1
    return sheep_counter