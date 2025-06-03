def even(n):
    even_numbers = []
    for num in range(1, n + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

print(even(4))