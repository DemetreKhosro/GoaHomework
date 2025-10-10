'''https://www.codewars.com/kata/54e6533c92449cc251001667/train/python'''
# Unique In Order

def unique_in_order(sequence):
    if not sequence:
        return []
    
    result = [sequence[0]]
    for item in sequence[1:]:
        if item != result[-1]:
            result.append(item)
    return result