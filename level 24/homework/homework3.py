words = ['Georgia', 'Blue', 'Mercedes', 'Palindrome', 'Paranormal', 'Normal', 'Visual', 'Studio', 'Code']
reversed = words[::-1]
counter = 0

for words in reversed:
    counter += 1
    print(reversed[::2])

if counter % 2 == 0:
    print('Even number of words')
else:
    print('Odd number of words')