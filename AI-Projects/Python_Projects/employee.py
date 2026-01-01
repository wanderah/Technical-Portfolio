# --- FIXED COMPANY FINANCIAL CONSTANTS ---
# Defined outside the class for easy updating
HOUSE_ALLOWANCE = 5000.00
MEDICAL_ALLOWANCE = 6500.00
TAX_RATE = 0.02  # 2% of Gross Salary
LEVY_RATE = 0.015  # 1.5% of Gross Salary


class Employee:
    """
    A class to capture employee details, perform net pay calculations,
    and display the payslip, ensuring data validation and 2dp formatting.
    """

    def __init__(self):
        """Initializes all employee data and calculation results."""
        # Employee Details (Inputs)
        self.id_no = ""
        self.name = ""
        self.gender = ""
        self.salary = 0.0
        self.phone_number = ""

        # Calculation Results
        self.gross_salary = 0.0
        self.tax = 0.0
        self.house_levy = 0.0
        self.total_deductions = 0.0
        self.net_pay = 0.0

    # --- INPUT AND VALIDATION METHODS ---

    def _get_valid_input(self, prompt):
        """Helper method to ensure input is not empty."""
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("⚠️ Input cannot be empty. Please try again.")

    def _get_valid_salary(self):
        """Validates that the salary is a positive number."""
        while True:
            try:
                salary_str = self._get_valid_input("Enter Basic Salary (Ksh.): ")
                salary = float(salary_str)

                # Validation Check: Salary must be positive
                if salary > 0:
                    return salary
                else:
                    print("⚠️ Salary must be a positive value.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number for salary.")

    def input_details(self):
        """Input all employee details as required by the task."""
        print("\n--- 1. Input Employee Details ---")
        self.id_no = self._get_valid_input("Enter Employee ID No: ")
        self.name = self._get_valid_input("Enter Employee Name: ")
        self.gender = self._get_valid_input("Enter Gender: ")
        self.salary = self._get_valid_salary()  # Use validated method
        self.phone_number = self._get_valid_input("Enter Phone Number: ")

    # --- COMPUTATION METHODS (Ensure all monetary values are 2dp) ---

    def compute_gross_salary(self):
        """Computes the gross salary."""
        # Gross = Basic Salary + House Allowance + Medical Allowance
        self.gross_salary = self.salary + HOUSE_ALLOWANCE + MEDICAL_ALLOWANCE
        self.gross_salary = round(self.gross_salary, 2)

    def compute_deductions(self):
        """Computes tax, house levy, and total deductions."""

        # Tax (2% of Gross Salary)
        self.tax = self.gross_salary * TAX_RATE
        self.tax = round(self.tax, 2)

        # House Levy (1.5% of Gross Salary)
        self.house_levy = self.gross_salary * LEVY_RATE
        self.house_levy = round(self.house_levy, 2)

        # Total Deductions
        self.total_deductions = self.tax + self.house_levy
        self.total_deductions = round(self.total_deductions, 2)

    def compute_net_pay(self):
        """Computes the final net pay."""
        # Net Pay = Gross Salary - Total Deductions
        self.net_pay = self.gross_salary - self.total_deductions
        self.net_pay = round(self.net_pay, 2)

    # --- DISPLAY METHOD (Prints Payslip) ---

    def display_payslip(self):
        """Prints the employee's payslip to the screen (PyCharm console)."""

        print("\n" + "=" * 60)
        print(" " * 15 + "WIMA COMPANY - EMPLOYEE PAYSLIP")
        print("=" * 60)

        # A. Employee Details Section
        print("** EMPLOYEE DETAILS **")
        print(f"ID No:           {self.id_no}")
        print(f"Name:            {self.name}")
        print(f"Gender:          {self.gender}")
        print(f"Phone Number:    {self.phone_number}")
        print("-" * 60)

        # B. Earnings Section
        print("** EARNINGS **")
        # The :,.2f format adds thousands separators and ensures 2 decimal places.
        print(f"Basic Salary:    Ksh. {self.salary:,.2f}")
        print(f"House Allowance: Ksh. {HOUSE_ALLOWANCE:,.2f}")
        print(f"Medical Allow:   Ksh. {MEDICAL_ALLOWANCE:,.2f}")
        print(f"GROSS SALARY:    Ksh. {self.gross_salary:,.2f}")
        print("-" * 60)

        # C. Deductions Section
        print("** DEDUCTIONS **")
        print(f"Tax ({TAX_RATE * 100:.1f}%):        Ksh. {self.tax:,.2f}")
        print(f"House Levy ({LEVY_RATE * 100:.1f}%):  Ksh. {self.house_levy:,.2f}")
        print(f"TOTAL DEDUCTIONS:Ksh. {self.total_deductions:,.2f}")
        print("=" * 60)

        # D. Net Pay Section (Final Result)
        print(f"NET PAY:         Ksh. {self.net_pay:,.2f}")
        print("=" * 60)


# --- MAIN EXECUTION BLOCK (FUNCTION) ---

def run_payslip_program():
    """The main function to execute the employee payslip generation process."""

    employee = Employee()  # Create a new Employee object

    # 1. Input and Validate Data
    employee.input_details()

    # 2. Compute Calculations (in order)
    employee.compute_gross_salary()
    employee.compute_deductions()
    employee.compute_net_pay()

    # 3. Print Payslip
    employee.display_payslip()

    print("\nPayslip generation complete.")


if __name__ == "__main__":
    run_payslip_program()