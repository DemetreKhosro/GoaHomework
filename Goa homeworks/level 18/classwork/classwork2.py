"""2) მოხმარებელს შემოატანინეთ თავისი გამოცდის ქულა, შემდეგ პირობითი განხცადების საშვალებით შეამოწმეთ ეს ქულა მეტია თუ 50-ზე, თუ მეტია დაუბეჭდეთ რომ გამოცდა ჩააბარა"""
score = int(input("Enter your score: "))

if score == 100:
    print("CONGRATULATIONS!!!")
if score > 50:
    print("You passed the exam!")
else:
    print("You failed!")