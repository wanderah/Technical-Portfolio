# Student Competency Evaluator (Enhanced Version)

while True:
    # Ask the user to enter a score or exit
    user_input = input("Enter the student's score (0 - 100) or type 'exit' to quit: ").strip()

    # Check if user wants to exit
    if user_input.lower() == "exit":
        print("Program terminated. Goodbye!")
        break  # Exit the while loop

    try:
        # Attempt to convert input to an integer
        score = int(user_input)

        # Check for valid range
        if score < 0 or score > 100:
            print("Error: Score must be between 0 and 100.\n")
            continue  # Ask again

        # Determine competency based on score
        if score >= 90:
            print("Competency: Excellent\n")

        elif 80 <= score <= 89:
            print("Competency: Good\n")

        elif 70 <= score <= 79:
            print("Competency: Average\n")

        elif 60 <= score <= 69:
            print("Competency: Pass\n")

        else:  # score < 60
            print("Competency: Fail\n")

        # Exit after a valid score is processed
        break

    except ValueError:
        # If conversion to int fails
        print("Error: Please enter a valid integer score or type 'exit' to quit.\n")
