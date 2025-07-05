person = {
    'name': 'Zion',
    'surname': 'Williamson',
    'height': '198cm',
    'team': 'New Orleans Pelicans'
}

print(person.items())

# გამოიტანს ყველა key/value წყვილს ჩვეულებრივ სტრინგებად და არა ლექსიკონად
for key, value in person.items():
    print(key, value)