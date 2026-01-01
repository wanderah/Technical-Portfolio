def get_positive_float_input(prompt):
    """Prompts user for input and validates it is a positive number."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value > 0:
                return value
            print("⚠️ Value must be a positive number.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


def compute_bmi_and_interpret():
    """
    Calculates BMI based on user input (weight/height) and provides
    the interpretation using Table 2 criteria.
    """
    print("--- Khalaba Mission Hospital: BMI Calculator ---")

    # 1. Input and Validate Data
    print("\n[Input Patient Measurements]")
    weight_kg = get_positive_float_input("Enter Weight (in kilograms): ")
    height_m = get_positive_float_input("Enter Height (in meters): ")

    # 2. Compute BMI
    # Formula: BMI = Weight (kg) / Height (m)²
    if height_m == 0:
        print("❌ Error: Height cannot be zero.")
        return

    # ** is the power operator in Python (height_m * height_m)
    bmi = weight_kg / (height_m ** 2)

    # Round BMI to one decimal place for display
    bmi_2dp = round(bmi, 2)

    # 3. Output Appropriate Interpretation (using Table 2)
    if bmi <= 20:
        interpretation = "underweight"
    elif bmi <= 25:  # BMI is > 20 and <= 25
        interpretation = "Normal"
    elif bmi <= 29:  # BMI is > 25 and <= 29
        interpretation = "overweight"
    else:  # BMI is > 29
        interpretation = "obese"

    # 4. Display Results
    print("\n--- BMI Report ---")
    print(f"Weight: {weight_kg:.2f} kg")
    print(f"Height: {height_m:.2f} m")
    print(f"Calculated BMI: {bmi_2dp}")
    print(f"Interpretation: **{interpretation}**")
    print("-" * 30)


# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    compute_bmi_and_interpret()