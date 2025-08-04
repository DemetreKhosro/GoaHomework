'''3) შექნებით რიცხვების სია, შექმენით ახალი ცლვადი სახელად squares, რომელიც შეინახავთ ყველა რიცხვს რომელიც იყო თავდაპირველ სიაში ოღონდ აყვანილ მეორე ხარისხში, ამისთვის გამოიყენეთ list, map და lambda ფუნქციები. ასევე ცვლადი even-ს რომელშიც შეინახავთ თადავპირველ სიაში არსებულ მხოლოდ ლუწ რიცვებს, ამ შემთხვევაში გამოიყენეთ filter ფუნქცია. დაამატეთ manual_map და manual_filter თქვენს დავალებას თუ დრო დაგრჩათ და კომენტარებით ახსენით როგორ მუშაობს map და filter ფუნქცია, ასევე დაწერეთ რა არის lambda გამოსახულება და რატომ არის კარგი'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

squares = list(map(lambda x: x ** 2, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))


def manual_map(func, iterable):
    result = []
    for i in iterable:
        result.append(func(i))
    return result


def manual_filter(func, iterable):
    result = []
    for i in iterable:
        if func(i):
            result.append(i)
    return result

# lambda არის იგივე რაც ფუნქციის ერთ ხაზზე დაწერა list(filter(lambda x: x % 2 == 0, numbers)) ასე და კარგია იმიტომ რომ უფრო სწრაფია
# filter ფილტრავს iterable-ს ფუნქციის მიხედვით
# map გადაუვლის ყველა ელემენტს და აბრუნებს შედეგს ფუნქციის მიხედვით