'''3) განხილულ მეთოდებზე: split, join, replace, strip მოიყვანეთ 2-2 მაგალითი. თითოეულს მიუწერეთ კომენტარებით ახსნა თუ როგორ მუშაობს'''
fruit = 'apple banana'
number = '1 2 3 4 5'

number.split(' ') # ყოფს სტრინგს იმ ადგილებში სადაც გადაცემული არგუმენტი ხვდება
fruit.split(' ')

' '.join(number) # აერთებს სიის ელემენტებს გადაცემული არგუმენტით
' '.join(fruit)

len(number.strip()) # შლის ბოლოს დარჩენი space-ებს
len(fruit.strip())