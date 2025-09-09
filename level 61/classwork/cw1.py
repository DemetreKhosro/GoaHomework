'''1) შექმენით data.txt ფაილი პითონით, ამისთვის გამოიყენეთ ფაილზე "x"-ის უფლებით გახსნა (open ფუნქციას)

ფაილის შექმნის შემდეგ გასხსენით ფაილი სტანდარუტი გზით, ჩაწერეთ ინფორმაცია და დახურეთ. შემდეგ ფაილი გახსენით with open as სინტქასით და readlines() მეთოდის დახამრებთ ცალცალკე ხაზებზე გამოიტანეთ ფაილში ჩაწერილი ინფორმაცია'''

my_file = open("data.txt", "x")
my_file.close()

my_file = open("data.txt", "w")

my_file.write("ABC")
my_file.write("123")

my_file.close()


with open("data.txt", "r") as my_file:
    lines = my_file.readlines()