from BankAccount import BankAccount
# class not needed
class Repository:
  
  mylist = []

  def add(self):
    mylist = ["deposit", "withdraw"]

  def add_transaction(self, balance, name, amount):
    mylist.append((balance, name, amount))
    return mylist