amount = float(input("Order amount (TRY): "))
stock = int(input("Available stock: "))
quantity = int(input("Requested quantity: "))
is_member = input("Is the customer a member? (yes/no): ").strip().lower() == "yes"

if amount <= 0 or stock < 0 or quantity <= 0:
    print("Order rejected: invalid input.")
elif quantity > stock:
    print("Order rejected: insufficient stock.")
elif is_member and amount >= 500:
    final_price = amount * 0.90
    print("Order approved: member discount (10%) applied.")
    print(f"Final price: {final_price:.2f} TRY")
else:
    final_price = amount
    print("Order approved: standard order, no discount.")
    print(f"Final price: {final_price:.2f} TRY")