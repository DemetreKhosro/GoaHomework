'''1) პირდაპირ გამოიყენეთ string-ებზე lower, upper, capitalize, მეთოდები კომენტარებით დაწერეთ რა არის მეთოდი რით განსხვავდება ჩვეულებრივი ფუნქციისგან, რა არის dot ნოტაცია. ასევე გააკეთეთ 3 მაგალითი find მეთოდზე, აუცილებლად უნდა იყოს 3 შემთხვევა: error, -1, რაიმე პოზიციას (index)'''

print('dEmeTrE'.upper())
print('dEmeTrE'.lower())
print('dEmeTrE'.capitalize)

word = 'GoalOrientedAcademy'
print(word.find('z'))
print(word.find('y'))
print(word.find(1))

# მეთოდი არის ფუნქცაი რომელიც იწერება dot ნოტაციის სინტაქსით
# მეთოდი ჩვეულებრივი ფუნქციისგან განსხვავდება იმით რომ მეთოდს ვიყენებთ მხოლოდ შესაბამისი ტიპის მქონე მნიშვნელობებთან
# dot ნოტაცია არის ჯერ .-ის დაწერა და შემდეგ ფუნქცია