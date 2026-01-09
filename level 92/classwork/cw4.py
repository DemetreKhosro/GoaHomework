<<<<<<< HEAD
''' შექმენით ფუქნცია სახელად case_swap რომელიც მიიღებს სიტყვას, ფუნქციამ ყველა დიდი ანბანის ასო უნდა გარდაქმნას პატარად და პირიქით, ხოლო სხვა სახის სიმბოლები იგივე უნდა დარჩეს (.upper(), .lower() მეთოდების გამოყენების გარეშე) '''

string = 'DemEtRE'

def case_swap(text):
  result = ''
  for ch in text:
    code = ord(ch)
    if 65 <= code <= 90:
      result += chr(code + 32)
    elif 97 <= code <= 122:
      result += chr(code - 32)
    else:
      result += ch
  return result

=======
''' შექმენით ფუქნცია სახელად case_swap რომელიც მიიღებს სიტყვას, ფუნქციამ ყველა დიდი ანბანის ასო უნდა გარდაქმნას პატარად და პირიქით, ხოლო სხვა სახის სიმბოლები იგივე უნდა დარჩეს (.upper(), .lower() მეთოდების გამოყენების გარეშე) '''

string = 'DemEtRE'

def case_swap(text):
  result = ''
  for ch in text:
    code = ord(ch)
    if 65 <= code <= 90:
      result += chr(code + 32)
    elif 97 <= code <= 122:
      result += chr(code - 32)
    else:
      result += ch
  return result

>>>>>>> 65faaba9bc09cf6dcbb40c514a9b58b45e705cc4
print(case_swap(string))