class BankAccount:
  balance = 0
  a = "balance"
  
  def __init__(self, balance):
    self.balance = balance
  
  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount
  
  def get_balance(self):
    return print(self.balance)
  
  def __str__(self):
    return f'Balance: {self.balance}'
  
  def __repr__(self):
    return f'Balance: {self.balance}'
  
