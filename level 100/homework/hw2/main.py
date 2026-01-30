while True:
  user_input = input("Enter 4 words or more: ")
  words_list = user_input.split()
  
  if len(words_list) >= 4:
    break
  
  print("Input must be 4 words or more")

file = open("words.txt", "w")
file.write(user_input)
file.close()

file = open("words.txt", "r")
content = file.read()
file.close()

consonants_list = "bcdfghjklmnpqrstvwxyz"
consonant_count = 0
for char in content.lower():
  if char in consonants_list:
    consonant_count = consonant_count + 1

words = content.split()
shortest_word = words[0]
for word in words:
  if len(word) < len(shortest_word):
    shortest_word = word

swapped_text = ""
for char in content:
  if char.isupper():
    swapped_text = swapped_text + char.lower()
  elif char.islower():
    swapped_text = swapped_text + char.upper()
  else:
    swapped_text = swapped_text + char

out_file = open("processed.txt", "w")
out_file.write(swapped_text)
out_file.close()

print("Word count:", len(words))
print("Consonants:", consonant_count)
print("Shortest word:", shortest_word)