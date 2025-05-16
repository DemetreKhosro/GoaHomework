"""2) მომხმარებელს შემოატანინეთ 2 რიცხვი, შემდეგ კი პირველი რიცხვიდან მეორეს ჩათვლით არსებული ყველა რიცხვი დაბეჭდეთ"""
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

for number in range(num1, num2+1):
    print(number)