string = 'Georgia, Armenia, Azerbaijan, USA, UK, Ukraine, Moldova, Romania, Brazil, Australia, Papua-New Guinea'
word = input('Enter a country: ')
position = string.find(word)

if position != -1:
    print(position)
else:
    print('Word not found')