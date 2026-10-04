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
