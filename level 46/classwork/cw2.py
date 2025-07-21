'''2) შექმენით რიცხვების სია, შემდეგ ყოველი რიცხვი რომელიც კენტია გაამრავლეთ ორზე და დაამატეთ new_list-ში, ჯერ გააკეთეთ ეს დავალება ჩვეულებრივად, შემდეგ კი list comperhensiosns გამოყენებით. ასევე გააკეთეთ კიდევ 2 მაგალითი თქვენით, პირველ მაგალითში აიღეთ მხოლოდ გამოსახულების დამატება list comperhensions-ში, მეორე მაგალითში კი აიღეთ მხოლოდ პირობა'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
new_list = []

for num in numbers:
    if num % 2 != 0:
        new_list.append(num)

new_list2 = [num * 2 for num in numbers if num % 2 != 0]

numbers1 = [1, 2, 3, 4, 5]
new_numbers1 = [num + 5 for num in numbers1]

new_numbers2 = [num * 2 for num in numbers]