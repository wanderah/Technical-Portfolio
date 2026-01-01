import matplotlib.pyplot as plt
import pandas as pd  # <-- IMPORT PANDAS


class LearnerReport:
    """
    Class using a pandas DataFrame for structured data storage,
    computation, and simplified plotting.
    """

    SUBJECTS = ["English", "Science", "Mathematics", "Kiswahili", "Social Studies"]

    def __init__(self):
        """Initializes learner data attributes."""
        self.name = ""
        self.student_number = ""
        self.student_class = ""
        self.gender = ""
        # The core data structure will be the DataFrame
        self.marks_df = pd.DataFrame(columns=['Subject', 'Marks'])
        self.total_marks = 0.0
        self.average_marks = 0.0
        self.grade = ""

    # SUBJECTS = [...] --> A class-level constant (variable) that holds the list of subjects.
    # ...Defines the required subjects, accessible by all methods in the class using self.SUBJECTS or LearnerReport.SUBJECTS.

    # def __init__(self): --> This is the constructor method. It runs automatically when you create
    # ...a new object (learner = LearnerReport()).

    # Sets up the initial state of the object. All variables (attributes) like self.name, self.marks,
    # ...self.total_marks, etc., are initialized to empty values ("", {}, 0, 0.0) before they receive actual data.

    # self.marks_df = pd.DataFrame(...) --> Initializes an empty Pandas DataFrame object.
    # This is the central data structure. It's a two-dimensional, labeled structure (like a table)
    # ....that will hold the 'Subject' and 'Marks' data together.

    # --- INPUT AND VALIDATION METHODS (Similar to previous approaches) ---

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
        """Input subjects and marks, then populate the DataFrame."""
        print("\n--- 2. Input Subject Marks (0-100) ---")

        data_to_add = []

        for subject in self.SUBJECTS:
            while True:
                try:
                    mark_str = input(f"Enter mark for {subject}: ")
                    mark = int(mark_str)

                    if 0 <= mark <= 100:
                        # Append data as a list/dictionary for the DataFrame
                        data_to_add.append({'Subject': subject, 'Marks': mark})
                        break
                    else:
                        print("⚠️ Mark must be between 0 and 100.")
                except ValueError:
                    print("❌ Invalid input. Please enter a whole number.")

        # def _get_valid_input(...) --> A helper function (the underscore _ suggests it's for internal use).
        # ....It takes a prompt string and an optional validation_func.
        # Ensures that required inputs (like name or student number) are not left blank. The while True:
        # ....loop forces the user to provide valid input before the program proceeds.


        # Create the final DataFrame after all data is collected
        self.marks_df = pd.DataFrame(data_to_add)

        # data_to_add = [] --> A temporary list designed to hold Python dictionaries.
        # We collect the data in a format ([{'Subject': 'English', 'Marks': 85}, ...]) that is easily converted into a DataFrame.
        # data_to_add.append({...}) --> Appends a dictionary containing the subject and its validated mark.
        # Collects the validated, structured data for all subjects.
        # self.marks_df = pd.DataFrame(data_to_add) --> Calls the pd.DataFrame() constructor on the list of dictionaries.
        # This builds the final, complete, and labeled DataFrame (self.marks_df) used for the rest of the program.

    # --- COMPUTATION METHODS (Leveraging Pandas) ---

    def compute_results(self):
        """Compute the total and average marks using pandas Series methods."""

        if self.marks_df.empty:
            print("❌ Cannot compute results: No marks entered.")
            return

        #if self.marks_df.empty --> Checks the .empty attribute of the DataFrame.
        # Simple, readable check to determine if the DataFrame contains any rows (i.e., if any marks were entered).

        # Use pandas Series methods (.sum() and .mean())
        self.total_marks = self.marks_df['Marks'].sum()
        self.average_marks = self.marks_df['Marks'].mean()

        # self.marks_df['Marks'] --> Selects a Series (a single column) named 'Marks' from the DataFrame.
        # Allows me to treat the 'Marks' column as a single numerical object for calculations.
        #.sum() and .mean() --> Calls the built-in pandas methods on the selected Series.
        # These methods are highly optimized and calculate the total and average for the entire column.

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

    # --- DISPLAY METHODS (Leveraging Pandas for clear tabular data) ---

    def display_report_form(self):
        """Display learners report form on the screen."""

        average_2dp = round(self.average_marks, 2)

        print("\n" + "=" * 60)
        print("          FINAL LEARNER ACADEMIC REPORT (Pandas)")
        print("=" * 60)

        # Display Learner Details
        print(f"**LEARNER DETAILS**")
        print(f"Name:           {self.name}")
        print(f"Student Number: {self.student_number}")
        print(f"Class:          {self.student_class}")
        print(f"Gender:         {self.gender}")
        print("-" * 60)

        # Display Subject Marks using the DataFrame (very clean output)
        print("**SUBJECT MARKS BREAKDOWN**")
        print(self.marks_df.to_string(index=False))  # to_string() prints a clean table

        #self.marks_df.to_string(index=False)...
        # Calls the to_string() method on the DataFrame. index=False prevents the row numbers from being printed.
        # Prints a  Professional Report Output: A perfectly aligned, clean, ASCII-based table
        # .... of subjects and marks directly to the console.

        print("-" * 60)

        # Display Computations and Grade
        print("**FINAL RESULTS**")
        print(f"Total Marks:    {self.total_marks:.2f}")
        print(f"Average Mark:   {average_2dp} (Corrected to 2dp)")
        print(f"Final Grade:    **{self.grade}**")
        print("=" * 60)

    def plot_bar_graph(self):
        """Plot and display the bar graph using the DataFrame's built-in plotting."""

        if self.marks_df.empty:
            print("Cannot plot graph: Marks data is missing.")
            return

        average_2dp = round(self.average_marks, 2)

        # 1. Initialize the plot
        fig, ax = plt.subplots(figsize=(10, 6))

        #fig, ax = plt.subplots(...) Creates a figure (the overall window) and an axes object (ax, the plot area) in one step.
        # Standard matplotlib setup when using pandas plotting.

        # 2. Plot directly from the DataFrame (the simplest way!)
        self.marks_df.plot(
            kind='bar',
            x='Subject',
            y='Marks',
            legend=False,
            ax=ax,
            color=['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#00BCD4']
        )

        # self.marks_df.plot --> Calls the .plot() method directly on the DataFrame.
        # pandas uses matplotlib behind the scenes but simplifies the syntax.
        # It automatically knows to use the 'Subject' column for the X-axis and the 'Marks' column for the Y-axis
        # Based on the x='Subject' and y='Marks' arguments.
        # ax=ax Passes the created axes object to the pandas plot method.
        # Ensures that any additional features (like the title, labels, and the average line) are applied to the correct plot.

        # 3. Add plot details
        ax.set_ylabel("Marks (Out of 100)")
        ax.set_title(f"{self.name}'s Subject Performance (Average: {average_2dp})")
        ax.axhline(self.average_marks, color='r', linestyle='--', label=f'Average: {average_2dp}')

        ax.set_ylim(0, 100)
        ax.legend()
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Display the graph
        plt.show()


# --- MAIN EXECUTION BLOCK ---

def run_learner_report_program_pandas():
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
    run_learner_report_program_pandas()