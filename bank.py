import locale

class BankAccount():

  def __init__(self):
    self.balance = 0
    self.account = None

  def add_money(self, amount):
    """Add money to a bank account

    Arguments:
      amount - A numerical value by which the bank account's balance will increase
    """
    self.balance += float(amount)

  def withdraw_money(self, amount):
    """Withdraw money to a bank account

    Arguments:
      amount - A numerical value by which the bank account's balance will decrease
    """
    pass
    self.balance -= float(amount)

  def show_balance(self):
    """Show formatted balance

    Arguments:
      None
    """
    locale.setlocale( locale.LC_ALL, '' )
    return locale.currency(self.balance, grouping=True)







