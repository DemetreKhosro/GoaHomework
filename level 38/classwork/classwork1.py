'''1) თითოეულ ფუნქციასა და მეთოდზე შეასრულეთ 2 მაგალითი, 1 ცვლადის გამოყენებით 1 პირდაპირ მნიშვნელობის ჩასმით

ფუნქციები:
.sort()
.isnumeric()
sorted()
min()
max()'''


cars = ['BMW', 'Mercedes', 'Audi', 'Lexus', 'Suzuki', 'Honda']
numbers = [6, 3, 9, 10, 4, 11]
random = [1, 'car', 12, False, True, 'Hyundai']
words = ['apple', 'banana', 'computer', 'phone', 'laptop']
word = 'extraperpendicular'
word2 = '1234'

print(sorted(cars))
print(sorted(6, 4, 3, 11, 34))

print(min(numbers))
print(min(1, 2, 3, 4, 5))
print(max(1, 3, 7, 23, 234))
print(max(numbers))

print(word.isnumeric())
print(word2.isnumeric())

print(cars.sort())
print(words.sort())