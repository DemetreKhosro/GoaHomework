'''1) შექმენით სია რომელშიც ჩამოწერეთ თქვენთვის სასურველი ელემენტები, მინიმუმ 10
**indexing**
- გამოიტანეთ სიაში არსებული მესამე ელემენტი
- ჩაანაცვლეთ სიაში არსებული პირველი ელემენტი
**slicing**
- დაბეჭდეთ 2-დან მე-5 ელემენტამდე 
- დაბეჭდეთ მეორე ელემენტიდან ყველა ელემენტი
- დაბეჭდეთ მეხუთე ელემენტამდე ყვეალფერი
- დაბეჭდეთ სია შემობრუნებულად'''

# indexing
car_brands = ['BMW', 'Mercedes', 'Peugeot', 'Volkswagen', 'Lamborghini', 'Ferrari', 'Porsche', 'Toyota', 'Audi', 'Ford']
print(car_brands[3])
car_brands[1] = 'Renault'

# slicing
print(car_brands[2:5])
print(car_brands[2:])
print(car_brands[:5])
print(car_brands[::-1])