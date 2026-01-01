import matplotlib.pyplot as plt


class LearnerReport:
    """
    A class to capture learner details, marks, compute results,
    determine the grade, and display the report and graph.
    """

    # This class level constant (Variable) defines the subjects once, as required by the task
    SUBJECTS = ["English", "Science", "Mathematics", "Kiswahili", "Social Studies"]

    def __init__(self):
        """Initializes learner data attributes."""
        self.name = ""
        self.student_number = ""
        self.student_class = ""
        self.gender = ""
        self.marks = {}  # Dictionary to store {subject: mark}
        self.total_marks = 0
        self.average_marks = 0.0
        self.grade = ""

    # --- INPUT AND VALIDATION METHODS ---

    @staticmethod
    def _get_valid_input(prompt, validation_func=lambda x: x.strip()):
        """Helper method for basic input validation (ensures not empty)."""
        while True:
            value = input(prompt).strip()
            if validation_func(value):
                return value
            print("⚠️ Input cannot be empty. Please try again.")

    # lambda x: x.strip() --> This is an anonymous function used as the default validation_func.
    # ... It checks if the stripped input (x.strip()) is not an empty string.
    # ....Provides the default validation: ensure the text entered is not just spaces.

    def input_learner_details(self):
        """Input learners details (name, number, class, gender)."""
        print("\n--- 1. Input Learner Details ---")
        self.student_number = self._get_valid_input("Enter Student Number: ")
        self.name = self._get_valid_input("Enter Student Name: ")
        self.student_class = self._get_valid_input("Enter Class: ")
        self.gender = self._get_valid_input("Enter Gender: ")

    def input_subjects_and_marks(self):
        """Input subjects and marks with validation (0-100)."""
        print("\n--- 2. Input Subject Marks (0-100) ---")
        self.marks = {}
        for subject in self.SUBJECTS:
            while True:
                try:
                    # Get input from the user
                    mark_str = input(f"Enter mark for {subject}: ")
                    mark = int(mark_str)

                    # Validation check: Mark must be between 0 and 100
                    if 0 <= mark <= 100:
                        self.marks[subject] = mark
                        break
                    else:
                        print("⚠️ Mark must be between 0 and 100.")
                except ValueError:
                    print("❌ Invalid input. Please enter a whole number.")

    # --- COMPUTATION METHODS ---

    def compute_results(self):
        """Compute the total and average marks."""
        # Calculate total marks from the dictionary values
        self.total_marks = sum(self.marks.values())

        # Calculate average marks
        num_subjects = len(self.SUBJECTS)
        if num_subjects > 0:
            self.average_marks = self.total_marks / num_subjects
        else:
            self.average_marks = 0.0

    def determine_grade(self):
        """Determine the grade attained by the learner."""
        average = self.average_marks
        if 80 <= average <= 100:
            self.grade = "Exceeding expectations"
        elif 60 <= average <= 79:
            self.grade = "Meeting expectations"
        elif 40 <= average <= 59:
            self.grade = "Approaching expectations"
        else:  # 0-39
            self.grade = "Below Expectations"

    # --- DISPLAY METHODS ---

    def display_report_form(self):
        """Display learners report form on the screen."""

        # Correct Average marks to 2dp
        average_2dp = round(self.average_marks, 2)

        print("\n" + "=" * 50)
        print("          FINAL LEARNER ACADEMIC REPORT")
        print("=" * 50)

        # Display Learner Details
        print(f"**LEARNER DETAILS**")
        print(f"Name:           {self.name}")
        print(f"Student Number: {self.student_number}")
        print(f"Class:          {self.student_class}")
        print(f"Gender:         {self.gender}")
        print("-" * 50)

        # Display Subject Marks
        print("**SUBJECT MARKS**")
        for subject, mark in self.marks.items():
            print(f"{subject:15}: {mark}")
        print("-" * 50)

        # Display Computations and Grade
        print("**FINAL RESULTS**")
        print(f"Total Marks:    {self.total_marks}")
        print(f"Average Mark:   {average_2dp} (Corrected to 2dp)")
        print(f"Final Grade:    **{self.grade}**")
        print("=" * 50)

    def plot_bar_graph(self):
        """Plot and display the bar graph of subjects and marks."""

        if not self.marks:
            print("Cannot plot graph: Marks data is missing.")
            return

        # Prepare data for plotting
        subject_names = list(self.marks.keys())
        marks_values = list(self.marks.values())
        average_2dp = round(self.average_marks, 2)

        plt.figure(figsize=(10, 6))

        # Create the bar chart
        plt.bar(subject_names, marks_values, color=['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#00BCD4'])

        # Add labels, title, and average line
        plt.xlabel("Subject")
        plt.ylabel("Marks (Out of 100)")
        plt.title(f"{self.name}'s Subject Performance (Average: {average_2dp})")

        # Draw a horizontal line for the average mark
        plt.axhline(self.average_marks, color='r', linestyle='--', label=f'Average: {average_2dp}')

        plt.ylim(0, 100)
        plt.legend()
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Display the graph
        plt.show()


# --- MAIN EXECUTION BLOCK (FUNCTION) ---

def run_learner_report_program():
    """The main function to execute the entire program flow."""
    learner = LearnerReport()

    # 1. Input Learner Details
    learner.input_learner_details()

    # 2. Input and Validate Marks
    learner.input_subjects_and_marks()

    # 3. Compute Results
    learner.compute_results()

    # 4. Determine Grade
    learner.determine_grade()

    # 5. Display Report
    learner.display_report_form()

    # 6. Plot Graph
    learner.plot_bar_graph()

    print("\nProgram finished. Check the separate window for the bar graph.")


if __name__ == "__main__":
    run_learner_report_program()