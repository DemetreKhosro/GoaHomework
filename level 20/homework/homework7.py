sentence = input("Enter a sentence: ")
vowel_counter = 0
consonant_counter = 0

for char in sentence:
    if char in "aeiou":
        vowel_counter += 1
    elif char not in "aeiou":
        consonant_counter += 1

print("Number of vowels in the sentence is", vowel_counter)
print("Number of consonants in the sentence is", consonant_counter)