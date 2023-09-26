#Oppgave

class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.transactions = 1

    def deposit(self, amount):
        self.transactions += 1
        self.balance += amount

    def withdraw(self, amount):
        self.transactions += 1
        self.balance -= amount

    def dump(self):
        s = f'{self.name}, {self.no}, balance: {self.balance}, transactions: {self.transactions}'
        print(s)

def test_Account():
    a = Account('js', 123, 0)
    a.deposit(34)
    a.withdraw(15)
    expected = (19, 3)
    success = (a.balance, a.transactions) == (19,3)
    assert success
test_Account()

a1 = Account('Joakim', 12345, 100)
a1.dump()
a1.deposit(1000)
a1.dump()
