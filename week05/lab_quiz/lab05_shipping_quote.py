FREE_SHIPPING_THRESHOLD = 500
SHIPPING_FEE = 49.90


def calculate_subtotal(items):
    """items: list of (unit_price, quantity) pairs. Returns the subtotal."""
    total = 0
    for price, quantity in items:
        total += price * quantity
    return total


def get_discount_rate(subtotal):
    """Returns the discount rate for a subtotal (0.10 means 10%)."""
    if subtotal >= 1000:
        return 0.10
    elif subtotal >= 500:
        return 0.05
    return 0.0


def get_shipping_fee(subtotal):
    """Returns 0 if the subtotal reaches the threshold, otherwise the flat fee."""
    if subtotal >= FREE_SHIPPING_THRESHOLD:
        return 0.0
    return SHIPPING_FEE


def calculate_final_total(items):
    """Combines the other functions and returns the amount to pay."""
    subtotal = calculate_subtotal(items)
    discount_rate = get_discount_rate(subtotal)
    shipping = get_shipping_fee(subtotal)
    return round(subtotal * (1 - discount_rate) + shipping, 2)


def print_quote(order_name, items):
    """Prints the quote to the screen. Returns nothing, it only prints."""
    subtotal = calculate_subtotal(items)
    print(f"--- {order_name} ---")
    print(f"Subtotal : {subtotal:.2f} TL")
    print(f"Discount : {get_discount_rate(subtotal) * 100:.0f}%")
    print(f"Shipping : {get_shipping_fee(subtotal):.2f} TL")
    print(f"Total    : {calculate_final_total(items):.2f} TL")
    print()


assert calculate_subtotal([(100, 2), (50, 1)]) == 250
assert get_shipping_fee(499.99) == 49.90
assert get_shipping_fee(500) == 0.0
assert get_discount_rate(500) == 0.05
assert calculate_final_total([(300, 1), (250, 2)]) == 760.0

order1 = [(120.0, 2), (45.5, 1)]
order2 = [(300.0, 1), (250.0, 2)]

print_quote("Order 1", order1)
print_quote("Order 2", order2)