import matplotlib.pyplot as plt
import numpy as np


class LearnerReport:
    """
    Class using numpy arrays for efficient numerical data storage and computation.
    """

    SUBJECTS = ["English", "Science", "Mathematics", "Kiswahili", "Social Studies"]

    def __init__(self):
        """Initializes learner data attributes."""
        self.name = ""
        self.student_number = ""
        self.student_class = ""
        self.gender = ""
        # We will store the marks as a standard dictionary initially
        self.marks_dict = {}
        # And convert them to a numpy array for calculation
        self.marks_array = np.array([])
        self.total_marks = 0.0
        self.average_marks = 0.0
        self.grade = ""

    # --- INPUT AND VALIDATION METHODS (Same as Approach 1) ---

    @staticmethod
    def _get_valid_input(prompt, validation_func=lambda x: x.strip()):
        """Helper method for basic input validation (ensures not empty)."""
        while True:
            value = input(prompt).strip()
            if validation_func(value):
                return value
            print("⚠️ Input cannot be empty. Please try again.")

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
        self.marks_dict = {}
        mark_list = []  # Temporary list for collection

        for subject in self.SUBJECTS:
            while True:
                try:
                    mark_str = input(f"Enter mark for {subject}: ")
                    mark = int(mark_str)

                    if 0 <= mark <= 100:
                        self.marks_dict[subject] = mark
                        mark_list.append(mark)  # Add to list for numpy conversion
                        break
                    else:
                        print("⚠️ Mark must be between 0 and 100.")
                except ValueError:
                    print("❌ Invalid input. Please enter a whole number.")

        # Convert the collected marks list into a numpy array
        self.marks_array = np.array(mark_list)

    # --- COMPUTATION METHODS (Leveraging NumPy) ---

    def compute_results(self):
        """Compute the total and average marks using numpy methods."""

        if self.marks_array.size == 0:
            print("❌ Cannot compute results: No marks entered.")
            return

        # Use numpy's built-in array methods for computation
        self.total_marks = self.marks_array.sum()  # Faster sum calculation
        self.average_marks = self.marks_array.mean()  # Direct average calculation

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

    # --- DISPLAY METHODS (Uses marks_dict for display) ---

    def display_report_form(self):
        """Display learners report form on the screen."""

        average_2dp = round(self.average_marks, 2)

        print("\n" + "=" * 50)
        print("          FINAL LEARNER ACADEMIC REPORT (Numpy)")
        print("=" * 50)

        # Display Learner Details
        print(f"**LEARNER DETAILS**")
        print(f"Name:           {self.name}")
        print(f"Student Number: {self.student_number}")
        print("-" * 50)

        # Display Subject Marks (using marks_dict)
        print("**SUBJECT MARKS**")
        for subject, mark in self.marks_dict.items():
            print(f"{subject:15}: {mark}")
        print("-" * 50)

        # Display Computations and Grade
        print("**FINAL RESULTS**")
        print(f"Total Marks:    {self.total_marks:.2f}")  # Formatted to 2dp
        print(f"Average Mark:   {average_2dp} (Corrected to 2dp)")
        print(f"Final Grade:    **{self.grade}**")
        print("=" * 50)

    def plot_bar_graph(self):
        """Plot and display the bar graph of subjects and marks."""

        if self.marks_array.size == 0:
            print("Cannot plot graph: Marks data is missing.")
            return

        # Prepare data for plotting
        subject_names = self.SUBJECTS  # Use the original list
        marks_values = self.marks_array  # <-- Pass the numpy array directly
        average_2dp = round(self.average_marks, 2)

        plt.figure(figsize=(10, 6))

        # Create the bar chart
        plt.bar(subject_names, marks_values, color=['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#00BCD4'])

        # Add labels, title, and average line
        plt.xlabel("Subject")
        plt.ylabel("Marks (Out of 100)")
        plt.title(f"{self.name}'s Subject Performance (Average: {average_2dp})")
        plt.axhline(self.average_marks, color='r', linestyle='--', label=f'Average: {average_2dp}')

        plt.ylim(0, 100)
        plt.legend()
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        plt.show()


# --- MAIN EXECUTION BLOCK ---

def run_learner_report_program_numpy():
    """The main function to execute the entire program flow."""
    learner = LearnerReport()

    learner.input_learner_details()
    learner.input_subjects_and_marks()
    learner.compute_results()
    learner.determine_grade()
    learner.display_report_form()
    learner.plot_bar_graph()

    print("\nProgram finished. Check the separate window for the bar graph.")


if __name__ == "__main__":
    run_learner_report_program_numpy()
