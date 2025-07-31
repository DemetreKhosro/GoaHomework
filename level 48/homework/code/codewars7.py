'''https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python'''
# Area or Perimeter

def area_or_perimeter(l , w):
    if l > w or w > l:
        return (l + w) * 2
    else:
        return l * w