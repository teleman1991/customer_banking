from Account import Account  # Import the Account class from the Account.py file

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        tuple: A tuple containing the updated CD account balance after adding the interest earned and the interest earned itself.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    cd_account = Account(balance, 0)  # Initialize with 0 interest

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100) * (months / 12)

    # Update the CD account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the Account class.
    cd_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the Account class.
    cd_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned