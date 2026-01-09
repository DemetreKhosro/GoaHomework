<<<<<<< HEAD
# quick sort - ირჩევს ერთ ელემენტს და ყოფს სიას ორ ნაწილად, მარცხნივ იმ ელემენტზე პატარა ელემენტებია, მარჯვნივ - დიდი და შემდეგ იგივე პროცესი მეორდება თითოეულ ნაწილზე
# merge sort - სიებს ყოფს ორ ნაწილად იქამდე სანამ სიებში თითო-თითო ელემენტი არ დარჩება, შემდეგ კი აერთიანებს მათ დალაგებულად

nums = [42, 7, 88, 19, 56, 3, 91, 25, 67, 10]

def quick_sort(arr):
  if len(arr) <= 1:
    return arr

  first_element = arr[0]
  left = []
  right = []

  for x in arr[1:]:
    if x < first_element:
      left.append(x)
    else:
      right.append(x)

  return quick_sort(left) + [first_element] + quick_sort(right)

print(quick_sort(nums))


def merge_sort(arr):
  # თუ სია 1 ან 0 ელემენტიანია, უკვე დალაგებულია
  if len(arr) <= 1:
    return arr

  # სიას ვყოფთ შუაზე
  mid = len(arr) // 2
  # ვალაგებთ მარცხენა და მარჯვენა მხარეს ელემენტებს
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  result = []
  # შედარებით ვაერთიანებთ დალაგებულ სიებს
  while left and right:
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))

  # ვამატებთ დარჩენილ ელემენტებს
  result += left + right
  return result

=======
# quick sort - ირჩევს ერთ ელემენტს და ყოფს სიას ორ ნაწილად, მარცხნივ იმ ელემენტზე პატარა ელემენტებია, მარჯვნივ - დიდი და შემდეგ იგივე პროცესი მეორდება თითოეულ ნაწილზე
# merge sort - სიებს ყოფს ორ ნაწილად იქამდე სანამ სიებში თითო-თითო ელემენტი არ დარჩება, შემდეგ კი აერთიანებს მათ დალაგებულად

nums = [42, 7, 88, 19, 56, 3, 91, 25, 67, 10]

def quick_sort(arr):
  if len(arr) <= 1:
    return arr

  first_element = arr[0]
  left = []
  right = []

  for x in arr[1:]:
    if x < first_element:
      left.append(x)
    else:
      right.append(x)

  return quick_sort(left) + [first_element] + quick_sort(right)

print(quick_sort(nums))


def merge_sort(arr):
  # თუ სია 1 ან 0 ელემენტიანია, უკვე დალაგებულია
  if len(arr) <= 1:
    return arr

  # სიას ვყოფთ შუაზე
  mid = len(arr) // 2
  # ვალაგებთ მარცხენა და მარჯვენა მხარეს ელემენტებს
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  result = []
  # შედარებით ვაერთიანებთ დალაგებულ სიებს
  while left and right:
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))

  # ვამატებთ დარჩენილ ელემენტებს
  result += left + right
  return result

>>>>>>> 65faaba9bc09cf6dcbb40c514a9b58b45e705cc4
print(merge_sort(nums))