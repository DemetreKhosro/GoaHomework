class Student:
    student_count = 0
    def __init__(self, name, grade, id):
        self.name = name
        self._grade = grade
        self.__id = id
        Student.student_count += 1

    @classmethod
    def get_student_count(cls):
        return cls.student_count
    

# _grade - protected - კლასის შიდა გამოყენებისთვის
# __id - private - კლასის გარედან ვერ მივწვდებით და არის private რადგან ყველა ახალ სტუდენტს უნიკალური კოდი ID უნდა ჰქონდეს