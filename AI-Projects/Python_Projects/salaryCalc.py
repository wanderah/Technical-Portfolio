# --- FIXED FINANCIAL DATA (KLM Company) ---
TAX_RATE = 0.12  # 12% of salary for Taxes

# Allowance map based on Job Group table
ALLOWANCE_MAP = {
    'J': 5000.00,
    'K': 5500.00,
    'L': 6000.00,
    'M': 6500.00
}


class EmployeeKLM:
    """
    Calculates salary components (Gross Pay, Taxes, Net Pay) based on
    employee details and job group allowance structure.
    """

    def __init__(self):
        """Initializes all employee data and calculation results."""
        # Inputs
        self.payroll_number = ""
        self.name = ""
        self.gender = ""
        self.job_group = ""
        self.salary = 0.0

        # Results
        self.house_allowance = 0.0
        self.gross_pay = 0.0
        self.taxes = 0.0
        self.net_pay = 0.0

    # --- INPUT AND VALIDATION METHODS ---

    def _get_valid_input(self, prompt, valid_options=None):
        """Helper for general validation, ensuring input is not empty, and optionally in a list of valid options."""
        while True:
            value = input(prompt).strip()
            if not value:
                print("⚠️ Input cannot be empty. Please try again.")
            elif valid_options and value.upper() not in valid_options:
                print(f"❌ Invalid Job Group. Must be one of {list(valid_options.keys())}.")
            else:
                return value.upper() if valid_options else value

    def _get_valid_salary(self):
        """Validates that the salary is a positive number."""
        while True:
            try:
                salary_str = self._get_valid_input("Enter Basic Salary (Ksh.): ")
                salary = float(salary_str)

                if salary > 0:
                    return salary
                else:
                    print("⚠️ Salary must be a positive value.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number for salary.")

    def input_details(self):
        """Prompts the user to enter all required employee details."""
        print("\n--- 1. Input Employee Details ---")
        self.payroll_number = self._get_valid_input("Enter Payroll Number: ")
        self.name = self._get_valid_input("Enter Employee Name: ")
        self.gender = self._get_valid_input("Enter Gender: ")

        # Validate Job Group against the ALLOWANCE_MAP keys
        self.job_group = self._get_valid_input("Enter Job Group (J, K, L, or M): ", valid_options=ALLOWANCE_MAP)

        self.salary = self._get_valid_salary()

    # --- COMPUTATION METHODS ---

    def determine_allowance(self):
        """Determines the house allowance based on the validated job group."""
        # Uses the Job Group to look up the allowance in the map
        self.house_allowance = ALLOWANCE_MAP.get(self.job_group, 0.0)

    def compute_gross_pay_and_taxes(self):
        """Computes Gross Pay and Taxes."""
        # Gross Pay = house allowance + salary
        self.gross_pay = self.house_allowance + self.salary
        self.gross_pay = round(self.gross_pay, 2)

        # Taxes = 12% of salary
        self.taxes = self.salary * TAX_RATE
        self.taxes = round(self.taxes, 2)

    def compute_net_pay(self):
        """Computes Net Pay."""
        # Net Pay = gross pay - taxes
        self.net_pay = self.gross_pay - self.taxes
        self.net_pay = round(self.net_pay, 2)

    # --- DISPLAY METHOD ---

    def display_report(self):
        """Displays employee details, allowances, and final net pay."""

        print("\n" + "=" * 50)
        print(" " * 10 + "KLM Company - Salary Report")
        print("=" * 50)

        # A. Employee Details
        print("** EMPLOYEE DETAILS **")
        print(f"Payroll Number:  {self.payroll_number}")
        print(f"Name:            {self.name}")
        print(f"Gender:          {self.gender}")
        print(f"Job Group:       {self.job_group}")
        print("-" * 50)

        # B. Allowances and Gross Pay
        print("** EARNINGS & GROSS PAY **")
        # Format : ,.2f ensures thousands separator and 2 decimal places
        print(f"Basic Salary:    Ksh. {self.salary:,.2f}")
        print(f"House Allowance: Ksh. {self.house_allowance:,.2f}")
        print(f"GROSS PAY:       Ksh. {self.gross_pay:,.2f}")
        print("-" * 50)

        # C. Taxes and Net Pay
        print("** DEDUCTIONS & NET PAY **")
        print(f"Taxes ({TAX_RATE * 100:.0f}% of Salary): Ksh. {self.taxes:,.2f}")
        print(f"NET PAY:         Ksh. {self.net_pay:,.2f}")
        print("=" * 50)


# --- MAIN EXECUTION BLOCK ---

def run_klm_salary_program():
    """Executes the entire program flow."""
    employee = EmployeeKLM()

    # i. Input
    employee.input_details()

    # ii. Determine Allowance (Crucial first step for Gross Pay)
    employee.determine_allowance()

    # iii. Determine Gross Pay, Taxes, and Net Pay
    employee.compute_gross_pay_and_taxes()
    employee.compute_net_pay()

    # iv. Display Report
    employee.display_report()


if __name__ == "__main__":
    run_klm_salary_program()