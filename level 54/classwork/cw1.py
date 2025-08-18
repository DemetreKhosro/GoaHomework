'''1) შექმენით პროდუქტების dictionary. შემდეგ გაფილტრეთ ეს dictionary და დატოვეთ ის პროდუქტები რომელთა ფასი ნაკლებია 100-ზე. საბოლოოდ დაბეჭდეთ ეს dict'''

dictionary = {
    'apple': 50,
    'banana': 20,
    'strawberry': 30,
    'watermelon': 110,
    'pineapple': 150,
}

filtered = dict(filter(lambda x: x[1] < 100, dictionary.items()))

print(filtered)