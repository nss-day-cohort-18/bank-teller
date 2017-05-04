import os
from bank import *


class Teller():
  """This class is the interface to a customer's bank acccount

  Methods:
    main_menu
  """

  def __init__(self):
    self.account = BankAccount()

  def build_menu(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Add money")
    print("2. Withdraw money")
    print("3. Show balance")
    print("4. Quit")

  def main_menu(self):
    """Show teller options

    Arguments: None
    """
    self.build_menu()
    choice = input(">> ")


    if choice == "1":
      deposit = input("How much? ")
      self.account.add_money(deposit)

    if choice == "2":
      withdrawal = input("How much? ")
      self.account.withdraw_money(withdrawal)

    if choice == "3":
      print(self.account.show_balance())
      input()

    if choice != "4":
      self.main_menu()


if __name__ == "__main__":
  teller = Teller()
  teller.main_menu()
