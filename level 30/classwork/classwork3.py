'''3) შექმენით ახალი new_greet ფუნქცია რომელსაც ექნება 2 პარამეტრი: first_name და last_name. ამ ფუნქციამ უნდა დაბეჭდოს შემდეგი ტექსტი: "Greetings [firstname] [lastname] ფუნქცია 2-ჯერ გამოიძახეთ და გადაეცით არგუმენტები. კომენტარებით ახსენით რა განსხვავებაა პარამაეტრებსა და არგუმენტებს შორის'''
def new_greet(first_name, last_name):
    print(f'Greetings {first_name} {last_name}')

new_greet('Demetre', 'Khosroshvili')
new_greet('Jackie', 'Chan')

# არგუმენტი არის მნიშვნელობა რომელსაც ფუნქცია იყენებს გამოძახებისას
# პარამეტრი არის ცვლადი რომელსაც ვწერთ ფუნქციაში როგორც new_greet(first_name, last_name)