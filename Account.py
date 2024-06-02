class Account:
    """Creating an Account class with methods"""

    def __init__(self, balance, interest):
        # Initializes an instance of the Account class with balance and interest parameters.
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        """Sets the balance for the account."""
        # Sets the balance attribute of the Account instance to the given balance value.
        self.balance = balance

    def set_interest(self, interest):
        """Sets the interest gained for the account."""
        # Sets the interest attribute of the Account instance to the given interest value.
        self.interest = interest