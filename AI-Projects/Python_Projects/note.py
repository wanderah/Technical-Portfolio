# print ("Hello World!")
# import math
# from linecache import clearcache
from scipy.constants import value

# ------ 🔥🔥🔥PYCHARM SHORTCUTS 🔥🔥🔥🔥---------------------------------------------------------------------

# -----------CURSOR, TYPE & TYPING SHORTCUTS---------------------------

# Ctrl + D --> Duplicate Line
# Shift + Enter --> cursor below
# Ctrl + Alt + Enter --> Cursor Above
# Shift + Alt + U/D arrow keys --> Move Line Above/Below
# Shift + Alt + U/D arrow keys --> Move Line Below
# Windows Key + semicolon (;) or bullet (.) --> type emoji
# Alt + Drag --> Add Selection
# Alt + Click --> Add Cursor to separate Line
# Shift + Delete --> Delete an entire line of code or selection

# TAB --> creates a 4-Space Indentation
# Shift + TAB --> Removes The 4-Space Indentation

# ---------------------INTERFACE SHORTCUTS---------------------------------

# Alt + R/L arrow keys --> Shift Right/Left Between open tabs
# Ctr + Tab --> Switch between recently viewed files/tabs using the Switcher
# -----------------------------------------------------------------------------------------------------------------


#------- VARIABLES => Named storage location for type {str, float, bool}----------------------------------

#string 'str' datatype  & string concatenation --> stores a series of characters enclosed in quotes
#remember the quotation marks "" OR '' for all string datatypes
#first_name = "Hawkins"
#last_name = "Wandera"
#full_name = first_name + " " + last_name
#print(full_name)
#print("Hello " + full_name) # => String concatenation
#print (type(full_name)) # => Print datatype

# integer 'int' datatype  & int--string concatenation --> stores integers, whole numbers
#age = 22
#age += 1 # => increment age by 1
#print (age)
#print (type(age)) # => Print datatype
#print ("Your age is" + " " +str(age)) # => Type casting--string casting

# float 'float' datatype  & float--string concatenation --> stores floating point numbers (decimals)
#height = 250.50
#height += 1 # => increment age by 1
#print (height)
#print (type(height)) # => Print datatype
#print ("Your height is" + " " +str(height) + "cm") # => Type casting--string casting

#boolean 'bool' datatype --> stores boolean values (true or false)
#human = True
#print (type(human)) # => Print datatype

#Multiple Assignment of Variables
#name, age, height, human = "Hawkins Wandera", 22, 195.00, True
#print(name, age, height, human)
#print (str(name) + " you are " + str(age) + " years old " + "and " + str(height) + "cm" + " tall")

#String Methods
##printname = "Hawkins Wandera"
#print (len(name)) #the length len method -->returns the length of the string
#print (name.find("s")) #the find method --> returns the index of the character under search
#print(name.capitalize()) #the capitalize method -->returns the name in caps or sentence case if there's a space
#print (name.upper()) # -->returns the name in caps
#print (name.lower()) # -->returns the name in lowercase
#print (name.title()) # -->returns the name in title case
#print (name.isdigit()) # -->returns true if the string contains numbers only
#print (name.isalpha()) # -->returns True if the string contains letters only
#print (name.count()) # -->returns the number of characters in the string
#print (name.count("a")) # -->returns the number of "a" characters in the string
#print (name.replace("a", "o")) # -->replaces all "a"  with "o" characters in the string
#print (name*3) # -->prints the string three times

# strip() is a built-in method of Python’s str class (string objects).
# It’s used to remove whitespace (or specified characters) from both ends of a string. 👇👇👇👇
# name = "   Alice   "
# print(name.strip())   # Output: "Alice"

#Type Casting & Concatenation --> Type casting converts one datatype into another
#x = 1
#y = 2.0
#z = "3"

#print("x is " + str(x))
#print(int(y))
#print(int(z))

#The Input function
# name = input("Enter your name? ")
#age = int(input("How old are you? "))
#height = float(input("How tall are you in cm? "))

