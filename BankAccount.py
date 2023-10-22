class BankAccount:
  balance = 0
  amount = 0
  name = ""
  a = "balance"

  def __init__(self, balance):
    self.balance = balance

  #Adding money
  def deposit(self, amount):
    self.balance += amount
    
  #Taking out money
  def withdraw(self, amount):
    self.balance -= amount
    
  #Return the total balance
  def get_balance(self):
    return print(self.balance)

  def __str__(self):
    return f'Balance: {self.balance, self.name}'

  def __repr__(self):
    return f'Balance: {self.balance, self.name}'

  ##Type of transaction
  def get_type(self, name):
    self.name = name

  def get_amount(self, amount):
    self.amount = amount

