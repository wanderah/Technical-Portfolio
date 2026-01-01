# -----------------------  Object-Oriented Programming (OOP) ---------------------------------------------------------
# OOP is a programming paradigm that organizes code into objects, which represent real-world entities (like a bank
# account, a student, or a car). # Each object bundles data (attributes) and behavior (methods) together. Python is
# a multi-paradigm language — meaning you can write procedural, functional, or object-oriented code. However, OOP is
# often preferred for building modular, scalable, and reusable systems.

# ------------------------------- Classes & Objects ----------------------------------------------------------------
# A class is a blueprint or template for creating objects.
# It defines the attributes (data) and methods (functions) that its objects will have.
# An object is an instance of a class — a specific version of the template. Look into the example 👇👇👇👇👇👇

# class Car:
#     # Class attribute
#     wheels = 4
#
#     # Constructor (initializer)
#     def __init__(self, brand, color):
#         self.brand = brand  # Instance attribute
#         self.color = color  # Instance attribute
#
#     # Method
#     def drive(self):
#         print(f"The {self.color} {self.brand} is driving.")
# Creating objects
# car1 = Car("Toyota", "Red")
# car2 = Car("BMW", "Black")
#
# car1.drive()   # Output: The Red Toyota is driving.
# car2.drive()   # Output: The Black BMW is driving.

# In this code; {Car → Class (blueprint), car1, car2 → Objects (instances),
# brand, color → Instance variables, # drive() → Instance method}

# ------------------------------------Encapsulation ----------------------------------------------------------------
# Encapsulation --> bundling of data (attributes) and methods (functions) that operate on the data into a single unit
# (a class), and restricting direct access to some of the object's components. This hiding of internal implementation
# details promotes modularity and data integrity. Encapsulation restricts direct access to an object’s data and only
# allows modifying it through well-defined methods. Python achieves this using access modifiers:
# Modifiers = {"Public": "self.name", "Protected":"self._name" , "Private":"self.__name"}
# A Public object is accessible anywhere in the program, A protected object is accessible within class and subclasses
# A Private object is accessible only within the class.

# In order to understand Encapsulation better, think about how discrete Bank Account systems are engineered
# An account's credentials can only be viewed by authorised personnel and the holder of the account
# The attributes {Objects --> Account Name, Balances and Security Credentials} must be encapsulated --> Hidden

# Below is a python class called BankAccount that simulates Encapsulation.(●'◡'●)
# •	Uses private variables to store the account holder's name and balance,
# •	Has methods used to deposit money, withdraw money and show the current balance

class BankAccount:
    def __init__(self, name, balance=0.0):
        # Private variables
        self.__name = name
        self.__balance = balance

    # Deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful! New balance: {self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw money from the account
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds! Withdrawal failed.")
        else:
            self.__balance -= amount
            print(f"Withdrawal successful! New balance: {self.__balance:.2f}")

    # Display current balance
    def show_balance(self):
        print(f"Account Holder: {self.__name}")
        print(f"Current Balance: {self.__balance:.2f}")

    # Getter method for the account holder's name
    @property
    def name(self):
        return self.__name

    # Setter method for the account holder's name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.__name = new_name.strip()
            print(f"Account holder name updated to '{self.__name}'")
        else:
            print("Invalid name! Name must be a non-empty string.")


# Example usage
account = BankAccount("Alice", 5000)

print("=== Initial Account Details ===")
account.show_balance()

print("\n=== Performing Transactions ===")
account.deposit(2000)
account.withdraw(1500)
account.withdraw(6000)  # Attempting to withdraw more than available

print("\n=== Final Account Details ===")
account.show_balance()

# Using the getter property
print(f"\nAccount holder's name (via getter): {account.name}")

# Using setter to update name
print("\n=== Updating Account Holder Name ===")
account.name = "Mary"
account.show_balance()

# Attempt invalid updates
account.name = ""
account.name = 123


# The Constructor Method __init__() is Called automatically when creating a new object.
# It Initializes private attributes __name and __balance.
# The double underscores (__) make them private, meaning they cannot be accessed directly from outside the class.

# The Deposit Method Allows controlled modification of the balance. It prevents invalid deposits (like negative amounts).
# The Show Balance Method Provides controlled read-only access to private variables.

# If you try to directly access the private variables using the print statement below:
# print(account.__balance)
# You’ll get: AttributeError: 'BankAccount' object has no attribute '__balance'
# Because the variable is encapsulated — hidden from direct external access.

# The Getter Property for Account Holder’s Name Allows read-only access to the private attribute __name.
# You can access it like a normal attribute: print(account.name)
# But you can not modify it directly (e.g., account.name = "Bob" will cause an error).

# The @name.setter is a setter method that allows you to access the account name (a private variable) and modify it
# @name.setter tells Python that this method belongs to the property called name so that when you try to update the
# name by writing account,name = "Mary" this method (def name(self, new_name):) is automatically called in the background.
# and the new value "Mary" is passed to the parameter new_name.

# if isinstance(new_name, str) and new_name.strip(): --> validates the input before changing the account name.
# isinstance(new_name, str) --> checks if new_name is a string.
# new_name.strip() removes spaces from the beginning and end of the string. If it’s empty (like " "), it returns False.
# So this condition ensures the name is a non-empty string that isn’t just spaces.

# self.__name = new_name.strip() --> If the validation passes: The private variable __name is updated with the
# cleaned-up version of the string.
# print(f"Account holder name updated to '{self.__name}'") --> Prints a message that confirms the update.

# else: --> If the validation fails (e.g., name is "", " ", or not a string),
# print("Invalid name! Name must be a non-empty string.") --> it does not update the variable and instead prints
# an error message.

# ---------------NOTE -------------------------------------------------------------------------------------------------
# strip() is a built-in method of Python’s str class (string objects).
# It’s used to remove whitespace (or specified characters) from both ends of a string. 👇👇👇👇
# name = "   Alice   "
# print(name.strip())   # Output: "Alice"


# ------------------------- WITHOUT ENCAPSULATION --------------------------------------------------------------------
# Class objects can be accessed and modified from anywhere in the program. Look into the code 👇👇👇👇👇👇

# BankAccount Class — Without Encapsulation
class BankAccount:
    def __init__(self, name, balance=0.0):
        # Public attributes (no encapsulation)
        self.name = name
        self.balance = balance

    # Deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: {self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw money from the account
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds! Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: {self.balance:.2f}")

    # Display current balance
    def show_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance:.2f}")


# Example usage
account = BankAccount("Alice", 5000)

print("=== Initial Account Details ===")
account.show_balance()

print("\n=== Performing Transactions ===")
account.deposit(2000)
account.withdraw(1500)

print("\n=== Final Account Details ===")
account.show_balance()

# Directly accessing and modifying internal data (unsafe!)
account.balance = -9999  # No restriction!
account.name = 12345     # Invalid data type but allowed
print("\nAfter unsafe modification:")
account.show_balance()

# There will be no data protection --> Attributes like balance and name can be directly accessed and modified.
# Anyone can change the balance to a negative number or set a name to an integer — which breaks the logic.
# There will be no way to enforce conditions when changing data.
# For example, we can set balance = "Hello" — which would crash future operations.
# The internal representation of data (variables, validation rules) is exposed to anyone using the class.
# If you later change how the balance is stored, every piece of code accessing it directly breaks.
