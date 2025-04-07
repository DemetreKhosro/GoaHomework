attempts = 0
pin = "1234"
guess = " "
while guess != pin:
    guess = input("Enter the pin: ")
    attempts += 1
print("Correct!")
print("It took you " + str(attempts) + " " + "tries to log in to your account!")