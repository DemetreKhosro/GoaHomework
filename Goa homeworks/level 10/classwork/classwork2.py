"""2) მომხმარებელს შემოატანინეთ თავისი სიმაღლე, შემდეგ შემოატანინეთ წლების რაოდენობა, მიღებული ინფორმაცია შეინახეთ ცვლადებში და გამოუთვალეთ მომხმარებელს სავაურდო სიმაღლე EH (Estimated Height) როდესაც გავა y წელი (რაც მომხმარებლმა შემოიტანა) თუ დაუშვათ ყოველ წელს სიმაღლე იზრდება 0.5-ით. საბოლოოდ გამოუტანეთ EH"""
#ვქმნით ცვლად height-ს რომელშიც მომხარებელს შემოჰყავს თავისი სიმაღლე და გარდავქმნით float-ად
height = float(input("Enter your height: "))
#ვქმნით ცვლადს years სადაც მომხმარებელს შემოყავს სასურველი წლების რაოდენობა და გარვდაქმნით მას integer-ად
years = int(input("Enter years: "))
#ვქმნით ცვლადს EH (Estimated Height) სადაც მომხმარებლის შემოყვანილი ინფორმაციით პროგრამა ითვლის თუ რა სიმაღლის იქნება მომხმარებელი მის შემოყვანილი წლების რაოდენობაში, თუ ის ყოველ წელს 0.5 სანტიმეტრით იზრდება
EH = height + (years * 0.5)
#ბოლოს გამოგვაქ შედეგი ტერმინალში
print("Your estimated height in" + " " + str(years) + " " + "years" + " " + "will be " + str(EH) + " " + "centimeters.")