# Week 5 Lab: Reusable Shipping Quote

## Program

`lab05_shipping_quote.py` calculates a shipping quote with four separate functions. `calculate_subtotal(items)` adds up unit price times quantity for every item. `get_discount_rate(subtotal)` returns 0% below 500, 5% from 500 and 10% from 1000. `get_shipping_fee(subtotal)` returns 0 from 500 and a flat 49.90 below that. `calculate_final_total(items)` combines them and returns the amount to pay. `print_quote(order_name, items)` only prints the result. The same functions are called for two sample orders, so no calculation code is copied.

## Print vs Return

`print` shows text on the screen but does not give the value back to the program. `return` sends the value back to the caller, so it can be stored in a variable, used in calculations or checked with `assert`. That is why the calculation functions return values and only `print_quote` prints.

## Boundary Tests

| Subtotal | Discount | Shipping | Expected Final Total |
|---|---|---|---|
| 499.99 | 0% | 49.90 | 549.89 |
| 500 | 5% | 0.00 | 475.00 |
| 999.99 | 5% | 0.00 | 949.99 |
| 1000 | 10% | 0.00 | 900.00 |

## Test I Ran

I ran `assert get_shipping_fee(500) == 0.0` to check the free shipping boundary. Exactly 500 TL should ship free. I also ran the two sample orders: Order 1 (subtotal 285.50) gave a total of 335.40, and Order 2 (subtotal 800.00) gave 760.00.

## What I Changed After Testing

My first version used `>` instead of `>=` in `get_shipping_fee`, so an order of exactly 500 TL was still charged shipping. The boundary assert failed, so I changed it to `>=`.