'''
შექმენით ბანკომატის სიმულაცია შემდეგი ფუნქციონალით:

•    საწყისი ბალანსი: 1000 ლარი
•    მთავარი მენიუ (while ციკლით):
ბალანსის შემოწმება
თანხის შეტანა
თანხის გატანა
ბოლო 5 ტრანზაქციის ნახვა
გასვლა
•    ყოველ ოპერაციაზე:
იყენებს try-except ბლოკს:
ValueError - არასწორი რიცხვის შეტანა
არასწორი მენიუს არჩევანი
თანხის გატანისას ამოწმებს საკმარისი ბალანსის არსებობას
შეტანისას და გატანისას ამოწმებს დადებითი რიცხვის შეყვანას
•    ინახავს ტრანზაქციების ისტორიას სიაში: [{'type': 'შეტანა/გატანა', 'amount': თანხა, 'balance': ახალი_ბალანსი}, ...]
•    აჩვენებს ბოლო 5 ტრანზაქციას ფორმატირებული სახით
•    გასვლისას აჩვენებს საბოლოო ბალანსს და ტრანზაქციების რაოდენობას

'''

balance = 1000
transactions = []

def check_transactions(log):
  if not log:
    print("ტრანზაქციები არ მოიძებნა")
  else:
    for trans in log[-5:]:
      print(trans)

def log_transaction(type, amount, current_balance):
  new_transaction = {
    "type": type,
    "amount": amount,
    "balance": current_balance
  }
  transactions.append(new_transaction)

def deposit(current_balance):
  while True:
    try:
      amount = int(input('შეიყვანეთ თანხის რაოდენობა: '))
      if amount <= 0:
        print('თანხის რაოდენობა უნდა იყოს 0-ზე მეტი')
        continue
      break
    except ValueError:
      print('შეიყვანეთ სწორი ციფრი')
  
  current_balance += amount
  print(f'ანგარიშს დაემატა {amount}₾')
  log_transaction('შეტანა', amount, current_balance)
  return current_balance

def withdraw(current_balance):
  while True:
    try:
      withdraw_amount = int(input('შეიყვანეთ თანხის რაოდენობა: '))
      if withdraw_amount <= 0:
        print('თანხის რაოდენობა უნდა იყოს 0-ზე მეტი')
        continue
      elif withdraw_amount > current_balance:
        print('თანხის რაოდენობა არ შეიძლება იყოს ბალანსზე მეტი')
        continue
      else:
        break
    except ValueError:
      print('შეიყვანეთ სწორი ციფრი')

  current_balance -= withdraw_amount
  print(f'წარმატებით შესრულდა ოპერაცია')
  log_transaction('გატანა', withdraw_amount, current_balance)
  return current_balance

while True:
  print('\n' + '=' * 30)
  print('--- მთავარი მენიუ ---')
  print('=' * 30)
  print('1. ბალანსის შემოწმება')
  print('2. თანხის შეტანა')
  print('3. თანხის გატანა')
  print('4. ბოლო 5 ტრანზაქციის ნახვა')
  print('5. გასვლა')

  try:
    choice = input('აირჩიეთ მოქმედება (1-5): ')
    if not choice.isdigit():
      print('გთხოვთ ჩაწეროთ სწორი რიცხვი')
      continue
    
    choice = int(choice)
    if not (1 <= choice <= 5):
      print('გთხოვთ აირჩიოთ მოქმედება 1-დან 5-მდე')
      continue
  except ValueError:
    continue

  if choice == 1:
    print(f"თანხა თქვენს ანგარიშზე: {balance}₾")
  elif choice == 2:
    balance = deposit(balance)
  elif choice == 3:
    balance = withdraw(balance)
  elif choice == 4:
    check_transactions(transactions)
  elif choice == 5:
    print('ნახვამდის')
    break