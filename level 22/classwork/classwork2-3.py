"""2) შექმენით ცივი სასმელების სია აქედან ერთ-ერთი ელემენტი უნდა ეწეროს ცვლადის სახით, შემდეგ მომხმარებელს შემოტანინეთ 1 ცივი სასმელი რომელსაც დაამატებთ თქვენს მაცივარში. შემდეგ მომხარებელს უნდა შემოატანინოთ არჩევანი ამ სასმელებიდან და სიიდან ელემენტის წამოღების indexing method-ის საშვალებით გამოუტანეთ ეს სასმელი. შექმენით ცვლადი რომელშიც შეინახავთ თქვენს სახელს, გამოიტანეთ ამ სტრინგიდან თქვენთვის სასურველი 3 სიმბოლო"""

# homework 2

drink = "Fuse tea"
user_drink = input("Enter a drink to add to the vending machine: ")
cold_drinks = ["Fanta", "Coca-Cola", "Sprite", "Pepsi", user_drink, drink]

user_choice = int(input("Enter a number for a drink: "))
print(cold_drinks[user_choice])

# homework 3

name = "Demetre"
print(name[4])
print(name[5])
print(name[6])