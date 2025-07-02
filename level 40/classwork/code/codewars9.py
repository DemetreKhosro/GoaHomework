'''https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python'''
# List Filtering

def filter_list(l):
    new_l = []
    for item in l:
        if type(item) == type(1):
            new_l.append(item)
    return new_l