"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
bonus1 = 0.1
bonus2 = 0.15

while sales >= 0:
    if sales < 1000:
        user_bonus = sales * bonus1
        print(f"Your bonus is: {user_bonus}")

    elif sales >= 1000:
        user_bonus = sales * bonus2
        print(f"Your bonus is: {user_bonus}")

    else:
        print("Error: Invalid number.")

    sales = float(input("Enter sales: $"))
print("Whoops! Please put a VALID NUMBER.")