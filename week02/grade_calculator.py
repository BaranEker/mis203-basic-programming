total_score = 0
student_count = 0

while True:
    student_name = input("Enter student name (or q to quit): ")
    if student_name == "q":
        break
    else:
        score = int(input("Enter score: "))
        if score < 0 or score > 100:
            print("Invalid score. Please enter a number between 0 and 100.")
            continue
        elif 90 <= score <= 100:
            print(f"{student_name}: {score} -> A")
        elif 80 <= score <= 89:
            print(f"{student_name}: {score} -> B")
        elif 70 <= score <= 79:
            print(f"{student_name}: {score} -> C")
        elif 60 <= score <= 69:
            print(f"{student_name}: {score} -> D")
        elif 0 <= score <= 59:
            print(f"{student_name}: {score} -> F")

        total_score += score
        student_count += 1

if student_count > 0:
    average_score = total_score / student_count
    print(f"Total students: {student_count}")
    print(f"Average score: {average_score:.2f}")
else:
    print("No students entered.")
