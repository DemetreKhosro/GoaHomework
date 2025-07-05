'''2) კომენტარებით რა არის dictionary, შემდეგ შექმენით 1 dictionary სახელად person რომელშიც გასაღებები იქნება: name, hobby, height, weight. გამოიყენეთ მეთოდები:'''
'''
clear()
copy()
get()
items()
keys()
values()
pop()
popitem()
update
'''
# Dictionary არის მონაცემთა ტიპი რომელიც მონაცემებს ინახავს key/value სახით

person = {
    'name': 'Timmy',
    'hobby': 'Football',
    'height': '162cm',
    'weight': '53kg'
}


print(person.copy())

print(person.get('name'))

print(person.items())

print(person.keys())

print(person.values())

print(person.pop('weight'))

print(person.popitem())

print(person.update({'hobby': 'Basketball'}))

print(person.clear())