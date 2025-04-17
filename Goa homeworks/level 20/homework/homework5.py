pin = 1234
attempts = 3
attempt = int(input("Enter your pin: "))
if attempt != pin:
    attempts -= 1
    print("Access denied!")
elif attempt == pin:
    print("Access granted!")