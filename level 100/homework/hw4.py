import random

total_g = 0
total_w = 0
total_a = 0

while True:
  num = random.randint(1, 100)
  tries = 7
  win = False
  used = 0

  while tries > 0:
    try:
      guess = int(input("guess: "))
    except:
      print("error")
      continue

    used += 1
    tries -= 1

    if guess == num:
      print("win", used)
      total_w += 1
      win = True
      break
    elif guess > num:
      print("too big")
    else:
      print("too small")

  if not win:
    print("lost", num)

  total_g += 1
  total_a += used
  stats = (total_g, total_w, total_a / total_g)
  print("stats:", stats)

  if input("again? (y/n): ") != "y":
    break