#print("Hello " + name)
#print("you are " + str(age) + " years old " + "and " + str(height) + "cm tall")

#Math functions
#pi = 3.14
#print(round(pi)) # --> rounds up pi to a whole number --> 3
#print(math.ceil(pi)) # --> Return the ceiling of pi as an Integral.This is the smallest integer >= x. --> 4
#print(math.floor(pi)) # --> returns the floor of pi as an Integral. This is the largest integer <= pi --> 3
#print(abs(pi)) # --> determines the absolute value of pi; how far pi is from zero
#print(pow(pi,2)) # --> raises pi to the power of 2 using the built-in pow() function
# The pow() function is used  to raise a number to a # certain power, it takes three arguments base; the number you
# want to raise, exponent: the power you want to raise it # to and modulus; which is useful in cryptography to calculate
# the remainder. For example pow (3,4,5) --> output = 1 because 3^4 = 81 % 5 = 1
#print(math.sqrt(420)) # --> determines the square root of 420

#String slicing --> used to create a substring by extracting elements from another string
#You can use an indexing[] operator or a slice function()
#For indexing, there are three fields we can fill in depending on where and how we want to slice the string
#They include [start_index:stop_index:step_index]
#text = "Yes his first name is Hawkins"
#first_name = text[22::1]
#reversed_first_name = first_name[::-1]#print
#print(first_name)
#print(first_name.upper())
#print(first_name.lower())
#print(reversed_first_name)

#The slice function creates a slice operator which can be referenced in print statements
#website1 = "https://google.com"
#website2 = "https://wikipedia.com"

#slice = slice(8,-4)
#print(website1[slice])
#print(website2[slice])

# If statement --> a block of code that will execute if a condition is true
# age = int(input("How old are you?"))
# if age >= 18:
#     print("You are 18 years old")
# else:
#     print("You are not 18 years old")

#Logical operators in python {and, or, not} --> used to check if two or more conditional statements are true
# temp = int(input("Enter the temperature: "))
# if temp >= 30 and temp <= 45:
#     print("The temperature is between 30 and 45")
# elif temp < 30 or temp > 45:
#         print("The temperature is not in range")

#While loop --> a conditional statement that will execute a block of code as long as the condition is true
# name = "" #in python, None, empty strings like "" or zero values are considered False
# while len(name) == 0:
#     name = input("Enter your name: ")
# print("Hello " + name)

# name = None #initializes the variable name with None (no value yet)
# while not name: #This loop will run as long as the name is empty or falsy
#     name = input("Enter your name: ") #Inside the loop, it asks the user to input their name, stores it in name variable
# print("Hello " + name) #once a valid non-empty name is entered, the loop ends and prints a message.

#for loop --> a statement that will execute its block of code a limited amount of times
#while loop --> iterates unlimited number of time, for loop --> limited number of times
# for i in range(10): #Loop from index 0 through index 9
#     print(i) #print all elements
#
# for i in range(50, 100, 2): #Loop from index 50 through index 100, count up by 2
#     print(i) #print all elements 50 is inclusive, 100 is exclusive.

#the benefit of a for loop is it can iterate through anything that is iterable
#the letters in a string or any sort of collection
# name = "Hawkins Wandera"
# for i in (name):
#     print(i)

# #a for loop can be used to simulate a countdown
# import time
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Time is Up")

#nested loops --> the inner loop will finish its iterations before finishing one iteration of the outer loop
# rows = int(input("Enter number of rows: ")) #gets a string-->int() converts it into a number for example 3 rows become 3
# cols = int(input("Enter number of columns: "))#gets a string-->int() converts it into a number for columns
# symbol = input("Enter symbol: ") #asks user fo character or symbol to be printed
#
# for i in range(rows): #outer loop runs once per row, if rows = 3 it runs 3 times(i=0,1,2)
#     for j in range(cols):#inner loop runs once per column inside each row, if column = 4 it prints 4 times per row
#         print(symbol, end=" ")# prints symbol on the same line, separated by space, end="" prevents moving to a new line
#     print () #after printing one full row, this moves to the next line

