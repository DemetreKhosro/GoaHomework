score = int(input("Enter your score: "))
if score > 80:
    grade = "A"
else:
    if score > 60:
        grade = "B"
    else:
        if score > 40:
            grade = "C"
        else:
            if score > 20:
                grade = "D"
            else:
                grade = "F"
    
print(f"You got a {grade} in the test!")