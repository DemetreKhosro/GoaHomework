"""3) შექმენით სია რომელშიც ჩამოწერეთ სპორტის სახეობებს (მინიმუმ 10 სახეობა), აქედან slicing-ის გამოყენებით ამოჭერით და დაბეჭდეთ:
1-5
3-8
-2-0
4-0
შემობრუნებული სია"""

sports = ["Football", "Basketball", "Handball", "Golf", "Chess", "Futsal", "Tennis", "Water Polo", "Cricket", "Volleyball"]

print(sports[1:5])
print(sports[3:8])
print(sports[-2:0])
print(sports[4:0])

print(sports[::-1])