#Loop control statements change the loop execution from its normal  sequence
#break --> used to terminate the loop entirely when it is encountered
# while True:
#     name = input("Please enter your name: ")
#     if name != "": #If name is not false or zero
#         break #end the iteration --> break
#
# continue skips to the next iteration of the loop
# phone_number = input("Please enter your phone number: ")
# for i in phone_number:
#     if i == "+":
#         continue
#     print(i, end="")

# The pass statement does not do anything, it acts as a placeholder
# for i in range(1, 21):
#     if i == 13:
#         pass
#     else:
#         print (i, end="")

# #combine pass and continue
# phone_number = input("Please enter your phone number: ")
# for i in phone_number:
#     if i == "+" or i == " ":
#         pass
#         continue
#     print(i, end="")

# #Lists in Python --> Variables used to store multiple items
# food = ["Rice", "Beans", "Greens", "Pork", "Eggs"]
# print(food [2])
# # You can always update and change the elements found within a list in a program
# food[0] = "Beef"
# print(food[0])
# for x in food:
#     print(x, end=",")

# #---- You can modify the list -----
# food.append("Fish") #adds fish to the list
# food.remove("Fish") #removes fish element from the list
# food.pop() #removes the last element in the list Eggs
# food.insert(5, "Mutton") #Inserts Mutton at Index [0]
# for x in food:
#  print(x, end=",")

#2D Lists in Python --> 2D Lists are also called Multi-dimensional lists --> List of separate lists
# beverages = ["coffee", "tea", "milk"]
# drinks = ["soda", "beer", "juice"]
# menu = [beverages, drinks] #This creates a 2D list of the two items
# print(menu[0][1]) #from list 1, print the element at index [1] --> tea
# print(menu[1][0]) #from list 2, print the element at index [0] --> soda

# #Tuples, these are collections that are ordered and unchangeable --> useful for grouping related data Looks like a .csv
# student = ("Hawkins", 21, "Male")
# print(student.index("Male")) # prints the index of the element "Male"
# print(student.count("Hawkins")) # returns the total number of items with "Hawkins"
# if 21 in student:
#     print(student.index(21))

# #Set --> a collection that is unordered and unindexed, they do not allow duplicate values.
# food = {"Rice", "Beans", "Greens", "Pork", "Eggs"}
# # food.add("Mutton") #adds Mutton from the set
# # food.remove("Mutton") #removes Mutton from the set
# #You can add a set to another set using the update function
# food2 = {"Chicken", "Bread", "Nuts", "Potatoes", "simsim"}
# # food.update(food2)
# #You can create a union of a set
# # food3 = food.union(food2)
# # food.clear() #clears the set
# #when printed, the order of the elements might not appear as they were ordered
# # for x in food:
# #     print(x) # print all elements in the food set
# # for x in food3:
# #     print(x) #print all elements in the union of food set and food2 set == food3 set
# # print(food.intersection(food2))#print all elements in food and food2
# print(food.difference(food2))#print all elements in food that are not in food2

# #A Dictionary --> A changeable (Mutable) unordered collection of unique key:value pairs
# #Fast because it uses Hashing --> allows faster access
# # In  order to associate a value and a key, use a colon between them.
# stats = {"PTS":"Points", "ASTS":"Assists", "REBS":"Rebounds", "STLS":"Steals", "BLKS":"Blocks"}
#
# # print(stats["ASTS"]) # this will print the Assists, just like the get function on the next line 👇👇👇
# # print(stats.get("ASTS")) # this will print Assists
# # print(stats.keys()) # this will print all the keys
# # print(stats.values()) # this will print all the values
# # print(stats.items()) # this will print the dictionary key and values
# for key, value in stats.items():
#     print(key, value) # this will print the entire dictionary

# #A Dictionary is Mutable, you can change it after the program is running, using Dictionary Methods
# stats.update({"T/O":"Turn Overs"}) #Updates the dictionary
# stats.pop("T/O") #Removves an entry from the Dictionary
# stats.clear() #Clears the Dictionary
#
# for key, value in stats.items():
#     print(key, value)

