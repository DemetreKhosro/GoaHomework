'''1) თითოეულ მეთოდზე: len, append, insert, pop, remove მეთოდებზე გააკეთეთ 3-3 მაგალითი. len ფუნქციაზე მოიყვანეთ string-ის მაგალითიც'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
name = 'Demetre'

print(len(numbers))
print(len(numbers))

numbers.append(10)
numbers.append(11)
numbers.append(12)

numbers.insert(2, 99)
numbers.insert(4, 58)
numbers.insert(6, 78)

numbers.remove(1)
numbers.remove(2)
numbers.remove(3)

numbers.pop(0)
numbers.pop(9)
numbers.pop(8)

print(numbers)