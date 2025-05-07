start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if end < start:
    print('არასწორი შუალედი')
else:
    total = 0
    print('რიცხვების შუალედი: ')
    for num in range(start, end + 1):
        print(num)
        total += num

print('რიცხვების ჯამი არის: ', total)