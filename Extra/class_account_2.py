from datetime import datetime

class Account:
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        #self._balance = initial_amount
        trans = {'time': datetime.now(), 'amount': initial_amount}
        self._transactions = [trans]

    def deposit(self, amount):
        trans = {'time': datetime.now(), 'amount': initial_amount}
        self._transactions.append(trans)
        #self.balance += amount

    def withdraw(self, amount):
        self.deposit(-amount)
        #self.balance -= amount

    def get_balance(self):
        balance = 0
        for t in self._transactions:
            balance = balance + t['amount']
        return balance
        #return self._balance

    def dump(self):
        s = f'{self._name}, {self._no}, balance: {self.get_balance()}'
        print(s)

    def print_transactions(self):
        for t in self._transactions:
            s = f"(t['time'] t['amount'])"
            print(s)

a = Account('js', 123, 100)
a.deposit(100)
a.withdraw(50)
print(a.get_balance())
a.dump()
a.print_transactions()
"""

def test_Account():
    a = Account('js', 123, 0)
    a.deposit(34)
    a.withdraw(15)
    expected = (19, 3)
    success = (a.balance, a._transactions) == (19,3)
    assert success
test_Account()

a1 = Account('Joakim', 12345, 100)
a1.dump()
a1.deposit(1000)
a1.dump()
"""
