# Week 3 Lab: Order Approval Policy

## Program

`lab03_order_approval.py` asks for the order amount, available stock, requested quantity and whether the customer is a member. It rejects invalid quantities and insufficient stock (no final price is shown). Members get a 10% discount on approved orders of at least 500 TRY.

## Boundary Tests

| Amount (TRY) | Member | Quantity / Stock | Expected Result |
|---|---|---|---|
| 499.99 | yes | 1 / 5 | Approved, no discount, 499.99 TRY |
| 500 | yes | 1 / 5 | Approved, member discount, 450.00 TRY |
| 500.01 | yes | 1 / 5 | Approved, member discount, 450.01 TRY |

## Test I Ran

I entered 500 TRY with stock 5, quantity 1 and answered "no" to the membership question. The expected result was 500.00 TRY with no discount.

## What I Changed After Testing

My first version did not turn the membership answer into a True/False value, so any answer (even "no") counted as a member and got the discount. I changed the input line to compare the answer with "yes" (`.strip().lower() == "yes"`), so only real members get the discount.