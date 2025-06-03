def vowel(string):
    vowel_counter = 0
    vowels = 'aeiouAEIOU'
    for char in string:
        if char in vowels:
            vowel_counter += 1
    return vowel_counter

print(vowel('Demetre'))