# Import the Account class from the Account.py file.
from Account import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        tuple: A tuple containing the updated savings account balance after adding the interest earned and the interest earned itself.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    savings_account = Account(balance, 0)  # Initialize with 0 interest

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the Account class.
    savings_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the Account class.
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned