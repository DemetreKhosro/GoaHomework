fruits = ["apple", "banana", "orange", "pineapple", "watermelon"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
colors = ['blue', 'red', 'yellow', 'orange', 'green']

# გვეუბნება მითითებული არგუმენტის ინდექსს სიაში
print(fruits.index("apple")) # 0
print(numbers.index(4)) # 3
print(colors.index("yellow")) # 2

# ითვლის თუ რამდენჯერ გვხვდება მოცემული არგუმენტი სიაში
print(fruits.count("banana")) # 1
print(numbers.count(9)) # 1
print(colors.count("yellow")) # 1

# ალაგებს სიას ზრდის/ანბანის მიხედვით, ანახლებს მის მნიშვნელობას
print(fruits.sort()) # None
print(numbers.sort()) # None
print(colors.sort()) # None

# ალაგებს სიას და არ ცვლის თავდაპირველ მნიშვნელობას
print(sorted(fruits)) # ['apple', 'banana', 'orange', 'pineapple', 'watermelon']
print(sorted(numbers)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sorted(colors)) # ['blue', 'green', 'orange', 'red', 'yellow']

# აბრუნებს სიაში ყველაზე პატარა ელემენტს
print(min(fruits)) # apple
print(min(numbers)) # 1
print(min(colors)) # blue

# აბრუნებს სიაში ყველაზე დიდ ელემენტს
print(max(fruits)) # watermelon
print(max(numbers)) # 9
print(max(colors)) # yellow