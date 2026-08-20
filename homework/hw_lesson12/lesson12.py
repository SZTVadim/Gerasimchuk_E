class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        return True if self.pages > 300 else False


book1 = Book('Унесенные ветром', 'Margaret Mitchel', 600)
book2 = Book('Десять негритят', 'Агата Кристи', 247)
book3 = Book('Белый клык', 'Джек Лондон', 301)

print(book1.get_info())
print(book1.is_long())
print(book2.get_info())
print(book2.is_long())
print(book3.get_info())
print(book3.is_long())


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if int(amount) <= int(self.balance):
            self.balance -= amount
            return True
        print('Недостаточно средств')
        return False

    def get_balance(self):
        return self.balance


my_bank_account = BankAccount('Kate', 50000)
my_bank_account.deposit(10000)
my_bank_account.withdraw(50000)
my_bank_account.withdraw(40000)
print(my_bank_account.get_balance())
