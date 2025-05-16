"""1) მოხმარებელს შემოატანინეთ რიცხვი, შემდეგ კი დაუბეჭდეთ ეს რიცხვი დადებითია, უარყოფითი თუ ნეიტურალი ანუ ნული. შემდეგ კომენტარებით ახსენით რა გასნხვავებაა if-სა და elif-ს შორის რატომ არ შეიძლება ზოგერ elif-ს ნაცვლად if-ის გამოყენება"""
number = int(input("Enter a number: "))
if number > 0:
    print("Number is positive!")
elif number < 0:
    print("Number is negative!")
else:
    print("Number is neutral!")

# elif - არის if  და else შეერთებული რომელიც გამოიყენება მაშინ როდესაც გვაქვს რამდენიმე პირობა