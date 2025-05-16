even_counter = 0
odd_counter = 0
num = 0

while num >= 0:
    num = int(input("Enter a number: "))
    if num >= 0:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print("The number of even numbers you entered is:", even_counter)
print("The number of odd numbers you entered is:", odd_counter)