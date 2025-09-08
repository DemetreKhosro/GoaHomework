class account:
    _count = 0
    
    def __init__(self, name):
        self.name = name
        self._protected = "protected"
        self.__secret = 'secret'
        account._count += 1

    @classmethod
    def get_count(cls):
        return cls._count
    


item = account('item')

print(account.get_count())

# protected ატრიბუტი - მისი გამოყენება არ შეგვიძლია კლასის გარეთ მხოლოდ მის შიგნით ან მემკვიდრეობით კლასებში. იწყება _-ით
# private ატრიბუტი - იწყება __-ით მისი სახელიდ დამალულია, კლასის გარედან არ შეიძლება გამოყენება