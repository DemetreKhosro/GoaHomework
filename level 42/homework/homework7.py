animal = {
    'name': 'Cheetah',
    'speed': '75mph',
    'count': '~8000',
    'weight': '21-65kg'
}

animal_copy = animal.copy()

animal.clear()
animal_copy.clear()

# გამოიტანს ორივე ცარიელ სიას
print(animal)
print(animal_copy)