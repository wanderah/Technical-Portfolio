# --- TASK 1: Kibabii Primary School Grading System ---

def kibabii_grading_system():
    """
    Prompts the user for marks in five subjects, computes the average,
    and assigns a grade based on the specified criteria.
    """
    subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
    marks = []

    print("--- Kibabii Primary School Grading System ---")

    # 1. Input Marks and Basic Validation
    for subject in subjects:
        while True:
            try:
                # Prompt the user
                mark = int(input(f"Enter mark for {subject}: "))

                # Validation check (0 to 100)
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("⚠️ Mark must be between 0 and 100.")
            except ValueError:
                print("❌ Invalid input. Please enter a whole number.")

    # 2. Compute Average
    if not marks:
        print("❌ No marks entered. Cannot compute average.")
        return

    total_marks = sum(marks)
    average = total_marks / len(marks)

    # 3. Determine Grade based on Table 1
    # Criteria: 80+ (A), 70-79 (B), 60-69 (C), 40-59 (D), 0-39 (E)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:  # 0-39
        grade = "E"

    # 4. Display Results
    print("\n--- Grading Report ---")
    print(f"Total Marks: {total_marks}")
    # The task doesn't require 2dp for average, but it's good practice
    print(f"Computed Average: {round(average, 2)}")
    print(f"Final Grade: **{grade}**")
    print("-" * 25)


if __name__ == "__main__":
    kibabii_grading_system()