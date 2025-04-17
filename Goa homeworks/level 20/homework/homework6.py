sum = 0
number = 0
counter = 0

while number != -1:
    number = int(input("Enter a number: "))

    if number != -1:    
        sum += number
        counter += 1

    if counter > 0:
        average = sum / counter
print("The average of the numbers you entered is", average)