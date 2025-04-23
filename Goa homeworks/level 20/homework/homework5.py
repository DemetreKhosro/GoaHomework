pin = 1234
attempts = 3

while attempts > 0:
    attempt = int(input("Enter your pin: "))
    if attempt == pin:
        print("Access granted!")
    else:
        attempts -= 1
        print("Access denied!")