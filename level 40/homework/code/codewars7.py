'''https://www.codewars.com/kata/55b42574ff091733d900002f/train/python'''
# Friend or Foe?

def friend(x):
    friends = []
    for friend in x:
        if len(friend) == 4:
            friends.append(friend)
    return friends