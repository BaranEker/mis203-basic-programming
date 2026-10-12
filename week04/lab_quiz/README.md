# Week 4 Lab: Savings Goal Planner

## Program

`lab04_savings_planner.py` asks for a starting balance, a monthly deposit, a monthly interest rate (%) and a savings goal. It re-prompts with `while` loops when the starting balance or rate is negative, or when the deposit or goal is not positive. Then it simulates the savings month by month (interest first, then deposit), prints one table row per month and stops with `break` as soon as the goal is reached. If the goal is still not reached, it stops after 60 months. At the end it prints whether the goal was reached, the number of months, the final balance and the total interest.

## Boundary Tests

| Start | Deposit | Rate (%) | Goal | Expected Result |
|---|---|---|---|---|
| 0 | 1000 | 0 | 3000 | Reached in 3 months (balance equal to goal counts), final 3000.00, interest 0.00 |
| 1000 | 500 | 1 | 3000 | Reached in 4 months, final 3070.80, interest 70.80 |
| 0 | 10 | 0 | 10000 | Not reached after 60 months, final 600.00, interest 0.00 |
| 3000 | 100 | 1 | 3000 | Goal already met, no table rows |

## Test I Ran

I entered starting balance 500, deposit 40000, rate 10 and goal 150000. The expected result was 4 months, final balance 186372.05 and total interest 25872.05. I checked it by hand: 186372.05 - 500 - 4 * 40000 = 25872.05.

## What I Changed After Testing

My first version printed the "goal reached" message and the final summary every month, because those lines were indented inside the `for` loop. I moved them out of the loop so they are printed only once, after the simulation. I also changed the rate prompt from "annual" to "monthly", because the program applies the rate every month.