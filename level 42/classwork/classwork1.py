# 1) შექმენით რიცხვების set, ჩამოწერეთ მისი ყველა თვისება, შემდეგ დაამტეთ და წაშალეთ 2 ელემენტი: add და remove მეთოდების საშვალებით. შემდეგ შექემნით მეორე set და არსებულ 2 set-ს შორის შეასრულეთ სამივე მოქმედება: union, intersection, difference

set1 = {2, 4, 6, 8, 10, 12, 13, 14}
set2 = {1, 3, 5, 7, 9, 11, 13, 15}

'''
set-ის ყველა მეთოდი 
.add()
.remove()
.union()
.difference() 
.intersection()
'''

print(set1.add(16))
print(set1.add(17))

print(set1.remove(4))
print(set2.remove(5))

print(set1.union(set2))

print(set1.difference(set2))

print(set1.intersection(set2))