num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive!")
elif num < 0:
    print("Number is negative!")
else:
    print("Number is neutral!")

if num > 0 and num % 2 == 0:
    print("Number is positive and even!")
else:
    print("Number is negative and odd!")