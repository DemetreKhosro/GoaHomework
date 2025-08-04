'''1) ახსენით კომნენტარებით raise keyword. მოიყვანეთ raise ბრძანების 2 მაგალითი'''

# raise - keyword რომელსაც გამოვიყენებთ ერორის ძალით გამოსასწვევად

index = int(input('input index: '))
if index < 0:
    raise IndexError('input positive index')

num = 10
if num < 0:
    raise IndexError('number is less than 10')