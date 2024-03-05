'''
We'll create an investment calculator & a home loan repayment calculation program
The user has 2 options to choose from (investment or bond)

Issue 2: Adding Constants for User Prompts and Messages
Coding strings directly into the code can make it challenging to make changes later on,
especially for repeated messages or prompts. Defining these strings as constants
at the beginning of the script can improve maintainability.
'''

import math

# Constants
INVESTMENT_PROMPT = "Enter 'investment' if you wish to calculate the amount of interest you'll earn on your investment"
BOND_PROMPT = "Enter 'bond' if you wish to calculate the amount you'll have to pay on a home loan"
CHOICE_PROMPT = "Please enter either 'investment' or 'bond' from the menu above to proceed: "
INVALID_INPUT_MESSAGE = "Invalid input. Please enter either 'investment' or 'bond'."
DEPOSIT_PROMPT = "Please enter the amount of your deposit: "
INTEREST_RATE_PROMPT = "Please enter your interest rate, as a percentage (e.g., enter 8 for 8%): "
YEARS_PROMPT = "Please enter the number of years you plan on investing: "
INTEREST_TYPE_PROMPT = "Would you prefer 'simple' or 'compound' interest? "
HOUSE_VALUE_PROMPT = "Please enter the current value of the house (e.g., 1000000): "
ANNUAL_INTEREST_PROMPT = "Please enter the interest rate as a percentage (e.g., enter 7 for 7%): "
MONTHS_PROMPT = "Please enter the number of months over which you plan to repay the bond (e.g., 120): "

def calculate_investment(p, r, t, interest):
    if interest == "simple":
        return p * (1 + r * t)
    elif interest == "compound":
        return p * math.pow((1 + r), t)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        return None

def calculate_bond(p, annual_interest, n):
    i = annual_interest / 12  # Converting annual interest rate to monthly
    return (i * p) / (1 - (1 + i) ** (-n))

# Main program
print("There are two types of calculations available: ")
print(INVESTMENT_PROMPT)
print(BOND_PROMPT)

choice = input(CHOICE_PROMPT).lower()

if choice == "investment":
    p = float(input(DEPOSIT_PROMPT))
    r = float(input(INTEREST_RATE_PROMPT)) / 100
    t = int(input(YEARS_PROMPT))
    interest = input(INTEREST_TYPE_PROMPT).lower()
    total_amount = calculate_investment(p, r, t, interest)
    if total_amount is not None:
        print(f"The total amount after {t} years is: {total_amount}")

elif choice == "bond":
    p = float(input(HOUSE_VALUE_PROMPT))
    annual_interest = float(input(ANNUAL_INTEREST_PROMPT)) / 100
    n = int(input(MONTHS_PROMPT))
    repayment = calculate_bond(p, annual_interest, n)
    print(f"Your monthly bond repayment will be: {repayment}")
else:
    print(INVALID_INPUT_MESSAGE)