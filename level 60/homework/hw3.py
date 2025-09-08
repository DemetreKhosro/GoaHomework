class Books:
    def __init__(self, books, secretCode):
        self._books = books
        self.__secretCode = secretCode

    @staticmethod
    def fine_calculator(days_late, fine_per_day=1):
        return days_late * fine_per_day


# staticmethod არ იღებს self-s ან cls-ს, ის ეკუთვნის კლასს მაგრამ არ უკავშირდება კონკრეტულ ობიექტს, ხოლო classmethod იღებს cls-ს და მუშაობს კლასის ატრიბუტებზე და მეთოდებზე