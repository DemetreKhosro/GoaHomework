num = int(input("Enter a number: "))
sum = 0

while num > 0:
    sum += num
    num = int(input("Enter a number: "))

if num < 0:
    print("Number is correct!")

print(f"The sum of the positive numbers you entered is", sum, "!")