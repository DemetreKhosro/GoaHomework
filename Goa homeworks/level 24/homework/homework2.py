user_word = input("Enter a word: ")
palindrome = user_word[::-1]

if user_word == palindrome:
    print("Your word is a palindrome!")
else:
    print("Your word is normal!")