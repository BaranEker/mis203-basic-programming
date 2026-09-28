# Lab 02 - Purchase Quote

## Program
lab02_purchase_quote.py asks for two items (name, quantity, unit price), a delivery fee and a tax percentage. It calculates each line total, the subtotal, the tax (applied to the item subtotal only) and the final total (subtotal + tax + delivery fee). Money is printed with two decimal places.

## Test
2 x 50 and 1 x 80, delivery 20, tax 10% -> final total 218.00 TRY (correct).

## Changed after testing
Prices were printed as 19.9 instead of 19.90, so I added :.2f formatting. I also added ": " to the input prompts because the answers looked stuck to the text.

## Why input() must be converted
input() always returns a string, so it must be converted with int() or float() before arithmetic. Otherwise "2" * 50 repeats the text instead of multiplying numbers.

## Stretch task
Typing letters for the quantity gives a ValueError. A later version could use try/except to ask the user again.

## AI tool use
I used Claude (Anthropic) as a tutor while working on this lab. It gave hints, explained my error messages (for example the unterminated f-string and the :.2f syntax) and helped me draft this README. I wrote the program and ran the tests myself.
