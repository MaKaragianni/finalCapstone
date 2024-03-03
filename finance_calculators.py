'''
This is an investment calculator & a home loan repayment calculation program
The user has 2 options to choose from (investment or bond)
Issue/Change 1 to existing program: Extracting Calculation Logic into Functions
The previous script processed directly the logic for investment and bond calculations within the main if-else blocks.
We're now extracting these calculations into separate functions to make the code more organized, readable and easier to test.
'''

import math

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
print("Enter 'investment' if you wish to calculate the amount of interest you'll earn on your investment")
print("Enter 'bond' if you wish to calculate the amount you'll have to pay on a home loan")

choice = input("Please enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if choice == "investment":
    p = float(input("Please enter the amount of your deposit: "))
    r = float(input("Please enter your interest rate, as a percentage (e.g., enter 8 for 8%): ")) / 100
    t = int(input("Please enter the number of years you plan on investing: "))
    interest = input("Would you prefer 'simple' or 'compound' interest? ").lower()
    total_amount = calculate_investment(p, r, t, interest)
    if total_amount is not None:
        print(f"The total amount after {t} years is: {total_amount}")

elif choice == "bond":
    p = float(input("Please enter the current value of the house (e.g., 1000000): "))
    annual_interest = float(input("Please enter the interest rate as a percentage (e.g., enter 7 for 7%): ")) / 100
    n = int(input("Please enter the number of months over which you plan to repay the bond (e.g., 120): "))
    repayment = calculate_bond(p, annual_interest, n)
    print(f"Your monthly bond repayment will be: {repayment}")
else:
    print("Invalid input. Please enter either 'investment' or 'bond'.")