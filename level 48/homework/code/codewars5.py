'''https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python'''
# If you can't sleep, just count sheep!!

def count_sheep(n):
    return ''.join(f"{num} sheep..." for num in range(1, n + 1))