while True:
    balance = float(input("Enter your starting balance: "))
    if balance >= 0:
        break
    print("Balance cannot be negative. Please try again.")

while True:
    deposit = float(input("Enter monthly deposit amount: "))
    if deposit > 0:
        break
    print("Deposit amount cannot be negative or zero. Please try again.")

while True:
    rate = float(input("Enter annual interest rate (as a percentage): "))
    if rate >= 0:
        break
    print("Interest rate cannot be negative. Please try again.")

while True:
    goal = float(input("Enter your savings goal: "))
    if goal > 0:
        break
    print("Savings goal must be greater than zero. Please try again.")

if balance >= goal:
    print("\nCongratulations! You have already reached your savings goal.")
    print(f"Final balance: {balance:.2f}")
    print("Total interest earned: 0.00")
starting_balance = balance
total_interest = 0.0
goal_reached = False
months = 0
print("\nMonth | Interest | Earned")
print("---------------------------")

for month in range(1, 61):
    interest = balance * (rate /100)
    balance = interest + balance + deposit
    total_interest = total_interest + interest
    months = month
    print(f"{month} | {interest:.2f} | {balance:.2f}")
    if balance >= goal:
        goal_reached = True
        break
    if goal_reached:
        print(f"\nCongratulations! You have reached your savings goal of {goal:.2f} in {months} months.")
    else:
        print(f"\nYou did not reach your savings goal of {goal:.2f} in 60 months.")

    print(f"Final balance: {balance:.2f}")
    print(f"Total interest earned: {total_interest:.2f}")
