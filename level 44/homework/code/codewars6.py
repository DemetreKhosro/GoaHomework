'''https://www.codewars.com/kata/555086d53eac039a2a000083/train/python'''
# Opposites Attract

def lovefunc( flower1, flower2 ):
    if (flower1 % 2 == 0 and flower2 % 2 == 1) or (flower1 % 2 == 1 and flower2 % 2 == 0):
        return True
    else:
        return False