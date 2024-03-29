# This is a Capstone project
# We'll create an investment calculator & a home loan repayment calculation program
# The user has 2 options to choose from (investment or bond)

import math

print("There are two types of calculations available: ")
print("Enter 'investment' if you wish to calculate the amount of interest you'll earn on your investment")
print("Enter 'bond' if you wish to calculate the amount you'll have to pay on a home loan")
choice = input("Please enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    
if choice == "investment": # If the user enters 'investment', the below user input is requested
    p = float(input("Please enter the amount of your deposit: "))
    r = float(input("Please enter your interest rate, as a percentage (e.g., enter 8 for 8%): ")) / 100
    t = int(input("Please enter the number of years you plan on investing: "))
    interest = input("Would you prefer 'simple' or 'compound' interest? ").lower() # The user has 2 options for interest (simple or compound)

    if interest == "simple":
        a = p * (1 + r * t)
    elif interest == "compound":
        a = p * math.pow((1 + r),t)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")

# We can then calculate the output is the amount they'll get back after the given period at the given interest rate
    print(f"The total amount after {t} years is: {a}")

elif choice == "bond": # If the user enters 'bond', the below user input is requested
    p = float(input("Please enter the current value of the house (e.g., 1000000): "))
    annual_interest = float(input("Please enter the interest rate as a percentage (e.g., enter 7 for 7%): ")) / 100
    n = int(input("Please enter the number of months over which you plan to repay the bond (e.g., 120): "))
    
    i = annual_interest / 12 # Converting annual interest rate to monthly
    repayment = (i * p) / (1 - (1 + i) ** (-n))

# We can then calculate how much money the user will have to repay each month
    print(f"Your monthly bond repayment will be: {repayment}")

else:
    print("Invalid input. Please enter either 'investment' or 'bond'.")