# #The index operator [] --> gives access to a sequence's element (str,list,tuple)
# name = str.title(input("Enter Your Full name? "))
# # if (name[0].islower()):
# #     name = name.capitalize()
# # print(f"Your name is '{name.title()}'")
#
# #Search for the index of the first letter of your first name and the letter itself
# first_letter = name[0]
# index =[0]
# print(f"The First letter of your name is: '{first_letter}' found at index: {index[0]}")
#
# # Search for the index of the first letter of your second name and the letter itself
# first_space = name.find(" ")
# index_second = name.find(" ") + 1
# print(f"The first letter of your second name is: '{name.upper()[index_second]}'found at index: {index_second}")
# print(f"Your last two names are: '{name[index_second:]}'")
#
# # #Search for the index of the first letter of your third name and the letter itself
# second_space = name.find(" ", first_space + 1)
# index_third = second_space + 1
# print(f"The first letter of your third name is: '{name.upper()[index_third]}' found at index '{index_third}'")
# print(f"Your last name is: '{name[index_third:]}'")

# ____________________________ STRING FORMATTING ----------------------------------------------------------------------

# The .format() method in python is a string formatting method used to insert values into a string at specified
# placeholder positions. It uses the syntax 👉 "string with {}" placeholders" .format(value1, value2, ...) For example:
# name = "Hawkins"
# age = 25
# print ("My name is {} and, I'm {} years old." .format(name, age)) # output --> My name is Hawkins Wandera, and I'm 25
# years old. This can also be written with positional index as ("My name is {0} and, I'm {1}. {0} loves coding."
# format(name, age)) or named placeholders as ("My name is {n} and, I'm {a}." format(n = name, a = age)) or with
# formatting as in: pi = 3.14159 print ("pi rounded to 2 decimal places: {:.2f}" .format(pi))

# introduced in Python 3.6+, the formatted string literal or f-string is a convenient way to embed expressions (like variables) directly
# inside string literals using the syntax 👉 f"some text {expression} for example:
# name = "Hawkins"
# age = 25
# print (f"My name is {name} and I'm {age} years old." # Output --> My name is Hawkins, and I'm 25 years old.
# f-string supports any valid expressions inside the {} for example: (f"Next year I will be {age + 1} years old.")
# It also allows you to add more formatting options for example: (f"pi rounded off to two decimal places: {pi:.2f}").
# This provides cleaner and more readable code as compare to the .format() or % formatting and it is great for building
# dynamic strings quickly

# ------------------------------ PYTHON BEHIND THE SCENES FUNCTION CALLS IN PYTHON -----------------------------------
## Python uses descriptors behind the scenes whenever you access or assign to attributes that have special behavior
# (like properties, methods, or even class variables with custom logic). Let’s unpack this carefully, because this
# concept is foundational to how Python’s object model works. A descriptor is any object in Python that defines one or
# more of these three special methods:

# __get__(self, instance, owner)
# __set__(self, instance, value)
# __delete__(self, instance)

# If a class attribute defines any of those methods, Python treats it as a descriptor. Python then uses this descriptor
# to call functions behind the scenes. Descriptors control how attributes are accessed, modified, or deleted. Whenever
# you do attribute access like this: 👉 account.name
# Python internally checks if name (in the class definition) is a descriptor.
# If it is, then Python calls one of its special methods:

#---------------------------------------------------------------------------------------------------------------------
# OPERATION                 BEHIND THE SCENES CALL                                  DESCRIPTOR
#---------------------------------------------------------------------------------------------------------------------
# account.name              type(account).name.__get__(account, type(account))      __get__ descriptor method
# account.name = "Mary"     type(account).name.__set__(account, "Mary"))            __set__ descriptor method
# del account.name          type(account).name.__delete__(account)                  __delete__ descriptor method
#---------------------------------------------------------------------------------------------------------------------


