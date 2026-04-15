# Python Strings - Complete Guide with Examples

# 1. CREATING STRINGS
print("=== CREATING STRINGS ===")
single_quotes = 'Hello'
double_quotes = "World"
multi_line = """This is a
multi-line
string"""
print(single_quotes)
print(double_quotes)
print(multi_line)

# 2. STRING CONCATENATION
print("\n=== STRING CONCATENATION ===")
first = "Hello"
second = "World"
combined = first + " " + second
print(combined)
combined2 = f"{first} {second}"  # f-string (best practice)
print(combined2)

# 3. STRING LENGTH
print("\n=== STRING LENGTH ===")
text = "Python"
print(f"Length of '{text}': {len(text)}")

# 4. INDEXING AND SLICING
print("\n=== INDEXING AND SLICING ===")
word = "Programming"
print(f"First character: {word[0]}")
print(f"Last character: {word[-1]}")
print(f"First 4 characters: {word[0:4]}")
print(f"Characters from index 3 to 7: {word[3:7]}")
print(f"Every 2nd character: {word[::2]}")

# 5. STRING METHODS
print("\n=== STRING METHODS ===")
text = "  Hello World  "
print(f"Original: '{text}'")
print(f"Lower: '{text.lower()}'")
print(f"Upper: '{text.upper()}'")
print(f"Strip: '{text.strip()}'")
print(f"Replace: '{text.replace('World', 'Python')}'")
print(f"Split: {text.split()}")

# 6. CHECKING SUBSTRINGS
print("\n=== CHECKING SUBSTRINGS ===")
sentence = "Python is awesome"
print(f"'Python' in sentence: {'Python' in sentence}")
print(f"'Java' in sentence: {'Java' in sentence}")
print(f"Starts with 'Python': {sentence.startswith('Python')}")
print(f"Ends with 'awesome': {sentence.endswith('awesome')}")

# 7. STRING FORMATTING
print("\n=== STRING FORMATTING ===")
name = "Alice"
age = 25
score = 95.5
print(f"Name: {name}, Age: {age}, Score: {score:.1f}")
print("Name: {}, Age: {}, Score: {}".format(name, age, score))

# 8. ESCAPE CHARACTERS
print("\n=== ESCAPE CHARACTERS ===")
print("Line 1\nLine 2")  # \n = newline
print("Tab\there")      # \t = tab
print("She said \"Hello\"")  # \" = double quote
print("Backslash: \\")   # \\ = backslash

# 9. ITERATING STRINGS
print("\n=== ITERATING STRINGS ===")
for char in "ABC":
    print(char, end=" ")
print()

# 10. IMMUTABILITY
print("\n=== STRING IMMUTABILITY ===")
original = "Hello"
print(f"Original: {original}")
modified = original.upper()
print(f"Modified: {modified}")
print(f"Original unchanged: {original}")