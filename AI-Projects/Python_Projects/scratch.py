import math


# --- i. Display Odd Numbers (0 to 50) ---
def display_odd_numbers():
    print("--- i. Odd Numbers (0 to 50) ---")
    odd_numbers = list(range(1, 51, 2))
    print(odd_numbers)
    print("-" * 30)


# --- ii. Display Even Numbers (0 to 100) ---
def display_even_numbers():
    print("--- ii. Even Numbers (0 to 100) ---")
    even_numbers = list(range(0, 101, 2))
    print(even_numbers)
    print("-" * 30)


# --- iii. Print Triangular Patterns ---
def print_triangular_patterns():
    print("--- iii. Triangular Patterns ---")

    # 1. Triangular Form (1, 22, 333, ...)
    print("A. Triangular Pattern:")
    for i in range(1, 6):
        print(str(i) * i)

    # 2. Opposite Right Triangle (using numbers 5 to 1)
    print("\nB. Opposite Right Triangle:")
    for i in range(5, 0, -1):
        spaces = " " * (5 - i)
        print(spaces + str(i) * i)
    print("-" * 30)


# --- iv. Find First Ten Fibonacci Numbers ---
def find_fibonacci():
    print("--- iv. First Ten Fibonacci Numbers ---")

    a, b = 0, 1
    fib_list = []

    for _ in range(10):
        fib_list.append(a)
        a, b = b, a + b

    print(fib_list)
    print("-" * 30)


# --- v. Lambda Function for Sum ---
def lambda_sum():
    print("--- v. Lambda Function for Sum ---")

    find_sum = lambda x, y: x + y

    num1 = 15
    num2 = 27
    result = find_sum(num1, num2)

    print(f"The numbers are: {num1} and {num2}")
    print(f"The sum found using the lambda function is: {result}")
    print("-" * 30)

# --- vi. Print "Artificial World" in reverse order ---
def reversed_text():
    # Correcting the roman numeral from 'v' to 'vi'
    print("--- vi. Reversed Text ---")
    text = "Artificial World"
    reversed_text = text[::-1]
    print(reversed_text)
    print("-" * 30)


# --- vii. Calculate Area of Circle ---
def calculate_circle_area():
    # Correcting the roman numeral from 'vi' to 'vii'
    print("--- vii. Calculate Area of Circle ---")

    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))

            if radius <= 0:
                print("Radius must be a positive number.")
                continue

            area = math.pi * (radius ** 2)

            print(f"Radius entered: {radius}")
            print(f"Area of the circle (A = πr²): {round(area, 2)}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the radius.")
    print("-" * 30)


# --- viii. Calculate Surface Area of a Sphere ---
def calculate_sphere_surface_area():
    # Correcting the roman numeral from 'vi' to 'viii'
    print("--- viii. Calculate Surface Area of a Sphere ---")
    try:
        radius = float(input("Enter the radius of the sphere: "))

        if radius < 0:
            print("Error: Radius cannot be negative.")
        else:
            # Formula for surface area of a sphere: 4πr²
            area = 4 * math.pi * (radius ** 2)
            print(f"The surface area of the sphere is: {area:.2f} square units")

    except ValueError:
        print("Error: Please enter a valid numeric value for the radius.")

    print("-" * 30)


# --- ix. Calculate the final price of a discounted product  ---
def calculate_discounted_product_price():
    print("--- ix. Calculate Discounted Product Price ---")

    # Data for the client's decision (Product X costing 1500)
    product_name = "Product X"
    product_price = 1500
    discount_threshold = 1000
    discount_rate = 0.10  # 10%

    print(f"Client buys {product_name} at {product_price}.")

    # Use IF statement to check the discount condition
    if product_price > discount_threshold:
        discount_amount = product_price * discount_rate
        final_amount = product_price - discount_amount

        # Print the result
        print(f"{product_name} is eligible for a discount.")
        print(f"Discount received: {discount_amount} ({int(discount_rate * 100)}%)")
        print(f"The amount paid by the client for {product_name} is: {final_amount}")
    else:
        # No discount
        final_amount = product_price
        print(f"{product_name} is NOT eligible for a discount.")
        print(f"The amount paid by the client for {product_name} is: {final_amount}")

    print("-" * 30)


# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    print("🚀 Running All Tasks 🚀")
    print("=" * 30)

    display_odd_numbers()
    display_even_numbers()
    print_triangular_patterns()
    find_fibonacci()
    lambda_sum()
    reversed_text()
    calculate_circle_area()
    calculate_sphere_surface_area()
    # Now this function call will work correctly
    calculate_discounted_product_price()