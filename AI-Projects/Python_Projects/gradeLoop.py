# Student Competency Evaluator

try:
    # Prompt the user to enter a score
    score = int(input("Enter the student's score (0 - 100): "))

    # Check for negative or invalid scores
    if score < 0:
        print("Error: Score cannot be negative.")

    elif score >= 90:
        print("Competency: Excellent")

    elif 80 <= score <= 89:
        print("Competency: Good")

    elif 70 <= score <= 79:
        print("Competency: Average")

    elif 60 <= score <= 69:
        print("Competency: Pass")

    elif score < 60:
        print("Competency: Fail")

except ValueError:
    # Handles non-integer inputs (like text or decimals)
    print("Error: Please enter an integer score.")

# try: -—> start of protected block
# ... a try block to catch errors that might happen when converting the user input to an integer.
# ... Anything inside this block that raises a ValueError will jump to the except ValueError: block below.

# If you want to accept decimal scores (e.g., 85.5), parse with float() instead of int() and adjust the type
# ... check/error message accordingly.
# If you want the program to keep asking until the user types a valid score, wrap the input/validation
# ... in a while True: loop