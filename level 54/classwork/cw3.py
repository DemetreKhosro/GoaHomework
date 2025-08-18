'''3) შექმენით decorator ფუნქცია, რომელიც თავისთავად შექმნის wrapper ფუნქციას და დააბრუენბს მას. აიღეთ მარტივი greet ფუნქცია რომელიც აბრუნებს "Hello World"-ს და გამოიძახეთ მიანიჭეთ მას decorator. საბოლოოდ გამოიძახეთ greet ფუნქცია'''

def decorator(func):
    def wrapper():
        print('Function start')
        func()
        print('Function end')
    return wrapper

@decorator
def greet():
    print('hello')