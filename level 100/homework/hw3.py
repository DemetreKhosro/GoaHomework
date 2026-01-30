def calculate_average(scores):
  total = sum(scores)
  count = len(scores)
  average = total / count
  return average

def get_grade(average):
  if average >= 91:
    return "A"
  elif average >= 81:
    return "B"
  elif average >= 71:
    return "C"
  elif average >= 61:
    return "D"
  elif average >= 51:
    return "E"
  elif average >= 41:
    return "FX"
  else:
    return "F"

def find_top_student(students_dict):
  best_student = ""
  highest_avg = -1
  for name in students_dict:
    avg = calculate_average(students_dict[name])
    if avg > highest_avg:
      highest_avg = avg
      best_student = name
  return best_student

students = {
  "Dato": [95, 88, 92, 100, 85],
  "Ana": [70, 65, 80, 55, 72],
  "Giorgi": [82, 90, 85, 88, 91],
  "Nino": [45, 50, 42, 38, 55],
  "Mariam": [60, 72, 68, 75, 58]
}

results = []
for name in students:
  avg = calculate_average(students[name])
  grade = get_grade(avg)
  results.append([name, avg, grade])

for i in range(len(results)):
  for j in range(0, len(results) - i - 1):
    if results[j][1] < results[j+1][1]:
      results[j], results[j+1] = results[j+1], results[j]

print("Name | Average | Grade")
print("-" * 25)
for res in results:
  print(res[0], "|", res[1], "|", res[2])

top = find_top_student(students)
print("-" * 25)
print("Top Student:", top)