'''შექმენით student dictionary, რომელშიც გექნებათ მინიმუმ 4 ელემენტი. შემდეგ გამოიყენეთ მეთოდები ამ dictionary-ზე

.update()
.pop()
ელემენტი შეცვალეთ'''

student = {
    'Name': 'John',
    'Age': '15',
    'Subject': 'History',
    'Country': 'USA'
}

student.update({'Country': 'Canada'})
student.pop('Subject')
student['Age'] = 16
