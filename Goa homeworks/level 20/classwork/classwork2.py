"""2) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ თუ ეს რიცხვი დადებითია დაბეჭდეთ ეს და კიდევ შეამოწმეთ ლუწია თუ კენტი, ხოლო თუ არაა დადებითი მხოლოდ დაბეჭდეთ რომ უარყოფითია"""
number = int(input("Enter a number: "))
if number > 0:
    print("Number is positive!")
if number % 2 == 0:
    print("Number is even!")

if number < 0:
    print("Number is negative!")
if number % 2 == 1:
    print("Number is odd")
    