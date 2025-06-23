'''2) შექმენით manual_max ფუნქცია რომელსაც პარამეტრად გადაეცემა სია და აბრუნებს ყველაზე დიდ მნიშვნელობას. ასევე შექმენით manual_len ფუნქცია რომელიც თვლის გადაცემული მიმდევრობის სიგრძეს'''

def manual_max(arr):
    largest = arr[0]
    for number in arr:
        if number > largest:
            largest = number
    return number


def manual_len(sequence):
    length = 0
    for char in sequence:
        length += 1
    return length