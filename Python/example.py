# Python Walkthrough - Syntax Guide for Programmers New to Python

# ============================================================================
# 1. VARIABLES AND BASIC TYPES
# ============================================================================
# Python is dynamically typed - no type declarations needed
name = "Alice"           # String
age = 30                 # Integer
height = 5.9             # Float
is_active = True         # Boolean

# Multiple assignment
x, y, z = 1, 2, 3

# ============================================================================
# 2. STRINGS
# ============================================================================
# String concatenation
greeting = "Hello, " + name
print(greeting)

# F-strings (formatted string literals) - very common in modern Python
message = f"My name is {name} and I am {age} years old"
print(message)

# String methods
text = "python"
print(text.upper())          # PYTHON
print(text.capitalize())     # Python
print(len(text))             # 6

# ============================================================================
# 3. COLLECTIONS
# ============================================================================
# Lists - ordered, mutable (like arrays in other languages)
numbers = [1, 2, 3, 4, 5]
print(numbers[0])            # Access by index: 1

numbers.append(6)            # Add to end
print(numbers[0])            # Access by index: 1

numbers.pop()                # Remove last item
print(numbers[0])            # Access by index: 1

# Tuples - ordered, immutable (like const arrays)
coordinates = (10, 20)
print(coordinates[0])        # 10

# Dictionaries - key-value pairs (like maps/objects)
person = {
    "name": "Bob",
    "age": 25,
    "city": "NYC"
}
print(person["name"])        # Bob
person["age"] = 26           # Modify value

# Sets - unordered, unique values (like Set in Java)
unique_numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}

# ============================================================================
# 4. CONTROL FLOW
# ============================================================================
# If/Else - Python uses indentation instead of braces
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Loops - for loop (iterate over collection)
for num in numbers:
    print(num)

# While loop
counter = 0
while counter < 3:
    print(f"Count: {counter}")
    counter += 1

# Break and continue
for i in range(10):
    if i == 3:
        continue             # Skip to next iteration
    if i == 7:
        break                # Exit loop

# ============================================================================
# 5. FUNCTIONS
# ============================================================================
# Function definition with type hints (optional but recommended)
def greet(name: str, times: int = 1) -> str:
    """
    Greet someone multiple times.
    Args:
        name: Person's name
        times: How many times to greet (default: 1)
    Returns:
        Greeting string
    """
    return f"Hello {name}! " * times

result = greet("Alice", times=3)
print(result)

# Functions can return multiple values
def get_coordinates():
    return 10, 20

x, y = get_coordinates()

# ============================================================================
# 6. LIST COMPREHENSIONS
# ============================================================================
# Concise way to create lists (very Pythonic)
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# ============================================================================
# 7. CLASSES AND OBJECTS
# ============================================================================
class Animal:
    """Simple class definition"""
    
    def __init__(self, name: str, species: str):
        """Constructor - initialize instance variables"""
        self.name = name
        self.species = species
    
    def speak(self) -> str:
        """Instance method"""
        return f"{self.name} makes a sound"
    
    @staticmethod
    def info() -> str:
        """Static method - doesn't need self"""
        return "This is the Animal class"

# Create instance
dog = Animal("Rex", "Dog")
print(dog.speak())

# ============================================================================
# 8. ERROR HANDLING
# ============================================================================
# Try/Except blocks
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This always runs")

# ============================================================================
# 9. WORKING WITH FILES
# ============================================================================
# Reading a file
with open("file.txt", "r") as file:
    content = file.read()

# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# ============================================================================
# 10. LAMBDA FUNCTIONS (Anonymous functions)
# ============================================================================
# Short function without def keyword
square = lambda x: x**2
print(square(5))  # 25

# Often used with map, filter, sorted
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))  # [2, 4, 6, 8, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# ============================================================================
# 11. MODULES AND IMPORTS
# ============================================================================
import math                    # Import entire module
from datetime import datetime  # Import specific item
from os import path as ospath  # Import with alias

# Use imported items
print(math.sqrt(16))          # 4.0
now = datetime.now()

print("--- End of Python Walkthrough ---")