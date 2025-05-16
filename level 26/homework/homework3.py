fruit_list = ['Pear', 'Apple', 'Cherry', 'Strawberry', 'Banana', 'Pineapple', 'Kiwi', 'Avocado', 'Blueberry', 'Mango', 'Peach']
favorite_fruit = input('Enter your favorite fruit: ')
fruit_in_basket = False

for fruit in fruit_list:
    if favorite_fruit.lower() == fruit.lower():
        fruit_in_basket = True

if fruit_in_basket:
    print('Good Choice!')
else:
    print('Fruit not in basket!')