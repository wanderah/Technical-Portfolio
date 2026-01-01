import math


def get_positive_float_input(prompt):
    """Helper function to ensure input is a positive number."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value > 0:
                return value
            print("⚠️ Dimension must be a positive number.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


def calculate_alizo_areas():
    """
    Prompts for the three dimensions (top, bottom, height, radius)
    and calculates the area of the trapezium, circle, and shaded part.
    """
    print("--- Alizo Metal Company Area Calculator ---")

    # 1. Prompt the user for dimensions
    print("\n[Enter Dimensions]")
    # Note: For this specific fixed figure, we use the values provided
    # but still prompt the user to fulfill the requirement.
    top_base = get_positive_float_input("Enter Top Base (a) in cm (Expected 46): ")
    bottom_base = get_positive_float_input("Enter Bottom Base (b) in cm (Expected 56): ")
    height = get_positive_float_input("Enter Height (h) in cm (Expected 18): ")
    radius = get_positive_float_input("Enter Circle Radius (r) in cm (Expected 10): ")

    # 2. Program calculates the areas

    # Trapezium Area: A = 0.5 * (a + b) * h
    area_trapezium = 0.5 * (top_base + bottom_base) * height

    # Circle Area: A = pi * r^2
    area_circle = math.pi * (radius ** 2)

    # Shaded Part Area: A_shaded = A_trapezium - A_circle
    area_shaded = area_trapezium - area_circle

    # 3. Display the calculations on the screen (Rounding all results to 2dp)
    print("\n--- Calculation Report ---")
    print(f"Top Base (a): {top_base:.2f} cm")
    print(f"Bottom Base (b): {bottom_base:.2f} cm")
    print(f"Height (h): {height:.2f} cm")
    print(f"Radius (r): {radius:.2f} cm")
    print("-" * 30)

    # 4. The display should appear as shown below.
    print("--- Final Area Results ---")
    print(f"Area of Trapezium is: {area_trapezium:.2f} sq. cm")
    print(f"Area of Circle is:    {area_circle:.2f} sq. cm")
    print(f"Area of Shaded Part is: {area_shaded:.2f} sq. cm")
    print("-" * 30)


# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    calculate_alizo_areas()