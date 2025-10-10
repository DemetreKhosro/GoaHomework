'''https://www.codewars.com/kata/555eded1ad94b00403000071/train/python'''
# Sum of the first nth term of Series

def series_sum(n):
    total = 0.0
    current_num = 1
    for i in range(n):
        total += 1 / current_num
        current_num += 3
    return f"{total:.2f}"