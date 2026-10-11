# mis203-basic-programming

- **Name:** Metin Baran Eker
- **Student Number:** 2404109055
- **Department:** Management Information Systems
- **Course Name:** MIS203 Basic Programming

---

### AI Tool Information

- **AI Tool Used:** Gemini
- **Prompt Used:** Create a simple python program. Your program should ask the user for Name, Department, Age, Career Goal. Then print a short student profile.
- **What did you change?** I added the specific Student Profile header and used python int() and f-strings to format the output exactly as requested in the assignment.

## Week 02

**AI Tool Used:** Gemini
**Prompt Used:** "Here is my code for the assignment. What is missing according to the instructions?"
**What did you change?** I fixed the boundary logic (<=), added the `continue` statement for invalid scores, and added variables to calculate the average score.
**What does break do in your program?** It immediately stops the loop when the user types 'q'.

---

## Week 03

**AI Tool Used:** Claude
**Prompt Used:** "Here is my code for the assignment. Tell me only what is wrong or missing, do not guide me."
**What did you change?** I fixed the input prompts to match the required output format and corrected the comparison and assignment syntax. I also added `.title()` to print customer names with a capital first letter.
**Tests:**
1. Age 5, weekend, student no → `Can: 0.00 TRY (Free)`
2. Age 6 (boundary), weekday, student no → `Deniz: 120.00 TRY (Child)`
3. Age 150 → `Invalid age.`
**Why does the order of the rules matter?** If the Student rule came before the Child rule, a 10-year-old student would get the Student discount (30%) instead of the Child discount (40%), because the first matching rule is applied and the rest are skipped.

---

## Week 04

**AI Tool Used:** Claude
**Prompt Used:** "Surprise me assignment: write code that surprises, using what we learned in Python so far and importing at least two libraries. Give me hints step by step, do not write everything."
**What did you change?** I chose the idea of a planet age program and wrote the age input loop with validation, the planet calculations and the `elif` menu myself with hints. Claude wrote some code blocks for me (for example the `random` and `datetime` parts and the final combined version), and I tested them, fixed the indentation errors, replaced the funny messages with serious "Did you know?" facts and removed the unused list. I also changed the program so that it asks the age again after every planet until the user types 0.
**Libraries used:**
1. `datetime`: `datetime.datetime.now()` gets today's date, and `today.year - age` estimates the birth year.
2. `random`: `random.choice(messages)` shows a different fact after each planet.
**Tests:**
1. Age 21, planet 1 → `Mercury age: 87` and a random fact
2. Age 150 → `Invalid age! Enter a number between 1 and 120`
3. Age 30, planet 99 → `Invalid choice.`
4. Age 0 → `Goodbye!`
**Why do we divide the days by the length of the planet's year?** I first convert the age to Earth days (`age * 365`), then divide by how many Earth days one year lasts on that planet (for example 88 for Mercury), so the result is the age on that planet.
