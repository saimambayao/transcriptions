# Python Full Course for free

**Channel**: Bro Code
**Duration**: 720:00
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=ix9cRaBkVe0
**Transcribed**: 2026-04-03 11:42

---

## Python Learning Guide — Standalone Reference Notes

> Source: Bro Code — *Python Full Course for free* (12 hours, 20+ projects)
> These notes are written as a standalone learning reference, not a video summary.

---

### Setup

**Install Python**
- Download the Python interpreter from [python.org](https://python.org) → Downloads → latest version
- On Windows: check **"Add Python.exe to PATH"** before installing — required for running Python from terminal
- The interpreter (`python.exe`) converts your written code into machine instructions at runtime

**IDE Options**
- **PyCharm** — dedicated Python IDE, more features, steeper learning curve
- **VS Code** — lightweight, multi-language, popular for Python with the Python extension
- Both have built-in terminals for running pip commands

**Running Python**
```bash
python main.py        # run a script
python3 main.py       # on Mac/Linux
```

---

### Variables & Data Types

A **variable** is a named container that stores a value. Python is **dynamically typed** — you don't declare the type, Python infers it.

```python
name = "Bro"          # str (string)
age = 21              # int (integer)
gpa = 2.5             # float (decimal)
is_student = True     # bool (True or False)
```

Check the type with `type()`:
```python
print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
```

**Naming rules:**
- Use lowercase with underscores: `first_name`, `is_logged_in`
- No spaces, no special characters, cannot start with a number
- Case-sensitive: `Name` and `name` are different

---

### Strings

Strings are sequences of characters enclosed in quotes (single or double).

**F-strings** (formatted string literals) — embed variables directly into strings:
```python
name = "Bro"
age = 21
print(f"Hello, {name}! You are {age} years old.")
```

**Format specifiers** — control how values are displayed inside f-strings:
```python
price = 9.99
print(f"Price: ${price:.2f}")        # 2 decimal places → $9.99
label = "hello"
print(f"{label:>10}")                # right-align in 10 chars
print(f"{label:<10}")                # left-align in 10 chars
print(f"{label:^10}")                # center in 10 chars
```

**String methods:**
```python
s = "Hello, World!"

len(s)               # 13 — number of characters
s.find("World")      # 7 — index of first occurrence (-1 if not found)
s.upper()            # "HELLO, WORLD!"
s.lower()            # "hello, world!"
s.strip()            # remove leading/trailing whitespace
s.replace("World", "Python")   # "Hello, Python!"
s.count("l")         # 3 — count occurrences
s.isdigit()          # False — True only if all chars are digits
s.isalpha()          # False — True only if all chars are letters
s.split(", ")        # ["Hello", "World!"] — split into list
" ".join(["a", "b"]) # "a b" — join list into string
```

**Indexing and slicing:**
```python
s = "Hello"
s[0]        # "H"   — first character
s[-1]       # "o"   — last character
s[1:4]      # "ell" — characters at index 1, 2, 3 (end is exclusive)
s[:3]       # "Hel" — from start to index 2
s[2:]       # "llo" — from index 2 to end
s[::2]      # "Hlo" — every 2nd character
s[::-1]     # "olleH" — reverse the string
```

---

### Type Casting

Convert a value from one type to another:
```python
x = int("21")          # str → int
y = float("3.14")      # str → float
z = str(100)           # int → str
b = bool(0)            # int → bool (0 = False, anything else = True)
```

**Falsy values** — these all evaluate to `False` in a boolean context:
- `0`, `0.0`, `""` (empty string), `None`, `[]` (empty list), `{}` (empty dict)
- Any non-empty string, even `"False"`, evaluates to `True`

---

### User Input

`input()` always returns a **string** — cast to the type you need:
```python
name = input("Enter your name: ")           # str
age = int(input("Enter your age: "))        # cast to int
height = float(input("Enter your height: ")) # cast to float
```

**Mad Libs example:**
```python
adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
print(f"The {adj} programmer loves to {verb} their {noun}.")
```

---

### Math & Arithmetic Operators

```python
# Basic operators
10 + 3    # 13 — addition
10 - 3    # 7  — subtraction
10 * 3    # 30 — multiplication
10 / 3    # 3.333... — division (always returns float)
10 // 3   # 3  — floor division (integer result)
10 % 3    # 1  — modulus (remainder)
10 ** 3   # 1000 — exponent (power)
```

**Augmented assignment operators:**
```python
x = 10
x += 5    # x = 15
x -= 3    # x = 12
x *= 2    # x = 24
x /= 4    # x = 6.0
x //= 2   # x = 3.0
x %= 2    # x = 1.0
x **= 3   # x = 1.0
```

**`math` module:**
```python
import math

math.sqrt(25)       # 5.0 — square root
math.ceil(4.2)      # 5   — round up
math.floor(4.9)     # 4   — round down
math.pi             # 3.141592653589793
math.e              # 2.718281828459045
math.log(100, 10)   # 2.0 — logarithm base 10
abs(-7)             # 7   — absolute value (built-in, no import needed)
round(3.7)          # 4   — built-in rounding
max(1, 2, 3)        # 3   — built-in max
min(1, 2, 3)        # 1   — built-in min
```

---

### Comparison & Logical Operators

**Comparison operators** return `True` or `False`:
```python
x = 5
x == 5    # True  — equal to
x != 5    # False — not equal to
x > 3     # True  — greater than
x < 10    # True  — less than
x >= 5    # True  — greater than or equal to
x <= 5    # True  — less than or equal to
```

**Logical operators:**
```python
# and — both must be True
x = 5
print(x > 1 and x < 10)   # True

# or — at least one must be True
print(x < 1 or x < 10)    # True

# not — reverses the boolean
print(not(x == 5))         # False
```

---

### Conditional Statements

```python
if condition:
    # runs if condition is True
elif another_condition:
    # runs if first condition is False and this is True
else:
    # runs if all above conditions are False
```

**Example — grade calculator:**
```python
score = int(input("Enter your score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

**Conditional expression (ternary):**

Compact single-line conditional:
```python
# syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # "adult"

# Example: temperature
temp = 30
weather = "hot" if temp > 25 else "cold"
```

---

### While Loops

Repeats a block of code **while a condition is True**.

```python
# Basic while loop
count = 1
while count <= 5:
    print(count)
    count += 1
```

**`while True` with `break`** — runs forever until you explicitly break:
```python
while True:
    answer = input("Enter 'quit' to exit: ")
    if answer == "quit":
        break
    print(f"You said: {answer}")
```

**`continue`** — skip the rest of the current iteration and go to the next:
```python
while True:
    name = input("Enter a name (skip blanks): ")
    if name == "":
        continue     # skip blank entries
    print(f"Hello, {name}!")
    break
```

---

### For Loops

Iterates over a sequence (list, string, range, etc.).

**`range()`** generates a sequence of numbers:
```python
range(5)           # 0, 1, 2, 3, 4
range(1, 6)        # 1, 2, 3, 4, 5
range(0, 10, 2)    # 0, 2, 4, 6, 8 (step of 2)
range(10, 0, -1)   # 10, 9, 8, ..., 1 (countdown)
```

```python
# Count from 1 to 5
for i in range(1, 6):
    print(i)

# Iterate over a string
for char in "Hello":
    print(char)

# Reversed
for i in reversed(range(1, 6)):
    print(i)   # 5, 4, 3, 2, 1

# With step
for i in range(0, 20, 5):
    print(i)   # 0, 5, 10, 15
```

**`break` and `continue` in for loops:**
```python
# Stop when we hit 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)   # 1, 2

# Skip 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)   # 1, 2, 4, 5
```

**`for...else`** — the `else` block runs only if the loop completes without `break`:
```python
numbers = [1, 3, 5, 7, 9]
target = 6

for n in numbers:
    if n == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found")   # runs because no break occurred
```
Use this instead of a `found` boolean flag in search loops.

**Nested loops:**
```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
```

---

### Lists

An **ordered, mutable (changeable) collection** that allows duplicates. Created with square brackets.

```python
fruits = ["apple", "orange", "banana", "coconut"]
```

**Accessing elements:**
```python
fruits[0]      # "apple"   — first element
fruits[-1]     # "coconut" — last element
fruits[1:3]    # ["orange", "banana"] — slice (end exclusive)
fruits[:2]     # ["apple", "orange"]
fruits[2:]     # ["banana", "coconut"]
```

**Modifying:**
```python
fruits[0] = "grape"          # change an element

fruits.append("mango")       # add to end
fruits.insert(1, "kiwi")     # insert at index 1
fruits.remove("banana")      # remove by value (first occurrence)
fruits.pop()                 # remove and return last element
fruits.pop(1)                # remove and return element at index 1
fruits.clear()               # remove all elements
```

**Querying:**
```python
fruits.index("apple")        # returns index of first "apple"
fruits.count("apple")        # count occurrences
len(fruits)                  # number of elements
"apple" in fruits            # True — membership check
```

**Sorting and ordering:**
```python
fruits.sort()                # sort in-place (alphabetical)
fruits.sort(reverse=True)    # sort descending
fruits.reverse()             # reverse in-place
sorted(fruits)               # returns new sorted list (original unchanged)
```

**Other:**
```python
fruits.copy()                # returns a shallow copy
fruits + ["fig"]             # concatenate lists
fruits * 2                   # ["apple", "apple"] — repeat
```

**Iterating:**
```python
for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

**2D lists (matrix):**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][0]   # 1 — row 0, column 0
matrix[1][2]   # 6 — row 1, column 2

# Iterate
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
```

---

### Tuples

An **ordered, immutable (unchangeable) collection**. Created with parentheses. Use when data should not be modified.

```python
coordinates = (10, 20)
rgb = (255, 128, 0)
single = (42,)          # single-element tuple — note the trailing comma!
```

**Accessing:**
```python
coordinates[0]    # 10
coordinates[1]    # 20
len(coordinates)  # 2
```

**Tuple unpacking:**
```python
x, y = (10, 20)      # x=10, y=20
r, g, b = (255, 0, 128)

# Swap variables
a, b = 1, 2
a, b = b, a    # a=2, b=1
```

**`*args` in functions** — variable positional arguments come in as a tuple:
```python
def add(*nums):
    total = 0
    for n in nums:
        total += n
    return total

add(1, 2)        # 3
add(1, 2, 3, 4)  # 10
```

---

### Sets

An **unordered collection with no duplicates**. Great for membership testing and removing duplicates. Created with curly braces.

```python
fruits = {"apple", "orange", "banana", "apple"}  # duplicate "apple" is removed
print(fruits)   # {"apple", "orange", "banana"} — order not guaranteed

# Empty set — must use set(), not {} (that creates an empty dict)
empty = set()
```

**Operations:**
```python
fruits.add("mango")             # add element
fruits.remove("banana")         # remove (KeyError if not found)
fruits.discard("banana")        # remove safely (no error if missing)
"apple" in fruits               # True — fast membership test
len(fruits)                     # number of elements
```

**Set math:**
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # {1, 2, 3, 4, 5, 6} — union
a & b    # {3, 4} — intersection
a - b    # {1, 2} — difference (in a but not b)
a ^ b    # {1, 2, 5, 6} — symmetric difference
```

---

### Dictionaries

An **ordered, mutable collection of key-value pairs** with no duplicate keys.

```python
capitals = {
    "USA": "Washington D.C.",
    "Philippines": "Manila",
    "Japan": "Tokyo"
}
```

**Accessing values:**
```python
capitals["USA"]                        # "Washington D.C." — KeyError if missing
capitals.get("Japan")                  # "Tokyo"
capitals.get("India", "Unknown")       # "Unknown" — default if key not found
```

**Modifying:**
```python
capitals["Germany"] = "Berlin"         # add new key-value pair
capitals.update({"China": "Beijing"})  # add or update
capitals.pop("Japan")                  # remove by key
capitals.popitem()                     # remove and return last inserted pair
capitals.clear()                       # remove all
```

**Iterating:**
```python
# Keys only
for country in capitals.keys():
    print(country)

# Values only
for city in capitals.values():
    print(city)

# Both key and value
for country, city in capitals.items():
    print(f"{country}: {city}")
```

**Check if key exists:**
```python
if capitals.get("France") is not None:
    print("France is in the dict")

# Or using 'in' on keys
if "France" in capitals:
    print("France is in the dict")
```

---

### Random Module

```python
import random

random.randint(1, 6)          # random integer between 1 and 6 (inclusive)
random.random()               # random float between 0.0 and 1.0
random.choice(["rock", "paper", "scissors"])   # random element from sequence
random.shuffle(my_list)       # shuffle list in-place
random.sample(my_list, 3)     # 3 random unique elements (returns new list)
```

---

### Functions

A **function** is a named, reusable block of code. Define with `def`, call with `()`.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Bro")      # Hello, Bro!
greet("Steve")    # Hello, Steve!
```

**Return values:**
```python
def add(x, y):
    return x + y

result = add(3, 4)   # result = 7
```

**Prefer return values over side effects** — functions that return values are composable and testable. Functions that only print are harder to reuse.

```python
# Less flexible (side effect only):
def display_area(w, h):
    print(w * h)

# More flexible (returns value):
def calculate_area(w, h):
    return w * h

area = calculate_area(5, 3)
print(f"Area: {area}")   # can be used elsewhere
```

**Default arguments** — used when the argument is omitted:
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Bro")              # Hello, Bro!
greet("Steve", "Hi")      # Hi, Steve!
```

**Keyword arguments** — pass by name, order doesn't matter:
```python
def create_user(name, age, job):
    print(f"{name}, age {age}, works as {job}")

create_user(age=25, job="developer", name="Bro")
```

**`*args` — variable positional arguments** (receives as tuple):
```python
def add(*nums):
    return sum(nums)

add(1, 2)           # 3
add(1, 2, 3, 4, 5)  # 15
```

**`**kwargs` — variable keyword arguments** (receives as dict):
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Bro", age=25, city="Metro Manila")
```

---

### Lambda Functions

**Anonymous, single-expression functions.** Best for short throwaway operations.

```python
# Syntax: lambda parameters: expression
double = lambda x: x * 2
add = lambda x, y: x + y

print(double(5))     # 10
print(add(3, 4))     # 7
```

**Most common use — as a sort key:**
```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# Sort by grade (second element of each tuple)
students.sort(key=lambda s: s[1])
print(students)   # [("Charlie", 78), ("Alice", 85), ("Bob", 92)]

# Sort descending
students.sort(key=lambda s: s[1], reverse=True)
```

---

### List Comprehensions

A compact way to create lists from existing iterables.

```python
# Standard syntax
[expression for item in iterable]

# With condition (filter)
[expression for item in iterable if condition]
```

**Examples:**
```python
squares = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

even = [x for x in range(1, 11) if x % 2 == 0]
# [2, 4, 6, 8, 10]

upper_names = [name.upper() for name in ["alice", "bob", "charlie"]]
# ["ALICE", "BOB", "CHARLIE"]

# Alternative to using random.choice 3 times:
symbols = ["🍒", "🍋", "🍉"]
row = [random.choice(symbols) for _ in range(3)]
# underscore _ = unused loop variable
```

---

### Modules

A **module** is a Python file containing reusable code. Import it with `import`.

```python
import math                     # import entire module
from math import sqrt, pi       # import specific names
import math as m                # alias
from random import *            # import everything (avoid in large projects)
```

**Commonly used built-in modules:**

| Module | Purpose | Key usage |
|--------|---------|-----------|
| `math` | Math functions | `math.sqrt()`, `math.pi` |
| `random` | Random numbers | `random.randint()`, `random.choice()` |
| `string` | String constants | `string.ascii_letters`, `string.digits`, `string.punctuation` |
| `os` | OS interaction | `os.path.exists()`, `os.getcwd()` |
| `sys` | System access | `sys.argv`, `sys.exit()` |
| `json` | JSON encoding/decoding | `json.dump()`, `json.load()` |
| `csv` | CSV files | `csv.writer()`, `csv.reader()` |
| `datetime` | Dates and times | `datetime.datetime.now()` |

**`if __name__ == "__main__":`**

Python sets `__name__` to `"__main__"` when a file is run directly. This pattern lets you have code that only runs when the file is executed directly (not when imported as a module):
```python
def main():
    print("Running main program")

if __name__ == "__main__":
    main()
```

---

### Exception Handling

**Exceptions** are runtime errors. Handle them with `try/except` to prevent program crashes.

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No errors occurred.")    # runs only if no exception
finally:
    print("This always runs.")      # cleanup code
```

**Common exception types:**

| Exception | Cause |
|-----------|-------|
| `ValueError` | Wrong value type (e.g., `int("abc")`) |
| `TypeError` | Wrong operation for type |
| `ZeroDivisionError` | Dividing by zero |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key not found |
| `FileNotFoundError` | File doesn't exist |
| `PermissionError` | No permission to access file |
| `AttributeError` | Object has no such attribute |

**Raising exceptions manually:**
```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

**Custom exceptions:**
```python
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough money!")
    return balance - amount
```

---

### File I/O

**Detecting files:**
```python
import os

path = "myfile.txt"
os.path.exists(path)    # True if path exists (file or folder)
os.path.isfile(path)    # True if it's a file
os.path.isdir(path)     # True if it's a directory
```

**Writing files** — always use `with` statement (auto-closes the file):
```python
# Write plain text
with open("output.txt", "w") as file:    # "w" = write (overwrites existing)
    file.write("Hello, World!")

# Append to existing file
with open("output.txt", "a") as file:   # "a" = append
    file.write("\nNew line added")

# Write mode "x" — creates file, errors if it already exists
with open("newfile.txt", "x") as file:
    file.write("Created fresh")

# Write a list line by line
employees = ["Spongebob", "Squidward", "Patrick"]
with open("employees.txt", "w") as file:
    for emp in employees:
        file.write(emp + "\n")
```

**Writing JSON:**
```python
import json

person = {"name": "Bro", "age": 25, "job": "Developer"}
with open("data.json", "w") as file:
    json.dump(person, file, indent=4)   # indent for readable formatting
```

**Writing CSV:**
```python
import csv

employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
]
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
```

**Reading files:**
```python
# Read plain text
try:
    with open("output.txt", "r") as file:
        content = file.read()          # entire file as one string
        # OR
        lines = file.readlines()       # list of lines
        # OR
        for line in file:              # iterate line by line (memory efficient)
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
```

**Reading JSON:**
```python
import json

with open("data.json", "r") as file:
    data = json.load(file)    # returns Python dict/list
print(data["name"])           # "Bro"
```

**Reading CSV:**
```python
import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)    # each row is a list
```

**File modes summary:**

| Mode | Meaning |
|------|---------|
| `"r"` | Read (default) |
| `"w"` | Write (overwrites existing) |
| `"a"` | Append |
| `"x"` | Create (error if exists) |
| `"rb"`, `"wb"` | Binary read/write |

---

### Object-Oriented Programming (OOP)

OOP organizes code into **classes** (blueprints) and **objects** (instances of a class).

#### Defining a Class

```python
class Car:
    # Class variable — shared by ALL instances
    count = 0

    # Constructor — called when creating an object
    def __init__(self, make, model, year):
        # Instance variables — unique to each object
        self.make = make
        self.model = model
        self.year = year
        Car.count += 1    # increment class variable

    # Instance method — operates on the object (self)
    def describe(self):
        print(f"{self.year} {self.make} {self.model}")

    def drive(self):
        print(f"You drive the {self.make}.")
```

**Creating objects:**
```python
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

car1.describe()    # 2020 Toyota Camry
car2.drive()       # You drive the Honda.
print(Car.count)   # 2 — class variable
```

#### Static Methods

No access to instance (`self`) or class (`cls`). Used for utility functions:
```python
class MathHelper:
    @staticmethod
    def add(x, y):
        return x + y

MathHelper.add(3, 4)   # 7
```

#### Class Methods

Access the class itself via `cls`. Used for factory methods or class-level operations:
```python
class Student:
    count = 0
    total_gpa = 0.0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"

s1 = Student("Alice", 3.8)
s2 = Student("Bob", 3.2)
print(Student.get_average_gpa())   # Average GPA: 3.50
```

#### Magic / Dunder Methods

Special methods called automatically by Python's built-in operations. All have double underscores.

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # Called when print(book) or str(book) is used
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        # Called for ==
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        # Called for <
        return self.pages < other.pages

    def __gt__(self, other):
        # Called for >
        return self.pages > other.pages

    def __add__(self, other):
        # Called for +
        return self.pages + other.pages

    def __contains__(self, keyword):
        # Called for 'in'
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        # Called for obj["key"]
        if key == "title": return self.title
        if key == "author": return self.author
        if key == "pages": return self.pages
        return f"Key '{key}' not found"

b1 = Book("The Hobbit", "Tolkien", 310)
b2 = Book("Harry Potter", "Rowling", 223)

print(b1)               # 'The Hobbit' by Tolkien
print(b1 == b2)         # False
print(b1 > b2)          # True (310 > 223)
print(b1 + b2)          # 533
print("Tolkien" in b1)  # True
print(b1["title"])      # The Hobbit
```

#### Property Decorator

Gives getter, setter, and deleter methods for attributes with additional logic:
```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width      # underscore = "private" convention
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"    # getter with formatting

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be > 0")

    @property
    def area(self):
        return self._width * self._height

rect = Rectangle(5, 3)
print(rect.width)    # "5.0cm"
rect.width = 10      # calls setter
rect.width = -1      # "Width must be > 0"
print(rect.area)     # 30
```

---

### Inheritance

A child class **inherits** all attributes and methods from its parent class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):              # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} says: Meow!")


dog = Dog("Rex")
dog.eat()    # Rex is eating.  — inherited from Animal
dog.bark()   # Rex says: Woof! — defined in Dog
```

#### `super()` Function

Calls the parent class's methods from within the child class:
```python
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        filled = "filled" if self.is_filled else "not filled"
        print(f"It is {self.color} and {filled}.")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)    # calls Shape.__init__
        self.radius = radius

    def describe(self):
        super().describe()           # extend parent's method
        area = 3.14 * self.radius ** 2
        print(f"Circle area: {area:.2f} cm²")


c = Circle("red", True, 5)
c.describe()
# It is red and filled.
# Circle area: 78.50 cm²
```

#### Multiple Inheritance

A child class inheriting from more than one parent:
```python
class Prey:
    def flee(self):
        print(f"{self.name} is fleeing!")

class Predator:
    def hunt(self):
        print(f"{self.name} is hunting!")

class Rabbit(Prey):     # only prey
    pass

class Hawk(Predator):   # only predator
    pass

class Fish(Prey, Predator):   # both!
    pass
```

#### Multi-level Inheritance

```python
class Animal:           # grandparent
    pass

class Mammal(Animal):   # parent
    pass

class Dog(Mammal):      # child — inherits from both Mammal and Animal
    pass
```

---

### Polymorphism

Objects of different classes responding to the same method name in their own way.

```python
class Shape:
    def area(self):
        pass    # to be overridden

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(shape.area())   # each calls its own version of area()
```

**Duck typing** — "if it walks like a duck and quacks like a duck, it's a duck." Python doesn't care about the class — only whether the object has the needed methods:
```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(duck):
    duck.quack()    # works on any object with a quack() method

make_it_quack(Duck())    # Quack!
make_it_quack(Person())  # I'm quacking like a duck!
```

---

### Multi-threading

Runs multiple functions **concurrently** (at the same time). Good for I/O-bound tasks (file reads, API calls).

```python
import threading
import time

def take_out_trash():
    time.sleep(2)
    print("You took out the trash.")

def get_mail():
    time.sleep(1)
    print("You got the mail.")

def walk_dog(name):
    time.sleep(3)
    print(f"You finished walking {name}.")

# Create threads
t1 = threading.Thread(target=take_out_trash)
t2 = threading.Thread(target=get_mail)
t3 = threading.Thread(target=walk_dog, args=("Scooby",))  # pass args as tuple

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all to finish before continuing
t1.join()
t2.join()
t3.join()

print("All chores complete!")
```

**Note:** Single-element tuples need a trailing comma: `args=("Scooby",)` — without the comma, Python treats it as just `"Scooby"` in parentheses, not a tuple.

---

### Working with APIs

APIs allow your program to fetch data from the internet. The `requests` library handles HTTP calls.

```bash
pip install requests
```

```python
import requests

BASE_URL = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{BASE_URL}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:       # 200 = OK
        data = response.json()            # parse JSON response → Python dict
        return data
    else:
        print(f"Failed. Status: {response.status_code}")
        return None

pokemon = get_pokemon("pikachu")
if pokemon:
    print(f"Name: {pokemon['name']}")
    print(f"ID:   {pokemon['id']}")
    print(f"Height: {pokemon['height']}")
```

**Common HTTP status codes:**
- `200` — OK (success)
- `201` — Created
- `400` — Bad Request
- `404` — Not Found
- `403` — Forbidden
- `500` — Internal Server Error

---

### PyQt5 — Graphical User Interface (GUI)

PyQt5 lets you build desktop apps with windows, buttons, labels, and more.

```bash
pip install PyQt5
```

**Boilerplate for a basic window:**
```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(700, 300, 500, 500)  # x, y, width, height
        self.initUI()

    def initUI(self):
        pass  # set up widgets here

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
```

**Common widgets:**

| Widget | Import | Use |
|--------|--------|-----|
| `QLabel` | `QLabel` | Display text or image |
| `QPushButton` | `QPushButton` | Clickable button |
| `QLineEdit` | `QLineEdit` | Text input box |
| `QCheckBox` | `QCheckBox` | Checkbox |
| `QRadioButton` | `QRadioButton` | Radio button (one-of-many) |
| `QButtonGroup` | `QButtonGroup` | Group radio buttons |

**Signals and slots** — the event system:
- **Signal**: an event (e.g., button clicked)
- **Slot**: a method called when the signal fires

```python
# Button example
from PyQt5.QtWidgets import QPushButton

self.button = QPushButton("Click Me", self)
self.button.clicked.connect(self.on_click)   # connect signal to slot

def on_click(self):
    self.button.setText("Clicked!")
    self.button.setDisabled(True)
```

**Applying styles with stylesheets (CSS-like):**
```python
self.setStyleSheet("QLabel { font-size: 30px; font-family: Arial; }")
self.label.setStyleSheet("font-size: 40px; color: red;")
```

---

### Key Projects in this Course

| Project | Concepts Used |
|---------|--------------|
| Mad Libs | `input()`, f-strings |
| Calculator | Conditionals, type casting |
| Weight/Temp Converter | Functions, conditionals |
| Number Guessing Game | `random.randint()`, while loop |
| Rock Paper Scissors | `random.choice()`, conditionals |
| Countdown Timer | for loop, `time.sleep()` |
| Concession Stand | Dictionaries, while loop |
| Dice Roller (ASCII) | Nested loops, dictionaries, tuples |
| Hangman | Lists, sets, functions, ASCII art |
| Slot Machine | Functions, lists, list comprehensions, random |
| Substitution Cipher | Strings, lists, `string` module, `random.shuffle()` |
| Number Guessing Game | Random, while loop, user input |
| Blackjack | OOP, lists, random |
| Pokémon API Lookup | `requests`, dictionaries, functions |
| Weather App | PyQt5, `requests`, API, GUI |

---

### Quick Reference — Built-in Functions

```python
len(x)         # length of string/list/tuple/dict/set
type(x)        # return type of x
print(x)       # output to console
input(prompt)  # read user input (returns string)
int(x)         # convert to integer
float(x)       # convert to float
str(x)         # convert to string
bool(x)        # convert to boolean
list(x)        # convert to list
tuple(x)       # convert to tuple
set(x)         # convert to set
dict(...)      # create dictionary
range(start, stop, step)   # range of numbers
enumerate(iterable)        # iterate with index
zip(a, b)      # pair elements from two iterables
sorted(x)      # return sorted version (original unchanged)
reversed(x)    # return reversed iterator
sum(x)         # sum all elements
max(x)         # maximum element
min(x)         # minimum element
abs(x)         # absolute value
round(x, n)    # round to n decimal places
help(x)        # show documentation
dir(x)         # list all attributes and methods
```

---

### What This Means for Your Work

This 12-hour course is the most comprehensive beginner Python reference in the knowledge base. It covers the full vocabulary of Python development — from variables to PyQt5 GUI — with 20+ hands-on projects.

**Stack applications:**
- **Django backends (e-Bangsamoro, Tarbiyyah-MS, OBCMS):** The OOP patterns (classes, inheritance, `__init__`, properties) map directly to Django models and serializers. The dunder methods (`__str__`, `__eq__`) are used throughout Django's ORM. The `@classmethod` and `@staticmethod` patterns match Django's custom managers.
- **`scripts/` utilities:** Apply "return values, not side effects" function design to make `generate_indexes.py`, `standardize_md.py`, and `apply_standardization.py` composable and testable. Use list comprehensions to replace manual `for` loops with `append()`.
- **Scrapers (BTA bills, laws, jurisprudence):** The `for...else` pattern replaces boolean `found` flags in search loops. `*args`/`**kwargs` make scraper functions more flexible. Exception handling (`FileNotFoundError`, `PermissionError`, `requests` errors) prevents scraper crashes.
- **File I/O:** The JSON/CSV read-write patterns are directly applicable to data export scripts and log file management across all projects.
- **API integration:** The `requests` + `.json()` + status code pattern is the foundation for the final Weather App project and applies to any REST API call in your Django backends.

### How This Can Improve Your Claude Skills and Workflows

- **`/scrape` skill:** The multi-threading section (`threading.Thread`, `start()`, `join()`) suggests adding a parallel scraping mode — run multiple URL fetches concurrently using threads to speed up the BTA bills and national laws scrapers.
- **`/fact-checker`:** The file I/O patterns (read/write JSON) could be used to build a persistent error log that tracks fact-check failures across sessions and updates a running `errors.json` file.
- **`/legal-researcher`:** The API integration pattern (`requests.get()` + `.json()`) is the underlying mechanism for any web-fetching in the research pipeline — understanding it helps you debug and extend the skill.
- **New skill opportunity — `/python-tutor`:** A skill that generates Python practice exercises from a topic (e.g., "give me 5 exercises on list comprehensions") would use this course as its knowledge base. Not yet in `~/Vault/Claude-Skills/index.md`.
- **e-Bangsamoro:** The PyQt5 section covers signal-slot architecture, which is analogous to React's event handling — the mental model transfers. Understanding widget geometry and stylesheet CSS helps when debugging PyQt5-to-web migrations.
---

## Transcript

[00:00] What's up everybody? In this video, I'm going to teach you everything you need to know to start coding with Python. I've also included 20 different hands-on projects to help you learn. You can find

[00:10] the entire list in the description of this video. Our final project will be a weather app that fetches real-time weather data from an API. Even if you've never coded anything in your life before, I'll walk you through the basics, the ABCs of programming. If that

[00:25] sounds good to you, then I encourage you to sit back, relax, and enjoy the show. This course doesn't cost you anything, but if you would like to help me out, you can help increase its reach by hitting the like button, leave a random comment down below, and subscribe if you'd like to be a fellow bro. Thank you. I appreciate it. I don't like

[00:47] boring introductions, so I say we just jump right in. There's two things we'll need to download. The first is a Python interpreter to convert our written code to machine code. We're going to head to

[01:00] python.org, go to downloads, and download the latest version. We will open this executable. If you're on Windows, you'll

[01:12] want to check this check box, add Python exe to path, and we will install now. The setup was successful. And that's all you need to do to download the Python interpreter. The second download we'll

[01:30] need is an IDE, an integrated development environment. Basically, a place where we can write code. For IDEES, there's two popular choices when writing Python code. PyCharm and VS

[01:43] Code. If you already use VS Code, you can stick with that. Just be sure to download the Python extension. I find

[01:50] PyCharm more beginner friendly if you've never coded before. If you would like to use PyCharm, go to jetbrains.com/pycharm. And we will click

[02:01] this green download button. There's two versions of PyCharm, the professional version and the community version. The professional version is paid for. I would not

[02:12] recommend using it only because there's plenty of free IDE on the market. We'll use the community edition, the free one, because I don't like to pay for things and I'm sure you don't either. Select the correct download for your operating system. I'm running Windows. I will

[02:27] download PyCharm. We will open this executable. Click next. You could select

[02:37] a destination folder. I'll keep it as is. Next, I'll create a desktop shortcut, but you don't necessarily need to. Click

[02:48] next. Install. And we'll just have to give it a moment. Okay, the setup is now complete.

[02:57] I'll check this checkbox to run PyCharm when we close this window. After opening PyCharm, we're going to create a new project. You can rename your Python project. I'll keep it as is. You can

[03:11] select a location. Again, I won't change that. You can create a sample welcome script, but for this tutorial, we won't.

[03:19] Let's select the latest Python version and create our new project. In the menu to the left, we're going to create a new Python file. File, new, Python file. Let's name this file main.

[03:38] But really you can name it anything and select Python file. Python files end with the py file extension. We should have our main Python file within our Python project folder. Now we're going to print

[03:55] something to the console window. Within our main Python file, we're going to write a print statement. So type print add a set of parenthesis. Between the

[04:06] set of parenthesis, we will add a set of double quotes to print something or single quotes. Either one. My own preference is double quotes. Normally in

[04:17] a programming tutorial, the instructor would tell you to print something such as hello world, but we like to be different here. Instead, think of your favorite food. In this case, I like pizza. I will

[04:30] print I like pizza. To run our Python program, we will click the screen arrow to run our main Python file. We should have a console window that displays our output. I like pizza

[04:48] or whatever your favorite food is. Let's print another line of code. Let's print it's really good. By adding a second print

[05:03] statement, we are printing a second line of code. Now we'll discuss comments. The Python interpreter doesn't output comments. To write a comment, you

[05:16] use a pound sign. I like to call this a hashtag. My comment will be this is my first Python program. Comments are used as notes for

[05:28] yourself or for other people reading this code. If I were to run this code again, this comment is not displayed to the output. We still have I like pizza.

[05:39] It's really good. All right, everybody. So, that is your very first Python program. And in the next topic, we'll

[05:45] discuss variables. All right, everybody. We are moving on to variables. A variable is a container

[05:54] for a value. There's four different data types. We'll discuss strings, integers, floats, and booleans. Yes, I know that's

[06:01] a silly name. A variable behaves as if it was the value it contains. Each variable should have a unique name.

[06:09] Let's say we have a variable of first name. To assign a variable, you use the assignment operator of equals. For text, a string is a series of text. This can

[06:20] be double quotes or single quotes. My own preference is double quotes. Why don't you type in your first name? This

[06:29] variable of first name will behave as if it was this value, this series of characters. So to demonstrate this, I'm going to print my first name variable. So place it within a print statement without quotes. That will

[06:46] print your first name. Now, you don't want this within quotes because then you're literally printing the word first name. You could use your variable along with some text by using what is called an F string. That's the easiest way to

[07:04] display a variable. So, you type F then a set of quotes. The F means format. So, let's say the word hello.

[07:14] Then we will add our variable. We will insert our variable into this text when using an F string. To do that, you need a set of curly braces. Then insert your

[07:24] variable. So the result is hello, whatever your first name is. In my case, bro. Let's create another

[07:33] variable. Let's say we have a variable of food. Food equals think of your favorite food. For me, I will type

[07:42] pizza. Let's print the following. You like add a placeholder.

[07:50] Again, I'm using an F string. Our variable of food. Hello, bro. You like

[07:58] pizza. Let's create an email. Use your own email or make up one. Let's say my email is

[08:05] bro123@fake.com. Then let's print our email. Your email is add a placeholder.

[08:19] Display our email variable. Your email is bro123@fake.com. So these are strings.

[08:30] I'm going to add a comment that these are strings. A string is a series of characters. They can include numbers but we treat them as characters. Now we have

[08:42] integers. An integer is a whole number. An example of this could be somebody's age. How old are they? According to my

[08:50] YouTube statistics, many of you are between the ages of 18 through 24. Let's say that I'm 25. Let me zoom in a little. Your

[08:59] integer should not be within quotes because it would be a string. Then technically if I would like to work with this variable again I'll use an f string. Let's say you are add a placeholder display our age variable years old. You are 25 years old.

[09:23] Another example of an integer could be a quantity. You are buying a certain amount of something. Maybe I am buying three items. I wouldn't have half an

[09:34] item. This would be a float technically rather than an integer. We are buying three of something. So let's print the

[09:43] following. You are buying. Add a placeholder.

[09:49] display our quantity items. You are 25 years old. You are buying three items. Another example of an integer

[10:01] could be an amount of people. Let's say num of students like a classroom. There are 30 students in our class.

[10:12] Then we will print your class has add a placeholder students. We will display the number of students. Num of students. Your class has 30

[10:30] students. Those are integers. They're whole numbers. And again, make sure

[10:34] they're not within quotes because then technically they would be a string. integers we can use in arithmetic expressions. If they were strings, we couldn't. Then we have floats. Float

[10:48] means floatingoint number. A float is a number, but it contains a decimal portion. An example would be a price. What is the price of

[10:58] something? $10.99. Let's print our price. Print.

[11:03] I'll use an F string. The price is add a placeholder. display our price. The price is

[11:12] $10.99. Let's preede our placeholder with a unit of currency. I'll pick

[11:17] American dollars, but feel free to pick something else. The price is $10.99. So, floats contain a decimal

[11:25] portion. What about a grade point average GPA? Let's say my GPA is 3.2.

[11:36] Then I will print your GPA is display our GPA. Your GPA is 3.2. What about a distance? A distance

[11:53] can contain a decimal portion. 5.5 kilometers maybe.

[12:01] Then I will print you ran. Add a placeholder. Display our distance. Then I'll add km

[12:09] for kilometers. Or you could add mi for miles, but I'll stick with kilome. You rand 5.5

[12:19] km. Okay. Then we have booleans. A

[12:22] boolean is either true or false. Let's say we're a student. is student equals. If we are a student, we

[12:34] could say that this is true. True starts with a capital T. If we weren't a student, let's say we graduate, we could say that this is false. Again, the first

[12:45] letter is capital. Booleans only have two options, true or false. So, let's say that I am a student. Then I will

[12:55] print are you a student? Then we will display our boolean value of is student. Are you a student? That is

[13:07] true. With boolean values, we really don't output them directly. You're more likely to see them used internally within a program, such as when working with if statements. This is a topic

[13:18] we'll discuss in the future, so don't worry. You may see if is student. If this variable is true, then we will print the following. Now, we don't need to use an

[13:31] string. We're not going to insert any variables. You are a student. If this

[13:37] were false, we can add an else clause where we will print you are not a student. Our variable of is student is true. We will print the if statement.

[13:53] You are a student. If this were false, we will print whatever is within else. You are not a student. Let's think

[14:02] of a few more examples. Is something for sale like a car or a product of some sort? Let's say that is true. I'll write another if

[14:13] statement. If for sale, if this variable contains true, we will do the following. Let's print that item is for sale. Else if it's false, we will print

[14:30] something else. That item is not available. For sale is set to true. This variable is true. We will

[14:44] print that item is for sale. else if it were false we print that item is not available. One more example. Let's say we have a

[14:55] boolean variable of is online. Is somebody online? I will set that to true. If is online. If that's true, we

[15:07] will print you are online. Else we will print you are offline. Is online is set to true. We

[15:19] will print you are online. else if it were false we print you're offline. All right everybody so those are variables. A variable is a reusable

[15:31] container for a value. There's four basic data types for beginners. A string which is a series of text, integers which are whole numbers, floats which are numbers but they contain a decimal portion and booleans which are either true or false. They're binary. Your

[15:50] assignment in the comment section is to post four variables. Post a string, an integer, a float, and a boolean. Try and think of a unique example if you can.

[16:00] And well everybody, those are variables in Python. All right everybody, so we are moving on to type casting. Typ casting is the process of converting a variable from one data type to another. We have

[16:15] various functions to convert a value or variable to a string, an integer, a float or a boolean. Let's create some variables. We will create a name variable. Type in your full

[16:29] name, an age, make up some age, a GPA for grade point average, let's say minus 3.2, and a boolean of is student. Are we currently a student? Let's say that's

[16:46] true. Now, you actually could get the data type of a variable or a value by using the type function. Then pass in a value or variable. However, when I run

[16:57] this, there's no output. So, I need a print statement. We will print what is returned by the type function. Get the

[17:07] type of our name variable, then print it. So our name variable is a string str. Our age variable is an integer and int GPA is a float is student is a boolean. Using

[17:29] these type cast functions we can convert from one data type to another. Here's how. Let's start with something simple.

[17:36] Let's convert our GPA to an integer. Currently, it's a float. I will reassign GPA. Use the int function to type cast

[17:46] to an integer. Then pass in my GPA. At the end, we will print our GPA. If we type cast 3.2 to a whole

[17:57] integer, what would the result be? A whole integer of three. We truncate the decimal portion. Let's convert our age to a

[18:07] floatingoint number. We will reassign our variable of age. Use the type cast function a float.

[18:15] Then insert our age variable. Let's print our age variable. And it should be a floating point number 25.0. Now we'll cover strings. Let's

[18:30] type cast our age to be a string. age equals call the type cast function of string str pass in our age variable. So the result is still going to appear the same 25. However, it's a string not an

[18:51] integer. And to prove that I will enclose my age variable with the type function. The type of variable age is a string.

[19:01] It would be the same as if we're taking this number and enclosing it within quotes. So this would make a difference because let's say that I add one to age. Age plus equals 1. Well, we would get a type error. Can

[19:18] only concatenate strings, not integers to a string. However, if I were to add a string of one to the end, we would be using string concatenation. So let's say it's my birthday and I add 1 to 25.

[19:33] Well, since we're working with strings now, the result would be 251. I am 251 years old. So strings and numbers behave differently. With numbers, we can use

[19:47] them within arithmetic expressions. Strings, not so much. We will take our name variable and type cast it to a boolean.

[19:58] name equals call the typcast function of bool pass in our name variable. This has an interesting result. So I'm going to print name.

[20:09] Booleans are either true or false. If I type cast my string of text into a boolean that gives me true. Now it really doesn't matter what I write here. If I were to change my

[20:23] name to a single character such as B, this would still be true. If our string variable was empty, there were no characters within it, that would actually give us false. We could use this to check to see if somebody enters in their name or not.

[20:39] If somebody types in their name, then we type cast it to a boolean. If somebody skips entering in their name, that would return false. We could reprompt the user to enter in their name again. All right,

[20:52] everybody. So, that is type casting. It is the process of converting a variable from one data type to another. This is

[20:59] especially useful with handling user input because user input is always a string. There may be at times where we want to convert it to an integer, a float or a boolean. And well everybody that is type casting in Python. All right everybody, in this

[21:16] topic I'm going to show you how we can accept user input in Python. We use the input function. It's a function that prompts the user to enter in data and it returns the enter data as a string.

[21:28] Here's an example. To accept user input, we will call the input function. When I run this program, we need to enter in data to our console window like so, then hit enter. However,

[21:42] we need a prompt. We need to tell the user what we want them to type in. So, let's ask a question. Our prompt will be within

[21:51] quotes. Let's say, "What is your name?" Let's try this again. What is

[21:59] your name? I can type in something. Why don't you go ahead and type in your full name, then hit enter. Now, with this input, we're not

[22:09] quite doing anything with it. The input function is going to return some data as a string. We can assign it to a variable if we would like. Let's create a

[22:18] variable of name. Name equals our user input. Then once we have our name, let's print a message. I'll use an fstring. We

[22:30] will print hello. Add a placeholder. Then insert our name variable within that placeholder. Let's try

[22:38] this. What is your name? Type in your name. Hit enter. Hello. Whatever your

[22:45] name is. Let's try a different name. I will pick Spongebob. Many people are

[22:50] familiar with Spongebob. Hello, Spongebob. This time we will ask a user how old they are. Let's assign a

[22:59] variable of age equals accept some user input. We need a prompt within quotes. How old are you?

[23:10] Once we have our age variable, let's print I'll use an f string. You are add a placeholder our variable age years old. What is your name? Type in your

[23:28] name. How old are you? Let's say that I'm 25. Hello. Whatever your name is, you

[23:36] are whatever your age is. Years old. All right. So, let's say that it's our

[23:42] birthday. Before we print our age variable, let's say happy birthday. Since I'm not inserting any variables within this print statement, this doesn't need to be an F string.

[23:58] You'll want to use an F string if you want to insert variables. Before we display the user's age, let's take the user's age and increase it by one. We could say age equals age + one. But there's one problem with

[24:14] this. Type in a name. How old are you? Type in an

[24:20] age. And we have a problem. We have a type error. Can only concatenate

[24:26] strings, not integers, to strings. When we accept user input, we store that input as a string. Before we increment our age by one, we'll need to convert it to an integer. We can't

[24:39] normally use strings within arithmetic expressions. But we can do that with integers and floats, though. After we accept some user input for our age variable, we could take our age variable and type cast it as an integer, which we talked about in the previous lesson. So

[24:58] let's say age equals our age after we type cast it then increment it by one. So type in your name type in an age and we get this message hello your name happy birthday you are whatever your age is years old. So strings we can't normally use with arithmetic expressions. We would

[25:24] have to type cast it to an integer or a float. However, we could condense some of these steps. We're taking up an extra line to type cast our age as an integer.

[25:35] What we could do instead is that when we accept your user input, we can enclose the input function within a type cast to int. And that would work the same. Type in your name, type in an age, and this works the same. And it takes less lines of code

[25:55] and is more readable. I would say when we accept user input, it returns that input as a string data type. Then we just have to type cast it to another data type if we need to. And in this

[26:06] case for age, we do. Now, we'll go over a couple exercises because it's important to practice what you've learned. In this first exercise, we're going to calculate the area of a rectangle. We need to prompt the user to

[26:20] enter in a length and the width of a rectangle. So we will create a variable of length. We will accept some user input using the input function. What is our prompt?

[26:32] Let's say enter the length. Let's do this with width. I'll just copy and paste what we have. Width

[26:42] equals enter the width. So we have the length and the width. To get the area of a rectangle, we have to multiply the length by the width. So let's say area equals our

[26:56] length variable. Now to use multiplication you use an asterisk. We'll discuss different arithmetic operators in the next lesson. So we have

[27:04] length time width. That is the area. I'm going to print our area because I need to test something. Enter

[27:15] the length. Let's say five 5 in 5 cm. Doesn't matter. Enter the width. six, we

[27:23] get a type error. Can't multiply sequence by non-int non- integer of type string. When we accept user input, it returns a value of the string data type.

[27:34] We can't use those strings in arithmetic expressions. We're multiplying the length times the width. We would need to type cast them as an integer or a float.

[27:44] Since we're working with basic geometry such as calculating the area, let's do float. So let's type cast our user input as a float for both length and width. Okay, let's try this again. Let's

[28:03] say 5 * 6. The area that's returned to us is 30. 30.0. This result contains a decimal.

[28:11] It's a floating point number, a float. So when we print the area, I'll use an f string this time. The area is I'll add a placeholder. Display our area

[28:25] variable. Let's add a unit of measurement afterwards. I'll pick centimeters. Now, since we're working

[28:31] with areas, if we would like to technically be accurate. So, we could say to the power of two or we could add a superscript. So, if you would like superscript 2 and you're on Windows, make sure num lock is on, hold alt, then type on the numpad 0178. So, we have a superscript of two.

[28:53] Again, it's not really necessary for this lesson. I just think it'd be cool to include it because then it's technically accurate. All right, let's say that the length is 6.1 and the width is 7.2.

[29:08] The area is 43.92 cm squared because we're working with areas. Let's cover a second exercise. This time we will create a

[29:19] shopping cart program. Exercise two, we're going to create a shopping cart program. We need three variables. An

[29:26] item, a price, and a quantity of those items. We will create a variable of item. We will accept some user input.

[29:37] What item would you like to buy? What are we trying to purchase? We'll keep the data type of the user input as a string. Then we need a price. What is

[29:51] the price of each item we're buying? Use the input function. What is the price? A price should be a floatingoint

[30:03] number. For example, we might have dollars and cents. We need a decimal. So

[30:08] let's type cast our input as a float. Then a quantity. We will accept some user input. Our prompt will be how

[30:21] many would you like? Quantities. They should be whole numbers. Let's type cast our input as an

[30:32] integer. Then we will have a total. What's the total that we have to pay?

[30:38] So, let's take the price of each item. Use an asterisk for multiply our quantity. Then, let's do a test run.

[30:48] Let's print our total. What item would you like to buy? Let's say a pizza. What is the price?

[30:57] $10.99. How many would you like? I would

[31:00] like five pizzas. and our total is 54.95. Let's say that before we display

[31:09] the total, let's print the following. I'll use an F string. You have bought insert a placeholder. Display our

[31:20] quantity X item or items. I'll add slash S. Then we will print I'll use an F string again.

[31:33] Your total is display our total. What item would you like to buy? I would like to buy a pizza. What is the

[31:45] price? $10.99. How many would you like? I would

[31:49] like nine pizzas. They're all for me. I'm going to eat all of them. You have bought 9 x pizzas. Your

[31:58] total is 98.91. Let's add a unit of currency before this. Pick unit of currency before

[32:05] displaying the total. I'll pick American dollars. I would like to buy pizza. What

[32:12] is the price? $9.99. How many would you like? I would

[32:18] like a dozen pizzas. 12. You have bought 12 x pizzas. Your

[32:25] total is $119.88. All right, everybody. That is

[32:30] how to accept user input in Python. And we've covered a few exercises. In the next topic, we're going to create a Mad Libs game. And that is how to accept

[32:39] user input in Python. All right, everybody. In this video, we're going to create a game of Mad Libs. Not because we have to, but

[32:47] because I want to. It would be a good exercise for us, just so we're more comfortable with accepting user input. If you're not familiar with Mad Libs, Mad Libs is a word game where you create a story by filling in the blanks with random words. So, we're going to create

[33:02] a story template. The story is going to be missing some components. We will fill in those components with random words that we type in. Here's a story that

[33:11] I've written myself. Print. Use an F string. Today, I went to a insert a

[33:20] placeholder zoo. For our placeholder, we'll insert an adjective. We'll insert a variable named adjective. Adjective. Adjective one.

[33:32] You're going to get an English lesson today, too. An adjective is a description of something. So, for our zoo, adjective one could be expensive, large, dirty. An adjective describe

[33:48] something. We'll fill this in when we accept user input. For our second print statement, let's print the following. In an

[33:59] exhibit, I saw a placeholder. We'll include a noun. Noun one. A noun is a

[34:09] person, place, or thing in English. Maybe a gorilla. A gorilla named Harambe, for example. Print. Use an F string. Let's

[34:20] say our noun one whatever this is we can reuse variables was we will create a second adjective adjective 2 we will be describing whatever noun one is this person place or thing and we will insert a verb verb one a verb is an action such as running or eating. Then for our last statement, let's print I was add a placeholder. We'll create adjective three. Adjective 3 will describe us. Now

[35:16] I'm going to add a reminder that an adjective is a description of something. Then we need noun one. Noun one equals input. Enter a noun. A noun is a person,

[35:35] place, or thing. Then we have adjective two. I'll just copy adjective one. Paste it.

[35:44] Change one to two. Then a verb. Verb one equals input. Enter a verb. I want verb one to

[35:55] be in current tense. I'll ask the user to end the verb with ing. Enter a verb ending with ing. Then it's current tense. our

[36:09] person, place, or thing of noun one is currently doing something such as eating. And then adjective three. And I'll just copy one of these adjectives. Adjective 3 equals input.

[36:23] Enter an adjective. Okay. And then we are ready to run this. Enter an

[36:28] adjective. An adjective describes something. I will say suspicious or some kids like to say sussy or sus even. I've also heard of

[36:40] kids nowadays using the word skipy. Feel free to type in whatever you would like. It is your story after all. I'm going to

[36:48] say suspicious. Enter a noun, a person, place, or thing. I like to poke fun at Mark Zuckerberg. So, I'm going to say my

[36:58] person is Mark Zuckerberg. Enter an adjective. That is a description.

[37:07] Angry. Enter a verb ending with ing. So, it's current tense. Uh,

[37:15] screeching. Enter an adjective. Happy. Here's my story. Today I went to

[37:23] a suspicious zoo in an exhibit. I saw a Mark Zuckerberg. Mark Zuckerberg was angry and screeching. I was happy. That's our

[37:35] game of Mad Libs. It's a word game where you create a story by filling in the blanks with random words. Also, post the output of your Mad Libs game in the comment section down below because I really want to read them. I want to see

[37:48] what you guys came up with. And well everybody, that is a Mad Libs game using Python. Hey everybody, in this video I'm going to show you all of the different math that we'll need throughout the rest of the series. I have a lot to cover and

[38:03] I'll split this video into different sections. We'll cover some basic arithmetic operators, built-in math functions, a few functions from the math module, and then a few exercises. Be sure to look at the timestamps if you would like to skip ahead to another section. Let's begin with some really

[38:19] easy stuff. We're going to cover some basic arithmetic operators. Let's say we have a variable friends. Currently, you have zero

[38:29] friends. If you need to increment a variable by one, you could say friends, the name of the variable equals the name of the variable again + 1. So, the plus sign is the addition operator. And I

[38:43] think we do have a little bit of experience with that already. So if I were to print my variable friends, guess what? You now have one friend. We could also shorten this line

[38:54] of code. You could say friends plus equals 1. That would do the same thing. This is

[39:03] known as an augmented assignment operator. That will give you the same result. I prefer to use augmented assignment operators just because they take less text and I think they're easier to read. Now let's use

[39:16] subtraction. Friends equals friends minus 2. So of course minus is the subtraction operator. Uh you have -2

[39:26] friends. I guess if you were to use the augmented assignment operator that would be friends minus equals 2. There you still have -2 friends.

[39:38] Okay. Multiplication. Let's change friends to how about five. Friends equals

[39:46] friends time 3. You now have 15 friends. Then the augmented assignment operator version of this would be friends time= 3. So again you have 15 friends. Let's

[40:05] cover division. Friends equals friends divided by two. So we have 2.5 friends. Somebody

[40:18] was cut in half. We have half a friend. Maybe it's just their legs or torso or something. Then the augmented assignment

[40:24] operator would be friends / equals 2. And the result is still the same. Now exponents friends equals friends to the power of two. So friends is

[40:42] currently five. Friends to the power of two would be 5 * 5 which is 25. The augmented assignment operator version of this equation would be friends exponent equals 2 and again friends is 25. Then we have modulus. Modulus gives

[41:06] you the remainder of any division. Suppose we have 10 friends instead of five. I will assign a new variable remainder. Remainder equals friends. The

[41:18] percent sign is known as the modulus operator. It will give us the remainder of any division. If I were to divide my group of friends by three, we will have one remaining. I'll store the remainder

[41:30] within a separate variable. We would have a remainder of one. It's kind of like in class when the teacher says for everybody in the class to go into groups of three, then there's always that one kid that's by themselves. That's kind of

[41:41] the same concept. We're dividing our friends into groups of three. then the modulus will give you the remainder. If

[41:48] we divided our group of friends into groups of two, well 10 divides by two evenly, so there is no remainder. So that is the modulus operator. It's fairly popular to use this operator to find if a number is even or odd because it will divide by two evenly if that number is even. If the remainder is one,

[42:06] that means that the original number is odd. Okay, so yeah, those are some basic arithmetic operators. addition, subtraction, multiplication, division, exponentiation, then modulus. Now what we're going to do is

[42:20] cover some built-in math related functions. Suppose we have three variables x= 3.14, y = 4, z = 5. It doesn't matter if these are

[42:34] floating point numbers or whole integers. The first is the round function. We have a variable named result. I'm going to round

[42:44] x. So there is a built-in round function. After the set of parenthesis, we can add some value or variable to be rounded. So we will round x to the

[42:55] nearest whole integer. Then print the result. So our result is three. So

[43:03] that's the round function. With the absolute value function, we can find the absolute value of a number. Uh let's change y to be -4 instead of four. We'll take result equals abs which

[43:19] means absolute value of y. The absolute value is the distance away from zero as a whole number. The absolute value of -4 is 4. Let's change y back to

[43:36] four. There's a built-in power function. result equals pow. Then we'll need a base and an

[43:46] exponent. What's y to the power of 3? That would be 4 * 4 * 4, which is 64.

[43:56] That's the power function. You can raise a base to a given power. The next two are really useful.

[44:04] Using the max function, we can find the maximum value of various values. What's the maximum value between x, y, and z? Then I'll just need to store this value.

[44:17] Uh results equals the max between x, y, and z. Well, the maximum value is five. Otherwise, there's min. What's the minimum value between X,

[44:34] Y, and Z? That would be 3.14. Now, in this next section, we do

[44:40] have some very useful constants and functions from the math class, but we'll need to import the math module at the top of our text editor. So, import math. If you need the value of pi, you'll type the name of the math module.py. And I'm just going to print

[44:59] this. print math.py. The value of pi is

[45:06] 3.14159 and a bunch of digits that come after. If you're working with physics, I do know that people use the constant e a lot. We won't be using e in this video

[45:17] series, but if you ever need access to it, just type math. E, and that will give you e, which is 2.71 something something something. I believe e is

[45:27] known as the exponential constant. If you need the square root of a number, let's say result equals math. SQRT, we can place a variable or a value within the square root function. Uh

[45:43] let's say we have x again. x= 9. What is the square root of x? Then

[45:51] I will print whatever the result is. The square root of 9 is three. That is the square root function. There's a ceiling function.

[46:04] Result equals math dot seal. Seal will always round a floatingoint number up. Suppose x is 9.1. So 9.1 rounded up is

[46:20] 10. Otherwise there's floor which will always round a number down. result equals math.f floor. Let's change x to

[46:32] 9.9. 9.9 rounded down is 9. Those are

[46:37] some useful math functions. Let's go over some exercises. Okay, this first exercise we are going to calculate the circumference of a circle. We'll need the help of the

[46:47] math module because there's some good functions in there. To calculate the circumference of a circle, the formula is 2 * * r. Let's ask a user for a radius because that's what r is. We'll

[47:02] accept some user input. Enter the radius of a circle. We will type cast the input as a floatingoint number to calculate the circumference.

[47:21] Again the equation is 2 * pi. We can get that from the math module times whatever the radius is. And the user is going to type that in. Then we will print

[47:34] whatever the circumference is. Print. We'll use an fstring the circumference is our variable circumference.

[47:48] Enter the radius of a circle. I'll enter 10, actually 10.5. Their circumference is

[47:57] 65.97. If you want to round and truncate some of these numbers, we can use the round function. Round

[48:04] circumference, then round to a given decimal place. I'll round to two digits. Again, 10.5 rounded is

[48:14] 65.97. You could add a unit of measurement, too. Let's say centimeters

[48:19] 10.5 is 65.97 cm. All right, that is the first

[48:25] exercise. For this next exercise, let's calculate the area of a circle. We'll import the math module. We'll ask for a radius. Much

[48:35] like before, radius equals input. Enter the radius of a circle. We'll cast our input as a floatingoint number. The equation for the area of a

[48:53] circle is pi time radius squared. We could easily use the built-in power function to raise our radius to the power of two. Then we will display the area. print. I'm using

[49:10] an F string. The area of the circle is our area to some unit of measurement. Let's say centime squared. Enter the radius of a circle

[49:29] 10.5. The area of the circle is 346.36. But I would like to round this

[49:35] number to two decimal places. I'll use that round function and I'll place area and the number of digits to round to within this function. Let's try that again.

[49:48] 10.5. The area of the circle is 346.36 cm squared. That is the second

[49:56] exercise. For this last program, we're going to find the hypotenuse of a right triangle. The formula to calculate the hypotenuse of a right angle triangle is C equ= the square of A^2 + B^2.

[50:12] We'll begin by importing the math module. We'll ask the user for the lengths of side A and B. A equals input. Enter side

[50:27] A. We'll cast the input as a floatingoint number. We'll do the same thing with side B.

[50:37] B equals enter side B. Now this part's going to be confusing. We'll calculate C. We'll need

[50:48] A^2 + B ^ 2. We'll take A to the^ of 2 plus B to the^ of 2. Then we'll need the square root of all of this. Whatever the result is, I

[51:05] will surround this equation with math. Square root and that should give us our answer. Let's print using an F string. Side C

[51:22] equals whatever C is. So, enter side A three. Side B will be four. side C is five. All right,

[51:33] everybody. So, that was everything related to some arithmetic operators and math related functions in Python. And in the next video, we're going to cover a few things involving string [Music] formatting. Hey everybody, in this topic

[51:48] I'm going to explain if statements. An if statement is used to do some code only if some condition we set is true. Else we could do something else. It's a

[51:58] basic form of decision-m. If it's true, we do something. If it's not true, we don't do it. Let's ask a user for their

[52:05] age. Age equals input. Enter your age. I will type cast

[52:13] the input as an integer. Depending on what the user's age is, we can do one of a few things. Let's pretend that the user would like to sign up for a credit card, but in order to do so, their age needs to be greater than or equal to 18. Well, we

[52:29] can check that. To use an if statement, type if, then some condition. What would we like to check? Let's check to see if

[52:37] the user's age is greater than or equal to 18. Then add a colon, then hit enter. Any code underneath the if statement should be indented. Make sure to pay

[52:49] attention to that because that's easy to miss. If the user's age is greater than or equal to 18, let's print you are now signed up. If I were to run this code, I'll type in my age. I'll type 21. Hit enter.

[53:07] This statement is true. Therefore, we will execute any code found within the if statement. You are now signed up.

[53:14] What if this condition was not true? Let's say my age is 13. Well, nothing happens. If the condition we

[53:22] check is instead false, we skip over this code. If you need to take a different course of action, you could add an else statement. If this is true, do this.

[53:35] Else, we can do something else. Let's print a different message. You must be 18 plus to sign up. I'll type in my age again. I'll say

[53:49] that I'm 13. Hit enter. You must be 18 plus to sign up. That's basically an if

[53:55] statement. Do some code only if some condition is true. Else you can do something else entirely. It's a basic

[54:04] form of decisionm. The else statement is kind of like a last resort. We can check more than one condition before reaching the else statement. We can add an else

[54:14] if statement which we just shortened to e l i if meaning else if. else if let's check if age is less than zero then we'll print a different message you haven't been born yet. Now if I run this code I'll say that my age is negative one.

[54:41] This condition is false. We skip this code. This condition is true. Therefore,

[54:47] we will execute this code and we skip the else statement. You haven't been born yet. Let's add another else if statement. You can add as many else if

[54:56] statements as you want. Let's check to see if somebody's age is greater than or equal to 100. We'll print a different message.

[55:05] Let's print you are too old to sign up. If I were to say my age is 111 years old, well, it states you are now signed up. The reason that we didn't reach this part of our else if statement. That's

[55:24] because this condition is still technically true. You do need to pay attention to your order of if and else if statements. If I want to be sure that nobody over 100 is signing up, I should probably move this to the beginning. If age is greater than or

[55:42] equal to 100, then else if age is greater than or equal to 18, we'll do something else. Enter your age. I am 111 years old. You are too old to sign up. So

[55:56] those are if statements. If some condition is true, do something. else if you can check something else. If no

[56:04] above conditions are true, you could do something else entirely. It's kind of like the default. Here's another example. We'll ask a user if they would

[56:12] like some food. Response equals input. Would you like food? We'll have the user type in Y for

[56:25] yes or N for no. If our response now to check to see if two values are equal, you would use double equals. If the response is equal to y, then we will print have some food. The doubles equal sign is the

[56:52] comparison operator. It will check to see if two values are equal. You don't want one equals because that's the assignment operator. Python in this case

[57:02] thinks we're attempting to assign the character y to response. So for comparisons use double equals else we can print no food for you. So would you like food? I'll type

[57:22] y. Have some food. Let's try it again. I'll type no

[57:28] and for no. No food for you. Here's a third example. We'll have

[57:34] a user type in their name. Name equals input. Enter your name. If our name is equal to an empty

[57:47] string, that means they didn't type in anything. So, let's yell at the user. You did not type in your name. Else we will print using an

[58:05] fstring hello whatever the name is. Enter your name. I'm just going to hit enter. You did not type in your

[58:14] name. Let's run this again. I'll type in my name. And we have executed the else

[58:20] statement this time. Hello bro. So one important thing that you should know is the use of booleans with if statements. Suppose we have some

[58:30] boolean variable named for sale. I'll set this to be true. Now using an if statement you can just use the boolean variable in place of a condition because a condition would evaluate to be true or false.

[58:46] We could just say if for sale if that's true then let's print this item is for sale. Else we will print. This item is not for sale. For

[59:08] sale is set to be true. This item is for sale. If this variable were false, well then the item is not for sale. Let's try a different variable.

[59:20] How about online? If online, the user is online. Else the user is offline. So the user is

[59:39] offline. I'll change the boolean to true. the user is online. So with if statements, you can

[59:46] either write a condition or you could use a boolean. All right, everybody. So those are if statements. Do some code only if

[59:55] some condition is true. Else you can do something else. It's a basic form of decision-m and those are if statements in Python. Hey everybody, this is a remake

[1:00:08] of my Python calculator program for absolute beginners. All you need to know to complete this exercise is just if statements and how they work. So let's get started. For this exercise, a user

[1:00:18] is going to select an arithmetic operator. Operator equals input. We will ask the user to enter an operator. This will be plus for

[1:00:30] addition, minus for subtraction, asterisk for multiplication, and a forward slash for division. You could enter more than this, but I don't want to make this exercise too complicated. We will create a variable of num one to contain our first number. Let's say we

[1:00:46] would like to add two numbers together. What is the first number going to be? Enter the first number. And let's do this with the

[1:00:57] second number. Num two. Enter the second number. Let me show you something.

[1:01:06] I'm going to add num one and num two together. Num one plus num two. We'll do a test run. Enter an operator. I would like to

[1:01:17] use addition. Enter the first number 10 and 11. Well, the result is 1,1. When we accept user input, they are

[1:01:28] string data types. What we've ended up doing is string concatenation. We've concatenated the string of 11 to 10.

[1:01:36] That's why we ended up with 1,1. We'll have to convert these two strings to be floating point numbers by type casting them as a float. So enclose your input functions with a type cast a float. And now we

[1:01:55] should be able to add those two numbers together. So let's add 10 and 11 and we get 21.0. 0. Depending on the operator

[1:02:04] that the user selects, we'll use some if statements to determine that. We will check if our operator variable is equal to a character of plus. And for now, I'll write pass as a placeholder. We'll get back to this

[1:02:20] later. Else if our operator is equal to minus, we will use subtraction. And for now, I'll write pass.

[1:02:32] Else if operator is equal to an asterisk for multiplication, we will multiply. Else if our operator is equal to a forward slash for division, we will divide. If our operator is addition, let's create a variable of result. Result equals num 1 + num

[1:02:57] 2. For subtraction, it's going to be num 1 minus num 2. Multiplication would be num 1 * num 2. Then division would be num 1 / num 2.

[1:03:15] Then we just have to print the result. Print our result. Be sure to do this with each of the else if statements as well. And let's see what we have.

[1:03:27] Let's add 5.5 + 6.9. That gives us

[1:03:35] 12.4. Let's subtract 420 minus 0.69. That gives us

[1:03:45] 419.31. Let's test multiplication. Multiply

[1:03:50] 3.14 times 3.14, which gives us 9.8596.

[1:03:56] 8596. Then division. Let's divide 69 by 13. And that gives us a really long

[1:04:07] number. So you could round a number if you would like. We would enclose our result within the round function. And we'll just update each of

[1:04:19] these print statements. This will round to the nearest whole integer. So let's divide 420 by 13. Let's say that we would like three

[1:04:31] digits after the decimal. Within the round function, we could add comma 3 for three decimal places. Enter operator. Let's use

[1:04:43] division. Divide 420 by 69. So that gives me 6.087. So, we can round to a given digit

[1:04:54] after a decimal. In this case, three places. What if somebody types in an operator that doesn't exist, like the word pizza? Then I will divide two

[1:05:05] numbers. Well, let's add an else statement. If somebody selects some input that is invalid, let's let them know. I'll use an fring.

[1:05:16] Let's say that the operator that the user has selected is not valid. And let's try this again. Enter an operator pizza.

[1:05:27] Enter the first number 420 and 69. Pizza is not valid. Let's say is not a valid operator instead. That makes

[1:05:38] more sense. Pizza will be my operator. First number is 420. Second number is

[1:05:47] 69. Pizza is not a valid operator. All right everybody. So that

[1:05:52] is a very simple Python calculator program you can make as a beginner. Hey there, it's me again. In today's topic, we're going to create a weight converter program in Python. This

[1:06:06] is an exercise that will follow up the lesson on if statements. We'll convert pounds to kilog or kilog to pound. The user is going to decide. We will begin

[1:06:15] by creating a weight variable. We will assign some user input. Enter your weight. We will convert this input into

[1:06:25] a floatingoint number. So add that cast. Then we will ask for a unit. Is this weight in

[1:06:32] kilogram or pounds? Input kilogram or pounds. We want the user to type in either K for kilogram or L for pounds. And these are

[1:06:49] capital letters, by the way. Using an if statement, let's first check to see if our unit is equal to a capital K. That means the current weight is in kilogram. We need to convert that

[1:07:03] weight to pounds. Let's reassign weight equal to our weight times 2.205. Else if unit is equal to L, we

[1:07:21] need to convert to kilogram. Weight equals weight divided by 2.205. Else the user did not type in

[1:07:31] something that was valid. Let's print using an fstring unit was not valid. At the end of our program, we will print the new weight. I'll use an

[1:07:48] fstring. Your weight is our new weight after it's reassigned. Now, we need a unit of measurement. This

[1:07:58] is what I'm thinking we'll do within our if and else if statements. Let's reassign our unit. We're reassigning unit to be lbs for pounds. Else if unit equals kgs for

[1:08:17] kilogram in our results, we will display our new unit. Let's take a look. Enter your weight. Actually, I'm just going to

[1:08:26] make one change. I'm going to add colon space there. That's much better.

[1:08:32] Enter your weight. Let's say I'm 180 lb. This is in pounds. I'll type capital L. Your weight

[1:08:41] in kilog is 81.63. I think I'm going to round this.

[1:08:47] I will enclose the weight variable within a round function. We will round to one decimal place. Let's try this again. Enter your

[1:08:56] weight. Maybe I'm 81 kg. I'll type k for kilogram.

[1:09:02] Your weight is 178.6 lb. Let's make sure that this else statement works, too.

[1:09:09] Enter your weight. 180 pizzas. Pizzas was not valid. So, we're

[1:09:16] still displaying our output. We would want to avoid that if somebody doesn't type in a valid unit. So, let's cut this line. Then, paste each within the if and

[1:09:28] else if statements. When we exit the else statement, we're not printing the output. So, let's make sure that this works. Enter your weight. I am 180

[1:09:41] pizzas. Pizza was not valid. All right, everybody. Well, that

[1:09:46] is a weight converter program in Python. I thought this would be a helpful exercise now that we have finished the section on if statements. And yeah, that is a weight converter program in Python.

[1:09:59] Hey everybody. In this topic, we're going to create a temperature conversion program as an exercise. We'll begin by asking what the current unit of measurement is. Unit

[1:10:10] equals will accept some user input. Is this temperature in Celsius or Fahrenheit? C slashF then we will ask for the temperature. I'll store the temperature

[1:10:36] in a variable named temp meaning temperature. temp equals input enter the temperature. Then we should cast our user input as a floatingoint number. If unit is equal to

[1:10:59] C, I'll fill this in momentarily. I'm just going to write pass as a placeholder. Else if unit is equal to F, we will do something else. Else, let's print something. Just

[1:11:16] an error message of some sort using an F string. unit is an invalid unit of measurement. Let's test this else statement. Is the temperature in Celsius

[1:11:35] or Fahrenheit? What if I were to type K for Kelvin? I'll make up some temperature like 100. K is an invalid

[1:11:43] unit of measurement. All right, we know the else statement works. Let's convert Fahrenheit to Celsius using this formula. We will take our

[1:11:52] temperature equals 9 * our temp / 5 + 32. I'll take all of this and use the round function. We'll round to one decimal place. Then we will print the current

[1:12:12] temperature in Fahrenheit. I'll use an F string. The Temperature in Fahrenheit is our temp variable degrees Fahrenheit. Let's test this if

[1:12:33] statement. Is the temperature in Celsius or Fahrenheit? It is currently in Celsius. What is 33° in Celsius

[1:12:42] converted to Fahrenheit? The temperature in Fahrenheit is 91.4°.

[1:12:48] All right, so this section is working. Let's work on the else statement. Else, if our unit is currently in Fahrenheit, we'll convert to Celsius. That formula is temp

[1:13:02] equals our temperature minus 32 * 5 / 9. Then I will round the result to one decimal place. Then we'll print the temperature in Celsius. The temperature in Celsius is

[1:13:26] temp° C for Celsius. Is the temperature in Celsius or Fahrenheit? It is currently in Fahrenheit. Enter the temperature.

[1:13:40] 91.4. The temperature in Celsius is 33.0°.

[1:13:46] Well everybody that is a simple temperature conversion program in Python. All right people, we're talking about logical operators today. Logical operators allow us to evaluate multiple conditions. We can link them together.

[1:14:06] There's three we'll discuss or and not. We'll begin with or. With or we can check more than one condition. If at

[1:14:16] least one of those conditions is true, then the entire statement is true. Here's an example. Let's say we have an outdoor event. And I will create two

[1:14:25] variables. One temp, meaning temperature. Let's say that this is in Celsius, 25° C. Pick Fahrenheit if you

[1:14:33] would like. And I will create a boolean variable of is raining. I will set that to be false. It is currently not

[1:14:41] raining. If the temperature is too hot, too cold, or it's raining, then I will cancel this outdoor event. We'll write an if statement to check that. If our

[1:14:53] temp short for temperature is greater than let's say 35 35° C then I'll use the or logical operator or if our temp is less than zero or if is raining is true. If one of these conditions is true, we're going to cancel our outdoor event. So let's print the following. The

[1:15:22] outdoor event is cancelled. Else we will print something else. The outdoor event is still scheduled. The temperature is reasonable

[1:15:42] and is raining is false. It's not raining. So we print the else clause.

[1:15:49] The outdoor event is still scheduled. What if the temperature was really hot, like 36°? Well, the outdoor event is cancelled. What if it's cold?

[1:16:05] -5°. The outdoor event is canled. This condition was true. Therefore, we

[1:16:10] execute the if statement. Or what if the temperature is reasonable, but it's raining? Is raining is true.

[1:16:18] Well, then the outdoor event is still canled. So with the or logical operator, at least one of these conditions needs to be true. If one of these conditions is true, you could consider the entire statement true. Now let's cover and. With and, we

[1:16:35] can link two conditions together. Both conditions must be true in order for that entire statement to be true. So again let's say we have temp short for temperature and we have a boolean variable of is sunny. I will set that to

[1:16:50] be true. We will check if our temp is greater than or equal to 28° and is it sunny. Is sunny if it's hot and if it's sunny. If

[1:17:08] this is true, let's print the following. It is hot outside. For fun, I'm going to add an emoji, but you don't have to. I just

[1:17:20] think it's more entertaining that way, but you do you. And I will print it is sunny. Sometimes these emojis are formatted differently. I'm just going to

[1:17:34] copy it from somewhere else. That's better. Currently, the temperature is 25 25° C and it's sunny. This condition was

[1:17:42] false, but this one is true. With the and logical operator, both conditions must be true in order for us to execute this block of code. If our temperature was 30°, well, then both conditions are true. It is hot outside and it is sunny.

[1:18:02] Let's write a few more. Let's add else if. Else if the temp is less than or equal to zero and is sunny. We will print something

[1:18:16] else. It is cold outside. I'll change the emoji and it is sunny. Let's set the temperature to

[1:18:28] be5°. It is cold outside and it is sunny. Both these conditions are true.

[1:18:37] So we do this instead. You can link as many conditions together as you would like. Let's see if our temperature is within a certain range. Else if temp is less than 28 and

[1:18:51] our temp is greater than zero and is sunny. to check to see if something is within a certain range. There is a shortcut too. PyCharm is recommending

[1:19:04] this. We can simplify chain comparisons. So this effectively does the same thing. If 28 is greater than

[1:19:12] our temp and our temp is greater than zero and it's sunny, then we will print it is warm outside rather than hot. and it's still sunny. So, let's say our temperature is 20° C and it's sunny. It is warm outside and it is

[1:19:38] sunny. Now, we have the not logical operator. It inverts the condition. We

[1:19:44] are checking to see if something is either not false or not true. So, let's check to see if it's not sunny. Really, I'll just copy what we have and paste it.

[1:19:58] else if not is sunny then that means it's cloudy and let's use a cloud emoji. So basically not does the opposite of what you're looking for. We are checking if not is sunny. Is sunny

[1:20:26] is false. Then this condition is true. Okay. Let's say our temp is

[1:20:33] 28. Is sunny is now false. It is hot outside. It is cloudy.

[1:20:41] What if our temperature was zero? It is cold outside. It is cloudy.

[1:20:48] What if the temperature was reasonable like 20°? It is warm outside. It is cloudy. So not

[1:20:56] it inverts the condition. If it's true, it's now false. If it's false, it's now true. All right, everybody. So those are

[1:21:04] logical operators. They allow us to evaluate multiple conditions. With or, at least one condition must be true.

[1:21:12] With and, both conditions must be true. And not. Not does the opposite. It

[1:21:17] inverts the condition. We check if something is not false or not true. And well everybody, those are logical operators in Python. Hey everybody. So today I got to

[1:21:30] explain conditional expressions in Python. A conditional expression is a oneline shortcut for using an if else statement. If you're familiar with other programming languages, this is also known as the trinary operator. It

[1:21:44] behaves similarly. Using conditional expressions, we can print or assign one of two values based on a condition. Here's the formula. Return X if our

[1:21:54] condition is true. Else return Y. Here's a basic example. We will create a

[1:22:00] variable for number just num. Let's say our number is five. I'm going to print.

[1:22:06] Then within our print statement, I will write a conditional expression following this formula. I'll just copy and paste it. Let's check to see if our number is positive. Let's print the text positive

[1:22:20] if our condition. What are we checking? Let's check to see if num is greater than zero. That means it's positive. If

[1:22:29] this condition is false, we will instead print whatever comes after else. Else negative number is five, that will print positive. If our number was neg 5, well, this condition would be false. We

[1:22:44] would instead print negative. Let's go over another. Let's check to see if our number is even or odd. Let's set num to

[1:22:54] be six. This time I will assign the result to a variable. Our result equals take our formula. Let's

[1:23:06] assign even if our num modulus 2 is our number divisible by two. Does that equal zero? Else return odd. Then let's print our

[1:23:23] result. R result number is six that is even. If it's five then it's odd.

[1:23:33] assign even if our number is divisible by two. Else return odd. Let's create variables A and B. A will equal 6. B will equal

[1:23:50] 7. Let's create a variable of max num equals. Follow our formula again.

[1:24:00] return variable a if a is greater than b else return b between a and b which is the maximum number that would be b of seven let's find the minimum this time min num a if a is less than b else return b the minimum number between 6 and 7 is This time we'll take an age. Age equals 25. We will create a variable of status equals. Use our formula

[1:24:40] again. Return a string of adult. If our age is greater than or equal to 18. Else

[1:24:49] return a string of child. Then we will print our status. Our age is 25. that's

[1:24:56] greater than or equal to 18, we will print adult. If our age was 13, then we are a child. We will instead return child. Let's work with the

[1:25:08] temperature. Temperature equals 30° C. So that's hot. Let's create a variable of weather.

[1:25:19] assign a string of hot if our temperature is greater than 20. Else we will return a string of cold. What's the weather outside today? Based on the

[1:25:32] temperature it is hot. If our temperature was 20 then the weather is cold. Okay, last example. We will work with a user role.

[1:25:46] I will set this to be admin. We will define a variable of access level equals again follow our formula return the text of full access if our condition of user ro is equal to a string of admin else we will return limited access. Our user role is an admin. Let's

[1:26:22] print our access level and we have full access. But what if we were a guest? Well, then we have limited access. All right, everybody. Those are

[1:26:32] conditional expressions. They're a oneline shortcut for the if else statement. It's similar to the turnary operator in other programming languages.

[1:26:41] Using conditional expressions, we can print or assign one of two values. based on a condition, you follow the formula of return x if our condition is true, else return y if it's false. And well everybody, those are a few examples of conditional expressions in Python. Hey everybody, in this topic I'm

[1:27:04] going to cover a few useful string methods that you may be interested in. Then at the end of this video, we will work on an exercise where we will validate some user input. As we know a string is just a series of characters.

[1:27:17] Let's ask a user for their full name. Name equals input enter your full name. The first method I'll show you well technically this is a function. The

[1:27:33] length function will give us the length of a string. How many characters is it? we will find the length of our variable name after the user types in some input.

[1:27:44] This function returns an integer. I'll store that result within a variable. Uh let's just say result. Then I will print

[1:27:52] whatever the result is. Why don't you go ahead and type in your full name. The length of this string in my example is eight characters. That does

[1:28:06] include spaces too. 1 2 3 4 5 6 7 8. If you ever need the length of a string, there is the length function. Let's move

[1:28:15] on. If we were to type our variable name followed by a dot, we have access to a whole bunch of different methods. We have the find method. The find method

[1:28:26] will return the first occurrence of a given character, the position. Let's find any spaces. I'll store the result within a variable named result. I will type in my full

[1:28:43] name. The first occurrence of a space, that's what we set, is at position three. When working with indexes, we always begin with zero. This first

[1:28:52] character would have an index of zero, then 1 2 3. That's why the find method returned three in place of four. Let's find the first occurrence of a capital B. See, it's zero. How about

[1:29:12] O? For me, that would be two. So remember, it's always the first occurrence. If you need the last

[1:29:19] occurrence, there is a different method, which is R find. R meaning reverse. We will find the last occurrence of an O that has a position of five. 0 1 2 3 4

[1:29:39] 5. If Python isn't able to locate a given character, it will return negative 1. Let's find any I don't know uh Q's. Python could not find any lowercase

[1:29:55] Q's. The rfind method will return negative 1 if there are no results. We can capitalize the first letter in a string by using the capitalize function.

[1:30:05] Name dot capitalize. This method will return a string. I will reassign that to name. Then we will print our name

[1:30:18] capitalized. I'll be sure to type in my name, all lowercase. Since this is all one string, only the first letter is capitalized, even though I'm including a first and last name. The upper method will take

[1:30:33] all of the characters in a string. Then make them all uppercase. Follow your variable that contains a string followed byupper. Then I will reassign the result

[1:30:45] to my name variable to overwrite it. Enter your full name. All of the letters are now uppercase. There is also lower to make

[1:30:56] all of the characters lowerase. Name equals name dot lower. Yep. All the characters are

[1:31:07] lowercase. Now the is digit method will return either true or false. If a string contains only digits, the result is a boolean, true or false. I'll store that

[1:31:20] within a variable named result, then print result. So if I were to type in my full name, is digit returns false. There are not only digits within that string. If

[1:31:34] my string was some combination of alphabetical characters and numbers, this method will still return false. It only returns true if my string only contains digits. I'll just type in 1 2 3. See

[1:31:49] that's true. That is the isdigit method. Otherwise, we have is alpha name is alpha. The is alpha method will return a

[1:32:02] boolean true or false depending if a string contains only alphabetical characters. I'll type in my full name. So, the reason that this came up false is because my full name contains a space, which is not an alphabetical character. If I typed in my full name

[1:32:22] excluding any spaces, this would now be true. Is alpha would also return false if my name contained any sort of digits. Bro 1 2 3. And that is also

[1:32:32] false. That is the is alpha method. Now let's ask for a phone number. Phone number equals

[1:32:46] input. Enter your phone number. With the phone number, they typically contain dashes. Let's count

[1:32:54] how many dashes are going to be in somebody's phone number. Phone number dot count method. Let's count the amount of dashes. So, place a character within

[1:33:09] the count method. This method will return an integer. Let's store that within a variable. Result equals phone

[1:33:17] number. Method. So, type in some phone number. 1-23

[1:33:25] 4-56- 8901. We have three dashes within the string. 1 2 3. That is the count method.

[1:33:35] We can count how many characters are within a string. We also have the replace method. Honestly, the replace method is probably one of the most useful methods of strings. We can replace any occurrence

[1:33:48] with one character with another. Replace. Let's replace any dashes with maybe a space. This method

[1:33:58] will return a new string. I'm going to reassign this to our phone number variable. Then print the phone number. Enter your phone number.

[1:34:12] 1-234-567-8901. So, here's my new phone number, but we've replaced all of the dashes with spaces. Even better yet, we could eliminate all the dashes completely by replacing the dashes or another character with an empty string.

[1:34:33] 1-234-567-8901. Here's our new phone number without any dashes. We've replaced all dashes with an empty string, no characters. If you would like

[1:34:42] a comprehensive list of all of the string methods available to you, you can use the help function. Type in the data type string string. Then I will print whatever the result is.

[1:34:57] Here's a bunch of methods you might be interested in in the future. Capitalize, case, fold, center, count, encode, ends with, just to name a few. All right, everybody. Here's an exercise for you.

[1:35:11] We will validate some user input. We would like a user to enter in a valid username. However, there's a couple of rules. The username can be no more than

[1:35:22] 12 characters long. The username must not contain any spaces and the username must not contain any digits. Let's assign a variable named username equals input. Enter a user

[1:35:42] name. First, let's check to see if our user input is more than 12 characters long. We can do that using the length function. we will find the length of our

[1:35:54] username. The length function returns an integer. Let's check to see if the length of our username is greater than 12 characters. If it is, we'll print a

[1:36:07] message. Your username can't be more than 12 characters. else we will print using an fstring welcome whatever our username variable is. Let's try it. I'll type in my first

[1:36:31] name, last name, then add a whole bunch of characters afterwards. Your username can't be more than 12 characters. Let's type in something that's under 12 characters. Yep. And that appears to

[1:36:47] work. Okay, so we have accomplished task number one. Our username can't be more than 12 characters. Next, our username

[1:36:56] must not contain any spaces. We can use the find method of a string. Username.find. We will find any spaces.

[1:37:08] That's a character. If no spaces are found, this method will return -1. Using an else if statement I'll add not if the find method of username equals1. If the result is not -1 meaning

[1:37:34] we found a space we will print your username can't contain spaces. I'll type in my first and last name. You might need to think of something that's underneath 12 characters. Your username can't contain

[1:37:54] spaces. So, we have accomplished rule number two. Three. Username must not

[1:38:00] contain digits. We can use the is alpha method of strings. The is alpha method returns a boolean if a string only contains alphabetical characters. So, let's copy

[1:38:14] that. I'll add another else if statement not username is alpha. Then we will print your username can't contain numbers. I guess

[1:38:34] technically is alpha would check for spaces too, but I'd rather have that be handled within a different if statement. All right, I'll type in a username. I'll include some digits. Your username can't contain

[1:38:50] numbers. All right, I think we've accomplished this. Let me make up a username following these three rules.

[1:38:59] Yep, it seems to check out. All right, everybody. And that is a few useful string methods that you may be interested in. Hey everybody. In this topic, I'm

[1:39:10] going to explain string indexing. Indexing allows us to access the elements of a sequence using a set of square brackets, also known as the indexing operator. Using this set of square brackets, following a string, there are up to three fields that we can fill in. We can access a starting point

[1:39:29] in the string, an ending point, and a step. Here's an example. Suppose we have a credit card number.

[1:39:36] credit number equals and I'll just make up some number 1 2 3 4-5678-9012 dash 3456. Good enough. If I need the first character within the string, I can type the name of my string variable followed by the indexing operator which is a set of square brackets. The first position has an

[1:40:01] index of zero. Computers always start with zero. So that's why the first index is zero. Then I'm going to go ahead and

[1:40:07] print this. Print credit card number at index of zero. That would be one. If I were to

[1:40:15] change the index to be one, 0 1, that should be two. Index two would technically be three. Then four is the dash within our string. As you can see here with the

[1:40:30] indexing operator, there's up to three fields that we can fill in a start, end, and a step. If you have just one field listed without any colons, it's assumed you're filling in the starting position. So now, what if you would like the first four digits of the string? Well, we would type the name of

[1:40:49] our string variable indexing operator. We'll need a starting index colon then an ending index. The first four digits would be zero colon 4.

[1:41:06] Then I will print this. And I'm just going to turn this first line into a comment. Yeah, there we go. We have the

[1:41:15] first four digits of our credit card number. 1 2 3 4. Just so you know, with the ending index, this index is exclusive. This first number would be

[1:41:25] zero 1 2 3 4. So we did not include that dash within the number. The starting index is inclusive. The ending index is

[1:41:34] exclusive. So you can omit the zero in the beginning. You could just say colon 4. Python assumes the starting position

[1:41:42] will be the beginning of the string. So that would work too. Let's get the next set of digits.

[1:41:49] 5678 credit number indexing operator. Let's find where the starting index would be. 0 1 2 3 4 5 5 colon 6 7 8 9. Then we will print whatever is

[1:42:11] here. The next set of digits is 5 6 7 8. Maybe we need the last 12 digits. Well,

[1:42:18] what we could do in that case, we will take our string variable credit number. Set the starting index to be let's see 0 1 2 3 4 5 5 colon. If you need everything up to the end of the string, you don't need to list an ending index. Just be sure to

[1:42:37] add that colon. Python then assumes you need everything up to the end of the string. So, I will print whatever we have. Then we should have everything

[1:42:47] besides the first four digits. Yep. 5 6 7 8 9 0 1 2 3 4 5 6. You could also use a negative

[1:42:58] index. Credit number. If you need the last character in a string, you would set the index to be -1. Then I will

[1:43:06] print this. Print credit number at index of -1. That would be six. -2 is

[1:43:18] five. -3 is four. -4 is three. And then5 would be

[1:43:25] that dash right here. Yeah, you can use negative indexes too. Let's talk about step. Using the step field, we can

[1:43:33] access the characters in a string by a given step. We can count by twos or we can count by threes. So here's an example. So let's take our credit

[1:43:43] number. If we're not filling in these starting or ending fields, but we need a step, we would need two colons. Then Python is assuming everything from the beginning of the string to the end. Then

[1:43:54] our step will be two. This will print every second character within our string. Yeah, here we are. We have 1 3

[1:44:04] dash 6 8 9 1 so on and so forth. If I were to change the step to three, we would count every third character beginning with 1 4 6 dash 1 36. All right, here's a practical example. Let's create a program to get

[1:44:30] the last four digits of a credit card number. I'm going to assign this to a new variable. Last digits equals our credit number indexing operator. So, we need

[1:44:49] the last four digits. Where would the starting index begin? Well, we could use negative indexing. This last digit is

[1:44:56] -1, -2, -3,4. We will begin at -4 colon. We can omit the ending index.

[1:45:06] Python assumes we need the rest of the string. Then really, that's all we need. So, let's print. I'll use an

[1:45:15] fstring. Uh maybe some x's. Maybe we're hiding somebody's credit card number except the last four digits. Okay. then variable

[1:45:26] last digits. All right. And here's our credit card number where only the last four digits are visible. Hey, you know what?

[1:45:36] Let's add one more exercise. Let's reverse the characters in the string. I'm going to reassign credit number equals credit number. If we need the entire string, we

[1:45:50] don't necessarily need a starting index or an ending index. But for the step, this will be negative. Negative -1 will reverse a string. Then let's print

[1:46:01] whatever our new credit card number is. Print credit number. And yeah, there is our credit number backwards. To reverse a string,

[1:46:12] you set the step to be -1. So yeah, everybody, that is string indexing in Python. We can access elements of a sequence using the indexing operator which is a set of straight brackets. You

[1:46:24] can list a starting position, ending position and even a step if you need to skip over characters. But yeah, that is string indexing in Python. Hey everybody, in this topic I'm going to explain format specifiers.

[1:46:39] Format specifiers when used in the context of an string, they allow us to format a value based on what flags are inserted. Following your value, you would type a colon and then some flags. Depending on what flags you insert, it will format your output a certain way.

[1:46:57] You could add decimal point precision, allocate space, zero pad values, left justify, right justify, center align, all sorts of things. Let's have some practice. I'll create three prices. Price

[1:47:12] one, price two, price three. Price one will be 3.14159. These values aren't in dollars

[1:47:23] and cents yet, but they will be. Price two will be 987.65. As you can see, I'm just making

[1:47:32] up numbers here. Price three is 12.34. Let's display our prices using

[1:47:39] some fstrings. Price one is placeholder price 1. Then we will do this for price two and price three. Price two is price two.

[1:47:54] Price three is price three. Within our placeholder following the value, we can add a colon. Then some flags. Those

[1:48:03] flags are the format specifiers. They will format our value a particular way depending on what we insert after the colon. To add decimal point precision, you would type after the colon dot then the amount of decimals to be displayed maybe two then f meaning floatingoint number. Let's do that with price two and

[1:48:25] price three colon.2f. Price one is now 3.14. Price 2

[1:48:35] is987.65. Price three is 12.34. I think I'm going to add some

[1:48:40] dollar signs before the placeholder. Yeah, that's much better. For less precision, maybe one decimal place, you can change the two to a one.

[1:48:51] So.1 F. Each number only displays one decimal. 0.1

[1:48:59] 6.3 whereas in 3F would display three decimal places.142 650.340 even though price 2 and price 3

[1:49:10] only have two decimal places in the original numbers we will concatenate some additional zeros to allocate space to display a value after the colon add some number some number for that many spaces how about 10. Each value now has a total of 10 spaces to display the output. 1 2 3 4 5 6 7 8 9 10. If you were to preede a number with

[1:49:42] zero, well, these numbers would be zero padded. Each number is now zero padded. To left justify a value, you would use a left angle bracket. All these numbers are now left

[1:50:00] justified. Then we have all of the space after. They're all uniform. Right

[1:50:06] justify would be a right angle bracket. And I believe that's the default. Center align I believe is the carrot symbol.

[1:50:22] Yep, our numbers are now centered. If you have any positive values and you would like to display a plus sign, just use plus. Any positive number is preceded with a plus sign. Any negative number is

[1:50:41] preceded with the negative sign. Or you could use a space for any positive numbers. So, colon space These numbers are lined up evenly even though we have a negative number in here. There is a thousand separator

[1:50:55] which is a comma. We should probably increase the value of our prices. 3,00 9,870 1,200. Each thousand's place is now

[1:51:10] separated with a comma. We could also mix and match flags. I would like a thousand separator along with decimal point precision of two decimal places. And why not? I will preede each

[1:51:26] number with a plus sign if it's positive. Yep, here we are. So based on what you're looking for, you can add some combination of flags. So yeah,

[1:51:39] those are format specifiers. everybody. Within your placeholder, insert your value, a colon, then certain flags based on what you're looking for exactly. But yeah, those are just a few

[1:51:51] format specifiers in Python. Hey everybody, in this topic, I'm going to explain while loops. A while loop will execute some code while some condition remains true. Here's an

[1:52:04] example. We'll use an if statement first. We will ask a user for their name. name equals

[1:52:10] input. Enter your name. If our name is equal to an empty string, that means the user didn't type in anything. Let's print a

[1:52:23] message. You did not enter your name. Else, we will print using an string, hello, our user's name.

[1:52:39] If I were to skip this prompt, we would execute this if statement. Then we continue with the rest of the program. What if I would like to continually prompt the user to type in their name? We can't continue

[1:52:51] until they type in something. Well, we could replace this if statement with a while loop. While this condition is true, continue to execute this code. within

[1:53:03] the while loop. I'm going to reprompt the user to type in a name. Then if we were to exit the while loop, then we will print hello. Whatever

[1:53:13] your name is. So let's run this. Enter your name. I'm going to hit enter. You

[1:53:18] did not enter your name. Enter your name. No. No. No. Okay, I give up. I'll

[1:53:24] type in my first name. Hit enter. Hello.

[1:53:26] Whatever your first name is. while this condition remains true, execute this code potentially forever until this condition is no longer true. So that's one of the main benefits of a while loop. If it's not true, then you exit

[1:53:41] out of the while loop. And that's why we're able to continue then print our name. Hello name. You do want some way

[1:53:47] to escape out of the while loop. Otherwise, you'll run into what's known as an infinite loop. So let's say while name is equal to an empty string, we will print you did not enter your name. So I'm going to hit enter. So we

[1:54:02] are stuck in an infinite loop. We can't actually escape this loop. We didn't give ourselves an exit strategy. That's why previously we

[1:54:11] reprompted the user to type in something. We're giving them a chance to escape. In a way, it kind of works like an if statement, but instead of executing some code once, it's potentially infinite. Here's another

[1:54:22] example. This time, let's ask for a user's age. Age equals, and I will convert the input to an integer. Enter your

[1:54:34] age. We'll need the user to type in a positive number. While age is less than zero, let's print a message to let the user know that they can't do that.

[1:54:50] age can't be negative. Then we need some strategy to escape. Let's reprompt the user to enter in their age. Once they type in something that's

[1:55:03] valid, we can escape out of the while loop. So let's print using an fstring you are age years old. So enter your age. I'm going to say

[1:55:18] negative one. Age can't be negative. -21 million. Okay, I give up. How about

[1:55:26] 21? You are 21 years old. So, that was another example. While our age variable

[1:55:32] is less than zero, repeat this code forever. Let's go over example three. I'm going to introduce some logical operators. We will have the user

[1:55:42] type in a food they like. food equals input enter a food you like. But in order to escape, they need to press Q to quit. While food is equal to the letter

[1:56:01] Q, continue this while loop. However, I'm going to make one change. We want to exit the while loop when they press Q.

[1:56:11] So you could say while not food equals Q. So within this while loop, let's print the food that they stated that they like. I'll use an F string. You

[1:56:23] like your variable food. Then we will prompt the user to enter in another food that they like. Enter another food you like. Q to

[1:56:33] quit. Then once we escape the while loop, we will print just buy. Okay. Okay. Enter a food you like.

[1:56:41] Q to quit. I like pizza. You like pizza.

[1:56:45] I like sushi. You like sushi. I like ramen. You like ramen. Okay, this

[1:56:51] program is kind of lame. So, I'm going to press Q to quit. And we escape the wild loop. We have printed by. So, you

[1:56:59] could do something while something is not true by using the not logical operator. All right, last example. Example four. We will use the or logical

[1:57:08] operator. We'll ask a user to type in a number between 1 and 10. Let's say num equals input enter a number between 1 through 10. Then I will type cast the input as

[1:57:28] an integer. While our number is less than one or our number is greater than 10, let's reprompt the user. Let's print using an fstring our variable num is not valid. Then we will reprompt

[1:57:52] the user. Enter a number between 1 and 10. Once we escape the while loop, then we will print our number using an fring.

[1:58:03] Your number is our variable num. Enter a number between 1 through 10. 0. Zero is not valid. Negative

[1:58:15] 1 100. Nope. Uh five. Your number is

[1:58:20] five. That's an example of how you can add logical operators to wild loops. while this condition is true or this condition is true, execute this code forever. All right, everybody. So, those

[1:58:32] are while loops. A while loop will execute some code while some condition remains true. It's fairly useful for verifying user input. If a user types in

[1:58:43] some input that is not valid, you can reprompt them. And there's many other uses that we'll discuss in the future. But yeah, those are while loops in Python. Why hello everybody. In today's

[1:58:55] video, we'll be creating a compound interest calculator in Python. For those that don't know, interest is a charge for the privilege of borrowing money to some individual or organization. When you place money in a bank account, you typically acrue interest. We'll create a

[1:59:10] program to tell you what your new balance will be after acrewing interest for so many years. But the user is going to decide the initial principle. That's the investment, the rate of interest, and the time in years that this balance has been acrewing interest. So let's

[1:59:24] begin. Let's declare three variables. A principle, a rate, that is rate of interest, and time. Time will be in

[1:59:32] years. We've recently learned about while loops. I would like to include those within this program just so we get the hang of using them. We will ask the

[1:59:39] user to type in an initial principal investment. We will continue to prompt the user to type in a principle that's above zero. Our condition will be while principal is less than or equal to zero.

[1:59:53] We will take our principal assign it some user input. Enter the principal amount. Then we would like to type cast our input as a floatingoint number.

[2:00:11] If our user input principle is less than or equal to zero, we need to inform the user principle can't be less than or equal to zero. So I'm going to test my program by printing the principal at the end. Just temporarily enter the principal amount.

[2:00:39] I can't type a negative number and continue. What if my investment was negative $1,000? Principal can't be less than or equal to zero. How about zero? Nope.

[2:00:49] Can't do that either. Is a,000. Okay?

[2:00:52] Yep. A,000 works. That is for the principal. Let's copy this while loop.

[2:00:58] Paste it. Replace principal with rate. This is the rate of interest. Enter

[2:01:05] the interest rate. interest rate can't be less than or equal to zero. Then let's copy this again. Paste

[2:01:17] it. Change rate to time. Let's type cast our input as an integer because we're working with whole years. Enter the time in years.

[2:01:35] time can be less than or equal to zero. I'm going to print my principal, rate, and time. We have principal, rate, time. Okay, we know that principle

[2:01:55] works. Enter the interest rate. Can my interest rate be -1? No, it can't. Can

[2:02:01] it be zero? Nope. How about 10? 10%. All

[2:02:05] right, that works. Time. Can time be zero? No, it can't. Can my time be

[2:02:10] negative 1? No, it can't. What about 3 years? All right, so we know that our

[2:02:16] while loops are working. Now, here's the formula to calculate interest. Let's say our total, that's our total balance equals our principal times 1 + our rate divided by 100. I'm

[2:02:34] going to enclose this function with the set of parenthesis. This portion of our function will take our interest rate, which is a whole number, then create a decimal. Enclose this function within the power function.

[2:02:48] raise this function to the power of time and that is how to calculate compound interest then we will print the new balance I'll use an fstring balance after our variable time the word years I'll add a placeholder we will add our total then I'll include a dollar sign maybe this will be in dollars but pick any unit of currency you would like. I will format this variable with the format specifier. We will display two decimal places 2F. Okay, let's try this.

[2:03:28] Enter the principal amount. I invest $1,000 into maybe the stock market. The interest rate is maybe 10% this year. The time in years will be 1.

[2:03:41] So, after one year at 10% interest, my new balance is $1,100. Let's try it one more time for good measure. Maybe $500 with an interest rate of 7 over 2 years. Your

[2:03:54] new balance would be $57245. All right. Now, there is another way of writing this program. What if we

[2:04:02] would like to allow the user to enter in values that are equal to zero while principal is less than zero? If principal is less than zero, principal can't be less than zero. Let's do that for rate. Interest can't be less than

[2:04:24] zero. Time can't be less than zero. Here's what happens to our program. Remember

[2:04:32] that we're declaring our variables at the top. Uh nothing happens. We go straight to the results. So the reason that this

[2:04:40] is happening is that when we reach the while loops, this condition is false from the beginning. We never end up entering these while loops. We skip over them because these three conditions are all false. We can write a different

[2:04:54] variation of this while loop where we could say while true. True is a boolean. That means this while loop will continue forever unless we explicitly break out of the while loop. We're going to add an

[2:05:07] else clause. Else we will break. Break will break out of a loop. With our second while loop, change

[2:05:17] rate is less than zero to while true. Then we will add an else clause. Else break out of the loop. While

[2:05:29] true. Else break out of the loop. We should be able to enter zero values in now. Enter the principal amount. 0 0 0.

[2:05:41] Balance after 0 years is $0. This should work the same as before, but we should be allowed to enter in zero values. $1,000. Interest rate of zero after one

[2:05:55] year is still $1,000. Well, okay then everybody. I thought that would be an interesting project to create now that we know how while loops work. You could write either

[2:06:05] a standard while loop with a condition such as principle is less than or equal to zero or you could say while true. This loop would continue forever. You would need to explicitly break out of the while loop using this break keyword which we'll cover again in four loops.

[2:06:22] But yeah, that is a compound interest calculator in Python. Hey everybody, in this topic I need to explain for loops. A for loop will execute a block of code a fixed number of times. You can iterate over a range,

[2:06:39] a string, a sequence, anything that is considered iterable. I'll have more examples for you in future topics. There is a lot of overlap where you could use either a while loop or a for loop, but for loops tend to be better in situations where you have to do something only a fixed number of times.

[2:06:55] Here's an example. Suppose we need to count to 10. If we were to use a for loop, we could write something like this. We would type four, then we would

[2:07:03] need some sort of counter. Typically, you see people write x. 4 x in, then we will use the range function. What number

[2:07:14] would we like to start at? I would like to start at 1, then count to 10. But the second number is exclusive. So really,

[2:07:22] we're going to write 11 if we want to count to 10. So then colon then hit enter. Whatever code you would like to repeat a certain number of times you will list underneath the for loop and make sure the code is indented too. I will print whatever our

[2:07:37] counter x is. When I run this code we will begin at 1 then stop once we reach 11. So yeah there we are. We have begun

[2:07:47] at one and we have counted all the way to 10. So that's the basic syntax for a for loop for some counter. Really, you can name this anything. Sometimes you'll

[2:07:55] see people name this as counter and that would work too, but let's stick with X in some range. Where would we like to begin? Where do we stop? Okay, now let's count backwards.

[2:08:10] Let's start at 10, then count down to zero. When we escape the for loop, let's print happy new year. When we print happy new year, we are outside of the for loop. To count

[2:08:24] backwards, you can enclose your range function within the reversed function reversed. So we begin at 10, count down to one, then print happy new year. In this case, to count backwards, you would enclose the range function within the reversed function. There is an

[2:08:45] additional parameter too you could add. That is the step. If you would like to count by twos, you would add comma 2. So I'm going to get rid of happy new

[2:08:55] year. Let's print the numbers 1 through 10, but we will count by twos. And this does begin at 1, though.

[2:09:03] So 1 3 5 7 9. If you were to change the step to three, you would count by threes beginning at 1 4 7 10. So the range function isn't the only thing you can iterate over. You can iterate over a

[2:09:17] string. Let's say we have a credit card number. Credit card equals I'll make up some credit card number with dashes. That is good enough. For x in

[2:09:33] credit card print x will hold our current position. At first it'll be one then 2 3 4 dash. So on and so forth. So

[2:09:42] here's our credit card number. 1 2 3 4 dash 5 6 7 8. I think you get the idea.

[2:09:49] So you can iterate over a string with a for loop as well. We'll have a few projects involving that. There are two useful keywords as well. These aren't

[2:09:57] exclusive to for loops. You can use these within while loops as well. They are continue and break. Suppose we going

[2:10:04] to count to 20. For x in range, we will begin at one, stop at 21. I think this is kind of a dumb example, but it gets the point across. 13 is considered an

[2:10:16] unlucky number, right? What if our counter reaches 13? I would like to skip over it. Well, we can do that with the

[2:10:23] continue keyword. If x is equal to 13, we will continue and skip over that iteration. Else, we will print whatever our counter is. So, let's take a look.

[2:10:39] Yeah, we have the numbers 1 through 20, but we have skipped the number 13. To skip over an iteration, you can use the continue keyword. Whereas the break keyword, we will break out of this loop entirely. If x is equal to 13, then

[2:10:57] break. So yeah, we have only counted to 12. Once we reach 13, we have escaped the loop. So yeah, everybody, those are

[2:11:05] four loops. You can execute a block of code a fixed number of times. You can iterate over a range, a string, a sequence, anything that is considered iterable. There is a lot of overlap

[2:11:17] where you could use either a while loop or a for loop. While loops tend to be better if you need to execute something possibly infinite amount of times, such as when you're accepting user input, for example. But yeah, everybody, those are for loops in Python. What is going on everybody? In

[2:11:36] today's topic, we're going to be creating a countdown timer in Python. We'll be using what we learned in the previous topics. Let's begin. We'll need

[2:11:44] to import the time module. There's a pretty cool function within the time module. That is the sleep function. Type

[2:11:52] time do sleep. Add a set of parenthesis. Within the set of parenthesis, our program will essentially sleep for a given amount of seconds, like three.

[2:12:03] After three seconds, let's print something. This is just a demonstration. Times up. When I execute this code, nothing

[2:12:15] happens for 3 seconds, but after 3 seconds passes, it displays our message times up. So, you can use the sleep function of the time module to sleep for a given amount of time. We will ask the user how long would they like to set the timer for. We will create a variable.

[2:12:32] Let's say my time my time will be in seconds. We will create a prompt. Enter the time in seconds. Then we should type cast our

[2:12:46] input as an integer. We'll need to create a loop. We could use either a while loop or a for loop. There's a lot of overlap where you

[2:12:57] could use either one. I'll use a for loop in this case. Four. We'll need some

[2:13:01] sort of counter X in our range zero through my time. After each iteration, we will sleep for 1 second. Let's test what we have so far. I would like to sleep for 3

[2:13:24] seconds. I think that's approximately three. But now we are going to print whatever x is. Print x. x is our

[2:13:35] counter. 0 1 2 times up. We're getting somewhere. But I would like to count

[2:13:43] backwards. What we could do is enclose our range function within the reversed function. But another technique that we can use is by using a step.

[2:13:56] Let's replace zero with my time. Then end at zero. But we will set the step to be - 1. Then we can

[2:14:06] increment backwards using this function. That's another technique too to count backwards. So let's wait for 3 seconds.

[2:14:14] 3 2 1. Times up. Now let's display a digital clock of some sort. But we would

[2:14:22] have to calculate how many hours, minutes, and seconds there are. So let's calculate seconds. Seconds equals x. X

[2:14:31] is our counter. Remember modulus 60. Within our print statement, we'll use an f string. We are displaying

[2:14:40] hours, minutes, and seconds. I'll add some placeholders for each of these fields. We have seconds. With our

[2:14:48] digital clock, we can't go above 60 for either seconds or minutes. That's why I'm using modulus 60. The modulus operator gives you the remainder of any division. Let's begin at 11. So 11 10 9.

[2:15:03] So it is counting down, but I would like to add some zero padding and we can do that with the format specifier. After seconds, I will add colon. I need to display two digits.

[2:15:16] Then zero pad those digits. Let's try that again. I will wait for 11 seconds.

[2:15:21] 11 10 9. Yeah. And we do have some zero padding. So that's looking more and more

[2:15:28] like a digital clock. Let's add minutes then. So to calculate minutes, let's assign variable minutes equal to x / 60 because there's 60 seconds within a minute. But then I'm going to type cast

[2:15:44] the result as an integer modulus 60. We would not like this field of minutes to go above 60. So let's add a placeholder. We're

[2:15:58] displaying minutes. Format specifier 02. Now I'm going to wait for 65 seconds. That is 1 minute and 5

[2:16:08] seconds. Then I just want to be sure that we go below a minute. Yep, it's working. Then let's calculate

[2:16:16] hours. Oh, by the way, to stop your program from running, hit this red square up in the corner. Let's calculate hours. Hours

[2:16:25] equals x / 3,600. There's 3,600 seconds in an hour. Then we will type cast the result as an integer.

[2:16:40] within our fing we will display ours format specifier 02. Then I will run this program. Let's wait for 3,65 seconds. That is 1 hour and 5

[2:16:56] seconds. And I just want to be sure that we go below 1 hour. Yeah. All right. So

[2:17:02] that works. So the reason that I didn't add modulus 24, I don't have days within my fing. We can display any amount of hours. I will

[2:17:13] exclude modulus 24. All right, everybody. Well, I thought that'd be some good practice with working with loops. We should try

[2:17:20] and do as many exercises as we can. And yeah, that is a countdown timer program in Python. Hey everybody. So I guess in

[2:17:30] today's topic, I'm going to be explaining nested loops. It looks like so a nested loop, think of it as a loop found within the code of another loop. You have a loop, right? Any code within

[2:17:41] that loop is indented underneath that loop. Well, you could have a looping structure found within the code of another looping structure. The loop on the outside is the outer loop. The

[2:17:51] internal loop within the outer loop is known as the inner loop. Where you'll encounter nested loops, it's really situational. You could have a while loop inside of a while loop, a for loop inside of a for loop, a for loop inside of a while loop, a while loop inside of a for loop, etc. So, here's a

[2:18:07] demonstration. Let's begin by displaying the numbers 1 through 9, but we'll use a loop for x. X is our counter in range 1, 10. Remember that the second

[2:18:20] number in this case 10, that's exclusive. Then I will print our counter X. This program will print the numbers one through nine. Now we have an exercise at

[2:18:34] the end of this topic. I should probably explain this feature. So with a print statement, we end each print statement with a new line character. If I need all

[2:18:42] of these numbers on the same line, at the end of my print statement, I can add comma end equals an empty string. Normally with a print statement, each ends with a new line character, but we can set that to be something else. So when I run this again, all of these numbers are on the same line. Or

[2:19:03] you could add a different symbol like dash or a space. Each of these characters is now separated with a space. But let's stick with an empty string. Okay, so we have used a loop to

[2:19:16] count the numbers 1 through nine. What if I would like to repeat this three times? Well, I could create another loop for x in range. You could say 1, 4,

[2:19:30] or you could just say three. Either way, whatever code is within this loop will be executed three times. Let's cut our original for loop, then place it within the code of our new loop. Our

[2:19:44] outer loop will have this code repeat entirely three separate times. Uh but we do have one thing we need to pay attention to. We have two counters with the same name. You'll want to be sure

[2:19:56] that they're different. Let's rename the counter of the inner loop to be y instead of x. And be sure to change that here as well. Now when I run this code, we're

[2:20:07] completing let's see 27 iterations. To exit this for loop, we need to count the numbers 1 through nine. Once we do so, that is one iteration of the outer loop.

[2:20:19] But our outer loop is saying, "Hey, we still need three total iterations." Now, if you would like these on separate lines, let's make this look a little different. Let's add each iteration of the outer loop onto a new line. So, within the outer loop, but not

[2:20:34] within the inner loop, I'm going to create just a blank print statement. This will just print a new line. Let's try this again. With the inner loop, we count the

[2:20:44] numbers 1 through nine. After we exit the for loop, we will print a new line. Then repeat this all over again until our outer loop is satisfied. So that's

[2:20:55] basically a nested loop. It's just a loop that's inside of another looping structure. So let's create a project.

[2:21:01] We're going to print a rectangle made of some symbol that we set. We'll have the user type in how many rows and columns this rectangle will have. We'll reuse this code that we have already written.

[2:21:12] So this time let's accept some user input. Rows equals input. Enter the number of rows. Then we

[2:21:23] should type cast this input as an integer. Let's copy this line. Paste it.

[2:21:30] Change rows to columns. For the second line, enter the number of columns. Then let's create a symbol.

[2:21:39] Symbol equals input. Enter a symbol to use. We already have this rectangle structure, right? Think of it as the

[2:21:52] outer loop is in charge of the rows. Let's change in range three to in range rows. The inner loop will be in charge of the columns. For y in

[2:22:05] range columns, we will print our symbol whatever the user chooses. So let's try this again. Enter the number of rows.

[2:22:15] How about four rows, 10 columns? I'll use a dollar sign. So here's our rectangle.

[2:22:25] We have four rows, then 10 columns. 1 2 3 4 5 6 7 8 9 10. Let's try it one more time. Three

[2:22:37] rows, five columns, and I'll use an asterisk. Yep, three rows, five columns. So, yeah, that's a nested loop.

[2:22:48] Really, it's just a loop that's inside of another loop. The type of loop really doesn't matter as well as what's within each loop. It's just a situation where you have a loop inside of another loop.

[2:22:58] And yeah, those are nested loops in Python. Well, hello everybody. Today I will be explaining a few different types of collections in Python. There's four

[2:23:09] general purpose collections. Three of them are lists, sets, and tpples. There are also dictionaries, but I'll save that for the next topic because they can be kind of tricky. A collection I would

[2:23:20] think of them as a single variable and I'm saying that within quotes that is used to store multiple values. That's how I would explain a collection to a beginner. For example, let's say we have a variable variable fruit. Fruit equals

[2:23:35] some value like apple. And then I can print this fruit which is apple. I could turn this variable into a collection by surrounding my values with either a set of square brackets for a list, curly braces for a set, or parenthesis for a tuple. Let's begin with a list. If I

[2:23:54] would like to store more than one value in this variable, I will surround my values with a set of square brackets. This variable is now a list. I can store multiple values separated with a comma.

[2:24:07] Not only do we have an apple in this variable, but we have an orange a banana and coconut. One naming convention that I like to use, if I declare a collection such as a list, set or tpple, I like to take the variable name and make it plural just so that it's more obvious that this is a collection of values. Technically, in the English language, fruit would still be plural. English is

[2:24:33] a weird language. We now have a list of fruit named fruits. If I were to print my list, this is the result. We have all

[2:24:43] of our values enclosed with a set of square brackets. To access one of these elements found within your list, you can use the index operator, much like what we can do with strings. The first element would have an index of zero.

[2:24:57] That would print my value apple. Index of one would be my orange. Two is banana. Three coconut. What about

[2:25:08] four? We don't have a value there. List index out of range. Each

[2:25:14] value in a collection is also known as an element. If we attempt to access an element that's not found within our collection, you'll run into an index error. With the index operator, you could set a beginning index, an ending index, and a step. I would like the

[2:25:31] first three elements. You could say zero colon three. That would give me apple, orange, banana. Technically, you don't even need

[2:25:41] the zero. You need that colon, though. We can even use a step. I would like

[2:25:45] every second element, apple, banana. It's every second element beginning from index zero. Maybe I would like my fruit backwards. I'll set the step to be

[2:25:55] negative 1. Coconut, banana, orange, apple. You can use the index operator with collections much like you can use with strings. Another cool thing you can

[2:26:04] do too with collections is that you can iterate over them with the for loop for x in my collection fruits. What would we like to do? I will print whatever x is. So we have iterated over our list.

[2:26:21] Apple, orange, banana, coconut. Now x isn't really too descriptive. What you'll see some people do is that with their collection name, it's plural, their counter will be the singular version of that word. If our collection

[2:26:33] name is fruits, let's rename x as fruit. Singular. It's not mandatory, but that's a common convention. It's more readable

[2:26:42] that way. For every fruit in fruits. If this were cars, you could say for car in cars. Our counter is storing whatever

[2:26:52] value is within our collection. So what are all the different methods that we can use with collections? To list the different methods that are available to a collection, you can use the dur function. Within this function, add your

[2:27:06] collection fruits. But we would need to print this. Let's surround this function with a print statement. These are all in alphabetical

[2:27:16] order. We have attributes, which I have not explained yet, but I will in a future topic. But if we scroll to the end, we have a bunch of different methods that this list can perform.

[2:27:27] Append, clear, copy, count, extend, index, insert, pop, remove, reverse, and sort. If you would like a description of each of these methods, there is a help function. Help. Add your collection to

[2:27:39] the parenthesis. Then we would need to print this. Here's the description of all the methods and attributes. For example, we

[2:27:51] have our sort method. And here's a description. Sort the list in ascending order and return none. And then a bunch

[2:27:58] of other stuff. If you ever forget what you're capable of with a list or other collection, you can always use the help function to print a description of the attributes and methods available. If you need the length of how many elements are within a collection, there is the length function. Return the length of my list

[2:28:17] fruits. Then let's print it. There's four elements within my list. The length

[2:28:23] function returns four. If I were to add an extra element like a pineapple, then that number would be five. Let's remove that. Using the in

[2:28:36] operator, we can find if a value is within a collection. Is our value apple in fruits? But then we would need to print this.

[2:28:48] This operator will return a boolean. So let's print whatever that is. Is apple in fruits? That is true.

[2:28:57] But is pineapple? Pineapple is not. It's false.

[2:29:02] You can use the in operator to find if a value is within a list. And that applies for your other collections, too. With lists, they're ordered and changeable. Duplicates are okay. We can

[2:29:14] change one of these values after we create our list. Let's take fruits at index of zero. I will set this equal to be a pineapple. Then let's iterate over our

[2:29:29] fruit. Using a for loop. Okay, the first element is no longer an apple. It's a pineapple. Then

[2:29:36] orange, banana, coconut. Using an index, you can reassign one of the values. If I were to change zero to one, well, now we have an apple, pineapple, banana, coconut. Let's cover some of the methods

[2:29:50] that are found within a list. We can append an element. Type the name of the list dot append. What would we like to

[2:29:58] append to the end of this list? Let's append a pineapple. I'm going to get rid of this for loop. I'm just going to display my

[2:30:06] list. There we have an apple, an orange, banana, coconut, pineapple. To add an element to the end of a list, use the append method. To remove an element, you can

[2:30:17] use the remove method. Fruits. Let's remove our apple. Our apple is no longer there. We

[2:30:25] have an orange, banana, coconut. Using the insert method, we can insert a value at a given index. Fruits do.insert list an index. Zero would be

[2:30:37] the beginning. Then a value. pineapple. Now we have a pineapple,

[2:30:45] apple, orange, banana, coconut. The sort method will sort a list. Fruits do.sort. These are all in alphabetical

[2:30:54] order now. Apple, banana, coconut, orange. To reverse a list, you would use the reverse method.

[2:31:04] Fruits.reverse coconut, banana, orange, apple. However, these are not in reverse alphabetical order. These elements are

[2:31:11] reversed based on the order in which we place them. If you would like reverse alphabetical order, you can first sort and then reverse. Now we have orange, coconut, banana, apple. To clear a list, use the clear

[2:31:26] method. Fruits. All of the elements are gone. We can return the index of a

[2:31:35] value. Let's return the index of apple. Fruits do index list an element. Then we will need to print

[2:31:47] this. Let's print the index that is returned. The index of apple is zero.

[2:31:57] Coconut that would be three. What if we don't find a value like a pineapple? Well, we have an error. Pineapple is not

[2:32:07] in list. You could count the amount of times that a value is found within a list because duplicates are okay. Fruits doc count. Let's count how many bananas

[2:32:18] are in this list. Banana. Then print it. One banana is found within this

[2:32:29] list. How about pineapples? There are zero. Now those are lists.

[2:32:36] Surround your values with a set of square brackets. These values are ordered and changeable. Duplicates are okay. Now let's talk about the next

[2:32:45] collection which is a set. To create a set, surround your values instead with a set of curly braces. Our collection of fruits is now a set. A set has different

[2:32:55] benefits. The values are unordered and immutable, meaning we can't alter these values. However, we can add and remove elements. A set does not include any

[2:33:05] duplicates. I'm going to delete these methods, then print fruits. We have all of the same values, but they're not in the same order as they were originally. A set is

[2:33:17] unordered. If I were to run this again, they will likely be in a different order. See, now we have a banana, apple, coconut, orange. To display all of the

[2:33:26] different attributes and methods of a set, you can use the dur function. And here's all of them. Some of these methods are a little more advanced, but there's a few we might recognize, like add, clear, copy. For an

[2:33:42] in-depth description of these methods, you can use the help function. Much like what we did before, to find the length of our set, we can use the length function, which is four. We can use the in operator to find if a value is found within this set.

[2:34:00] Unfortunately, pineapples are not within our set. Now, if I was to use the index operator of my set, this is what would happen. We have an error. Set object is

[2:34:13] not subscriptable. We're not able to use indexing on a set because they're unordered, much like what we can do with a list or a string. We can't change the values of a set, but we could add or remove elements. Let's use the add method to

[2:34:28] add guess what? A pineapple. That is okay. Orange, apple,

[2:34:35] pineapple, coconut, banana. We can remove an element fruits. Let's remove our apple. Our apple is gone. Coconut,

[2:34:47] orange, banana. We can pop. The pop method will remove whatever element is first. But it's going to be

[2:34:58] random though. Orange, coconut, banana, apple, coconut, banana, apple, banana, coconut. You can clear fruit.

[2:35:12] The elements of our set are gone. Those are a few of the more useful methods for beginners. As a summary, a set is a collection that is unordered and immutable. You can't change the values,

[2:35:23] but adding and removing elements is okay. No duplicates are allowed. Let's try that real quick. I'm going to add a

[2:35:29] second coconut. Yeah, see, we only still have one coconut. Sets may work well if you're working with constants. Maybe

[2:35:39] colors for example. You need to find if a color is within a set. All right. Now

[2:35:44] lastly, let's talk about tpples. A tpple is a collection that is surrounded with a set of parenthesis. Tpples are ordered and unchangeable. Duplicates are okay. One

[2:35:55] benefit of a tpple over a list is that tpples are faster than lists. If you're working with a collection, and it's okay if the collection is ordered and unchangeable, you might as well use a tpple because it's faster. When I print our tpple, all of these values are surrounded with a set of parenthesis.

[2:36:12] Again, we have the dur function to display the attributes and methods. There's not as many for a tpple. For methods, we only have count and index.

[2:36:20] Again, there's also help to display a description of these attributes and methods. You can find the length of a tpple with the length function. We have five elements within here. Using the in operator, we can find

[2:36:34] if a value is found within our tpple. Our pineapple is not within our fruits. So there's only two methods we have access to. Let's find the index of

[2:36:45] apple. Fruits.index apple. Then I will print

[2:36:50] whatever is returned. Apple is found at index zero. There is also count fruits.ount how many coconuts are found

[2:37:02] within our tpple fruits. Count the coconuts. Then print this. How many coconuts? We have two

[2:37:13] coconuts. And then again with any of these collections, they're iterable. So you can iterate over them using a for loop. Four fruit and

[2:37:22] fruits. Yep. Apple, orange, banana, coconut, coconut. All right, everybody.

[2:37:27] So, those are collections. Think of them as a single variable used to store multiple values. There's four general purpose collections for beginners.

[2:37:36] Lists, sets, tpples, and then dictionaries, which we'll talk about next. Each of them has unique benefits. Lists are ordered and changeable.

[2:37:46] Duplicates are okay. A set is unordered and immutable, but adding and removing elements is okay. No duplicates allowed.

[2:37:54] A tpple is ordered and unchangeable. Duplicates are okay and they are faster than lists. Use tpples if you can over a list. But yeah, those are a few

[2:38:04] collections in Python. Hello everybody. Today we will be creating a shopping cart program.

[2:38:12] This program will be an exercise to follow the previous lesson on lists, sets, and tpples. The more that we practice with those collections, the better we'll be at using them. So, I thought we'd create an exercise to get the hang of it before moving on. In this

[2:38:26] program, we will have two lists. Foods. These lists will be empty. We'll declare

[2:38:31] them, but not use them quite yet. And prices, then a total. Total equals zero.

[2:38:40] The reason that I'm not using tpples is that tpples are unchangeable. We're going to ask a user what food they would like to buy. We can't append any elements to a tpple. We're not using

[2:38:51] sets because sets are unordered. I mean, I guess technically you could, but at the end of this program, I'm going to print our shopping cart in order. So, I think lists would probably be the best.

[2:39:01] We have an empty list of foods and an empty list of prices. We'll use a while loop. While true. If our condition is set to true,

[2:39:12] we'll need some way to break out of the while loop. We'll need a break statement somewhere. We'll get to that later. We will ask the

[2:39:19] user what food would they like to buy. Let's declare variable food equal to input enter a food to buy. To exit the while loop, you need to press Q to quit.

[2:39:40] Then let's check if food is equal to Q lowercase Q then we will break. We're not done with the program but let's at least test it. Pizza hamburger hot dog Q to quit. Okay, it

[2:40:01] looks like it works. Now, what if somebody types in uppercase Q? Pizza hamburger uppercase Q. Well, we

[2:40:11] can't actually quit. After accepting our user input, if food lower method, this will take our input, make it lowercase just for a comparison. Let's try that again. Pizza hamburger.

[2:40:30] I'll type capital Q to quit and that is valid. Follow food with the lower method to temporarily make the user input lowercase just in case they type in capital Q. If the user doesn't want to quit, let's add an else statement. Else, let's take our foods,

[2:40:49] use the append method, then add whatever food the user typed in. We'll also need a price. Let's ask a user for the price.

[2:41:00] price equals input enter the price of let's use an F string a whatever food the user types in pick a unit of currency I'll pick dollars we are working with numbers we should type cast our input as a floatingoint number since we're working with prices so we will accept a price. Add our food item to our list of foods. Do the same thing with prices.

[2:41:36] prices.append whatever the price was. And that is the while loop. Let's

[2:41:42] test this program again to be sure that everything's working. Pizza. Pizza will be $5.99. Enter a food to buy. Hamburger.

[2:41:54] Hamburgers will be 350. Hot dog. Hot dogs will be 175. I

[2:42:00] would like to quit. I will type either capital Q or lowercase Q. Both will work. And we have escaped the while

[2:42:06] loop. So the while loop is now complete. Outside of the while loop, let's display our shopping cart. Let's print some

[2:42:13] decorative text. Maybe five dashes your cart. Then another five dashes.

[2:42:22] I will then iterate over all of the elements found within my foods list. For every food in my list of foods, let's print each food item. Let's take a look so far. Again, we have a

[2:42:40] pizza. The price was $5.99. Hamburger, the price was

[2:42:46] 350. Hot dog 175. Q to quit. Okay, your

[2:42:53] cart that will display the individual list items. If you would rather have these list items arranged horizontally in one line, you can add this keyword end equals. This end keyword will replace the new line character at the end of a print statement with some other character like a space. Let's try that

[2:43:13] again. I'll try not to take too much time. Pizza 5.99.

[2:43:23] Hamburger 350. Hot dog 175. Q to quit. Yeah, that's much

[2:43:33] better. We are horizontally listing all of the different items within our list. You could revert back to the vertical list if you'd prefer that. I'll keep my

[2:43:41] output like this. Then we will need to iterate and add up all the prices. For every price in prices, we do have a total variable that we declared. Let's utilize that. Total

[2:43:55] equals total plus price. Otherwise, we could shorten this to plus equals price. That would do the same thing. Then we will display the

[2:44:07] total. Print. I'll use an fstring.

[2:44:11] Your total is I'll add a unit of currency. I picked the dollar sign. Whatever the total is. Okay, let's run this program one

[2:44:23] last time. Enter a food to buy. Pizza, which was $5.99. Hamburger, which was 350. Hot

[2:44:35] dogs, they are 175. Q to quit. Here's your shopping cart. I'm

[2:44:42] just going to add one new line real quick right before we display the total. Just an empty print statement. Here are the results. Your

[2:45:00] cart, pizza, hamburger, hot dog. Your total is $11.24. All right, everybody. Well, that

[2:45:07] is a shopping cart program. I thought this would be a fun exercise to follow the previous lesson on lists, sets, and tpples. And well, yeah, that is a shopping cart program in Python. Hey, what's going on everybody?

[2:45:23] So, today I'm going to be explaining 2D lists. 2D meaning two-dimensional. You do also have the capability of creating 2D tpples. I thought today we would use

[2:45:32] 2D lists just because they're pretty flexible. A two-dimensional list is just a list made up of lists. It's really useful if you ever need a grid or matrix of data, kind of like an Excel spreadsheet. Let's create three lists. A

[2:45:47] list of fruit, vegetables, and meat. I'm going to speed up this video. Feel free to pause if you need to catch up.

[2:46:11] Here I have three lists. A list of fruit, vegetables, and meat. Each of these lists is a one-dimensional list.

[2:46:19] To create a two-dimensional list, well, you would begin by creating a one-dimensional list. Let's create a list of groceries. All I would need to do is add my individual lists as elements to the outer list, the 2D list. We have fruits,

[2:46:35] vegetables, and meats. Normally, to print a list or your other collections, you would print the name of the list. In my list, fruits, I have apple, orange, banana, coconut. To access or

[2:46:51] change one of the elements, you would type the name of the list, then use the index operator. So fruits at index of zero is a pineapple. Again, with a 2D list, it's a little different. If I were to print my 2D list

[2:47:05] of groceries, we would lay out the entire 2D list flat. We have individual lists separated with a comma, all enclosed within a set of square brackets. Taking the elements found within our 2D list, I'm going to line these up kind of like this. It kind of represents a grid or

[2:47:24] matrix with rows and columns. Each individual list resembles a row. Each element resembles a column. If I were to

[2:47:32] print groceries at index zero in place of returning one element found within one of the lists, that would return an entire row. So groceries at index zero is my fruits list. Groceries at index one is my vegetables list. groceries at

[2:47:51] index 2 is my meats list. For one of the elements found within one of the rows, you would need two indices. If I need the apple from the first row within my 2D list of groceries, that would be row 0, column 0. It's kind of like coordinates. Row 0,

[2:48:10] column 0. That would be my apple. 01, which is an orange.

[2:48:18] 02 is banana, 03 is coconut. For the next row, I would set the first index to be one. Row one, column zero, that would be celery. I'm going to speedrun this real

[2:48:32] quick just to show you all the different elements. 1 one is carrots, one two is potatoes. If we try to access 13, that index is out of range because we only have three elements within this row. So then the next row would have an

[2:48:49] index of two. Column 0 would be chicken. 2 1 is fish. 2 is

[2:48:58] turkey. 2 3 is out of bounds. To access an element from a 2D list, you would need two indices in place of one because using just one would return the entire row like so. Now, when you declare a 2D

[2:49:13] list, you don't need to necessarily give each inner list a name. We could do something like this. I'm going to replace these names with the rows. I'm just going to put these on a

[2:49:29] new line to make it more readable. There, that would work, too. Just separate each inner list with a comma, then enclose everything with a set of square brackets. If you ever need

[2:49:45] to iterate over the elements of a 2D list, you can use nested loops. If I were to use a single for loop, let's say for every uh maybe collection, for every collection in groceries, let's print what our collection is. Using a single for loop would iterate over the rows. But to also

[2:50:11] iterate over the elements found within each row, we would use a nested loop. for every food in our collection. Let's print what our food is. Using nested loops, we can iterate

[2:50:30] over all of the elements found within our 2D list. But I'm going to make this more organized like that grid structure we have. I'm going to replace the new line character at the end of a print statement with a space.

[2:50:42] Then when we exit the nested loop, I will print a new line by using just an empty print statement there. That kind of resembles our grid structure, we have rows and we have columns. With two-dimensional collections, you're not limited to just lists. You could create

[2:51:00] a list of tpples. So the inner rows will be surrounded with a set of parenthesis. You know, this is also valid too. Or you could make a 2D tpple.

[2:51:13] It's a tpple that's made up of tpples. You could make a tpple made up of sets. Sets are enclosed with a set of curly braces. Here we have a tpple made of

[2:51:28] sets. Use whatever is best for your own programs. Let's go over an exercise.

[2:51:34] Let's create a two-dimensional keypad that you would normally find on a phone. We have three data types. a list, a set or a tpple. The elements in a set are

[2:51:44] unordered, so we can't use that. These numbers need to be in order. If we have the option, a tpple is faster than a list. A tpple is ordered and

[2:51:53] unchangeable, so we should use it if we can, and that's perfectly fine. Let's create a 2D tpple this time. I will name this 2D tpple numpad. We have an outer set of

[2:52:05] parenthesis, then an inner set of parenthesis for each row. We will have four rows. The first row will be 1 2 3. The

[2:52:17] second row, I'm going to put this on a new line. 4 5 6. The next row will be 7 8 9. Then the

[2:52:28] last row will be an asterisk character. Then zero. Then the pound sign. So numpad in

[2:52:37] this case is a 2D tpple. Let's use a for loop to iterate over every row. This will be the outer loop. For every maybe

[2:52:47] row for every row in numpad, let's begin by printing our row. So we're printing every row in our numpad, but I'd like to remove the parenthesis. Let's create a nested loop for every maybe num for num in row. Print whatever that num

[2:53:16] is. We have one long vertical line. Let's replace the new line character at the end of our print statement with a space. Then when we escape the nested

[2:53:28] loop, let's print a new line. And there is our telephone number pad. You can see it's a grid made up of rows and columns. So yeah, that's a 2D list.

[2:53:40] Well, a 2D collection. It's a collection that's made up of collections. Then with our numpad, we made a 2D tuple. If you

[2:53:48] ever need a grid or matrix of data, a 2D collection would work perfect. And there you have it, everybody. Those are 2D collections in Python.

[2:54:00] Hello again everybody. So today we're going to create a quiz game in Python. Let's declare all of the different collections and variables that we'll need. First we will need a tuple of

[2:54:11] questions, a 2D tuple of options. My quiz will have five questions, but you can add more or less questions. Then a tuple of answers.

[2:54:28] A list of guesses. We will be appending guesses to our list. That's why we're using a list rather than a tpple. A score variable, which I will

[2:54:39] set to be zero. Then question number. This variable will keep track of what number question we're on. All

[2:54:46] right, let's begin with our questions. I have five. Here are my questions. They're all

[2:55:16] science related. Feel free to choose your own. This is what I have. How many

[2:55:21] elements are in the periodic table? Which animal lays the largest eggs? What is the most abundant gas in Earth's atmosphere? How many bones are in the

[2:55:30] human body? Which planet in the solar system is the hottest? These are the questions, but we'll need options. Let's

[2:55:37] add four options for every question. That's why we're using a two-dimensional tpple. Each inner tpple will consist of four elements.

[2:55:54] They will be options A, B, C or D. Let's copy these elements then paste them within each tpple. This first element corresponds to my first question. How many elements are

[2:56:13] in the periodic table? I'll come up with some answers. I'll add some answers for the rest of these tpples, too.

[2:56:50] We have a tuple of correct answers. The orders are C, D, A, A, B. If you come up with your own options, your answers may be different.

[2:57:08] Now that we have all of our different collections and variables taken care of, let's display each question. I will iterate over our tpple of questions. They are iterable. For every question in

[2:57:22] questions, I'm going to print some decorative text. I think that's probably good. Then I will print each question we're iterating over. So let's see what

[2:57:36] we have so far. There's all five questions. After we display every question, I need to display every option for every option in options. Our options options is a 2D

[2:57:55] tuple. Let's add the index operator. The index is going to be our question number variable. It's a number. So at first

[2:58:05] we're accessing options at index of zero. Then 1 2 3 4 5. We will print every option in options. Add a given row number. Let's

[2:58:19] test this. Okay, we have some options. But all of these options are for the first question. We will need to

[2:58:27] increment our question number. So let's do that. Maybe here.

[2:58:34] question number plus equals 1. That is much better. Before iterating the question number, we will ask the user for a guess. Guess equals

[2:58:53] input enter A B C D. In case the user types in something that's lowercase, I will follow this input with the upper method to make the user input uppercase. We will take our list of guesses, use the append method, add our guess to that list. If our guess is equal to the

[2:59:26] answers tpple at index of question number that means the user guessed the right answer. Let's increase the user score. Sc score score plus equals 1.

[2:59:38] Then print the word correct. Correct. Else we will print incorrect.

[2:59:51] I'll use an fstring. Our answers at index of question number is the correct answer. All right, let's answer some of these questions. C. Correct. Which animal lays

[3:00:16] the largest eggs? Um, definitely the whale because the whale is the largest creature, right? Incorrect. D is the correct

[3:00:25] answer. What is the most abundant gas in Earth's atmosphere? Nitrogen. Correct.

[3:00:30] How many bones are in the human body? D. That is incorrect. A is the right

[3:00:34] answer. Which planet in the solar system is the hottest? Mercury, because it's closest to the sun, right? Wrong. Incorrect. B is the

[3:00:43] correct answer. We're keeping track of our answers successfully. Once we complete all the questions, let's print the results. I'm going to add some

[3:00:53] decorative text. Not necessary, but I think it would look cool. I will display the results. We will iterate over all of the

[3:01:08] answers and the guesses. Print answers. I'm going to set the ending character to be an empty string for every answer in answers.

[3:01:32] Print each answer. I will set the ending character to be a space to separate each answer. Then I'll add a new print line. Let's do this with

[3:01:46] guesses. Change answers to guesses for every guess. In guesses, print each guess. Okay, I'm going to run this

[3:01:58] again. I'm just going to make up some answers. A B C D A. Here are the correct

[3:02:06] answers. Here are the guesses. I guess none of them right. Then we will print a

[3:02:12] score. Score equals take our score divided by I'm going to use the length function. Then pass in our questions.

[3:02:23] How many elements are within our questions tuple then I will multiply all of this by 100 to give us a percentage. Then type cast this whole formula as an integer. So, we're basically just reassigning our score variable. Then, let's print using an

[3:02:43] fring, your score is our score variable. Then add percent. I'm going to intentionally get all the answers right. C D

[3:02:59] A B. Here are the answers. Here are your guesses. Your score is 100%. This time

[3:03:06] I'll try and get a few incorrect intentionally. C C. Your score is 20%. All right, everybody. Well, that is

[3:03:17] a quiz game. Feel free to add more or less questions or come up with your own questions. And that is a quiz game written in Python. Hey everybody. In today's video,

[3:03:29] I'm going to explain dictionaries. A dictionary is one of the four basic collection types for beginners. A dictionary consists of key value pairs.

[3:03:38] They are ordered and changeable. No duplicates allowed. A few examples of key value pairs could be an ID and a name, an item, and a price. But in

[3:03:48] today's example, we'll create a dictionary of countries and capitals. Let's name our dictionary capitals. Capitals equals enclose your dictionary with a set of curly braces, much like what you do with sets. The first country

[3:04:03] will be the USA. To add a value to this key, type colon then some other value. The capital of the USA will be Washington DC. Separate each key value pair with a

[3:04:19] comma. Then we can add another key value pair. So the capital of India that will be New Delhi. We'll add

[3:04:30] two more. China. The capital is Beijing.

[3:04:39] Russia, the capital is Moscow. I think that's good enough. Just as a reminder, if you would like to see all of the different attributes and methods of a dictionary, you can use the dur function. Pass in

[3:04:52] your dictionary capitals. Then we'll need to print this. Here's all the different attributes and methods of a dictionary. If you would

[3:05:03] like an in-depth description of all these attributes and methods, you can use the help function. Uh, that's herp help. There we go. So, yeah, that's just a

[3:05:20] reminder. All right, let's go over a few of the methods. To get one of the values from a dictionary, you would get the key. Type the name of the dictionary.

[3:05:31] Capitals.get. Let's get the capital of the USA. Then we'll print

[3:05:39] it. The value associated with this key, the USA is Washington DC. If I picked a different country like India, well then we would get that associated value which is New Delhi.

[3:05:54] Another thing, if Python doesn't find a key, this is what will be returned. Let's get Japan which is not in our dictionary. This method would return none. We can use this within an if

[3:06:08] statement. If capitals get Japan if a value is returned then we will print that capital exists else we will print that capital doesn't exist so Japan is not in our dictionary that capital doesn't exist but Russia is that capital does exist. That's how to check to see if a key is within our dictionary. You can use the get

[3:06:47] method. All right, moving on. Let's update our dictionary.

[3:06:54] Capitals.update. So within a set of curly braces, I will add a key then a value.

[3:07:03] Germany followed by Berlin. Then let's print our dictionary. I'll use a print statement.

[3:07:11] Print capitals. Yeah. And there's Germany right there. Using the update method, we

[3:07:18] can insert a new key value pair or update an existing key value pair. Let's also change one of the existing values with our key USA. Let's update the capital to be Detroit. Yeah, see the value has been

[3:07:34] updated. The capital of the USA is now Detroit, Michigan. To remove a key value pair, you can use the pop method. Then pass in

[3:07:44] a key. Let's remove China. China no longer exists within our dictionary. It's gone. You can remove

[3:07:52] the latest key value pair within a dictionary by using the pop item method. Capitals do pop item. With pop item, you don't need to pass in a key. Pop item

[3:08:06] will remove the latest key value pair that was inserted. Then we have clear capitals.clear. That will clear the

[3:08:15] dictionary. It's pretty self-explanatory. The next few methods are a little tricky to explain. To get

[3:08:22] all of the keys within the dictionary, but not the values, there is a keys method. Capitals. I think I'm going to insert this within a variable keys equals capitals keys.

[3:08:37] Let's see what happens when we print this. The keys method will return all of the keys within our dictionary. Technically, keys is an object which resembles a list. I haven't discussed

[3:08:49] object-oriented programming yet. This is a little bit above our level. If you ever need the keys in a dictionary, you can use the keys method. One use is that

[3:08:57] we can use that within a for loop. They're iterable. For every key in capitals keys method, let's print every key. If at any time you need to iterate

[3:09:12] over all the keys, you can use a for loop to iterate over every key that is returned from the keys method of your dictionary. There is also the values method to get all of the values within your dictionary. There is a values method. Values equals capitals do values

[3:09:34] method. Then let's print our values. Like before with the keys method, the values method will return an object which resembles a list. Let's

[3:09:46] iterate and print over every value within our dictionary. for every value in capitals do values. Print every value. Here are all the values within

[3:10:05] our dictionary. This next one is probably the most tricky. It is the items method.

[3:10:11] Capitals do items. I will assign what is returned to a variable named items. Then we will print items.

[3:10:22] items returns a dictionary object which resembles a 2D list of tpples. It's really complicated. How might this be useful? This time we're going to use a

[3:10:31] for loop to print every key, value in capitals do items method. We have in essence two counters. This time I will print using an fstring every key value pair. I will print every

[3:10:51] key as well as every value in our print statement. So there's our dictionary laid out. We have iterated over every key value pair. It's kind of an advanced

[3:11:03] topic, but I thought I would at least bring it up now. So yeah, that's a dictionary, everybody. It's a collection of key value pairs. They are ordered and

[3:11:11] changeable. No duplicates allowed. You have a bunch of different methods such as get, update, pop, pop item, clear.

[3:11:19] Then you can get the keys, the values, or both, which is the items method. We'll be using dictionaries in a few game programs we'll be making in the future. And well, yeah, those are dictionaries in Python. Hey everybody. Today we will be

[3:11:35] creating a program to mimic a concession stand, much like what you would see at a movie theater. We will be utilizing a dictionary to keep track of a menu item and an associated price. More or less, this is just a program to help us get used to working with dictionaries. Let's

[3:11:50] begin. We'll create a dictionary named menu. What items are on the menu? We'll

[3:11:56] need an item and a price. I'll think of some. I'm going to speed up this video.

[3:12:00] Feel free to pause if you need more time. and here's my menu, everybody. I thought of a few food items you might find at a movie theater concession stand. Pizza,

[3:12:25] nachos, popcorn, fries, chips, soft pretzels, soda, lemonade. Movie theater popcorn is really expensive for some reason. Okay, we have our menu. A user

[3:12:35] is going to select specific keys from this menu. Depending on what the key is, we can get the associated value to calculate a total. To keep track of the user selected items, I will create an empty list named cart. I will also

[3:12:49] declare a variable named total to keep track of the total. We need to lay this dictionary down flat to display it to a user. Well, we do have the items method of a dictionary which we covered in the last video. for every key value in our

[3:13:06] dictionary menu dot items method. The items method of our dictionary will return a key and a value during each iteration. I'm simply going to print every key and value. I'll use an

[3:13:21] fstring. I will print every key colon space then a value. Let's take a look so far.

[3:13:32] Here's our menu. I'll make a few changes. The price will be in dollars and cents, but feel free to pick your own unit of currency. I'll preede my

[3:13:41] value with the dollar sign. Then using a format specifier, I will display two decimal places 2F. That's better. I will line up all

[3:13:54] the keys. After the key, I will add a format specifier. then allocate 10 spaces. Yeah, look at that. It's all

[3:14:04] lined up. Now before and after displaying our menu with this for loop, I will add some decorative text. Let's say menu. Then outside of the for loop, I'll

[3:14:22] display a bunch of dashes. Yeah, look at that. Let's move on to the next step. We will ask a user for some input.

[3:14:36] What item would they like to buy from the menu? While our condition will be true. If our condition is set to true, we'll need to break out of this loop one way or another. We will ask for some

[3:14:48] user input. food equals input select an item Q2 to quit. If food is equal to a lowercase Q, then we will break. Let's test

[3:15:12] it. Select an item. Pizza, nachos, soda, Q to quit. Yeah, it works. Okay.

[3:15:23] What if the user types in capital Q? Well, we can't escape the while loop. If a user types in capital Q, we're assuming that they would like to quit. When we accept our user input, I'm

[3:15:36] going to add dot lower method. This will take our user input and make it all lowercase. So, we should be able to acknowledge any uppercase letters. Yeah,

[3:15:47] it works. Cool. Let's add an else- if statement. What if a user types in an

[3:15:54] item that's not on our menu? Well, there is a get method of dictionaries. If menu get pass in our food which is user input. If the user selection is not

[3:16:09] within our menu as a key it will return none. So we can use that else if menu.get food is not none then we would like to append that food item to our cart. cart.append

[3:16:30] append our food item. So, outside of the while loop, I'm going to print our cart temporarily just to test it. Okay, select an item. Pizza,

[3:16:46] soda, pretzel. How about a potato? Q to quit. We have our pizza,

[3:16:54] soda, and pretzel, but not our potato. We don't want that in our cart because that's not on the menu. Yeah, you can just add that line. Else if menu item

[3:17:03] get food is not none. That will complete our while loop. Let's calculate a total for every food in our cart. Let's

[3:17:14] take our total variable. Set this equal to total plus. Then we need a value associated with a key plus menu. Get method get the food item found

[3:17:32] within our cart. But I'm going to shorten this to total plus equals menu.get the value associated with this food in our cart. I will also

[3:17:45] display that food item. Print food. I'm going to avoid printing our food item on every line. I will set the ending

[3:17:54] character in our print statement just to be a space. Okay, let's see what we have so far. I would like popcorn, soda, pretzel. Q to quit. Popcorn, soda,

[3:18:10] pretzel. Then we will display the total. I will print a new line.

[3:18:18] print I'll use an fstring total is add a unit of currency total I'll add a format specifier 2F to display two decimal places I'm going to add one line of decorative text let's copy maybe this. All right, let's test it out. Select an item.

[3:19:03] Popcorn, pretzel, soda, potato. Q to quit. All right, here's our cart. Popcorn,

[3:19:14] pretzel, soda. We did not include the potato. That was not found within our dictionary. The total is

[3:19:21] $12.50. Well, there you have it, everybody. That is a concession stand

[3:19:25] program. The point of this program was to help us get used to working with dictionaries. A dictionary is a collection of key value pairs such as an item and a price. And yeah, that's a

[3:19:37] concession standard program in Python. Well, hello again everybody. It's me. In

[3:19:45] today's topic, I'm going to show you how we can generate some random numbers in Python. Then at the end of this video, as an exercise, we're going to create a number guessing program. Let's begin. We

[3:19:55] will be importing the random module. Type import random. The random module gives us access to a lot of useful methods involving random numbers. For a

[3:20:05] comprehensive list, you can use the help function. pass in the random module and then we would want to print this. Here's what we all have access to.

[3:20:19] We have a shuffle method, set state, seed, sample, random range, random, random int, random bytes, and there's a ton of others, but we'll discuss a few of the more useful methods for beginners. For a random whole integer, maybe you're rolling a six-sided dice. You would type the name of the random module dot then a method. For a random

[3:20:42] whole integer, type rand int add a set of parenthesis. Within the set of parenthesis, you will list a range. If I'm rolling a six-sided dice, I would like the numbers 1 through 6, 1, 6. Then

[3:20:56] I will assign what is returned to maybe a variable. print whatever my number is. My random number is a four, three, one, four. All right. I tend to play a

[3:21:12] lot of Dungeons and Dragons. We use polyhedral dice that have more or less than six sides. There is a 20sided dice.

[3:21:20] For a random number between 1 and 20, I would set the range to be 1, 20. Here I rolled a 16 and a seven and an eight. Within the rand int method, you can place variables as well as long as they contain numbers. I will create a

[3:21:37] variable named low. I'll set that equal to one. And a variable named high. I will

[3:21:43] set that to be 100. I will replace the numbers with my variables that behave as numbers. Give me a random integer between my low variable and high variable. So between 1 and 100 in this

[3:21:57] example, I have rolled a 75. Now in 88, if you need a random floatingoint number, you can use the random method. Random.random. Then let's assign this to

[3:22:09] a variable. Number equals the random method of the random module. That would return a random floatingoint number between 0 and 1.

[3:22:21] You can pick a random choice from a sequence. In the future, we're going to create a game of rock paper scissors. Let's say we have a tpple of options. Options

[3:22:34] equals rock paper scissors. We are accessing the random module. Dot. Then use the choice method.

[3:22:46] Place your sequence within the choice method. give me a random choice from options. I will store this within a variable. Let's say option equals random

[3:22:58] choice from my options. Then I will print the option. Our computer has generated scissors, paper, rock. So the choice method is a

[3:23:10] great use for games if you ever need a random element. Now there's also shuffle. This time maybe we have a deck of cards.

[3:23:19] cards equals I guess I'll use a list this time. I have a list of cards that you would normally find within a deck of playing cards. Well, besides the suit 2 through 10, Jack, Queen, King, Ace.

[3:23:42] Using the shuffle method, I can shuffle this sequence. Access the random module. Shuffle. Pass in your

[3:23:51] sequence. In my case, it's cards. Then I will print cards. Yeah, look at that. My cards are

[3:23:59] now shuffled. In the future, we'll be creating a game of blackjack. The shuffle method will be used then to shuffle our deck of cards. Those are a

[3:24:07] few methods found within the random module. For some practice, let's create a number guessing game as an exercise. Hey everybody. So today we're

[3:24:18] going to create a number guessing game using Python. This is a project meant for beginners. By completing this project, it will help us reinforce our understanding of previous topics. Let's

[3:24:27] begin. We will import the random module. We'll need to pick a random number. The

[3:24:34] random module is going to handle that for us. What is the range of random numbers for our number guessing game? We'll store those as variables.

[3:24:43] We will have one variable named lowest number. I'll set that to be one as well as a variable for highest number which I will set to be 100. Feel free to pick a different range if you would like. I'll

[3:24:57] set the range to be 1 through 100. A random number will be selected between this range which will be stored within a variable named answer. What is the correct answer? So to choose a random

[3:25:10] number between these two values, we will access the random module called the rand int method. We will choose a random integer between these two values. The two arguments will be lowest num, highest num. For the second

[3:25:31] argument, let's perform a test run. I will print my answer. the number is going to be between 1 and 100. Okay, we know that that

[3:25:46] works. Here's a few more variables. We need to keep track of the number of wrong guesses which I will store as a variable named guesses. We want the user to keep

[3:25:57] guessing as long as our application is running. We will create a boolean variable of is running which we will set to be true. Once the user wins the game, we will set is running to be false. We will print a welcome

[3:26:17] message. Let's say Python number guessing game. We will prompt the user. I'll use

[3:26:28] an fstring. Select a number between. I'll add two placeholders. Select a number between

[3:26:41] our lowest number and our highest number. Python number guessing game. Select a number between 1 and 100. Now,

[3:26:52] if I was to change the range of these variables, that should be reflected temporarily. I changed the lowest number to be 10 and the highest number to be 1,00. But let's set that back. Between one and 100 is

[3:27:09] good. We'll need a while loop to continue the game each round. We will say while is running. Since is running is a boolean,

[3:27:21] we don't need to say while is running equals true. We can just say while is running while this value remains true. Continue playing the game.

[3:27:31] We will ask the user for some input. We will create a local variable of guess. Guess equals use the input function. Then

[3:27:42] enter a prompt. Enter your guess. There's one thing we want to check. Python number guessing game.

[3:27:52] Select a number between 1 and 100. Enter your guess. What if somebody doesn't type in a number like they type in the word pizza?

[3:28:00] We should let the user know that that's an invalid guess. We'll write the following if statement. If our guess use the is digit method. If our guess is a digit a

[3:28:16] number, then we will execute any code underneath this if statement. For the time being, I'll write pass. We'll get back to that later. Else we will do

[3:28:25] something else. Let's print the following. print invalid guess. Let's copy this print statement

[3:28:37] because I'm lazy and I don't feel like typing it out. Please select a number between our lowest number and our highest number. Let's try that again. I will guess pizza, which isn't a

[3:28:54] number. And we get the message invalid guess. Please select a number between 1 and 100. All right, that works.

[3:29:04] Underneath our if statement, we'll write the following. Once we get a guess that is a digit, we need to convert it to a number because when you accept user input, it's a string. We will reassign our guess equal to type cast our guess as an integer.

[3:29:24] Then increase the number of guesses by one. Guesses plus equals 1 because we have already made one guess. Here's another scenario. What if somebody guesses a

[3:29:36] number outside of this range like one cajillion? Well, we should give a warning that that guess isn't valid. If our guess is lower than the lowest number or our guess is greater than the highest number, we will print the following. That number is out of

[3:30:08] range and I will reprompt the user. Please select a number between the lowest number and the highest number. Let's perform a test run. I will

[3:30:23] guess one cajillion. That number is out of range. Please select a number between 1 and 100. We'll add an else if statement.

[3:30:34] Else if our guess is less than our answer, we will print the following. too low. Try again. Else if our guess is greater than

[3:30:53] our answer, we will print to high. Try again. If our guess isn't less than our answer and our guess isn't greater than our answer, that means we must have the correct answer.

[3:31:10] within an else statement we will print. I'll use an F string. Correct. The answer was insert our

[3:31:23] answer, our answer variable. Then print the number of guesses it took. Number of guesses. Add a

[3:31:34] placeholder. Place in our guesses within the placeholder. Now to escape the while loop, we will take our boolean variable of is running, which is normally true, and set that to be false to escape. And that should be all we need.

[3:31:50] Let's run this one last time. Python number guessing game. Select a number between 1 and 100. Let's

[3:31:57] select a number right in the middle. 50. Too low. Try again. So the number is

[3:32:02] between 50 and 100. 75. Too high.

[3:32:08] It's between 50 and 75. Then 62. Too high.

[3:32:18] 56. 53. 55. Correct. The answer was 55. Number

[3:32:26] of guesses. It took me six. All right, everybody. That is a

[3:32:30] Python number guessing game you yourself can create as a mini project. Hey everybody. In today's topic, I thought we would create a game of rock paper scissors. Now that we know how the

[3:32:43] random module works, let's begin by importing the random module. We will create some options. We will use a tpple. We're not going to be changing

[3:32:53] the options. So a tpple would be better than a list. We have three options.

[3:32:59] Rock, paper, or scissors. I'll create a variable named player to store the player's choice. For now, I'm going to set this to be none as well as a computer. Our computer is going to

[3:33:15] pick a random choice from these options. Rock, paper, or scissors. In order to do so, we can use the choice method of the random module.

[3:33:26] Random.choice. Pick a random choice from options.

[3:33:32] Let's have the player enter in some input. Enter a choice. Rock, paper, scissors. Then we will display the

[3:33:52] player's choice and the computer's choice. I'll use an fstring player colon space the variable player. Let's copy that. Paste it. Then

[3:34:08] change player to computer. Let's see what we have so far. Enter a choice. Rock, paper,

[3:34:18] scissors. So, I pick rock. The computer picks scissors. Let's try it again just

[3:34:24] for good measure. I pick paper. This time the computer picks scissors. I pick scissors. The computer

[3:34:31] picks paper. Okay, we know that the computer is successfully picking a random choice from our options. Now, what if the player picks something that's not within this tpple such as the gun? Well, we would want to stop that,

[3:34:45] right? We need the user to pick a valid option. Only rock, paper, or scissors. I

[3:34:50] think what we'll do is that when we accept the user input, let's place it within a while loop. So indent this line while this condition is going to be kind of weird. While our player variable is not in our tpple options. Let's try

[3:35:10] this again to see what happens. I pick the gun. Enter a choice. All right.

[3:35:15] Well, if I can't pick a gun, how about a sponge? Well, I can't pick that either. Rock.

[3:35:21] That works. Our condition is while the player variable is not found within our options. If the player doesn't pick one of these options, this while loop will continue forever. Once we pick something

[3:35:36] that's within our options, we then escape the while loop. Let's check some win conditions. Now if the player is equal to computer that means it's a tie.

[3:35:48] I will print it's a tie. I'll add a few else if statements. Else if the player is equal to rock I'll use the and logical operator and the computer is equal to scissors. That means you win.

[3:36:11] Let's print you win. Let's add another condition. Else if the player picks paper and the computer picks rock, then you also win. You

[3:36:34] win. L if the player picks scissors and the computer and the computer picks paper then we will print you win. else. If the player's choice is not the

[3:36:58] same as the computers and we don't meet any win conditions, that must mean we lose. Print, you lose. Let's see if this works. Enter a

[3:37:11] choice. Rock, paper, scissors. I pick the gun. Nope, I can't pick that. I pick

[3:37:15] rock. I pick rock. The computer picks scissors. You

[3:37:19] win. Let me see if I can lose. I'll pick paper.

[3:37:24] You win again. Scissors. I need to stop winning. I need

[3:37:29] to see if the lose condition works. Okay, it's a tie at least. But I need to lose. All right, there we go. I pick

[3:37:38] rock. The computer picks paper. You lose. What if the user would like to

[3:37:42] play again? Let's place all of this code within a while loop. Let's do so right about here. Now I'm not going to write

[3:37:51] while true like I normally do. This time I'm going to create a variable. Let's say running. Is our game running? I will

[3:37:59] set that to be true. While running equals true or we could shorten this to just while running. That's simpler. I will place all of this code

[3:38:14] within the while loop. To mass indent some code, just highlight all of the code, then press tab. Hey everybody, this is Bro from the future. I forgot to

[3:38:23] explain something. The reason I'm not setting the condition of my while loop to be true is that if you have a lot of code within a while loop, it can be really difficult to find where the break statement is. If I set my condition to be a boolean variable such as running, it's a lot easier to find any instance where I use this variable. If I were to

[3:38:42] highlight it, we can see that running is found down here. If I need to change any instance of this variable and rename it to something, you can refactor. Let's rename running as maybe playing. Then I

[3:38:55] will refactor. So my variable running is now playing. And that change was made down here too. So it's a coding

[3:39:03] preference. Every time we start a new game, I will reset the player as well as the computer. Let's move these two lines into the while loop at the beginning. So when we start a new game,

[3:39:15] we will reset the player. The computer will pick a new random choice. So let's see what we have so far. Rock. I pick rock. The computer

[3:39:25] picks rock. It's a tie. Then we have to play again. So paper, you lose.

[3:39:32] Scissors. It's a tie. Now what if we would like to escape the while loop after our win conditions? I'm going to

[3:39:39] create a temporary variable. Let's name this play again. Then we will ask for some user input. Play

[3:39:51] again. Y slashn meaning yes or no. If the user types in something that's capital, I'm going to use the lower method to make it lowerase. So if our play again variable

[3:40:05] is equal to Y, we would like to escape. What I would like to do is I would like to see if the player types in something that's not Y. I will preede this condition with the not logical operator. If the user does

[3:40:23] not want to play again, then let's take our boolean variable running. Normally it's true. and set that to be false. Running equals

[3:40:35] false. That means we will escape the while loop. Once we escape the while loop, I will print. Thanks for

[3:40:45] playing. Now, I'm going to change this momentarily. I just want to test it.

[3:40:50] Rock. Play again. Yes. Paper. Play

[3:40:54] again. Yes. Scissors. You lose. Play again. Nope.

[3:41:00] Thanks for playing. This is entirely optional. I try and create as few variables as possible. I would

[3:41:06] personally rather avoid creating a variable here. Another way in which I could write this is that I can get rid of this variable. Let's move if not in front of the input and follow our input here. Then

[3:41:28] use the comparison operator. Then add a colon. If the user's input after making it lowercase does not equal a Y for yes, set running to be false. So that should

[3:41:43] work the same. Rock play again. Yes. Enter a

[3:41:49] choice. Paper. Play again. No. Thanks

[3:41:52] for playing. This line would work the same, but it's a little more complex for beginners to read. or you can use the other method that I showed you. All

[3:42:01] right, everybody. Well, that's a game of rock, paper, scissors. Hello everybody. Today, we

[3:42:08] will be creating a dice roller program in Python. We will be utilizing some ASI art. I'll post all of the ASI art that we'll need in the description of this video. You can copy and paste it to save

[3:42:19] time if you'd like. All right, let's get started, everybody. We will begin by importing the random module because we will be rolling some random numbers between 1 through six. If we're going to

[3:42:30] create some ASI art, we'll be utilizing Unicode characters. To enter in a Unicode character, it really varies depending on your operating system. I think the easiest way would just be to use Python. To enter a Unicode

[3:42:42] character, type a forward slash, then a given code for each character. Here are all of the codes that we'll need. After writing these seven unic code characters, let's run this program.

[3:43:03] These symbols that are output, let's copy them. I'll add them to a comment. Then we can delete this line. These are

[3:43:11] the unic code characters we'll need to build some ASI art, some dice. Each die will be made out of five lines. Let's begin with the first. We'll need a

[3:43:23] left corner, nine dashes, then the right corner. For the second line, copy this vertical bar. Add nine spaces. Then a vertical bar. We can copy

[3:43:42] this whole line. Paste it two times. Let's use the left bottom corner. Add a

[3:43:49] nine of these dashes. Then the bottom right corner. And here's a basic box shape.

[3:43:58] Depending on what the number die is, we can add one of these bullet points. For a one, we can add that right to the middle. So that's good for now. We'll

[3:44:06] delete this later. Let's create a dictionary. I will name this dictionary dice art. Our dictionary is made out of

[3:44:15] key value pairs. So the keys will be the numbers 1 through six beginning with one. The value will be a tpple. It's a

[3:44:25] dictionary made out of key value pairs where the value is a tpple. Within the tpple, let's add these lines each separated with a comma. I'm going to format these so they form a box shape. Let's take our bullet point,

[3:44:55] place it right in the middle, then add a comma to the end of this key value pair. That is the first key value pair. Let's copy all of this. Paste it again. Change one to two.

[3:45:08] Let's move this bullet point. We need two bullet points about right here and here. Let's repeat this process for keys three through six.

[3:45:43] Be sure to get rid of the comma at the end. And here is our dictionary of dice art. Each key is a number. Each value is

[3:45:52] a tuple made of strings. Let's create a list of dice. Our dice will be numbers randomly generated between 1 and six.

[3:46:04] a total to calculate the total. I'll set that to be zero. Then we will ask a user for a number of dice. This will be some

[3:46:16] input. How many dice? Then type cast the input as an integer. We don't want somebody to

[3:46:25] write, you know, 2.5 dice. You can't roll half a dice. To generate a random

[3:46:30] number, you can use the rand int method of the random module. We need a random number between one and six. Then we need to append this number to our list of dice.

[3:46:45] dice.append. Then we can move this line to within the append method. We need to do this a number of

[3:46:52] times depending on how many dice the user enters in. We can place this line within a for loop for every die in our range number of dice. This will be a number. Let's print our list of dice to

[3:47:11] see what numbers we have in here. How many dice? I would like five dice. 5 3 3

[3:47:17] 4 6. Okay, we know that that works. Let's calculate a total. We'll need to iterate

[3:47:24] and sum all of the elements within our list. We can do that with the for loop. For every die in our list dice, take our total variable plus equals the current value within our dice. Then we will print a total. I'll

[3:47:46] use an fstring total colon space. Our total variable. Let's see what we have so far. How many dice? I would like five

[3:47:58] dice. Our total is 19. Now between these two for loops, we will display our ASI art. The easiest way would be to create

[3:48:07] some nested for loops. The outer for loop will be in charge of the number of dice for every die in our range number of dice. The inner for loop will be in charge of printing every tpple. For every line in then to get a

[3:48:36] value in our dictionary, we would type the name of the dictionary dice art then use the get method. What are we getting? We're getting a value at a given key. Let's

[3:48:48] take our list of numbers dice at index of die our counter. Depending on what the user types in for the number of dice, die will begin at one then increment within the inner for loop. We will print the line. So let's take a

[3:49:09] look. How many dice I would like? Three dice. And here's our asky art. 6 + 2 + 4

[3:49:16] that equals 12. If you would prefer, we can display all of these dice on a single horizontal line instead of one vertical line. It's a little more tricky though. If you

[3:49:28] would prefer that approach, let's turn this chunk of code into comments. We will write this nested loop a little different. So each tpple is made up of five elements, right?

[3:49:43] So, if we're printing a horizontal line, let's say we roll the numbers 1 through three, we would first need to display this line of the first dice, then the first line of the second dice, then the first line of the third dice. During the next iteration of the outer loop, we would display the second line of the first dice, the second line of the second dice, the second line of the third dice. So, it's a little more complex.

[3:50:12] Let's create an outer loop that will iterate five times. For every line in range five, then the nested loop will be for every die in dice. How many dice do we have within our list? We will print. We're going to get

[3:50:36] one of the values found at one of the numbers that we roll. take our dictionary of dice art. Get then a number 1 through six. That will be the value found within

[3:50:52] our list of dice. Get the current die. Remember that this is a number 1 through six. We would then need one of the

[3:51:00] elements found within our tpple. So get the first line, then the second line, third, fourth, fifth. So let's add the index operator. Place our counter of line

[3:51:16] within the index operator. Let's see what we have so far. We need to add one more thing. How

[3:51:22] many dice? Three. This is an abomination. There's

[3:51:27] one more change we need to make. At the end of our print statement, let's set the ending character to be an empty string. And that should fix that. How

[3:51:39] many dice? Three. Okay, we're getting better results. Then when we escape the

[3:51:44] inner loop, we will print a new line. How many dice? Three. And there we are. 3 + 6 + 1 is

[3:51:54] 10. All right, everybody. So, that is a dice roller program. It is kind of

[3:51:59] complex, but I thought this might be a good exercise. If you would like a copy of this code, I will post all of this in the comment section down below. And well, yeah, that's a dice roller program in Python. Hey everybody, today I need to

[3:52:14] explain functions. Think of a function as a block of reusable code. To invoke a function, you place a set of parenthesis after the function name. To invoke it,

[3:52:24] here's a scenario. I need to sing happy birthday three times. I know it's a weird example, but it makes a lot of sense. Just trust me on this. If I need

[3:52:32] to sing happy birthday three times, I would write something like this. I'm going to create my own version of the happy birthday song. This is one verse. If I need to

[3:52:48] repeat this code three times without using functions, I could either repeat this code or maybe place it within a loop. So, here's my happy birthday song three times. But there's a better way of handling this that doesn't involve repeating our code or using loops. What

[3:53:05] if I could write this code once then reuse it whenever I need to? That's where functions come in. To define a function, you would type def then a unique function name. Let's name this

[3:53:17] function the happy birthday function. Add a set of parenthesis a colon. Any code that belongs to the function you'll want to indent underneath. Then to

[3:53:28] invoke this function, I would type the name of the function, happy birthday, add a set of parenthesis, and that's it. When you invoke this function, you will execute this code once. If I need to execute this code three times, I would just call it two more times. Happy birthday. Happy birthday.

[3:53:48] Happy birthday. To invoke a function, you type the function name, then add a set of parenthesis. I like to think of the parenthesis as a pair of telephones talking to each other. You call a

[3:53:58] function to invoke it. Hey, happy birthday function. Execute your code.

[3:54:02] With functions, you are able to send data directly to a function using what are known as arguments. You can send values or variables directly to a function. Place any data within the set of parenthesis. I'll send my function a

[3:54:15] first name. Any data you send a function are known as arguments, but you need a matching set of parameters that are in order. What exactly is the data we're sending in? Well, it's a name. I will

[3:54:27] add one parameter to my happy birthday function. I will name this data name. A parameter is kind of like a temporary variable that's used within a function.

[3:54:37] I'm going to replace this instance of u with a name. I will use an fstring. Replace U with a placeholder. I

[3:54:46] will add my parameter name. So, happy birthday to bro. We could pass in some other names. What about

[3:54:57] Steve and Joe? Here we are. Happy birthday to bro.

[3:55:04] Happy birthday to Steve. Happy birthday to Joe. When you invoke a function, you can send more than one argument. Let's

[3:55:11] send an age this time. I'll send 20, 30, and 40. But when I run this, we have an error. We're passing in two

[3:55:23] arguments, but our function is set up only to take one. I would need a matching number of arguments. To invoke this function, we will need two parameters. We have a name and we have

[3:55:35] an age. Then let's use this age. You are.

[3:55:40] Let's make this line an F string. age years old. Let's try that again. Happy birthday to bro, you are 20

[3:55:53] years old. Happy birthday to Steve, you are 30 years old. Happy birthday to Joe, you are 40 years old. When you invoke a

[3:56:00] function, you can pass in some data. Those are known as arguments, but you'll need a matching set of parameters. The order does matter. Let's see what

[3:56:08] happens when I switch these two parameters. age then name. Happy birthday 220, you are bro years old. Happy birthday 230, you are

[3:56:20] Steve years old. Happy birthday 240, you are Joe years old. So the position of the parameters does matter. Same thing

[3:56:28] goes with the arguments. You also could name these parameters something unique. Maybe X and Y. Happy birthday to X. You

[3:56:37] are Years old. That's also valid. Let's try another example. I'm going to create a function

[3:56:44] to display an invoice. There will be three parameters, a username, an amount, and a due date. Let's print hello. I should make

[3:57:02] this an F string. username. We'll use another fing your bill of amount. Let's precede this placeholder

[3:57:21] with the unit of currency. I will also add a format specifier 2F is due on our due date. whatever that parameter is. To invoke this function,

[3:57:36] we will type the function's name, add a set of parenthesis, a username, an amount, and a due date. Let's make up some username, an amount, I guess $42.50. I'm just making up a number

[3:57:51] here. Then a due date, the 1st of January, I guess. Here's my invoice.

[3:57:57] Hello, bro code. Your bill of $42.50 50 cents is due on January 1st. Let's

[3:58:03] change these arguments. Joe Schmo is the username. He owes $100 and one penny.

[3:58:11] Due on the 1st of February or January 2nd, depending on how you read dates in your region. Hello, Joe Mo. Your bill of $1001 is due on 1/2. That's another

[3:58:24] example. Now, we need to explain the return statement. Return is a statement that is used to end a function and send a result back to the caller. Here's an

[3:58:34] example. We have a variable Z. Z will equal we'll invoke a function to add two numbers together such as the numbers 1 and two. When we invoke a function, we

[3:58:46] can send some data back. After adding 1 and two, we will send the result which would be three. Then this value can be assigned to a variable. then we can

[3:58:57] print whatever Z is. So let's create some functions. Let's create a function to add two numbers together. The

[3:59:04] parameters will be X and Y. Let's say Z equals X + Y. Then we will return our value Z. So I'm not going to

[3:59:18] print Z directly right now. Let's subtract X and Y. Subtract Z = X - Y. Return

[3:59:30] Z. Multiply X * Y then divide. X / Y return Z. Let's invoke our

[3:59:48] add function. Pass in two numbers, one and two. Then I'm going to print the result. After adding these two numbers

[3:59:58] together, the result is three. What about subtract? Subtract 1 and two. The result

[4:00:07] is -1. Multiply. The result is two. Then

[4:00:18] divide. 1 / 2 is 0.5. After we resolve

[4:00:23] this function, a value is returned. Just imagine that after we finish this function, this function becomes whatever is returned three. This function becomes -1. This function becomes two. This

[4:00:36] function becomes 0.5. Let's write something a little more complex. We will create a function to

[4:00:45] create a full name. Create name. We'll need two parameters for a first name and a last name. I'll

[4:00:53] name these first and last. What do we want to do within this function? Let's capitalize the user's first name. First equals first dot

[4:01:04] capitalize method. Then do the same thing with the last name. Last equals last. capitalize.

[4:01:15] Then I'm going to return the user's first name plus their last name. Then I'll add a space in between their first and last name. This is also valid. Outside of the

[4:01:26] function, let's create a full name variable. Then invoke the create name function. So this function is going to capitalize the first and last name for us. I'll type in my first name all

[4:01:39] lowercase. Same thing with my last name. Then let's print our full name. And here is my full name variable.

[4:01:50] We sent our function some arguments. We have some parameters set up. We took those values, made them uppercase, then concatenated these strings together, then returned them as a single string.

[4:02:01] Let's try this with a different name. Spongebob Squarepants. Spongebob now has a full name. The first and last names are now

[4:02:13] capitalized. Using the return statement, you can return some data back to the place in which you call a function. Well, everybody, that's a function. It's

[4:02:23] a section of reusable code. To call a function, you type the function's name, add a set of parenthesis. You can send a function some data, which are known as arguments, but you'll need a matching set of parameters. You also do have the

[4:02:37] option of returning some data back to the place in which you invoke a function. We'll be using functions a lot in the future, but we will get more practice with them. And those are functions in Python. Hey everybody, today I'm going

[4:02:51] to explain default arguments. Default arguments are a default value for certain parameters. The default is used when that argument is omitted when you invoke a function. In the last topic, we

[4:03:04] discussed positional arguments. Today, we will be examining default arguments. Then in future topics, we'll examine keyword and arbitrary arguments. Let's

[4:03:13] begin. Let's define a function to calculate net price. There will be three parameters.

[4:03:20] An original list price, a discount if there is one, and sales tax. We will return a net price. And here's the formula. List price

[4:03:37] times 1 minus our discount percentage times 1 + our sales tax. Maybe I'm buying a PlayStation 5 for $500. I will pass in 500 for the list price. Well, I can't actually execute

[4:03:57] this function without also passing in an argument for discount and tax. Perhaps the discount is zero and the sales tax is 5%. 0.05. Well, this would work. And I

[4:04:09] should probably put this within a print statement so you can see it. There we are. My total is $525. The list price of $500, no

[4:04:19] discount, and 5% sales tax. Now suppose that maybe 90% of the time when we're executing this function, most of the time discount is zero and our sales tax is almost always the same. What we could do to make this function a little more flexible is to set these two parameters to have a default value. In place of

[4:04:39] sending in three arguments, we can pass in one. Then set our discount and our tax to have a default value. So I will set discount to be zero and tax to be 0.05 meaning 5%. So this function would

[4:04:55] work. Our total is 525 and that's assuming that our discount is zero and our tax is 5%. The nice thing about using default arguments is that let's say that somebody has a discount. Well, this function would also

[4:05:09] accept up to two additional arguments. So, let's print our net price 500 and our customer has a coupon for 10% off. I'll add a second argument of 0.1. If we're passing in an argument for

[4:05:29] our discount, we'll use whatever is passed in rather than the default. Our total now is $472.50. Or maybe this

[4:05:38] time they are not paying sales tax. I will set the sales tax to be zero. Now the customer's total is $450. So that's kind of the nice thing

[4:05:49] about default arguments. It makes your functions more flexible and it can reduce the number of arguments, especially if the arguments that you're passing in tend to be consistent. Most of the time people don't have a discount and almost everybody is paying 5% sales tax. Why pass in arguments we don't have

[4:06:05] to? Let's cover an exercise. We'll create a count up timer. We will import

[4:06:11] the time module. We will define this function. Define count. There will be

[4:06:18] two arguments start and end. For X in range, start comma end. Within the range function, the second argument is exclusive. So I'm going to add one to

[4:06:38] the end of our time. Then I will print x. To make this thread that's running the program sleep, you can access the time modules sleep method. Pass in one for 1 second. Then

[4:06:52] outside of the for loop, let's print the word done. To invoke this function, I need to pass in two arguments, a start time and an end time. I'll set the start time to be zero. the end time to be 10. 10

[4:07:08] seconds. So, we start at zero, then we will increment by one every second. I'll speed up the video. I think you get the

[4:07:15] idea, but we'll stop at 10. Let's assume that most of the time a user would like to begin at zero. Well, we don't necessarily need to pass that in as an argument. Let's set our start

[4:07:29] parameter to have a default value of zero. We only need to pass in one argument. But we do have a problem. Non-default

[4:07:38] arguments should follow default arguments. So if you use any default arguments, you'll want to be sure that they're after any positional arguments. So let's reverse these. And that should

[4:07:52] work. So now when I run this program, it's assuming we'd like to start at zero, but we'll need to pass in an ending amount of seconds. When do we want to stop? That works the same, but now we do

[4:08:07] have the option of starting at a different number. This time let's end at 30, but we will begin at 15. We're beginning at 15. Then we will

[4:08:19] count to 30. I'll speed up the video. There we are. All right,

[4:08:28] everybody. So in conclusion, default arguments they are default values for certain parameters. The default value is used when an argument is omitted. They

[4:08:38] can make your functions more flexible and reduce the number of arguments you have to pass in especially if those arguments are consistent most of the time. So those are default arguments and in the next topic we will discuss keyword arguments and well yeah those are default arguments in Python. Hey friends, it's me again. Today I'm

[4:08:58] going to explain keyword arguments. A keyword argument is an argument preceded by an identifier. It has
a few benefits.

[4:09:06] It helps with readability and the order of the arguments doesn't matter if they're keywords. Keyword arguments are one of four basic styles of arguments. We discussed positional, default, then next we'll discuss arbitrary, but today we'll be focusing on keyword. Suppose I

[4:09:22] have a function to display a message like a greeting. I will name this function the hello function. We will need a greeting, a title, Mr., Mrs., doctor, a

[4:09:36] first name, then a last name. All I'm going to do within this function is print anstring. I will print my greeting the user's title, first name, last name. Then to invoke the hello function,

[4:09:59] I will need to pass in four arguments. A greeting, a title, a first name, and a last name. So for my greeting, let's say hello. The title will be

[4:10:13] mister. The first name will be Spongebob. Last name Squarepants. So you know this does work.

[4:10:23] We're currently using positional arguments. The position of these arguments does matter. So what if I were to switch these around? We have hello

[4:10:32] Spongebob Squarepants followed by mister. Hello Spongebob Squarepants mister. An optional feature when sending arguments to a function is that we could turn these into keyword arguments.

[4:10:45] Prefix any arguments with the name of the parameter followed by equals. Title equals mister first equals Spongebob. Last equals Squarepants. Then

[4:10:57] with these keyword arguments, the order really doesn't matter. Maybe we move the first name to the end. And the still would print out is the same thing. We have title, first

[4:11:09] name, last name. If you're mixing and matching positional arguments and keyword arguments, you want to be sure that the positional arguments are first. So if I was to move the string, our greeting to the end, well, this technically wouldn't work. We have a syntax error. Positional

[4:11:27] arguments follow keyword arguments. So, make sure any positional arguments are first before using any keyword arguments. Two helpful benefits of using keyword arguments is that it helps with readability and the order of the arguments doesn't matter. We know what

[4:11:41] this argument is as well as these two title, last name, first name. Let's say we have a first name and a last name. John James.

[4:11:56] These two names kind of sound like first names. Is our first name John or is it James? We could use keyword arguments to clarify which is which. You thought John

[4:12:06] was the first name, but it's actually the last name and the first name is James. Then our title is still the same. Hello, Mr. James John. Let's cover

[4:12:17] another example. I'm going to print the numbers 1 through 10 using a for loop for x in range 1, 11 because the second argument is exclusive. Then I will print x. After each print statement, we print

[4:12:36] a new line. Do you remember in previous topics how we would follow our print statement with comma and then a new character such as a space? While end is a keyword argument found within the built-in print statement, in place of ending each print statement with a new line, we are using this keyword argument of end and sending it to be a space. Another one is separate that's

[4:13:02] found within the print statement. Maybe we have some numbers. They're all separate strings. The numbers 1 through 5. I can

[4:13:15] use the separate keyword argument then separate each of these strings with a given character or characters. I will separate each of these strings with a dash. A lot of built-in functions such as the print function. They have some

[4:13:30] keyword arguments you can use. Let's go over an exercise now. We're going to create a function to generate a phone number, but we'll need to pass in a country code, area code, the first three digits, and the last four digits. Let's define this function

[4:13:45] as define get phone to get a phone number. We have a country code area code first meaning first few digits then last meaning last few digits. We will return an fstring. We will place our country code

[4:14:09] first dash then our area code dash the first few digits dash the last few digits my phone number phone num equals I will invoke the get phone number function we just created but we'll need a country code an area code. First few digits, then last few digits. And remember, the order doesn't necessarily matter. Usually, I try and

[4:14:44] be consistent with the order of the parameters. Make up a phone number. I'm in the United States. My country code is

[4:14:51] 1. Area code 1 2 3. The next few digits will be 456. The

[4:14:57] last few will be 7890. Then let's print this phone number. print phone num and here is my phone number.

[4:15:08] Although you can change it up based on how you do phone numbers in your country. This is typically how you would see a phone number in the United States. All right, everybody. So those are

[4:15:17] keyword arguments. They are just arguments preceded by an identifier that matches the name of a function's parameters. It does help with readability and the order of the arguments doesn't matter. When invoking

[4:15:30] a function, it could be helpful to identify some of these arguments. And well everybody, those are keyword arguments in Python. Hello friends, it's me again.

[4:15:41] Today I need to explain arbitrary arguments. Arbitrary meaning a varying amount of arguments. We don't know how many arguments the user is going to pass in when they invoke a function. To

[4:15:51] accept a varying amount of arguments, developers tend to use these parameters of args and quarks. Args means arguments. Quarks means keyword arguments. You would want to prefix each

[4:16:04] of these parameters with the unpacking operator, which is an asterisk. When you invoke a function that has args or quarks as parameters, you will pack all of those arguments into a tpple if it's args or a dictionary if the parameter is quarks. Let's go over an example. I will

[4:16:21] create a function to add two numbers together. define add function there will be two parameters a comma b all I'm going to do is return a + b I will invoke this function pass in two arguments because we have two parameters set up one 2 then I'm going to print the result big surprise there my function return three all right well what if I would like to pass in three parameters this time. Well, I can no longer use this function. The add function takes

[4:17:00] two positional arguments, but three were given. I could modify this function so that it could accept a varying amount of arguments, any amount. I'm going to replace the parameters with asterisk then the word args meaning arguments. So

[4:17:16] when we use the unpacking operator, what's going to happen now is that with the arguments that we pass into this function, we will pack them all into a tpple. And if you don't believe me, let's test it. I'm going to print the type of args. Then I'm going to remove

[4:17:33] this print statement for now. My parameter args is a tpple that I could work with. We can use the built-in methods of this tpple or we could iterate over it.

[4:17:44] I'm going to iterate over this tpple for every arg in args for every argument in arguments. What we'll do is create a variable named total to keep track of the total. Total plus equals the current arg that we're iterating over. Then at the

[4:18:05] end I will return the total. Let's print the result. Print.

[4:18:11] Add these three numbers together. There we are. My total is six. Then we can

[4:18:16] pass in any amount of arguments. Four this time, maybe five or even one. With my parameter args, you can change this name to something else like nums meaning numbers for every num in nums. Total plus equals num. This would

[4:18:39] work too. The name of the parameter isn't as important as the unpacking operator. Just by typical naming conventions, people tend to stick with args. But the parameter name can vary.

[4:18:51] Let's try a different example. Let's create a function to display somebody's name. Display name. We will accept a varying amount of

[4:19:01] arguments. Use the unpacking operator. Then follow the unpacking operator with the unique parameter name. For every arg

[4:19:10] in args, let's print each argument. Then replace the ending character of my print statement with a space. Now sometimes people can have a varying number of names in their full name. There can be a first name, middle

[4:19:27] name, last name, maiden name, a title, etc. So, I'm going to pass in just a first name and a last name. Spongebob Squarepants. If I need to add a middle

[4:19:43] name, I can do that. Spongebob Herald Squarepants or a title Dr. Spongebob Herald Squarepants. The third

[4:20:00] Yeah, as I was saying with the unpacking operator followed by a unique parameter name, you can pack all of these arguments into a tuple which you can use within this function. Now let's discuss quarks. You use two unpacking operators.

[4:20:17] Then typically people follow this with the word quarks meaning keyword arguments. It allows you to pass multiple keyword arguments which we discussed in the last topic. I think this would be great for an address.

[4:20:31] Define print address function. Use double asterisks. Then we can add a parameter name, but people usually stick with quarks, meaning keyword arguments. Just as a

[4:20:46] placeholder, I'm going to type pass. Pass doesn't do anything. I want this program to be able to run. We'll get

[4:20:52] back to this function momentarily. I'm going to invoke this function. print address. Then pass in multiple keyword

[4:21:01] arguments. With an address, you would typically have a street, a city, state. Depending on what country you live in, you may have more or less of these keyword arguments. I live in

[4:21:16] the United States. We have a state. Then a zip code. Okay. My street will be I'm just

[4:21:24] making something up here. One, two, three. Fake street. City will be

[4:21:32] Detroit, state, Michigan. Zip code 5 43 2 1. Just to make this look better, I'm going to place each of these keyword arguments on a new line. For me,

[4:21:45] that's just more readable, but you do you. When I pass in these keyword arguments, we will pack them into a dictionary. Just to prove it, let's print the type of quarks. Look at that class

[4:22:02] dictionary. Within this function, you can treat quarks as if it's a dictionary. There's a lot of built-in methods. Or we could iterate over the

[4:22:10] keys, the values, or both. to iterate over the values. Let's say for every value in our dictionary quarks dot values method print every value. Here's all the values for the

[4:22:30] keys. Let's change this for loop to be for every key in quarks keys method print every key. Here are the keys for both. You

[4:22:43] could say for every key, value in quarks do items method print every key. Actually, let me turn this into an F string. Print every key colon value. The items method will return key

[4:23:06] value pairs. We can pass in a varying amount of keyword arguments. I'm going to add an apartment number. Apartment equals

[4:23:21] 100. Our keyword argument of apartment was packed into a dictionary along with all these other keyword arguments. So that's kind of nice. We can pass in a

[4:23:30] varying amount of keyword arguments. Let's cover an exercise. We're going to use both args and quarks together.

[4:23:38] We will print a shipping label. Define shipping label function. The parameters will be both args, quarks. Then just for now, I'm

[4:23:50] going to write pass just so that this program will work for now. We'll fill in the shipping label function momentarily. When we invoke the shipping label function, we will first pass in any positional arguments followed by keyword arguments. and it won't work the other

[4:24:06] way around. I'll prove that in a little bit. So, let's say we have Dr.

[4:24:16] Spongebob Squarepants the third. Then I'll add my keyword arguments. I'm going to put this on a new line. Street equals 1 2 3 fake

[4:24:30] street. Apartment equals 100. City equals Detroit. State equals

[4:24:49] Michigan. Zip equals 543 2 1. When we invoke this function, we have a mix of arbitrary positional arguments and arbitrary keyword arguments. This

[4:25:03] shipping label function is designed to accept both. You do need args first followed by quarks. This program will run. But if we have it the other way

[4:25:13] around, quarks followed by args, it's not going to function properly. You can see that we have a syntax error. With your parameters, make sure that your keyword arguments follow your positional arguments. Let's iterate over

[4:25:29] the positional arguments first. For every arg in args, let's print each arg. Then I will change the ending character of my print statement to be a space. Here's the name of the user who

[4:25:46] we're shipping something to with the shipping label function. I will print a new line. Then we will iterate over all the keyword arguments. For every value in my

[4:26:00] dictionary quarks dot values method, I will print each value. Then I will change the ending character of my print statement to be a space. All right, it's not looking too bad so far.

[4:26:18] If you were to remove some keyword arguments or some positional arguments, this should work still, which it does. I'm going to change the format of this address slightly. Let's add our street on one line, then the city, state, and zip code on the next line.

[4:26:36] Let's get rid of this for loop. To print the street, I'm going to print use an F string. add a placeholder quarks.get method. I'm going to get the

[4:26:51] street key. With this get method, you'll probably need to place them within single quotes because if you use double quotes, Python gets confused as to where this fring ends. We will use single quotes. Let's test it. All right, we

[4:27:06] have a street. On the next line, we will print the city, state, and zip. print ft string placeholder quarks.get within single quotes the

[4:27:24] city I'll add another placeholder quarks.get state then quarks.getzip. Let's see what we have.

[4:27:41] All right, not too bad. What if the user has an apartment keyword? Apartment equals number 100. Well, we should probably add that

[4:27:53] too. Within this top print statement, I will add another placeholder. Invoke the get method of the dictionary. The key we are looking

[4:28:03] for is apartment Dr. Spongebob Squarepants 23 Fake Street, apartment number 100, Detroit, Michigan 54321. What if our print statement is set up to display a street and an apartment, but the user doesn't have an apartment? This would display none, and

[4:28:22] we don't want that. I'm thinking what we'll do is we'll place this print statement within an if statement. What we'll check is if apartment in quarks. If there's an apartment key in

[4:28:43] quarks, our dictionary, then print this line. Else we will print just the street. The person doesn't have an apartment. We won't print the apartment

[4:29:01] then. But if they do have an apartment, apartment equals number 100, then we will 123 Fake Street, apartment number 100. Here's a challenge round. What if a

[4:29:15] user has a PO box? Let's change apartment to PO box. The string will be PO box number 100,1. I suppose I'll add an else- if

[4:29:30] statement. else if PO box in our dictionary quarks. Let's print the street. I'll

[4:29:43] copy this line, paste it, followed by a second print statement. Quarks.getp box. There we are. Dr. for Spongebob

[4:30:00] Squarepants 123 Fake Street PO Box 10001 Detroit Michigan 54321. All right, everybody. Those are arbitrary arguments. When you invoke a

[4:30:10] function, you can pass in a varying amount of arguments. Set up your parameter to be args for a varying amount of non-keyword arguments or quarks for a varying amount of keyword arguments. You can set up both in your parameters, which we did for this exercise. And well everybody those are

[4:30:28] arbitrary arguments in Python. Hey everybody. So today I got to talk about iterables in Python. An

[4:30:38] iterable it's a category. Any object or collection that can return its elements one at a time is considered an iterable. If an object or a collection is considered an iterable, then it can be iterated over in a loop. For example,

[4:30:53] let's create a list of numbers. numbers equals a list. I'll add the numbers 1 through 5 to keep it simple.

[4:31:00] Lists are considered iterable. We can use them within a for loop. In the context of a for loop, we're going to be given each element one at a time. Each element that we're working

[4:31:13] with, we can give a temporary nickname. Let's say number. For every number in my iterable of numbers, let's just print each number. This will give us 1 through

[4:31:29] 5. The name of the current element in our iterable should be descriptive of what we're iterating over. For example, I don't want to rename the current number that we're working with as something like blah blah blah.

[4:31:43] You know, this would work, but other people looking over your code might not understand what a blah blah blah is, and I don't blame them. Each element that we're given from our iterable, the name should be descriptive of what we're given. Or you might see item. For every

[4:31:59] item in numbers, print each item. That's also a good choice. Now, you could even iterate backwards by enclosing our iterable within the reversed function.

[4:32:12] So take our iterable of numbers and reverse it. Then we get the numbers 5 4 3 2 1. If you would rather not print each element on a new line, we can replace the new line character at the end of print statements with something else. Print is a function. We can pass

[4:32:30] in a keyword argument of end. Rather than end each line with a new line character, let's end with a space. This will space out each of the elements. Or we could replace it with

[4:32:41] something else. Or what about a dash? After each element, append a dash character. We could even add multiple

[4:32:50] characters such as a space, a dash, and a space if we so choose. It's up to you. Tpples are also iterable. Let's convert our list to a

[4:33:02] tpple by enclosing our numbers within a set of parenthesis. And I no longer want this reversed. For every number in my iterable of numbers, print each number. Then again,

[4:33:16] we get the numbers 1 through 5. Let's cover sets. I will create a set of fruit, which I will name fruits. For a set, enclose any values

[4:33:28] within a set of curly braces. Let's add a string of apple, a string of orange, a string of banana, and a string of coconut. So with our for loop, let's say for every fruit in my iterable of fruits, I will print each fruit. That would give me apple, banana,

[4:33:53] orange, coconut. Now sets, they're actually not reversible. I will attempt to enclose our iterable of fruits within the reversed function. Here's what happens. We have a

[4:34:06] type error. Set object is not reversible. Sets you can't reverse. Let's cover strings. I will

[4:34:15] create a string of name. Type in your full name. I'll use my YouTube channel name. For every character in my iterable

[4:34:25] of name, I would like to print each character. Maybe I would rather not have each character end with a new line. I will set the keyword argument of end to be a space. Last, we have dictionaries, which

[4:34:45] are the most complicated. Let's name this dictionary my dictionary. Dictionaries you enclose with a set of curly braces, kind of like a set, but each element is a key value pair. I will

[4:34:59] add a key of A with an associated value of 1, a key of B which has a value of two, a key of C which has a value of three. If you iterate over a dictionary, the dictionary is going to return all the keys but not the values. We'll test that. For every key in my iterable of my

[4:35:25] dictionary, let's print each key. This would give me the keys of A, B, and C, but none of the values 1 2 or three. If you need the values, we're going to follow this iterable of my dictionary, use the built-in values method.

[4:35:46] This will return all the values of your dictionary as an iterable. But let's rename a key as value because now we're working with the values. Then we're given all the values 1 2 and three. If you need both the keys

[4:36:03] and the values, you're going to use the items method. We'll be given both a key and a value. Make sure that the value and the key is separated with a comma.

[4:36:16] Let's print each key followed by the value. We get the key of A with its value of 1 B 2 C 3. We can reformat the output however we want. Let's use an F

[4:36:32] string. I will add two placeholders. Let's print each key equals then the value A equals 1, B= 2, C= 3. Okay,

[4:36:46] everybody. So those are iterables. An object or a collection that can return its elements one at a time is considered an iterable. Meaning that object or

[4:36:55] collection can be iterated over using a loop. And well everybody, those are iterables in Python. Hello again. So today I got to talk

[4:37:07] about membership operators in Python. They are the operators in and not in. They're used to test whether a value or a variable is found within a sequence which include but are not limited to strings, lists, tpples, sets, or dictionaries. Here's an example. I'm

[4:37:25] going to create a word, a secret word. Let's say apple. I'm going to turn this into a game. I will have a user guess a letter.

[4:37:35] I will accept some user input. Guess a letter in the secret word. What I would like to do is check to see if my letter is found in my word.

[4:37:52] I can write the following statement. if our letter in our word in is going to return a boolean value of true if that letter is found or false if it's not. So if our letter is found I'm going to print the following statement. I'll use an f string. There

[4:38:14] is a add a placeholder insert our letter else. Let's print. I'll use an F string. Our

[4:38:27] letter was not found. Let's test this. Guess a letter in the secret word. I will guess a

[4:38:36] capital A. So all these letters are uppercase. Do take note of that. Is

[4:38:42] there an A? There is an A. Let's guess a letter that's not within this word, such as Z.

[4:38:50] Z was not found. The in membership operator will test to see if a value or a variable is found within a sequence. If it is, it returns true. If not, it

[4:39:02] returns false. Or for the inverse, you could say not in. If letter is not in Word, we would have to flip these statements around.

[4:39:19] If this value or variable is not found in this sequence, it returns true, otherwise false. So, it does the opposite of in. Guess a letter in the secret word. Is there an E? There is an

[4:39:33] E. Is there a Q? Q was not found.

[4:39:38] Depending on the statement you're trying to write, you can use either in or not in, whichever makes more sense in that context. Let's go over another example. We were searching for a value or a variable found within a string. Let's

[4:39:52] try a set. List tpples and sets are going to behave similarly. I will create a set of students. For a set, you need a set of

[4:40:01] curly braces. Let's add a few student names such as Spongebob, Patrick, and Sandy. I will have a user. Type in a

[4:40:15] student to search for. We will accept some user input. Enter the name of a student.

[4:40:26] We're going to check if our student is in our sequence of students. If in returns true, let's print the following. I'll use an f string. Insert our

[4:40:42] student is a student. Else we will print. I'll use an fstring.

[4:40:53] Insert that student was not found. Enter the name of a student. Let's search for Spongebob.

[4:41:04] Spongebob is a student. Enter the name of a student. Let's attempt Squidward.

[4:41:10] Squidward was not found. And much like the first example, we can do the opposite. See if a value or a variable is not in a sequence.

[4:41:22] We would have to switch these statements around. Enter the name of a student. Is Sandy a student? Sandy is a student.

[4:41:35] Enter the name of a student. Is Larry a student? Larry was not found. Now we'll cover dictionaries. I

[4:41:43] will create a dictionary of grades. Student grades like a grade book. Let's say that the student of Sandy, she will be a key has a value of A.

[4:42:00] Squidward, the key of Squidward has a value of B. Spongebob, he is also a key. Spongebob has a grade of C. Then Patrick.

[4:42:16] Patrick has a grade of D. Here is my dictionary of grades. Then we'll search for a student.

[4:42:30] Student equals input. Enter the name of a student. We'll check if let me close this. If our

[4:42:43] student is found within grades, then I will print the following. We're looking for keys. Is there a matching key? If we find that

[4:42:53] student, I'll make this an F string. Let's display the associated value of that key. student students grade is I'll add a placeholder. Once we find a student, we

[4:43:12] have to get that value at the given key. To do that, we'll take our dictionary of grades at index of student. This will retrieve the value at a given key. If we don't find a student, we'll

[4:43:28] output the following. Again, I'll use an fstring. Student was not found. So now, if I search for a student

[4:43:40] such as Spongebob, we're given a grade. We're given the value at that key that we're searching for. Let's test Sandy. Sy's grade is A.

[4:43:54] Squidward. Squidward's grade is B. And Patrick.

[4:43:59] Patrick's grade is D. But Larry is not a student. If I search for him, well, Larry was not found. Let's go over one last

[4:44:11] example. We're going to create a variable of email. It's going to be a string. Type in whatever your email is.

[4:44:21] Brocodegmail.com. I would like to see if this email is valid. Does it contain at

[4:44:26] and a period? I will write if our value of at that character is in our email and a period is an email. We have two conditions. Check if

[4:44:44] at is an email and check if a period is an email. If so, it's a valid email. Then we'll print valid email.

[4:44:57] else we will print invalid email is my email valid that email is valid I'll get rid of the at invalid email I'll get rid of the period following Gmail that email is also invalid in this example we're checking two conditions If this value is found within this sequence and this value is found within this sequence. All right everybody. So those are membership operators in and not in. They will

[4:45:38] return a boolean based on whether a value or a variable is found within a sequence which include but are not limited to strings, lists, tpples, sets or dictionaries. And well everybody those are membership operators in Python. Hey, what's going on everybody? So, in

[4:45:58] today's video, I got to explain list comprehensions in Python. A list comprehension is a concise way to create lists in Python. They're compact and easier to read than traditional loops.

[4:46:09] Basically, you have to follow this formula. For every value in something that's iterable, meaning you can loop through it, check some condition, then do this expression. So, let me give you an example with using a traditional loop. then you'll be able to see why a

[4:46:24] list comprehension is useful. We're going to create a list and double the numbers 1 through 10. Doubles equals an empty list. Using

[4:46:34] a traditional for loop, we will say for every value, let's say x in range 1 through 11. Remember that in the range function, the second number is exclusive. This will give you the numbers 1 through 10. For the first

[4:46:51] iteration, x is going to be 1, then two, 3, all the way up until 10. So, we'll iterate 10 times. During each iteration, I'm going to take my list of doubles, use the built-in append method, we will append x. During each iteration, that's

[4:47:10] going to be the value times two. So, if I were to print my list of doubles, here's the result. We have the numbers 1 through 10 all doubled. 2 4 6 8 10 12 14 16 18 20. So

[4:47:26] this is a lot to write. We can use a list comprehension to make this code more compact and easier to read. Here's how. We need a name for this list. Let's

[4:47:37] say doubles equals an empty list. Within our list, we'll follow this formula. We have an expression for value in iterable and optionally we can check a condition. We'll do this in exercises

[4:47:53] later on in this topic. We'll begin with for every value let's say x in our iterable. Our iterable is going to be a range 1 through 10. Again for the first

[4:48:08] iteration x will be 1. Then the second iteration x will be two all the way up until 10. During each iteration, what would we like to do with x, our value?

[4:48:19] Let's take x, multiply it by two, and return it. Then, if I was to print my list of doubles, we have the numbers 2 4 6 8 10 12 14 16 18 20. For every value in this iterable, do this. Multiply it by two.

[4:48:38] This is a list comprehension. It's a concise way to create lists in Python. We'll go over a few exercises. So this time we will triple

[4:48:47] each number. We'll create a list of triples equals let's say this time for every y in range 1 through 10. So we have to write 11 take y and multiply it by three. Then

[4:49:06] we will print our list of triples 3 6 9 12 15 18 so on and so forth. Let's square each number. We'll create a list of squares for every Z in range 1 through 10. To square a number, we take that

[4:49:25] number, multiply it by itself. So the numbers 1 through 10 squared is 1 4 9 16 15 36 49 64 81 100. So 10 * 10 is 100. Now we're going to

[4:49:43] work with strings. We'll create a list of fruits. Equals. Let's think of some fruit. These

[4:49:50] are all going to be strings. Apple, orange, banana, coconut. I'm going to take each string in this list and make it uppercase. We could assign this to a new

[4:50:04] list such as uppercase fruits or we can simply just reassign it. Just to keep it simple, I'll reassign it. So again, we're following this formula. I like to begin with the four

[4:50:18] value in iterable portion. For every fruit in our iterable of fruits, what do we want to do? Well, let's take each fruit. Take each

[4:50:30] fruit. Use the built-in upper method to make it uppercase. Then I'm going to print my list of fruits. Each string in this list is now

[4:50:42] all uppercase. You could even cut down on one of the steps. With our iterable of fruits, I will place this list. And this does work too. Although I

[4:50:57] do find this a little more difficult to read, but you can take either option. How about instead of making each string uppercase, we'll take the first letter of each string, then put it within a new list. So let's take each fruit at index of zero. That will give us the first

[4:51:15] letter. We'll place it within a new list of fruit chars, meaning characters. Here's the result. A O B C.

[4:51:27] For every fruit in our list of fruits, return the first character of each string. A O B C. Now we'll work with conditions. We'll create a list of

[4:51:42] numbers both negative and positive. numbers equals let's say 1 -2 3 -4 5 -6. We'll create a list comprehension to create a new list where all of the numbers are positive. Our new list will

[4:52:01] be positive nums equals we'll write a list comprehension for every let's say num in numbers we'll write a condition return this number if our num is greater than or equal to zero. We do need an expression if we're not modifying each value. we can just return the value of num. During this exercise, we're more

[4:52:33] focused on the if condition rather than the expression. If our value of num meets this condition, simply return it and place it within this new list. Let's print our list of positive numbers. And we have

[4:52:51] 135. Let's do this with negative numbers. I'll just copy what we have and change a few things around. This list

[4:52:57] will be negative numbers. Negative nums. For every num in numbers, check this condition. Check to see if num is

[4:53:07] less than zero. If so, return that number. Let's print our list of negative numbers. -2, -4,

[4:53:16] -6. Let's check to see if there's any even numbers. Even nums equals for every num in numbers check to see if our num is divisible by two. And we can do that

[4:53:33] with the modulus operator followed by two. The modulus operator will give you the remainder of any division. If our number is even, number modulus 2 will equal zero. If it's even, this is going

[4:53:46] to equal zero. If it's odd, it's going to be one. We're not modifying our value. We're just going to return our

[4:53:55] number. Our list of even numbers should be -2, -4, -6. Let me add one more value. Let's add

[4:54:05] positive 8 -24 -6 pos 8. Maybe we'll add one more. -7. Okay, let's find any odd numbers.

[4:54:18] Let's copy this line of code. Replace even numbers with odd numbers. If num modulus 2 is equal to 1, that means that number doesn't divide by two evenly, then we'll print our odd numbers. 1 3 5 - 7. All these numbers

[4:54:39] are odd. Here's the last exercise. We'll create a list of grades.

[4:54:48] We'll create a new list of any grades that are considered passing, meaning they scored 60 or above. So, let's say one student has a grade of 85, another with a 42, 79, 90, 56, 61, let's say 30. I will create a new list of passing grades.

[4:55:17] Equals again follow this formula for every grade in grades. Check our condition. If our grade is greater than or equal to 60, we will return the current grade. Then let's print our list of

[4:55:39] passing grades. That will give us 85, 79, 90, and 61. All of these grades are greater than or equal to 60. All right,

[4:55:51] everybody. So, that is a list comprehension. It's a concise way to create lists in Python. They're compact

[4:55:57] and easier to read than traditional loops. Remember, for every value in your iterable, optionally, you can check a condition. You can write an expression to modify that value if you choose and return something. All right everybody.

[4:56:12] So those are list comprehensions in Python. Hey everybody. So today I'm going to explain match case statements in Python. If you're familiar with other

[4:56:23] programming languages, this is also known as a switch. Match case statements are alternatives to using many else if statements. We execute some code if a value matches a case. The benefits of using a match

[4:56:38] case statement is that they're cleaner and the syntax is more readable. In this sample program, I have a function. There is one parameter, a day. Day will be a

[4:56:48] number, ideally a number 1 through 7. Depending on this number, we'll return a string corresponding to the day of the week. If day equals 1, then it is Sunday.

[4:57:02] two, it is Monday all the way up to 7 where it will be Saturday. I do have an else clause if we pass in something that's not valid like pizza. Pizza is not a day, but it really should be not a valid day. A cleaner and

[4:57:21] more readable alternative is to use a match case statement instead of many else if statements. Here's how. I'm going to take my if and many else if statements and enclose them within a match case. Match case. The case is going to

[4:57:40] be the value we're examining. The case will be day colon. We're going to examine our value of day against matching cases. We're going to replace if day

[4:57:55] equals with the following. just simply case. So let's do that with each of these statements. If you have an else clause,

[4:58:15] you're instead going to have a case of underscore. An underscore in a match case statement is a wild card. We will perform this case if there are no matching cases.

[4:58:27] This case would function as the else statement. Here's what we're working with. Now, if I pass in one and return the day of the week, we would get Sunday. 2 would be Monday. 3 Tuesday.

[4:58:45] 7 is Saturday. And then let's try that day of pizza. That is not a valid day. A match

[4:58:53] case statement is an alternative to using many else if statements. I find this much easier to read than the many else if statements. Both would technically function. Let's go over a

[4:59:04] second example. We will create a function of is weekend. We have to pass in a day. This

[4:59:13] time our day is going to be a string such as Monday. The value for each case instead of a number is going to be a string. If our day matches a case of Sunday, let's return how about a boolean of true. We're checking to see if it's

[4:59:32] the weekend. If our day is equal to a case of Monday, then we will return false. Let's do this with the other days. I'm going to fast forward the

[4:59:44] video. We will call the function of is weekend then pass in a day of the week such as Monday. So is Sunday the weekend? That

[5:00:13] is true. Monday that is false. Saturday. That is true. And we do have a

[5:00:23] wild card case. If there are no matches, is pizza a day of the weekend? That is false. There is a way we can

[5:00:31] modify this match case, too. We tend to be repeating ourselves a lot. The days Monday through Friday all return false.

[5:00:39] We're going to use the or logical operator, which is represented with a vertical bar. If the case of Saturday or Sunday return true. If the case is Monday or Tuesday, we can get rid of that.

[5:01:01] or Wednesday or Thursday or Friday then we will return false. We can keep our wild card case. So is Saturday part of the weekend that is true. is

[5:01:32] Monday false Sunday true Friday false and pizza we have our wild card case that gives us false. All right everybody so those are match case statements. They're similar to switches in other programming languages. They're an alternative to

[5:01:56] using many else if statements. We execute some code if a value matches a case. The benefits is that the code is cleaner and the syntax is more readable.

[5:02:07] And well everybody, those are match case statements in Python. Hello friends, it's me again. Today I'm going to explain modules. A

[5:02:17] module is just a Python file containing code you want to include in your program. You use the import keyword to include a module. You can use built-in modules or create your own. Sometimes

[5:02:28] it's useful to break up a large program into reusable separate files. For a list of all the modules found within the standard Python library, you can use the help function, pass in the word modules, and then we would need to print this. Here are many of the different modules available to you. A few you may

[5:02:49] recognize would be math, string, time. One of my favorite names of a module is the pickle module. Unfortunately, it doesn't have anything to do with pickles. It's used for serialization. To

[5:02:59] list all of the different variables and functions found within a module, you can place that name of the module within the help function. For example, with the math module, here are a few different variables we would have access to and a few different functions. To include a module, we would type import the name of the module, for example, math. I now have access to

[5:03:21] everything found within the math module, including those variables and functions. To access those variables and functions, I would normally type the name of the module dot the name of the variable or function such as pi. Then let's print this. Pi from the math module is 3.14

[5:03:41] and some change. Another way to import is to type import the name of the module as. You can give your module a nickname, an alias, whatever you think of such as M. M short for math. We would no longer

[5:03:55] refer to this module as math. We would refer to it as our alias M. Using an alias would reduce some of the typing you have to use. If you have

[5:04:06] a very long module name, another way to import is to use from the name of the module. Import something specific. PI for instance, you would no longer need the module name. From math import pi, pi would be

[5:04:23] included within our name space. However, I tend to not use from import as much just because it's possible there could be name conflicts. Here's an example.

[5:04:32] Let's say from math import E. E is an exponential constant. E is 2.71. What if I was to create a program

[5:04:43] where we have four variables named A, B, C, D. A = 1, B = 2, C = 3, D= 4. Then I'm going to print E from the math module to the power of A. That would give me 2.71.

[5:05:03] Then let's do this with B, C, and D. E to the power of B, E to the power of C, E to the power of D. Here are the results. Let's say we have a different

[5:05:14] variable E. E will be five. Then I will print E to the power of E. We have

[5:05:24] imported E from the math module. When we have declared all of these variables, technically what we've done is we have created another version of E. We will end up using the second version rather than the version that we have imported from the math module. All my results are

[5:05:40] now different and it's possible you may not realize it. I like to be more explicit. I'm going to import math. If

[5:05:47] I'm using a variable or function from a module, I much prefer to prefix that variable name or function with the name of the module in which it's from. math. E to the power of A to the power of B to the power of C to the power of D. Math E

[5:06:03] to the power of our variable E. And these results are to be expected. Now to create a module, what we're going to do is right click on our project folder, go to new Python file, think of a module name, maybe example, then click Python file. We now have two tabs. main and

[5:06:26] example. Declare whatever you would like within this module. Let's create our own variable pi. pi=

[5:06:34] 3.14159. Then a few functions. Let's

[5:06:36] create a function to square an argument that's passed in. Define square. We will accept an argument which we will name x.

[5:06:46] Then return x to the power of two. Let's define a cube function. We will accept one argument. Then return x to the^ of

[5:06:58] 3. Maybe a circumference function. Define circumference. We will accept a

[5:07:05] radius. Then return 2 * * radius. Then an area function to calculate the area of a circle. We will accept a

[5:07:16] radius as an argument. Then return pi * radius to the power of 2. All right, here is our example module within our main Python program. Let's

[5:07:30] import the name of our module which we named example. We now have access to everything within this module. I'm going to declare a variable result and set it to the name of my module.py. Then I will print the

[5:07:47] result which is 3.14159. Let's utilize the square function. result equals example

[5:07:57] dosquare. Let's square three which is 9. Let's use the cube function that would be 27.

[5:08:13] Circumference that would give me 18.8. Then area that would be 28.2.

[5:08:23] That's how to create your own module. It can be useful at times to separate your program into individual files. All right, everybody. In conclusion, a

[5:08:31] module is just a file containing code you want to include in your program. You use import to include a module. You can use built-in modules or create your own.

[5:08:40] If you do need a list of the modules available to you, again, you can use the help function, then pass in the word modules. And well everybody, that's how to get started with modules in Python. Hey friends, it's me again. Today I'm

[5:08:53] going to explain both variable scope and scope resolution. Variable scope is where a variable is both visible and accessible. With scope resolution, when we're using a variable, there is a certain order known as the LEGB rule in which we locate that variable. Local,

[5:09:10] enclosed, global, built-in. We'll get to this momentarily. Let's begin with variable scope. I have two functions,

[5:09:17] function one, function two. within function one a equals 1 then we print a within function two b equals 2 then we print b. If I were to invoke these functions let's invoke function one then function two. We would print 1 then two.

[5:09:36] Variables declared within a function have a local scope. Variable a is local to function one. Variable b is local to function two. within function one. If I

[5:09:46] were to print B and function two, if I were to print A, we would run into a name error. Name B is not defined. And the same thing would apply with A.

[5:09:57] Functions can't see inside of other functions. Imagine that we're function one. This is our house. We can see

[5:10:04] everything that's going on inside of our house, but function two is our neighbor's house. We can't see what's going on inside of our neighbor's house. We have no idea what B is with function 2. Function 2 has no idea what A is.

[5:10:17] That's where variable scope comes in. It's where a variable is visible and accessible. Functions can't see inside of other functions, but they can see inside of their own function. That's why

[5:10:27] we sometimes pass arguments to functions so that our functions are aware of them. Using this concept, we could create different versions of the same variable. Let's rename a to be X and B to be X as well.

[5:10:41] Then I will print x. We have two different versions of x. A local version of x found within function one and a local version of x found within function two. Whenever we

[5:10:54] utilize a variable, we will first look to see if there's any local instance of that variable. If there isn't, we would move to the enclosed scope. With an enclosed scope, one example is when you have a function declared within another function. I'm going to place function

[5:11:10] two within function one. This is allowed in Python. This is a more advanced concept. We'll cover this more in the

[5:11:17] future. So, I'm going to eliminate this print statement. Let's get rid of function two. At the end of function one, we will

[5:11:25] invoke function two. Like I said, it's pretty complex. We won't be using this until much later. Within function two,

[5:11:33] if I was to print x, we would use the local version where x equals 2. If I was to eliminate this variable declaration, we would use the enclosed version instead where x equals 1. There's an order of operations. Use any

[5:11:49] local variables first, then enclosed variables. We're printing x within function 2. Since x wasn't found within the local scope, we would use x within the enclosed scope. But like I said,

[5:12:02] that's a more advanced topic. You should at least be aware of it. Let's move on to the global scope. global meaning

[5:12:08] outside of any functions. I will eliminate these variable declarations. Within function one, we're printing X and within function two, we're also printing X. I will declare a

[5:12:20] global version of X where X equals 3. X is outside of any functions. When I run this program, we're printing three twice. Once for function one and once

[5:12:32] for function two. There's no longer a local version of X for both of these functions. If there were, we would end up using these local versions instead.

[5:12:41] Function one prints one, function two prints 2. If there's no local version as well as no enclosed version, we would move on to the global version where X equals 3. Last in our order is built in.

[5:12:54] I think what we'll do though is from math import E. E is an exponential constant. I'm going to print what E is.

[5:13:04] E is 2.71. E is built in. I will create a

[5:13:09] function to print E. Define function one. All I'm doing is printing E. Then

[5:13:16] we should invoke it. Invoke function one. If I was to set E to be a different value like three, what we're doing technically is creating two different versions of E. Variables can share the

[5:13:30] same name as long as they're within a different scope. We have a built-in version of E and a global version of E. If I was to print E now, it would print my global version because using the leggb order, we would first look for any local version of E, then enclosed version, then global, which we do have one of, then lastly builtin. All right,

[5:13:53] everybody. So in conclusion, variable scope is just where a variable is both visible and accessible. Python has a scope resolution order levb. If we're

[5:14:03] using a variable, we will first look in the local scope for that variable. If we don't find that variable in the local scope, we will move over to an enclosed scope, then global, then built-in. We will have more practice with this in the future. And well everybody, that is both

[5:14:18] variable scope and scope resolution in Python. Hey everybody. So today I got to talk about this if statement. If dunder

[5:14:27] name is equal to a string of dunder main. When you see this if statement, it's usually followed by a call to a function named main or something similar. A majority of the driving code behind a program is usually found within some sort of main method. When you see

[5:14:43] this if statement, basically speaking, it means that this script can be imported or it can run standalone. Functions and classes in this module can be reused in other programs without the main block of code running. Sometimes you would like the functionality of a program without executing the main body of code. A good example could be a

[5:15:02] library. In a Python library, we would like to import some of the useful functions such as the math module. But if we were to run that library directly instead of importing it, we could instead display a help page. But if

[5:15:16] we're importing that library, we don't necessarily want to display that help page only if we're running it directly. In many Python scripts, you'll see the statement of if done name is equal to main. If we're not running this program directly, don't do it. In this example,

[5:15:31] we're going to delete our main Python script. Be sure to recreate it at the end of this topic in case I forget to mention that. We will create two new scripts. Go to file, new, Python

[5:15:42] file, script one. file new Python file script 2. We have to add new run configurations for script one and script two. So if you

[5:15:58] go to the top, go to run, edit configurations. We will add a new run configuration. Select Python. Select a

[5:16:06] new script path to script one. Okay. Apply. Again, we have to do this with

[5:16:13] script two. Add Python. Select a script path of script 2. Okay. Apply. Then okay. Using this

[5:16:24] drop-own menu, we can select which run configuration we would like. Would we like to run our main Python file, but we have deleted it. Do we want to run script one or script two? For the time

[5:16:37] being, we'll select script one. Within script one, if I was to print, then call the dur function dur meaning directory. Python has all of these built-in attributes. If you're not

[5:16:51] familiar with object-oriented programming, for now, think of an attribute as a variable. Dunder name is a special type of variable. Dunder meaning double underscore. If I was to

[5:17:02] print what's contained within dunder name, we would receive a string of dunder main. That's why in a script you may see the statement if dunder name is equal to a string of dunder main. If so, then you usually call a function named main to start your program. I'm going to undo that. So

[5:17:27] let's import script two. From script two, import everything. Asterisk means everything. Within script two, I will

[5:17:40] print dunder name. And we'll see what's within it. Again, I'm running script one.

[5:17:49] Within script 2, dunder name is equal to a string of script 2, the name of the Python script. However, within script one, dunder name is equal to a string of dunder main. This means I am running script one directly. Let's delete this

[5:18:07] import. Then go to script 2. Import script one. From script one, import

[5:18:15] asterisk meaning all. We're now going to change our run configuration from script one to script two. We are running script two directly. Now dunder name within script

[5:18:26] one is the name of the Python script script one. Dunder name within script 2 is now dunder main. So by adding this if statement of dunder name is equal to dunder main we can check to see which file is being run directly. If dunder name

[5:18:49] equals dunder main we will call a function of main to contain the main body of our program. But we need to define this function define main. Our main function will contain the majority of our Python code. anything

[5:19:04] that's not already within a function. So let's print this is script one. Then we'll define another function of favorite food. We will have

[5:19:21] one parameter of food. Let's print the following message. I'll use an fstring. Your favorite food is add a

[5:19:33] placeholder. add our parameter of food. Within our main function, let's call the favorite food function. Pass in your

[5:19:41] favorite food as a string. I'll type in pizza. Then let's print the word goodbye. We're going to run script

[5:19:52] one. Run it. Here's the result. From the top down, all of our

[5:19:58] code is within functions. We skip over it because we're not calling it quite yet. The first thing we do in this program is check this if statement. If

[5:20:06] dunder name is equal to dunder main. Are we running this program directly? Which we are. We're running script one. If so,

[5:20:14] call the main method to start the program. We print this is script one. Your favorite food is pizza. Goodbye.

[5:20:22] Now I'm going to go to script two. Delete our print statement. Change the run configuration to script two and run it. Nothing should

[5:20:31] happen. That's good. Now, if we were missing this if statement of if dunder name is equal to main, then we delete our main function. Here's what would happen.

[5:20:43] We're importing script one, but we're running script two. This is script one. Your favorite food is pizza. Goodbye. I

[5:20:51] don't want this code to execute. We're not running it directly. That's why we have that if statement. If under name is equal to

[5:20:59] main. I only want to run this code if we're running it directly. So what we'll do within script 2 now is define a function of favorite drink. There's one parameter of

[5:21:15] drink. I will print use an fring your favorite drink is I'll add a placeholder. We'll add our parameter of drink. Let's print the

[5:21:29] message. This is script two. We will call from script one the favorite food function. Pass in your

[5:21:40] favorite food. This time I'll say sushi. Let's call our favorite drink function. Favorite drink. I'll pass in

[5:21:51] coffee. Then we will print goodbye. Okay, we are running script two. This is script two. Your favorite

[5:22:01] food is sushi. Your favorite drink is coffee. Goodbye. We're running script 2, but

[5:22:07] we're importing the functionality of the favorite food function from script one. Sometimes from another Python script, you want to borrow something, but you don't want to run the main body of code directly. I just want to borrow this function from script one, and that's it.

[5:22:23] Script 2 can be run as a standalone program, but I can't import it without this body of code running. I can add that if statement. If dunder name is equal to a string of dunder main. If we're running this program

[5:22:39] directly, execute this code. So let's call a function of main. Define main. Then place our main body of code

[5:22:50] within it. If I run script 2, we have the same message. So by adding this if statement of if name is equal to main. This script

[5:23:01] can be run as a standalone program or it can be imported. A more practical example of this could be a Python library. You can import the library for functionality. But if you run the

[5:23:11] library directly, you could instead display a help page. It is good practice to include if dunder name equals dunder main. It makes your code more modular, helps with readability, leaves no global variables, and avoid unintended execution. And well everybody, that is

[5:23:29] the purpose of if dunder name equals dunder main in Python. Hey, what's going on everybody? So in this video, we're going to create a very simple banking program using Python. This is meant to

[5:23:41] be more of an exercise to get us used to working with functions. When creating a project, I like to divide that project into smaller sections, then handle them one at a time. So, we'll do that by declaring all the functions we'll need first. With a banking program, we'll

[5:23:54] need to show a user their balance. We'll define a function to show balance. For the time being, I'll write pass just as a placeholder. We'll need to make a

[5:24:06] deposit. Define deposit. Make a withdrawal.

[5:24:14] define withdraw. Near the end of this project, we will be creating a main function and placing the main body of our code within it. We'll handle that near the end just to contain everything. We have our three

[5:24:28] functions with our banking program. We'll need to show a balance, make a deposit, or make a withdrawal. What are some variables we'll need? Well, we'll

[5:24:36] need a balance, which I will set to be zero initially. I will also create a boolean of is running. This will be true. If at any time we set is running

[5:24:48] to be false, we'll exit the program. So with the majority of our code, we'll place it within a while loop. While is running. You can check to

[5:24:59] see if this is equal to true, but since this is a boolean, that's not necessary. We will just say while is running. If is running becomes false, we'll exit the while loop. Within our

[5:25:11] while loop, we'll print some sort of welcome message. Let's print banking program. Then list some options. Let's print

[5:25:26] one, show balance. Two, deposit. Three will be withdraw. Four will

[5:25:48] be exit. Afterwards, we will set a choice variable to equal some user input. input. Enter your

[5:26:04] choice 1 through 4. We're encouraging a user to type in a number 1 through 4 to select an option. Do they want to show their balance, make a deposit, make a withdrawal, or exit? We'll add a few if

[5:26:17] and else if statements. Let's check to see if the user's choice is equal to one, and that is a string of one. Our user input is a string data type unless we were to type cast it to something else. If our choice

[5:26:32] is equal to one, we will call the function to show balance. Else if our choice is equal to two, we will make a deposit by calling the deposit function. Else if choice is equal to three, we will call the withdraw function. Else if choice is equal to

[5:27:04] four, that means we would like to exit. So we need to exit this while loop. We can do that by setting our variable of is running is this program running equal to be false to exit. If somebody types

[5:27:18] in some input that's not valid, we can handle that with an else statement. Else, let's print that is not a valid choice. Okay, let's see what we're working with currently to test everything. We haven't written anything

[5:27:36] within these functions yet. Show balance, deposit, or withdraw. So, we can type one, two, three, and four to exit.

[5:27:47] processed finished with exit code zero. So we can exit the program. We just have to select option four. With this else statement, this

[5:27:55] will execute if we type in something besides the numbers 1 through 4 because there's no other options left. So to test that, enter your choice 1 through 4. Uh I'm just going to type the word poo. That is not a valid

[5:28:10] choice. So we know that the else statement is working. Once we exit the while loop, let's print a message that says, "Thank you. Have a nice

[5:28:30] day." If I was to type four to exit, we should exit the program. Thank you. Have

[5:28:36] a nice day. Let's make that h capital. Now, we'll work on our functions beginning with show balance.

[5:28:43] Currently, these two variables are global. We don't need to pass them as a parameter to these functions quite yet. We will be enclosing all of this code within a main function. We'll handle

[5:28:53] that later, though. So, with show balance, all we're going to do is print. I'll use an fring. Your balance is add a dollar sign

[5:29:06] or other unit of currency of your choosing. Add a placeholder. our balance variable and let's see what we have. I will type one to show balance.

[5:29:20] Your balance is $0. I'll display our balance with two decimal places. After I will add a format specifier after balance colon 2f will add two decimal places. We covered

[5:29:34] format specifiers in a previous topic. So if I were to run this again, type one, we show $0 and 0. We're displaying two floatingoint decimal places. Now we need to make a deposit.

[5:29:48] That will be the next function. We will define a local variable of amount equals accept some user input. Enter an amount to be deposited.

[5:30:07] Again, when we accept user input, it's a string. We'll type cast it to a number, a floatingoint number, because we have to include dollars and cents. We'll add some checks, though, after accepting some user input. If our

[5:30:23] amount is greater than zero, we don't want anybody to make a negative deposit. Let's print that's not a valid amount. Else we are going to return our amount. So this function is

[5:30:46] going to return something. So within our else if statement, we will take our balance plus equals the deposit we're being returned with. This will add our deposit to our balance. balance plus

[5:31:04] equals deposit. Let's try it. Let's show our balance. Our balance

[5:31:12] is $0. We'll make a deposit of $100. Exactly.

[5:31:20] Again, we'll show our balance after making the deposit. Your balance is $100. Let's attempt to deposit negative money. We'll select two to make a

[5:31:31] deposit. We'll deposit 42069. That's not a valid amount. So, we have a problem. We have a

[5:31:42] type error. Unsupported operand for float and non type. So within this statement, within if within our deposit function, we're not returning anything. Let's just return zero. We

[5:31:57] have to return something. And within this if statement, we didn't return anything previously. We'll either return zero or return a valid amount. Let's try this

[5:32:09] again. Let's make a deposit. I will attempt to deposit 42069.

[5:32:17] That's not a valid amount. Our program's not crashing. That's good. Now we'll

[5:32:23] attempt to make a valid deposit. $501. Then show my balance. Your balance

[5:32:30] is $501. Okay, that is the deposit function. We'll work on the withdraw function.

[5:32:40] Next, we will create a local variable of amount. accept some user input. Enter amount to be withdrawn. Our user input is going to be

[5:32:57] a string. We will type cast it to be a floatingoint number. We need to check to see if our amount we're trying to withdraw is greater than our balance.

[5:33:10] Users shouldn't be able to withdraw more money than what they have in their bank account. If the amount is greater than our balance that we have, we will print insufficient funds. Else if the amount somebody's trying to withdraw is less than zero, we will print a different message.

[5:33:39] amount must be greater than zero else we will return our valid amount. So with our if and else if statements we do need to return something if we take one of these routes we will return zero. We're not making any changes within our else if statement where we select choice three. We're

[5:34:10] going to take our balance minus equals the withdraw amount. Let's test this banking program. Let's show our balance. Our balance is

[5:34:26] zero. We'll make a deposit of $100. Show my balance again. Your

[5:34:32] balance is $100. Let's press three to withdraw money. Enter amount to be withdrawn. One cajillion

[5:34:41] dollar. Insufficient funds. Yeah, no kidding. Let's attempt to withdraw money

[5:34:48] again. We shouldn't be able to select a negative amount. 42069. Amount must be greater than

[5:34:57] zero. Let's enter in a valid number. This time I would like to withdraw $49.99. That has appeared to work. We'll

[5:35:06] show our balance again. Your balance is now $501. Then we can exit by pressing four to exit. Thank you and have a nice

[5:35:16] day. The last few changes I'm going to make is that I'm going to enclose all of this code, our main portion of code within a main function just to encapsulate all of our variables and help with readability. We will define a function of main. Take

[5:35:33] all of our code within the main body of our program and place it within the function. I'm just going to select all of it and indent it. At the end of our program, we need to call a main function to run it. If you're familiar with the

[5:35:48] statement of if dunder name is equal to a string of dunder main that means this program can be imported or run standalone. It is good practice to include this if statement. We discussed this in the previous video. If we're

[5:36:05] running this program directly execute the main function. However, our variables of balance and is running they're now enclosed within this local scope. These other functions have no idea what these variables are of balance. So we need to pass in our

[5:36:21] balance to those functions of withdraw and show balance. When we show our balance, we have to pass in our variable of balance. Same thing with withdraw. Then set up those

[5:36:36] parameters. Within show balance, we will have one parameter of balance. The same thing with withdraw. The last thing I'm

[5:36:43] going to do is add a little bit of text decoration around my program just to make it look nice. So, I will print a bunch of asterisks. It's not necessary, but I think it'll look nice.

[5:37:05] Let's add some text decoration before and after the title of banking program. Also before our choice. Basically whenever we print anything we'll add some text decoration. Let's do that with show

[5:37:27] balance our deposit and within withdraw. Okay, let's run this one last time. banking program. Let's show our

[5:37:58] balance. Your balance is $0. We'll make a deposit.

[5:38:04] $1001. Show our balance again. Your balance is $1001. We will withdraw money. Enter an

[5:38:13] amount to be withdrawn. $1,000. Insufficient funds. Let's try

[5:38:18] that again. Let's withdraw $50. Show our balance again.

[5:38:24] $501. Then press four to exit. Thank you and have a nice day. All right,

[5:38:30] everybody. That is a simple banking program you can write using Python. Hey everybody. In today's video,

[5:38:36] we're going to create a beginner's slot machine program using Python. This project's meant for beginners. So, let's get started. When creating a project, I

[5:38:45] like to break up that project into different sections, then tackle them one at a time. So, with the slot machine, what are some of the different functions we'll need? Well, we'll need to spin a row. We'll define a function to spin row

[5:38:59] as a placeholder. I'll write pass. We'll return to this function later. We need

[5:39:03] to display or print the row. Print row. If somebody gets matching symbols on the slot machine, we need to give them a payout, we'll create a function to get payout. In this function, we'll

[5:39:22] calculate what that payout is going to be, but again, we'll get to that later. We'll write the majority of our code within a main function. At the end of this program, I will add the if statement of if dunder name is equal to a string of dunder main. Then we will call the main

[5:39:46] function which drives our code. This program can be imported or standalone. It is good practice to have this if statement. A majority of the code we're

[5:39:54] going to write is going to be within our main function. So within our main function, let's declare the variables we'll need throughout this program. We will need a starting balance which I will just name balance. We will start

[5:40:06] with 100 as in $100. We'll need to display some sort of welcome message. Let's print something.

[5:40:15] We will print welcome to let's name our game Python slots. Just for some flavor, I'm going to add some text decoration. Just a bunch of asterisks.

[5:40:28] I think it'll look cool, but you don't have to. Let's display our symbols. We're going to use symbols. I'll add some emojis. We'll

[5:40:41] use emojis in this program in place of images. If you're on Windows, you can hold down the window key plus semicolon. Let's add a cherry. You typically see a

[5:40:51] lot of fruit in slot machines. A watermelon. a lemon. There's also a lot of bells for

[5:41:04] some reason, but we'll add those. And a star. Let me just align everything. Let's do a test

[5:41:22] run. Welcome to Python slots. Let me make one adjustment. Okay, I'm happy with

[5:41:32] that. So, after our welcome message, we'll continue playing this game while our balance is greater than zero. While we still have money, we can continue playing. We will print I'll use an

[5:41:47] fstring current balance colon space. I'll add a placeholder. Pick a unit of currency.

[5:41:55] I'll pick American dollars. Then we will display the user's balance. We will prompt the user to enter in their bet which we will assign to a variable of bet. So

[5:42:11] input place your bet amount. Let's do a test run. Welcome to Python slots. Current

[5:42:21] balance $100. Place your bet amount. We won't deduce the bed amount from the balance quite yet. I just want to be

[5:42:28] sure that we can enter in something. $1. Good. $10.

[5:42:35] $100. What if somebody types in a word like pizza? We need to prevent that input and correct it. We'll check if take our bet. use the

[5:42:50] is digit method. Is our bet a digit? If somebody types in a word like pizza, we need to tell them that's not valid. So,

[5:42:59] this will return true if our bet is a digit. But we're going to use the not logical operator. If our bet is not a digit, then do this.

[5:43:12] We will print please enter a valid number followed by the continue keyword. The continue keyword will skip the current iteration of this loop and start from the beginning. Let's test it. Place your bet amount.

[5:43:36] Pizza. Please enter a valid number. We have our current balance again. Place

[5:43:41] your bet amount. I'll type in one. Okay, we did not get that message of please enter a valid number. This bet

[5:43:49] of $1 is valid. So if our bet is a digit, we'll convert it to be an integer using type casting because when you accept user input, it's a string. It has the string data type. Let's reassign our bet. Type

[5:44:05] cast our bet as an integer. Then we will check to see if our bet is greater than our balance. People can't bet money that they don't have. If the bet is greater than the

[5:44:21] current balance, if bet is greater than balance, we will print this message instead. Insufficient funds. Then continue. If somebody tries to bet

[5:44:39] negative money or no money, we'll add this statement. If bet is less than or equal to zero, we will print bet must be greater than zero and continue. If all these checks pass, if our bet is not a digit, if our bet is greater than our balance, or if our bet is greater than zero, we will take our original balance minus equals our bet to subtract it. Let's do a test

[5:45:21] run. Place your bet amount. Pizza.

[5:45:25] Please enter a valid number. I will bet one cajillion dollars. Insufficient funds. Yeah, no kidding.

[5:45:36] 0. Bet must be greater than zero. What about $1? Our bet should be subtracted

[5:45:43] from our balance. Let's try 10. We are now down to 89. Let's bet

[5:45:51] $90. Insufficient funds. 89. And that has appeared to

[5:45:57] work. Once we subtract our bet from our balance, we will call the function to spin row. This function is going to return a list which we will assign to be row. Row

[5:46:13] will be a list. Using the spin row function, we have to generate three random symbols then return them within a list. We'll work on the spin row function next. Within our spin row function, we

[5:46:26] will declare a list of symbols. Add your symbols, but these need to be strings. Make sure they're all comma separated.

[5:46:54] There we go. This is where list comprehensions can come in. If you don't know what a list comprehension is, here's an alternative. We will declare

[5:47:04] an empty list of results. This is an empty list. We need a for loop to generate three random symbols. We could

[5:47:12] say for symbol in range three. This for loop will iterate three times. During each iteration, let's take our empty list of results. Use the append

[5:47:29] method. We will append a random choice among our symbols. So we need to import the random module. We'll do so at the

[5:47:45] top. Import random. We're telling the random module to pick a random choice from this list of symbols. Then we will append them to our

[5:47:56] empty list of results. After we escape the for loop, we will return our results. It's a list. Now, a much better

[5:48:06] option is to use a list comprehension. Here's how. It's going to be a lot more concise. We will return a list. Within

[5:48:16] the list we will write a list comprehension for every let's say symbol in range three. There is no condition. What do we want to return during each iteration? Access the random module. Use

[5:48:35] the choice method. Then pass in our symbols. Symbol isn't used in this example. What you may see people do is

[5:48:45] use an underscore as a placeholder. Basically, what we're saying is for every iteration in range three, return a random symbol. That's all we need for the spin row function. Going back, we have our list

[5:49:00] of row. Afterwards, I am going to print it to test it. Print row. And we should have three random

[5:49:10] symbols after making a bet. All right, it looks like it's working. We'll make a few changes though. Instead of printing our row, I'm

[5:49:23] going to print the word spinning, I will add a new line character just to give us some space like after this word of spinning. Then we will call the print row function. We'll pass in one argument, our row, that's returned to us after we spin the row. So going to our print row

[5:49:49] function, we need to set up one parameter, our row that we receive. It's going to be a list. One easy way to print the elements of a list is that we can print pick some sort of separator for each item in the list. For example,

[5:50:03] I'll just print a space. With strings, there are built-in methods. we will use the join method then pass in our list or other iterable. Basically what we're

[5:50:14] saying using the join method we're going to take our iterable in this case our list join each element by a space a space character. Here's the result. We have three symbols. You could

[5:50:28] join them by a different character. I'll add a vertical bar. Enter your bet amount $1. Now we

[5:50:36] have a vertical bar between each of these symbols. We could include more than one character. I'll add a space before and after this vertical bar just to space things out. I think that looks a lot better.

[5:50:50] And you don't have to, but I'm going to add some text decoration before and after. I'll add a bunch of asterisks. Let's see what we're working with. Not bad.

[5:51:07] So every time we make a bet, we get a new set of symbols. Now what if all three symbols match? We need to calculate a payout and give it to the user cuz well they won. So after we print our row, we will

[5:51:23] call the get payout function, but we will pass in our row. It's a list. And our bet. How

[5:51:33] much did we bet? We will be returned with a payout which we will add to our balance. Let's go to the get payout function. We're sending two arguments to

[5:51:47] our get payout function. A row and a bet. We have to check to see if each element in our row is all the same. Is

[5:51:57] it all the same character? We can do that with an if statement. If our row at index of zero, that's going to be the first symbol, is equal to row at index one, that's the second symbol, is equal to row at the second index, and that's the third symbol. If all three symbols

[5:52:19] match, we have to return the bet multiplied. Within our if statement, we will add another if statement. I will check to see if our row at index zero is equal to our first symbol of cherry. Be sure to place it within

[5:52:38] quotes because it's a string. Now, the reason I'm only checking if row at index zero is a cherry emoji, all these symbols are going to be the same. If we're within this if statement, all of these symbols are going to match. We only need to

[5:52:53] check one of them. It could be zero, one, or two. But I'll just add zero.

[5:52:58] They're all going to be the same regardless. If somebody has all cherries, we will return their bet times three or some other amount. You can make the payouts higher or lower. Else if row at index zero is

[5:53:15] equal to a watermelon, then we will return their bet times four. So watermelons are worth more than cherries. Else if row at index zero is equal to a lemon, we will return their bet time 5. Else if row at index zero is equal to

[5:53:49] a bell, let's give them time 10. Return bet* 10. else if row at index zero is equal to a star that's worth the most. We will return their bet time 20.

[5:54:15] Make sure we're not within our if statement anymore. If all three symbols don't match within our list, we don't want to give the user anything. They lost that spin. We will return zero.

[5:54:27] That's all we need for the get payout function. Scrolling back down after receiving a payout, it's returned to us from this function. We'll check to see if our payout is greater than zero. That

[5:54:41] means they want to spin. I will print. I'll use an F string.

[5:54:49] U1 I'll add a placeholder. Proceed this with a unit of currency. I'll use dollars. will display the

[5:54:58] payout. Else if they did not receive a payout, that means they lost that spin. We will print sorry you lost this round. Then take our

[5:55:14] balance. This is our original balance. Plus equals our payout. In most cases,

[5:55:20] the payout is going to be zero. But if the user wins something, we will add that to the balance. Okay, let's do a test run. I will bet $1. Sorry, you lost this

[5:55:33] round. And my current balance is 99. Let's bet again. I'll just keep on doing this

[5:55:40] until I win. We're going to lose more times than what we win. Okay, see I got all bells. It says you

[5:55:55] won $10. Once somebody runs out of money, we want to stop them from playing or if they would like to exit. We'll create a variable of play again. We will accept some user

[5:56:09] input. Do you want to spin again? We'll add y for yes slashn for no. If our variable of play again does

[5:56:26] not equal a character of capital y, then we will break to break out of this loop. Let's do a test run. Enter your bet amount. I'll just bet a dollar. Do you

[5:56:39] want to spin again? If I type in anything besides a capital Y, we will exit. I will type in no. Then we

[5:56:49] exit. Enter your bet amount. I'll bet a dollar. If somebody were to type in a

[5:56:55] lowercase Y, that doesn't register. We'll make it uppercase by following our input with the upper method to make it uppercase. Place your bet. A dollar.

[5:57:05] Hey, I won. I won $3. Do you want to play again? I'll type in a lowercase Y.

[5:57:11] Yes, I would like to play again, but I did not hold shift in order to make this a capital Y. That will still register. And our current balance is $12. We're ahead currently. Place your

[5:57:24] bet amount. I'll bet $10. We lost this round. I will press N

[5:57:30] because I don't want to play again. Then we exit. So at the end of our program, I will print I'll use an fstring game over your final balance is I'll add a placeholder. Pick a unit of

[5:57:49] currency. I'll pick dollars. Display our balance. Then I'll just add some text

[5:57:55] decoration before and after to make it all look nice. Okay, let's play this one last time. Enter your bet amount. I'll bet a

[5:58:07] dollar. Sorry, you lost this round. Do you want to spin again? Yes, I do. I

[5:58:12] will bet $5. You lost. Spin again. Yes, I will

[5:58:16] bet 10. 20 again. I'll bet 20. I keep losing.

[5:58:28] I'm running out of money, guys. Hey, I won $10, though. Do you want to spin again? No. Game over. Your final balance

[5:58:35] is $13. That's why you shouldn't gamble. You tend to lose more money than what you gain. All right, everybody. So, that

[5:58:42] is a slot machine program you can write using Python. Hello everybody. Today, I'm going to show you how we can write a substitution cipher encryption program.

[5:58:52] Basically speaking, what we're going to do is that we have a message. To hide the message, we can encrypt it by replacing every instance of one character with another chosen at random using the same key. We can then decrypt the message. When I was at my

[5:59:08] university, I took an intro to cyber security course. I turned this program in as a final assignment, and I did get an A on it. I don't know, maybe it'll help you. At the very least, it's a good

[5:59:19] exercise. All right, let's get started, everybody. We will begin by importing the random module as well as the string module. Let's create a string of

[5:59:29] characters named chars. Whatever characters you would like to use for your encryption program, list them here as a string. However, this can be a lot to write. I think a better solution

[5:59:41] would be to import some constants from the string module. I'm going to include some punctuation. I will import the punctuation constant of the string module. How the heck do you spell

[5:59:53] punctuation? Okay, that's right. Plus, I will add some digits. String dot digits

[6:00:01] constant plus string dot asy letters. Let's take a look at our character so far. We have one long string of characters. What if I would like to

[6:00:21] include a space, a white space? Well, there is a constant for that, but that includes things like carriage return. That's going to warp our results. Let me

[6:00:32] show you just for a demonstration. String dot whitespace plus all the other stuff. We have a carriage return and some other characters. I would like to

[6:00:44] avoid that. So in place of importing the whites space constant from the string module, I'm going to add a space character. That's good enough. Here are all the characters I

[6:00:55] will be using this program. Feel free to add more or less. This is all one long string. I'm going to turn the string

[6:01:03] into a list where each character is an individual element. To do that, I'm going to take our string of chars, reassign it, then type cast my string of characters as a list. Then let's print it again. print

[6:01:22] chars. Instead of one long string, we have a list. A list of all the characters we'll need. I am then going

[6:01:29] to create a key, which we will shuffle eventually. Key. Then to create a copy of a list, you can type the original list dotcopy method. Then I will print my

[6:01:44] key. I'm going to place these lists within an F string. chars then key. Let's see what we

[6:02:05] have. We have two identical lists. One for the original characters and the other for the key. We're going to

[6:02:13] shuffle this key. random.shuffle shuffle pass in our list of key. Look at that. All of the characters

[6:02:25] are now shuffled in a random order. What we'll be doing when somebody types in some text to be encrypted, we will replace every instance of one character within that string. Let's say an O, then replace it with another one. Every time

[6:02:41] we run this program, this key will be reshuffled. Let's ask for some user input. This part of our program we will do some encryption. Plain text is the original

[6:02:54] message. Plain text equals we will accept some user input. Enter a message to encrypt. Cipher text is the name of the

[6:03:09] encrypted message. That will be an empty string. Okay. Let's say a user types in

[6:03:16] a message. Enter message to encrypt. I like pizza. It's a very important

[6:03:23] message. Every instance of a character within my plain text, I will refer to the key and replace that letter with a different one. For example, any Z's, I have two Z's in this program, will be replaced with, let's see, capital B. Every time we run this

[6:03:42] program though, it's going to shuffle the key. So, it's not going to be consistent. What we're going to be doing is iterating over every letter in our plain text. For every letter in plain

[6:03:54] text, strings are iterable. Find the index of every letter from our plain text within our list of characters. Let's assign a variable index. index

[6:04:09] equals take our list of chars, use the index method. We are looking for that letter, whatever letter we're currently on, then return an index, then refer to our key, get whatever letter is at that same index. So, we will append that to our cipher text. It's currently an empty string.

[6:04:30] cyper text plus equals our key at the given index. Our cipher text should be the encrypted message. Now let's print it out. Print I'll use an

[6:04:49] fstring original message. Let's print our plain text. Then our encrypted message. Print our cipher text

[6:05:08] string. Let's take a look so far. Enter a message to encrypt. I like

[6:05:16] pizza. Then here's the new encrypted message. Every instance of a character within my plain text was replaced with another. So, for example, any Z's were

[6:05:26] replaced with E. I have two E's within this encrypted message. If I were to run this program again, it would likely be different. I like

[6:05:35] pizza. And here's my new encrypted message. My Z's were replaced with semicolons this time. For every ladder

[6:05:43] in our plain text, get the index of each letter. Then refer to the key. Add the new character to our encrypted message.

[6:05:51] It's probably best for us not to display the characters and the key. So, let's hide those. We will be reusing this key for decryption. Now, to decrypt the message,

[6:06:02] let's copy this section of code. Paste it. We are now decryptting. We will ask for some cipher

[6:06:11] text. Then reset our plain text. For every letter in our cipher text, refer to our key, append a character to our plain text within our list chars at a given index. We will display our encrypted

[6:06:34] message followed by the original message. Let's try it one last time. Enter a message to encrypt. I like

[6:06:47] tacos. Here's my original message. Then the encrypted message. If I were to

[6:06:52] decrypt the encrypted message, it should give me my original message. I will type in these characters exactly. Hit enter. And here is my

[6:07:03] message decrypted. I like tacos. All right, everybody. So, that is

[6:07:08] a substitution cipher encryption program for beginners. When I was at university, I did turn this program in for a final assignment for a cyber security class. And I did get an A on it, so maybe it'll help you. And well, yeah, that's an

[6:07:21] encryption program for beginners in Python. What's up everybody? So, in today's video, we're going to create a game of Hangman using Python. I thought

[6:07:32] that this would be a good mini project for us. While learning to code, it is important to create small projects as you go along. Here's one that we can make together. When creating a project,

[6:07:42] I like to declare the various variables and data structures I'll need first, followed by the functions I'll need for this game. We will need a set of words. One of these words is going to be chosen at random. So, let's create a few words.

[6:07:57] I'll add some fruit. Apple, orange, banana, coconut, and one more pineapple. Using the random module, let's import that. Import

[6:08:15] random. Using the random module, we will pick one of these words at random. We won't be able to see what it is, but we can guess what the word is one letter at a time. Once we reach six

[6:08:28] incorrect guesses, we lose the game. Before each guess, we will display some ASI art, which I will name as hangman art. This will be a dictionary. A dictionary

[6:08:40] where each key value pair contains a tuple. So this is a dictionary of we'll have a key which will be a number and a tpple. The key is going to represent the incorrect number of guesses. So we'll start at zero. We

[6:09:00] will display a tpple which will contain some asy art. Then let me just copy this. For one incorrect guess, we'll display some different ASI art. I'll just put each on a new line

[6:09:15] for readability. So, we're going to go all the way up to six. Once we hit six incorrect guesses, we lose the game. Each key corresponds to the number

[6:09:33] of incorrect guesses. Once we reach six, we lose the game. Each tpple that corresponds to the incorrect number of guesses, we will display a certain image. If you would like, feel free to

[6:09:45] look in the description of this video if you would like to copy this to save you some time. Each tpple will consist of three rows, three strings. For no incorrect guesses, where incorrect guess is a zero, we will display nothing. We can't see our

[6:10:02] hangman person. For one incorrect guess, we will display their head. For two incorrect guesses, we will display their head and the main torso of their body, which will represent with a vertical bar. Let me copy this

[6:10:21] one. For three incorrect guesses, we will display their left arm represented with the forward slash. with four incorrect guesses, we will display their right arm. However, if you

[6:10:35] use a backslash, that's an escape sequence within a string. You have to use double backslashes to literally print a backslash. So, with five incorrect guesses, we will display their left leg of the person. Then, once we reach six

[6:10:52] incorrect guesses, we display the full person. That's when we lose the game. when we see the entire person. That's

[6:10:59] some asy art that we can use. So, let's test it just to be sure that everything is working fine. I will print my hangman art at the key of zero to represent no incorrect guesses. Okay. So when we display this

[6:11:18] person, we're going to have to use some sort of loop for every let's say line in hangman art at index of zero for zero incorrect guesses. I will print each line with no incorrect guesses. We don't display anything. That's

[6:11:42] correct. We can't see the person and that's okay. So with one incorrect guess display the dictionary where the key is one that displays the person's head. Two two would be the main torso of

[6:12:01] their body. Three, their left arm. Four, their right arm. Five, their

[6:12:11] left leg. And six, their right leg. Once we see the entire person, we lose the game.

[6:12:19] So, we can delete these two lines of code. We no longer need them. We know that our dictionary is working. I'm

[6:12:26] going to zoom out a little bit. Following our dictionary, we'll declare the various functions we'll need throughout this program. We will define a function to display man, our hangman. There will be

[6:12:39] one parameter wrong guesses. And then for the time being I'll write pass. We'll fill in this function later. When we display our man,

[6:12:51] we need to know the number of incorrect guesses to display the right image. We have a display man function and a display hint function. We will have a string of hint. Then I'll write pass for now. Our

[6:13:14] hint is going to be a list, a list of underscore characters. For each letter that we guess, right, we'll flip one of those underscores to be a letter if that letter is correct. I'll create a function of display answer. Within this function, we will

[6:13:32] display the correct answer either when we lose the game or win the game. And I will write pass. We will create a function of main to contain the main body of code of our program. Again, I'll write pass for

[6:13:48] now. I'll add the following if statement. If dunder name is equal to a string of dunder main. If we are running

[6:13:59] this file directly, I would like to call the main function to start the program. All right, let me zoom out. This will be the main skeletal structure of our program. Import the random module. We

[6:14:12] have our set of words. We'll be importing more from a separate file near the end of this video. We have a dictionary where the key is a number to represent the number of incorrect guesses. And a tpple to display some asy

[6:14:24] art. We have four functions. Display our man, display the hint, display the answer, and the main function to contain the main body of code. All right, let's

[6:14:34] work within our main function. Within our main function, we will create a variable of answer. What is the correct answer that we have to guess? I will access the random module,

[6:14:46] call the method of choice, then pass in our set of words. One of these words will be chosen at random. Let's test that. I will print

[6:14:58] our answer just temporarily. We should get a random word. Apple.

[6:15:04] Apple. Pineapple. Apple. I guess it

[6:15:08] really likes apple for some reason. There we go. We have orange. We are

[6:15:11] choosing a word at random. We no longer need this print statement. Looks like everything is working fine. Now we'll display our

[6:15:21] hint. Our hint is going to be a list of underscore characters. I need the number of underscore characters to equal the number of characters in one of these words that is chosen at random. So I could multiply my list by

[6:15:40] the length using the length function of my answer. So let's print our hint to see what we're working with. With my selected word, we have how many underscores? 1 2 3 4 5 6 7. Okay,

[6:15:59] we have a different word. 1 2 3 4 5. That is probably apple. It has five

[6:16:07] characters. All right, so that's our hint. It's a list of underscore characters. When we guess a letter, if

[6:16:14] it's correct, we'll fill in one of the underscores with that correct character. We need to keep track of the number of wrong guesses. We'll create a variable of wrong guesses. Set that

[6:16:26] equal to be zero. When we start the game, we're going to keep track of all of the incorrect guesses that we've made. We will create a set of guested letters. For an empty set, we'll call

[6:16:40] the set function. Normally in Python, you can't create an empty set with just a set of parenthesis. We have to use the set function. Then I will create a

[6:16:49] boolean variable of is running. Set that to be true. While our game is running, continue playing. Once we lose

[6:16:58] or win the game, we will switch this to be false to exit the game. We will keep this as true when we initially run this program. After we declare the variables we'll need within the main function, we'll create a loop, a while loop. While is running, we don't need to

[6:17:16] say while is running is equal to true. We don't necessarily need to create that comparison. We can just say while is running while this is true continue doing some code. So what would we like

[6:17:29] to do? Let's call the function of display man. But we have to pass in the wrong number of guesses. Call our function of display

[6:17:40] man. Pass in our variable of wrong guesses. When we begin the game, we would like to display one of these images.

[6:17:49] Then we will display our hint. Then we'll call the function to display our hint. Pass in our hint. That was the

[6:17:58] list of underscore characters to represent the answer we have to guess. We will create a variable of guess and accept some user input. We'll prompt the user to enter a letter.

[6:18:14] Just in case a user types in a character that's uppercase, let's add the lower method to make it lowerase. So, let's fill in our display man function. There's not a lot to write here. When we call this function, we

[6:18:30] need to display one of these images based on the wrong number of guesses, one of these keys. Within the display man function, we'll create a for loop for every line in my hangman art this dictionary at the key of wrong guesses. This will be a number 0 through six. Depending on what this number is, I

[6:18:59] will print each line. Print each line of that tpple. Let's see what we're working with. We'll

[6:19:08] do a test run. So, we are displaying no person. We can't see them. For testing purposes,

[6:19:16] I'm going to change wrong guesses to be one, we're displaying their head. Two, displays their body. Three displays left arm.

[6:19:29] Four is their right arm. Five their left leg. and six is their full body. That's when we

[6:19:40] lose. Now, you don't necessarily need to do this, but I'll add some text decoration before and after. I'll add just a bunch of asterisks before and after. I think that looks better, but

[6:19:56] you do you. Let's be sure to set wrong guesses back to zero. After we display our hangman, we have to display the hint. what's the

[6:20:05] clue we're trying to solve. So we will call our display hint function and pass in our list of hint. So within the display hint function, let me zoom out. I will print

[6:20:18] the following. Between each character within our hint, each underscore, we will display a space character. Strings have a built-in join method. We'll call that then pass in our

[6:20:32] hint. For each character within our hint, join it by an empty space. So now when we do a test run, we are displaying an underscore to represent each character. Each is separated with the

[6:20:49] space. While we're here, we'll fill in the display answer function. We just have to copy this line of code from display hint. Replace hint with answer.

[6:20:59] And that's all we need for the display answer function. So let me test that real quick. After displaying our hint temporarily, I will display our answer just to be sure that it's working. Yep, there's our hint. And

[6:21:14] there's our answer that we have to guess. Okay, let's delete this line of code. We don't want to display the answer. I was just testing it. So the

[6:21:24] user is going to be able to type in a letter to guess such as a for example. Once we guess a letter, if that letter is found within the hint, if it's one of these characters, we need to switch that underscore to be one of those characters. So we'll write the following if statement. If our guess is in our

[6:21:48] answer, in is a membership operator. If this letter is found within our string of answer, we're going to create a loop. We will create a loop that will iterate once for each character within the answer. But we don't know the length of

[6:22:02] the answer because Python will choose it at random. So let's say for every index, we can shorten this to i. for I in range the length of my answer. Let's say the word is apple. The

[6:22:22] length of the word apple has five characters. This would return five for i in range five. Then we will iterate five times. We'll iterate this loop once for

[6:22:34] the number of characters within my answer. We'll check during each iteration if our answer at index of I during the first iteration that will be zero then the second iteration it will be 1 then two so on and so forth strings are iterable if our answer at index of i is equal to our guess if there's a match if we guess the correct letter then we're going to take our hint at that given index of I and set that equal to be our guess. Looks like this if statement is outside of the while loop. I'm just going to indent it by one

[6:23:17] somewhere within it. Okay, let's do a test run. I'm going to guess the letter A. Yes, we have one A. Let's do

[6:23:29] something that's probably not in here. Q. Okay. So, there were no matches. We

[6:23:36] don't end up doing anything. So, what is this word? Probably this should be the word orange. So, let's guess

[6:23:46] O R N E G. All right, we know that it works. What if somebody types in some input that's not valid? Before checking if

[6:24:00] that guess is correct, we'll do some input validation. What if the user types in a whole word like pizza? We want the user to only guess a single character, not many characters. We'll add the following

[6:24:16] line. If the length of our guess that we type in does not equal one, then I will print the following message. Let's say invalid input. Then we will use the keyword of

[6:24:35] continue to skip this loop. Continue. Okay. Enter a letter. I will

[6:24:43] type the word pizza. We get this message of invalid input. We skip that loop's current iteration. I will guess A. There are two

[6:24:53] A's. I will type banana. And again we get invalid input. We have to guess one

[6:24:59] letter at a time. What if somebody types in a number like one? We would like to prevent that. So within this if statement I

[6:25:12] would like to execute this code if our guess is not an alphabetical character. I can add the following or not. Take our guess dot use the is alpha method. If our guess is an

[6:25:30] alphabetical character, this returns true. If it's not an alphabetical character, it's false. So we are checking if this is not an alphabetical character, we execute this code. Let's

[6:25:44] try this again. I will type in one invalid input 42069 invalid input. Let's say we guessed the letter A. What if we type in a letter we have

[6:25:59] already guessed? I will guess A again. If they already guessed a letter, I don't want that to count. We'll skip

[6:26:06] the current loop iteration. I'll add another if statement. If our guess is in our set of guess letters, then I will print the following. I'll use an F

[6:26:27] string. Our guess is already guessed. Oh, one thing I'm forgetting.

[6:26:38] Once we check that our guess is not within our guess characters, we'll take our guess letters. This is a set, add the guess. We're keeping track of the letters we have already guessed. So I will type let's guess A.

[6:26:57] We have one A. If I were to guess A again, we get that message of A is already guessed. And then be sure to add continue to skip the current loop iteration. All right. Now going down to

[6:27:12] this if statement. If guess is in our answer. If we guess a character that's incorrect, we will take our variable of wrong guesses incremented by one. Wrong

[6:27:25] guesses plus equals 1. Let's do a test run. I will guess A.

[6:27:34] There is an A. What about Q? There is no Q. We display our dictionary where the

[6:27:40] key is one. We display that ASKI art. R. Is there an R? Yes, there is an

[6:27:47] R. This is probably orange. I would like to be sure we display the entire person. I will guess

[6:27:56] some wrong characters. We know that that works. Now, we need a win condition if we guess all of the correct characters and display the entire word. We'll work on that

[6:28:11] next. If there are no underscore characters not in our hint, this will be true if there are no underscore characters in our hint. if underscores not in hint. We'll call our function of display

[6:28:31] man. Pass in the wrong number of guesses. Call the function of display answer. Pass in our

[6:28:44] answer. We will print the text of you win. Then set our boolean variable of is running equal to be false. Let's win this time. I already

[6:28:59] know that this word is probably pineapple. Let's guess something incorrect. There we go. We have two

[6:29:14] wrong guesses, but we have correctly guessed the word pineapple. You win. and we exit the program. What if we lose?

[6:29:22] I'll add the following if statement. Else if our variable of wrong guesses is greater than or equal. So the length of our hangman art is a total of seven. There's seven total

[6:29:42] keys. But once we hit six, we lose the game with this else if statement. If the length of our hangman art, the length of our hangman art is going to be seven. So we are going to

[6:29:58] subtract one for six for a total of six. Once our wrong guesses is greater than or equal to six, that means we lose the game. We will call the display man function. Pass in the wrong number of

[6:30:14] guesses. Display what the correct answer should have been. Display answer. Pass

[6:30:19] in our answer. We will print you lose. Then take our boolean variable of is running. Set that to be

[6:30:35] false. I'll guess incorrect letters. There the word was coconut. We have six

[6:30:46] incorrect guesses. We display the entire hangman. The correct answer was coconut.

[6:30:51] You lose. If you would like to import a larger variety of words, we could create a separate Python file for that. So within our project folder, we will create a new Python file. I will name

[6:31:04] this Python file words list. This will be a Python file. Let's take our set of words. Cut

[6:31:16] it. I'll add a note that these are words for hangman game. Words will be a set. I recommend

[6:31:27] looking online for a very large set of words that we can use. Then just copy and paste them within here. While browsing online, I found an extensive list of animals that I can use.

[6:31:39] So here are all the possible words for my game. So from my main Python file, I have to import this module of words list. From the module of words list, import words. And now I have a greater variety

[6:31:59] of words I can use. Let's run this one last time. This word has four letters.

[6:32:05] I'll guess the vowels. There's an A. No.

[6:32:09] E. I O. There is an O. Is it

[6:32:16] goat? Nope. T R bore. All right. The word was boar. You

[6:32:26] win. All right everybody. So that is a game of hangman that we can create using Python. Hey everybody. So we have

[6:32:34] finally made it to Python objectoriented programming. This is a very important topic. In Python, an object is a bundle of related attributes and methods.

[6:32:45] Attributes are similar to variables to describe what the object has. So look around you right now. You are surrounded by different real world objects. Next to

[6:32:55] me, I have a phone, a cup, and a book. Each of these objects can have different attributes to represent it. For example, an attribute of the phone next to me could be version number. I could set

[6:33:07] that to be 13. Is on could be another attribute. Is the phone powered on or not? That could be true or false. Or

[6:33:14] even a price. I have a cup next to me. What liquid is within the cup? In this

[6:33:19] case, coffee. What's the temperature of the cup? Is the cup empty? Is empty? Or

[6:33:25] even a book. What's the title of the book? That could be a string. How many

[6:33:30] pages does the book have? Pages could be another attribute. Now, objects also have the capability to do things. They

[6:33:37] have methods, which are functions that belong to an object. People mix up functions and methods all the time. They're technically different. Even when

[6:33:46] teaching, I tend to make that mistake, calling a method a function, and a function a method. Usually, people know what you're referring to, though. A method is a function that belongs within an object. What are some actions these

[6:33:58] objects can perform? With a phone, you can make a call or receive a call. Turn the phone on or turn the phone off.

[6:34:07] Those could all be functions. With a cup, you could fill the cup, drink from the cup, or empty the cup. With a book, you can open the book, read the book, and close the book. An object is a

[6:34:19] bundle of related attributes and methods. They can represent real world items. To create many objects, we'll need to utilize a class. A class is a

[6:34:31] type of blueprint used to design the structure and layout of an object. We need to design what our objects have, their attributes, and what they can do, their methods. We will create a class of car. We will create some car

[6:34:47] objects. Class car. To construct a car object, we need a special type of method called a constructor. It works similarly to a

[6:34:58] function. We will define a function of double underscore init meaning initialize double underscore again and then follow this with a set of parenthesis. This is our constructor method. We need this method in order to

[6:35:15] construct objects. It's a dunder method. Dunder meaning double underscore. That's

[6:35:20] a future topic. I don't want you to be overloaded with information right now. All you need to know is that we need this method in order to create objects.

[6:35:29] This method behaves similar to a function. We need to set up the parameters. Self is already provided to us. Self means this object we're

[6:35:38] creating right now. This car. So what are some attributes that a car should have? A model, that could be a string

[6:35:48] like a BMW, a year, that could be a number, a color. Let's add a boolean of for sale. Is the car for sale or not? That's true

[6:36:02] or false. To assign these attributes, we're going to access self. self dot the name of the attribute self domodel equals the model we receive these are parameters when we receive the name of a model we will assign it to this object let's do this with year self doyear equals year self doc color equals color self for sale equals for sale.

[6:36:37] This is an example of a few attributes that a car might have. A model, year, color, and if it's for sale or not, represented by a boolean. Now, to construct a car object, we need a unique name for this car. Let's just say car 1.

[6:36:53] Car 1 equals take the name of the class. Add a set of parenthesis to invoke the constructor. We're going to do this almost exactly like a function. We have

[6:37:05] parameter set up. We need to send a matching number of arguments. Self is provided to us behind the scenes automatically. We need a model, year,

[6:37:14] color, and if it's for sale or not. So, pick a car of your choosing. I'll pick my favorite car. The model will be a

[6:37:23] Mustang. For the year, I'll go with the recent year of 2024. A color, I'll pick red. Is the car

[6:37:32] for sale? I like this car. So, no, I will set that to be false. Make sure

[6:37:37] false is capitalized. Let's see what happens if I attempt to print our car object of car 1. What we're given is the memory address of this car object where it's located. But I would like one of the

[6:37:54] attributes located at this memory address. Instead of printing the object itself, we're going to access one of the attributes found within this car, we will follow the name of the car with a dot. This dot, it's known as the attribute access operator. I would like

[6:38:13] the model of car 1. That would give me Mustang. Let's access the year. Take the

[6:38:21] name of the car, car 1 dot the year 2024, followed by the color car 1 dot color red car 1 is it for sale. We'll print that. That is false. Now let's create a second car.

[6:38:45] We're going to reuse this class to create a second car. We will create car 2 equals car. We'll pass in some different arguments. A Corvette. The year will be

[6:38:58] 2025. The color will be blue. Is this car for sale? Let's say that is

[6:39:05] true. Instead of accessing car 1's attributes, let's access car 2's attributes. That would give us a Corvette. The year is 2025. The color is

[6:39:17] blue for sale is set to true or even a third car. Car 3 equals a new car. We will pass in a string of charger. The

[6:39:31] year 2026 the color will be yellow. Is this car for sale? Let's say that is true as well. Then I will print car 3's

[6:39:41] attributes. The model is Charger. The year is 2026.

[6:39:48] The color is yellow. For sale is set to true. With classes, they can take up a lot of space. For better organization,

[6:39:57] you can place them within a new Python file. So, let's cut our class. And we will create a new Python file within our project folder. File,

[6:40:09] new, Python file. The name of this Python file is going to be all lowercase car. Then we will paste the class that we cut originally. Class car which has a

[6:40:25] capital C. So from our main Python file, we're going to import our car file, our car module. From the name of the module, car, import the name of the class, car.

[6:40:39] Then when I run this program, nothing should change. We should still have access to all of our car objects. You could either keep your classes within your main Python file or import them if you would like to organize things. Let's talk about

[6:40:55] methods. Methods are actions that are objects can perform within our class. We will define a method of drive. self is

[6:41:05] going to be provided to us when we invoke the drive function. Let's print you drive the car. What other things can cars do? Let's

[6:41:19] stop. We will print you stop the car. Let's take car one access the drive method.

[6:41:35] You drive the car. Car 2 also has a drive method. You drive the car. Same

[6:41:41] thing with car 3. You drive the car. Let's access the stop method. Car one.

[6:41:51] Stop. Car 2. And car 3.top. These methods are identical for

[6:42:00] each car object. Instead of printing the word car, let's insert the model of the car, I will convert these print statements to fstrings. Instead of the word car, let's add a placeholder. Let's add self dot

[6:42:18] model. Self is referring to the object we're currently working with. Use the attribute access operator followed by the name of the attribute. Let's also do

[6:42:29] this with the stop method. self do. Let's take car one. Use the drive

[6:42:40] method. You drive the Mustang. car one stop. You drive the Mustang. You stop

[6:42:49] the Mustang. Let's do this with car two. You drive the Corvette. You stop

[6:42:55] the Corvette. Car three, you drive the Charger. You stop the charger. Now within our F strings, let's

[6:43:04] also insert Let's insert the color. I'll add a placeholder. self dot color. Do this with stop as

[6:43:15] well. self dot color. You drive the yellow Charger, you stop the yellow Charger. Car one, you

[6:43:27] drive the red Mustang, you stop the red Mustang. Car two, you drive the blue Corvette, you stop the blue Corvette. Let's add one last method. Let's create a method to

[6:43:40] describe our car. We'll print the details of the car. Let's print I'll use an fring. Add three placeholders.

[6:43:51] Let's print self dotyear followed by self dot color then self do model. We'll take car 1 use the describe method that we created. Describe car 1. Car 1 is a 2024

[6:44:14] red Mustang. Describe car 2. Car 2 is a 2025 blue Corvette. Car 3 is a 2026

[6:44:24] yellow Charger. All right, everybody. So, those are objects in Python. An

[6:44:29] object is a bundle of related attributes. Attributes are variables that an object has and methods. Methods are functions that belong to an object.

[6:44:41] They define what this object can do. And well everybody that is a summary of object-oriented programming using Python. Hey everybody today I got to talk about class variables in Python.

[6:44:54] Class variables are shared among all instances meaning objects created from a class. Instance variables are defined inside of the constructor. Class variables are defined outside of the constructor. With class variables, they

[6:45:09] allow you to share data among all objects created from the class. With instance variables, each object has their own version. With a class variable, all those objects share one variable. Here's an example. We will

[6:45:24] create a class of student. We also need a constructor. When we create a student object, this constructor is automatically going to be called, but we need to pass in some arguments. We are provided with self.

[6:45:39] Self refers to the object we're currently working with. We will set up a name parameter and an age parameter. We will assign self the object we're currently working with. Set the name

[6:45:53] attribute to equal the data for the name that we receive from this parameter. And self age equals age. Let's construct two student objects. We will have student

[6:46:07] one equals then call the constructor for student. So type the name of the class followed by a set of parenthesis to invoke it. This will automatically call the constructor. But we have to pass in

[6:46:19] data for the name and the age. For the name, let's pass in Spongebob because basically everybody in the world knows who Spongebob is. I don't know how old Spongebob is. We'll say he's 30. We'll

[6:46:32] create another student object which we will refer to as student two. We will call the constructor of our student class. Pass in data for the name and age. Student two will be Patrick.

[6:46:45] Patrick will be 35. Okay, let's make sure this works. Let's print student one's name followed by student one's age.

[6:47:01] And we should get Spongebob and his age is 30. Let's print student 2's name and student 2's age. Patrick. Patrick is 35.

[6:47:12] Now we'll create a class variable. Class variables are defined outside the constructor and they are shared among all objects created from that class. Each object has their own name and age property. These are instance variables.

[6:47:27] But class variables are defined outside the constructor. Each object will share this one variable. So if we're working with students, let's say there is a class variable of class year. What is the

[6:47:44] graduating year of this class? 2024. Now let's print student one's graduating year.

[6:47:55] print student one dot class year. Okay, so Spongebob has a class year of 2024. That's when he's graduating. Let's check student

[6:48:15] two. Patrick, his age is 35. His graduating class year is 2024. Now with

[6:48:22] class variables, you can access them through any one object such as student one or student two. It's good practice to access a class variable by the name of the class rather than any object created from the class. Since we're accessing class year, we'll access this class variable by the name of the class of student. Make sure the S is

[6:48:47] capital. This helps with clarity and readability. If I was looking at this print statement, I can tell that class here is a class variable because we're accessing it directly from the class and not any instance from this class.

[6:49:02] Without looking at this class, I can't tell if class year is an instance variable or a class variable. But if I access it via the class name, it's more explicit. So, it's good practice to access a class variable by the class name itself and not any one instance of this class.

[6:49:21] Let's create another class variable. We'll create a class variable to keep track of how many students we have created. This class variable will be num students meaning number of students equals zero. So within our

[6:49:37] constructor we can write any code that we want. This code will always be executed when we instantiate an object. I would like to take our number of students and increment it by one each time we construct a new student object.

[6:49:52] So instead of using self, self refers to the object we're currently working with. If we're constructing student one, just imagine we're replacing self with student one or student two if we were constructing student two. If we're going to be modifying a class variable, in place of self, we'll use the name of the class student. access our class of

[6:50:15] student get the class variable of number of students then I will increment it by one plus equals 1. We are constructing two student objects. I will print access our class of student get the number of students and print it. We're constructing two student

[6:50:39] objects. If I print the number of students that we have, it should be two. Then just to be sure that this is working, let's construct a third student object. Student three equals student.

[6:50:53] This student will have a name of Squidward. Squidward's age will be 55. Now we have three students. And for good measure, let's

[6:51:04] construct one more. Student 4 equals we will create a new student with a name of Sandy. Sy's age will be 27. The number of students is now four.

[6:51:20] Just as an exercise using an fstring let's print the student classes class year as well as the number of students. I will print use an F string my graduating class of let's add a placeholder access the class of student then access the class year my graduating class of 2024 has then we need the number of students we'll add a placeholder access the class of student access the number of students has blank students. Let's see if this works. My
[6:52:10] graduating class of 2024 has four students. Now, if I were to change 2024 to 2025, my graduating class of 2025 has four students. Let's print the name of each student. These are instance variables.

[6:52:28] Student one name. Then we need student two, three, and four. My graduating class of 2025 has four students. Spongebob, Patrick,

[6:52:44] Squidward, Sandy. All right, everybody. So, those are class variables.

### **Wave 3: Dictionaries, Functions & Logic (26-40)**

**26. Dictionaries**
- **Mastery Core:** Unordered, changeable, and indexed collections of key:value pairs.
- **Technical Reference:**
  | Method | Action |
  | :--- | :--- |
  | `.get(key)` | Safely retrieves value; returns `None` if key missing |
  | `.update({k:v})` | Adds or modifies key-value pairs |
  | `.pop(key)` | Removes key and returns its value |
  | `.keys()` / `.values()` | Returns view objects of all keys or values |
  | `.items()` | Returns list of key-value tuples for iteration |

**27. Project 9: Concession Stand**
- **Logic Blueprint:**
  1. Define dictionary `menu = {"pizza": 3.00, "nachos": 4.50, ...}`.
  2. Initialize an empty `cart = []` and `total = 0`.
  3. Loop with `input()` to allow users to add items until "q" is pressed.
  4. Iterate through the cart, print items, and accumulate `total += menu.get(food)`.

**28. Random Module**
- **Technical Reference:**
  - `random.randint(min, max)`: Inclusive integer.
  - `random.choice(sequence)`: Pick one random element.
  - `random.shuffle(list)`: In-place randomization of a list.

**29. Project 10: Number Guessing Game**
- **Logic Blueprint:** Generate a target using `randint()`. Use a `while` loop to track `guesses` count. Provide "Too High/Low" hints until `guess == answer`.

**30. Project 11: Rock Paper Scissors**
- **Logic Blueprint:** Use a tuple `options = ("rock", "paper", "scissors")`. Use `random.choice()` for computer. Compare using `if-elif-else` chain.

**31. Project 12: Dice Roller**
- **Logic Blueprint:** Input number of dice. Loop `range(num)` and append `random.randint(1, 6)` to a list. Join list into a string for display.

**32. Functions**
- **Mastery Core:** A block of reusable code defined with `def`.
- **Logic & Nuance:** Functions must be defined *before* they are called. Parameters are the variables in the definition; arguments are the values sent during the call.

**33. Default Arguments**
- **Technical Blueprint:** `def greet(name, greeting="Hello"):`. If `greeting` is omitted in the call, it defaults.

**34. Keyword Arguments**
- **Mastery Core:** Passing arguments by name: `func(last="Doe", first="John")`. Order doesn't matter, improving readability.

**35. Arbitrary Arguments (\*args, \*\*kwargs)**
- **Mastery Core:** Handle a variable number of arguments.
  - `*args`: Packs positional arguments into a **Tuple**.
  - `**kwargs`: Packs keyword arguments into a **Dictionary**.

**36. Iterables**
- **Mastery Core:** Any object capable of returning its members one at a time (Lists, Tuples, Sets, Strings, Dictionaries).

**37. Membership Operators**
- **Technical Reference:** `in` and `not in`. Used to check if a value exists within an iterable.

**38. List Comprehensions**
- **Technical Blueprint:** `[expression for item in iterable if condition]`. A concise way to generate new lists.

**39. Match-Case (Python 3.10+)**
- **Mastery Core:** A switch-statement alternative. Pattern matching for cleaner control flow.

**40. Modules**
- **Mastery Core:** Using `import` to access code from other files. Prevents "God files" by separating logic into distinct `.py` units.

---

### **Wave 4: Object-Oriented Mastery & File I/O (41-60)**

**41. Intro to OOP**
- **Mastery Core:** Classes serve as a blueprint for objects. Objects possess **attributes** (what it is) and **methods** (what it can do).

**42. Constructors (\_\_init\_\_)**
- **Logic & Nuance:** `self` refers to the specific instance of the object being created. It allows attributes to be unique to each object.

**43. Class Variables**
- **Mastery Core:** Variables shared among all instances of a class. Defined outside the constructor. Access via `ClassName.variable` or `instance.variable`.

**44. Inheritance**
- **Mastery Core:** A child class inherits attributes and methods from a parent class. Promotes code reuse.

**45. Multiple Inheritance**
- **Mastery Core:** A child class inheriting from more than one parent. `class Child(ParentA, ParentB):`.

**46. Multilevel Inheritance**
- **Mastery Core:** A chain of inheritance: `Grandparent -> Parent -> Child`. The Child inherits from all levels above.

**47. Super() Function**
- **Mastery Core:** Used in a child class to call methods from the parent class (especially `__init__`). Avoids hardcoding parent names.

**48. Polymorphism**
- **Mastery Core:** "Many forms". Treating different objects as the same type through a common parent class or interface.

**49. Duck Typing**
- **Mastery Core:** "If it looks like a duck and quacks like a duck, it's a duck." Focus on methods/attributes rather than class inheritance.

**50. Static Methods**
- **Mastery Core:** Use `@staticmethod`. Methods that don't require `self` or `cls`. They are utility functions associated with a class namespace.

[6:53:02] well everybody, those are class variables in Python. What is going on everybody? So today I got to talk about inheritance in Python. Inheritance allows a class to


[6:53:29] we're going to create an animal class. The dog, cat, and mouse class will inherit attributes and methods from the animal class. We will create a class of animal. Then I will define the

[6:53:45] constructor. When we construct an animal object, let's pass in a name. It's not required, but it might be good for this example. We will assign the attribute of

[6:53:56] name equal to the name we receive. Let's also add an attribute of is alive. Whenever we create an animal, we will set their is alive attribute to be true and that is a capital T. All animals can eat. Define eat. We

[6:54:16] will print using an string. Add a placeholder self.name. The name of this animal is

[6:54:25] eating. All animals should be able to sleep. Define sleep. Print. I'll use an

[6:54:34] fstring. Insert self.name is sleeping. And that is all

[6:54:41] we need for the animal class. Let's define class dog. For a child class to inherit the attributes and methods from another class after the class name that's going to inherit, we need to add an inheritance list with a set of parenthesis. Then list the name of the

[6:54:59] class we're inheriting from the parent. The dog class is going to inherit all of the attributes and methods of its parent animal. For the time being, as a placeholder, I'll add pass just to demonstrate this.

[6:55:14] Class cat is also going to inherit from animal. And class mouse will also inherit from animal. Okay, I will collapse this for now. We'll create a dog object. Dog

[6:55:32] equals dog. Then pass in a name for this dog because we have one parameter set up of name. This dog will be named Scooby as in Scooby-Doo. Cat equals call the cat

[6:55:50] constructor. This cat will be named Garfield. And mouse mouse equals mouse. Our mouse will

[6:56:00] have a name of Mickey. Even though there's nothing within this dog, cat, or mouse class, we should still have these attributes and these methods. If you inherit the animal class, you should have a name attribute and is alive attribute set to true. You

[6:56:17] can eat and you can sleep. Let's print our dog's name. dog.name.

[6:56:27] Scooby print dog is alive. Our dog is alive. That is true. Let's have our dog object use the

[6:56:39] eat method. Scooby is eating and sleep. dog sleep. Scooby is sleeping. Let's replace

[6:56:50] dog with cat. The name of the cat is Garfield. Garfield is alive. Garfield is eating.

[6:56:59] Garfield is sleeping. And mouse. Replace any instance of cat with mouse. Our mouse's name is Mickey.

[6:57:08] Mickey is alive. Mickey is eating. Mickey is sleeping. Even though these

[6:57:12] children classes are empty, we're still inheriting these attributes and methods from its parent of animal. This is convenient because you don't need to copy and paste these attributes and methods for every single class. For example, if I were to copy these attributes and methods and paste them, well, we have a lot more code to write. And as a consequence, if I need

[6:57:37] to make a change to one of these methods, I would have to do that to every single instance of this method. For example, let's replace is sleeping with is asleep. Well, now I need to find every single sleep method and change it manually. It's not too bad if you only

[6:57:58] have a few classes, but imagine if you have hundreds of classes. That's going to take a lot of work. It's a lot easier to write the code once and then reuse it. And I only need to make that change

[6:58:09] in one place rather than make that change many times. So, let's change is sleeping to is asleep and see if that works again. Mickey is asleep. Let's replace mouse with

[6:58:26] dog. Scooby is asleep. Not only that, but with children classes, they can have their own attributes and methods that are different from one another. So, dogs have all these

[6:58:37] attributes and methods and they can speak. Let's create a speak method. And I will print a unique message for dogs. Woof.

[6:58:48] Cats will also have a speak method, but it's going to be different. Cats will meow. Then for our mouse class, they will squeak. Let's have our dog speak.

[6:59:11] Woof. Let's have our cat speak. Meow. And our

[6:59:17] mouse. Squeak. All right, everybody. So, that's

[6:59:20] an introduction to inheritance. Inheritance allows a class to inherit attributes and methods from another class. Much like in real life, a child can inherit traits from a parent. These

[6:59:33] are also known as sub and superasses which is a topic for another day. Inheritance helps with code reusability and extensibility. If all of these children classes inherit these attributes and methods from another class, we only need to write that code once and not copy it for every single class that needs it. We can write and

[6:59:54] change the code in one place for better reusability and extensibility. And well everybody, that is an introduction to inheritance in Python. Hey everybody. So today we got to talk

[7:00:04] about both multiple and multi-level inheritance. We'll begin with multiple inheritance. That's when a child class inherits from more than one parent class. For example, a class of C can

[7:00:17] inherit the traits from both class A and B. In Python, you can have more than one parent. Multi-level inheritance we'll talk about near the end of this topic.

[7:00:27] So in this example, we're going to create two parent classes. prey. I'll write pass for now. And

[7:00:39] predator we'll create a class of rabbit, a class of hawk, then class fish. Rabbit, hawk, and fish are going to be children classes. Prey and predator will be parents. If one of

[7:01:03] these classes, rabbit, hawk, or fish, inherit from prey, they get the ability to flee. We will define a method of flee. All we'll do in this example is print the following text. This animal is fleeing. If you're

[7:01:21] a predator, you get the method to hunt. Define hunt. We will print this animal is hunting. Rabbits, they will inherit from

[7:01:37] the prey class. They're typically not predators except that one rabbit in Montipython and the Holy Grail. That's the exception. Rabbit will inherit the

[7:01:46] prey class. Then it gets access to a flea method. Hawks are predators. They

[7:01:52] will inherit the predator class. Now fish, they will hunt smaller fish and flee from bigger fish. You can consider fish both prey and predators. So they

[7:02:04] will inherit both classes. We will use multiple inheritance. They will inherit everything from the prey class and the predator class. Now let's see if this

[7:02:14] does in fact work. Now we'll create a rabbit object. Rabbit equals rabbit.

[7:02:19] There are no parameter setup. We don't need to send any arguments to the constructor. hawk equals hawk and fish equals fish. So, let's take our rabbit object

[7:02:32] and they should have a flea method. Rabbit.flea method. This animal is

[7:02:37] fleeing, but they do not have a hunt method because they're not predators. Rabbit object has no attribute hunt. Hawks can hunt. They're predators. They inherited

[7:02:50] that method. This animal is hunting, but they can't flee. They're not prey. Hawk

[7:02:57] object has no attribute flee. Fish can do both. They inherit from the prey class and the predator class.

[7:03:06] Fish.fle. This animal is fleeing.

[7:03:11] Fish.unt. This animal is hunting.

[7:03:14] Children classes can inherit from more than one parent, which is what we did for fish. They are both prey and predators. Whereas in rabbits are just prey, hawks are just predators. If you

[7:03:25] need to inherit from more than one parent, you just add that additional class to the inheritance list. With multi-level inheritance, a parent can inherit from another parent. We will create a class of animal. And for now, I'll write pass.

[7:03:44] Prey and predator are going to inherit from the animal class. So, we need to add animal to each inheritance list. Let's say if you're an animal, you get a method to eat. All animals will

[7:04:00] eat. Print this animal is eating and you can sleep. Define sleep.

[7:04:12] Print this animal is sleeping. So think of rabbit, hawk, and fish as children classes. Prey and predator are those classes parents, and animal is the grandparent. Prey and predator will

[7:04:31] inherit everything that the animal class has. Rabbit, hawk, and fish will inherit everything the prey and predator classes have. So now our rabbit, hawk, and fish classes should have the ability to eat and sleep. And we'll test that.

[7:04:48] Rabbit. This animal is eating. Rabbit. This animal is sleeping. Let's

[7:04:55] check out fish. fish fish. This animal is eating.

[7:05:02] Fish. This animal is sleeping. Okay, we're going to expand upon our example a little bit. Let me

[7:05:09] zoom out. Each of our objects is going to have a name. Our rabbit will have a first name of bugs. Hawk will be Tony as

[7:05:19] in Tony Hawk. Our fish will be Nemo. Within our classes, we don't have any constructor set up. In which class

[7:05:29] should we assign the name attribute? Let's do so within our animal class. So, we will define a constructor to assign these attributes.

[7:05:42] we will receive a name. We'll assign self.name equals name. Now, with these

[7:05:51] other classes, if you're not assigning any attributes or if you don't need any other initialization logic, you don't need a constructor. We'll implicitly use the constructor we inherit from the parent. Let's convert each of these print statements to an fstring.

[7:06:10] Replace animal with self.name. Now let's have our rabbit use the eat method. Oh, we should get rid of

[7:06:34] this. There we go. Bugs is eating rabbit.

[7:06:41] Bugs is sleeping. Rabbit flee. Bugs is fleeing. Let's check out

[7:06:47] our hawk. Hawks don't have a flea method because they're predators, not prey. Let's eat. Tony is eating. Let's

[7:06:58] sleep. Tony is sleeping. Let's hunt. Tony is hunting. Let's check our

[7:07:06] fish next. Our fish can eat. Nemo is eating. Our fish can

[7:07:11] sleep. Nemo is sleeping. They can flee. Nemo is fleeing and

[7:07:19] hunt. Nemo is hunting. Okay, everybody.

[7:07:23] That is both multiple and multi-level inheritance. With multiple inheritance, a child can inherit from more than one parent class. You just add each additional class to the inheritance list. With multi-level inheritance, a

[7:07:39] child can inherit from a parent which inherits from another parent. Class C can inherit from B where class B inherits from A. Think of C as the child, B is the parent and A as the grandparent. C will have all the

[7:07:55] attributes and methods even available within the grandparent class of A. And well everybody that is both multiple and multi-level inheritance in Python. Hey everybody. So today I got to talk about

[7:08:07] the super function in Python. Super is a function. It's used within a child class to call methods from a parent class. The

[7:08:16] child class is the subclass. The parent class is the superass. Hence why this function is named the super function.

[7:08:23] Using the super function, it allows you to extend the functionality of the inherited methods. Here's an example. We'll create a few shape objects. We'll

[7:08:32] need to set up the classes though. We'll have class circle. For the time being, I'll just write pass. We'll fill it in later.

[7:08:40] Class square and class triangle. For each of these classes, in order to instantiate objects, we'll need a constructor. We will define our constructor, our innit method.

[7:09:00] When creating circles, what sorts of attributes should a circle have? Let's say a color. What's the color of the circle? Is it filled or

[7:09:10] not? Filt will be another attribute and a radius. Then let's assign these. Self doc color equals the color

[7:09:20] that we receive. self do.filled equals filled. Self do.t radius equals

[7:09:31] radius. Let's do this with the square and triangle. Really, I'll just copy our constructor and paste it. Squares don't

[7:09:39] have a radius. With a square, the width and the height are the same. Let's replace radius with width. We'll also

[7:09:46] keep the color and field attributes. Self do width equals width. Now, with triangles again, let's copy our constructor. We'll need a width and a

[7:10:01] height. self.height equals height. So with programming, we try not

[7:10:08] to repeat ourselves if we don't have to. What do all of these classes have in common? They all share the attributes of color and filled. The ways in which they are

[7:10:20] different is that circle has a radius attribute, square has a width, triangle has a width and a height. If we have to make any changes to one of these attributes, we would have to do so manually. For example, let's replace filled with is filled. Now, I need to

[7:10:35] look throughout my code for any instance of filled and replace it with is filled. It's a lot of work and I might make a mistake such as here and here. It's better to write your code once and try and reuse it. So, that's where

[7:10:51] inheritance and the super function can come in handy. We're going to take the attributes of color and is filled and place it within a parent class. These children classes will inherit those attributes. So class, what do they all

[7:11:05] have in common? They're all shapes. Class shape. And for now, I'll write

[7:11:10] pass. Circle is going to inherit from its parent of shape. That also applies with square and triangle. We'll set up a

[7:11:19] constructor for shape. define init. We will pass in the color and is filled. Then we will assign these

[7:11:35] attributes self.c color equals color self.isfilled equals is filled. We don't

[7:11:46] need to manually assign these attributes within each of these constructors for the children. Instead what we have to do is within the constructor for each of these children classes we have to call the constructor for the parent also known as the superass of shape. So we will eliminate these two lines of code. Use the super

[7:12:09] function dot call the constructor of the parent that is the dunder init method. But we need to pass in the color that we receive and is filled. This will be a boolean. And let's do this with the

[7:12:26] square class and the triangle class. We still need radius for the circle, width for the square, width and height for the triangle. We're going to call the super function to take care of whatever attributes all these types of shapes have in common such as color and is filled. Now let's see if this works.

[7:12:46] Let's construct a few objects. We will create a circle named circle called a constructor for circle. We have to pass in a color, a boolean if it's filled or not, and a radius. So for

[7:12:59] the color of the circle, let's say red is filled. Let's say that is true. And a radius of five. You could even use

[7:13:09] keyword arguments for better readability. Although not necessary, but for clarity, let's say color equals red is filled equals true radius equals 5. Let's see if this works.

[7:13:25] I will print our circles color. It is red. Print our colors is filled attribute. The circle is filled. That is

[7:13:42] true. And the radius print circle dot radius. The radius of the circle is five. We could even convert

[7:13:52] this to an string. I'll add a placeholder. Then add centimeters 5 cm. Let's construct a

[7:14:07] square object. Square equals square. We'll need a color is filled and a width. I'll just copy what we have and

[7:14:16] make a few changes. Replace radius with width. The color will be blue. Is filled

[7:14:24] will be false. The width will be six. We don't need a height because squares have an even width and height. If we ever

[7:14:31] need the height, we can assume it's the same as the width. In this case, six. Let's check out our square. Square.color

[7:14:40] square.filled square.idth. Our square is blue. It's

[7:14:47] not filled in. The width is 6 cm. Let's create a triangle object. Triangle

[7:14:54] equals triangle. Pass in our arguments. The color will be yellow. Is

[7:15:02] filled will be true. The width will be seven. And the height will be eight. Let's print our triangle's color.

[7:15:13] Is it filled? Its width and its height. Our triangle is yellow. It's filled in.

[7:15:25] The width is 7 cm. The height is 8 cm. So that's how you can use the super function to reuse the constructor of a parent class. We don't need to manually

[7:15:36] assign each of these attributes within each of the children classes. We can do that in just one place. When we refer to super, imagine that we're replacing this with the parent class name such as shape. That might be a good way to think

[7:15:51] of it. Use the constructor of the parent class of shape and pass these arguments in. What you could do as well is extend the functionality of a method. So within

[7:16:03] our shape class, let's create a method of describe. We will describe the attributes of this shape. We will print use an fstring. When we want to

[7:16:17] describe our shape, let's say it is at a placeholder self doc color. What is the color of this shape? And is it filled or not? And add a placeholder. We'll use a

[7:16:30] turnary operator. Print filled. If self is filled is true else we will print not filled. Each of these types of shapes

[7:16:48] circle square and triangle will have access to a describe method. Let's attempt to use it. Take our circle. Use the describe

[7:16:58] method that's inherited. It is red and filled square. It is blue and not filled triangle. It is yellow and

[7:17:11] filled. So then we also have method overwriting. What if we create a similar method of describe within circle, square, and triangle? Let's do

[7:17:21] that. Define a describe method within our circle. Let's calculate the area. What's the area of

[7:17:32] the circle? I'll use an F string. It is a circle with an area of then we'll calculate the area given the radius. To calculate the area of a

[7:17:47] circle, we can take pi, I'll just say 3.14 just to keep it simple, times the radius squared self. Time self.raius.

[7:17:59] If I were to call the describe method, will we use the parents version of describe or the child? So let's take our circle use the describe method. The result it is a circle with an area of 78.5. I should really add

[7:18:19] centime squared after that. Cime squared. This is called method overwriting. If a child shares a similar

[7:18:29] method with a parent, you'll use the child's version and not the parents. This is method overriding. If you would like to extend the functionality of a method from a parent, you can use the super function. Not only do I want to

[7:18:43] use the describe method of the child, I would also like to use the describe method of the parent. So within this function we will use the super function access the describe method of the parent. What we're doing is extending the functionality of the describe method. It is a circle with an area of

[7:19:05] 78.5 cm squared. The circle is red and it's filled. Or you could change up the

[7:19:12] order. Let's use the parent classes describe method and extend the functionality with our own print statement. It is read and filled. It is

[7:19:24] a circle with an area of 78.5 cm squared. Let's finish this with the square and triangle classes. I'll copy

[7:19:32] what we have for the describe method within the circle class, but we'll make a different calculation. Describe the square. It is a square with an area of take self dowidth times self.width. The height and the width are

[7:19:52] going to be the same if it's a square. Then describe our triangle. It is a triangle with an area of width time height. We have a height in this case

[7:20:08] divided by two. We've already described our circle. Let's describe our square. It is a square with an area of

[7:20:17] 36 cm squared. It is blue and not filled. Let's describe our triangle. It is a triangle with an area

[7:20:25] of 28.0 cm squared. It is yellow and filled. All right, everybody. That is

[7:20:31] the super function. It's used in a child class to call the methods from a parent class, also known as the superass. It allows you to extend the functionality of the inherited methods within a child class. You could use it within a

[7:20:45] constructor to assign any attributes that all of its siblings have in common, such as color or if that shape is filled. When used within any other method, you can extend the functionality of that method. Not only are we printing this message from the parent, we're tacking on another print statement before that. And well everybody that is

[7:21:07] the super function in Python. What is going on everybody? So today I got to talk about polymorphism in Python.

[7:21:15] Polymorphism is a programming concept. It's a Greek word that means to have many forms or faces. Poly means many.

[7:21:23] Morph means form. In programming, an object can take one of many forms. There's two ways to achieve polymorphism. One is through

[7:21:31] inheritance. An object could be treated of the same type as a parent class. There's also duct typing, which we'll talk about in the next topic. In this

[7:21:40] video, we're more focused on inheritance. What we'll do in this video is create a class of shape. We'll write pass as a placeholder. We will create a

[7:21:50] class of circle which will inherit from shape. Again writing pass class square inherits from shape class triangle which inherits from shape. If I was to create a circle object circle equals circle our circle identifies as a circle. And since our circle class

[7:22:20] inherits from the shape class, our circle is also considered a shape. It has two forms. It's a circle and it's a shape. But our circle isn't a square or

[7:22:30] a triangle. That could also apply to our square class. Our square is a square. Our

[7:22:37] square is also considered a shape. But our square is not a circle or a triangle. Those are two possible forms for our square. It's a square and a

[7:22:45] shape. So let's say we would like to create a list of shapes. What do they all have in common? Well, they're all

[7:22:51] shapes. A descriptive name for this list would be shapes equals an empty list. I will instantiate a circle object, a square object, and a triangle object. Our circle is a circle and a

[7:23:09] shape. Our square is a square and a shape. Our triangle is a triangle and a shape. Each of these objects has two

[7:23:17] forms or two faces. Let's fill in some of these classes. Let's say that with our shape class, we will define an area method. Define area. I'm going to turn

[7:23:29] this into an abstract method. I'll just write pass. To work with abstract classes, we need to import that from ABC import capital ABC as well as abstract method. Preceding the area

[7:23:45] method, I will add a decorator of abstract method. Our circle, square, and triangle classes, they're all considered shapes. They inherit from this class. We

[7:23:55] need to define an area method for each since they're all considered a shape. Every shape has an area with our class of circle. Let's define a constructor. Define

[7:24:08] init. We will pass in one argument. A radius. What is the radius of the circle

[7:24:14] assign an attribute of radius equals the radius we receive. Let's do this with square. Define innit one parameter the length of a side. self dot side equals side then

[7:24:33] triangle define init. We have two parameters base and height self.base equals base self.height equals

[7:24:51] height. All right. Now let's finish defining these area methods for each class.

[7:24:57] We will return 3.14 time self.US to the power of 2. So given a radius that's how to

[7:25:11] calculate the area of a circle. Then with our square define area we will return self do side to the power of two. Then with our triangle define area return self.base time self.height

[7:25:42] height time 0.5. Now we have to pass in some arguments. For our circle, we need a

[7:25:49] radius. I'll pick four. For the square, the length of a side will be five. Then

[7:25:54] our triangle, the base will be six. The height will be seven. We're going to write a loop to iterate through our shapes. for every shape in

[7:26:05] shapes. Then we're going to print for every shape called the area method. And that would give me these numbers. If you would like, you can

[7:26:19] format the output. I'll just use an F string. I'll add centime squared.

[7:26:35] Much better. What if we were to create a class that's completely unrelated to shapes? I will create a class of pizza. I will define a

[7:26:50] constructor. To construct a pizza object, we need a topping and a radius. What is the radius of the pizza?

[7:27:01] self. Equals topping self.raius equals radius. Within my list of shapes, I'll

[7:27:12] add a pizza object. But I have to pass in a topping such as pepperoni. And what is the radius of the pizza? Let's say 15 cm. So, our pizza,

[7:27:26] our pizza class doesn't have an area method. Here's what happens when I run this. We get an attribute error. Pizza

[7:27:35] object has no attribute area. Our pizza object is considered a pizza, but it is not considered a shape. It does not inherit from the shape class at the top here. You know what? A pizza

[7:27:48] is circular. It could be considered a circle. So, how about this? Let's take

[7:27:53] the pizza class. it will inherit from the circle class. And within our circle class, we're already assigning the radius to the radius attribute. So

[7:28:03] instead of doing that here within the constructor for our pizza class, let's call the super constructor super, which refers to the parent, use its constructor, then pass in the radius we receive. Let's see if this works. Now that does. Here is the area of our

[7:28:24] pizza. Our pizza is considered a pizza. It inherits from the circle class. So,

[7:28:29] it's also considered a circle. And our circle class inherits from the shape class. Our pizza has three forms. Our

[7:28:37] pizza is considered a pizza. It's also considered a circle and it's also considered a shape. It would make sense for it to fit into this list of shapes because our pizza also identifies as a shape. So that's polymorphism everybody.

[7:28:52] It's a Greek word meaning to have many forms or faces. Poly meaning many, morph meaning form. In Python, there's two ways to achieve polymorphism. One

[7:29:01] through inheritance. An object could be treated of the same type as a parent. And there's also duct typing, which we'll discuss more in the next topic.

[7:29:10] Stay tuned for that. And well everybody, that's polymorphism in Python. Hey everybody. So today I got to

[7:29:18] talk about duct typing in Python. Duct typing is another way to achieve polymorphism besides using inheritance. Objects can be treated as if they're a different type as long as they meet the minimum necessary attributes and methods required of them. It follows this adage.

[7:29:33] If it looks like a duck and quacks like a duck, it must be a duck. As long as an object resembles another, it could also be treated of that type. So in this example, let's create a class of animal.

[7:29:48] We will have a class attribute of alive. If you're an animal, you will have an attribute of alive. You're a living creature. Let's create a class of dog.

[7:30:00] The dog class will inherit from the animal class. They will inherit the alive attribute. Let's also define a speak method. If you're a dog, you gain

[7:30:10] the ability to speak. We will print woof. Then we'll create a cat class. Class cat inherits from animal.

[7:30:23] For the speak method, we will print meow. Let's create a list of animals. What do these two classes have in common? They both can be considered

[7:30:33] animals. Let's create a list of animals. We will construct a dog object and a cat object.

[7:30:42] If I was to write a for loop for every animal in my list of animals, have each animal use its speak method, which will result in the dog going woof, the cat going meow, they're both speaking. What if we add a class that has nothing to do with animals like class car? Cars will have a horn method. That's how

[7:31:11] they speak. When you honk the horn, you will print honk. Within my list of animals, let's create a car object. It really doesn't

[7:31:24] belong in here, but let's see what happens. We have an attribute error. Car object has no attribute speak. Our car object doesn't have the

[7:31:37] minimum necessary attributes and methods. When iterating through this list of animals, we're calling each animal speak method, which our car object doesn't have, but it does have a horn method. So, what if we rename our horn method as speak? Maybe it's an AI

[7:31:56] car or something. Well, this would work. The dog goes woof. The cat goes meow. The

[7:32:03] car goes honk. So our car object, it quacks like a duck. We could consider it a duck. It has the minimum

[7:32:14] necessary methods to be considered an animal. Animals inherit this alive attribute. Let's utilize that. After the

[7:32:23] animal speaks, let's print their alive attribute. Print my animals alive attribute. my car object doesn't have that attribute. We get an attribute

[7:32:36] error. Car object has no attribute alive. But if I was to add that attribute alive equals false, we have true for the dog, it's living. True for the cat, it's living.

[7:32:53] But false for the car, it's not living. It's not a living creature. My car meets the minimum necessary requirements to be considered an animal.

[7:33:04] If I were to set this to be alive, well then it would be a living car. Kind of like the movie Cars. So with Python, duct typing is another way to achieve polymorphism besides using inheritance. As long as an object has

[7:33:20] the minimum necessary attributes and methods, you could treat it as a different type of object. If it looks like a duck and quacks like a duck, it must be a duck. And well everybody, that is duck typing in Python. Hey, what's going on everybody?

[7:33:36] Today I'm going to talk about static methods in Python. A static method is a method that belongs to a class rather than any object from that class, any instance. Instance methods, we're already familiar with them. They are

[7:33:51] methods that belong to individual objects created from that class. They're best for operations on instances of that class, any objects. Whereas static methods, they're best for utility functions within a class that do not need access to class data. I'll

[7:34:07] demonstrate the differences between an instance method and a static method. We'll begin by creating a class of employee. We'll need a constructor.

[7:34:18] Let's define that. To create an employee object, we'll need a name and a job position. We will assign self.name equals name.

[7:34:33] self.position equals position. We will create an instance method of get info. We will return

[7:34:42] employee info. We will return an fstring where we will display self.name.

[7:34:52] name equals self.position. Get info is an instance method. Each object that we create from

[7:35:03] this class will have their own get info method to return the information on that object. The object's name and the object's position. Now we'll create a static method. To create a static method, we

[7:35:16] need a decorator of static method. Static methods are best for general utility functions within a class. We'll define a method to check to see if a job a position is valid, which we will name is valid position. So static methods, they don't

[7:35:38] have self as the first argument. We're not working with any objects created from this class. To check to see if a position is valid, we will pass in a job position, which I will name as position. I will create a list of

[7:35:54] valid positions. Let's assume that our company is the Krusty Krab. What are some valid positions? A manager is a valid

[7:36:05] position, a cashier, a cook, then let's say a janitor. Then we will return we'll use a membership operator. Check if position that we receive is in our list of valid positions. What we have done is that we

[7:36:31] have created a static method. We don't need to rely on any objects to use this method. For example, to use a static method, we will use the name of the class rather than any object that we create from this class such as this. We don't need to do

[7:36:51] that. We type the class name followed by the static method is valid position. Then I did set this up to accept one argument. Let's check to see

[7:37:06] if a cook is a valid position. Then I do need to print this. What is the output? A cook is a valid position. What

[7:37:19] about a rocket scientist? That would probably be Sy's job. That is false. A

[7:37:27] rocket scientist is not a valid position at the Krusty Krab. This is a static method. It belongs to the class, not any object created from that class. Now let's

[7:37:38] create a few employee objects. Let's say employee 1 equals a new employee. We have to pass in a name and a job. Eugene will be the first name.

[7:37:50] That's Mr. Krabs. He will be a manager. Employee

[7:37:57] 2 equals employee Squidward will be a cashier. Employee 3 equals employee. Employee 3 will be Spongebob. Spongebob will be a

[7:38:17] cook. To call an instance method, we have to access one of the instances of the class in order to use it. If I want to check the info on employee 1, I will access that object, that instance. Use the get info method. Then

[7:38:35] I need to print it. Take employee one, get the info. Eugene is the manager. Let's do this

[7:38:45] with employee 2 and employee 3. Eugene, Mr. Krabs, is the manager.

[7:38:53] Squidward is the cashier. Spongebob is the cook. For an instance method, you access an object, then call the instance method. With a static method, you only

[7:39:04] need to access that class. You don't even need to create any objects from that class. It's a general utility method. All right, everybody. Those are

[7:39:14] static methods. They're a method that belongs to a class rather than any objects created from that class. They're usually used for general utility functions that do not need access to class data. And well everybody, those

[7:39:28] are static methods in Python. Hey, what's going on people? So today I got to talk about class methods in Python. A class method allows

[7:39:38] operations related to the class itself. They take CLS as the first parameter whereas instance methods will take self. Self refers to any object created from that class. Cls meaning class refers to

[7:39:51] the class not any objects. Here's an example. We will create a class of student. We'll need a constructor to

[7:40:01] construct some student objects. All students will have a name and a GPA. self.name equals name.

[7:40:14] self.gpa equals GPA. We will also create a class variable for this demonstration of count. We will

[7:40:23] count how many students we create. Whenever we construct a student object, we will access the class of student take our count variable incremented by one. Whenever we create a student object increase count by one. I will create an instance method of

[7:40:44] get info. Instance methods have self as the first parameter. We're referring to the object we're currently working with. I

[7:40:55] will return an fstring where we will display the students name and their GPA. self.name name self.gpa. I'll add a comment that this

[7:41:11] is an instance method. Now to create a class method to work with class data, we will declare a class method with a class method decorator. Class method. What we're going to do is define

[7:41:28] a method to get the count the class variable of count. This method will be called get count. Rather than self as the first parameter, we'll be working with a class cls meaning class. I will return an

[7:41:47] fstring total number of students. Add a placeholder cls count. Let's test this. To call a class

[7:42:01] method, you take the name of the class followed by the class method get count. And then we do need to print this. What is the count of my current students? Total number of students is

[7:42:18] zero. Let's create a few student objects. We will create student one equals call the student constructor. We

[7:42:26] have to pass in a name and a GPA. Let's say that the name is Spongebob. Spongebob has a GPA of 3.2. We'll create two more

[7:42:37] students. Student two. Student three.

[7:42:40] Student two will be Patrick. Patrick has a 2.0. Then Sandy. Syy's smart. In fact,

[7:42:50] she's a genius. She has a perfect 4.0. Now, let's count the number of

[7:42:56] students. Total number of students is three. When we call this class method, we can access or modify class data. This class variable of count.

[7:43:10] Rather than using self, we use CLS for the class. Let's create one more class method. This time I'll calculate the total GPA of all my students. We'll need a class variable to

[7:43:24] hold that data. Let's say total GPA equals zero. Whenever we construct a student object, we will access our class of student get the total GPA. Then add plus equals this student's

[7:43:44] GPA that we have just created. Basically speaking, the total GPA, this variable is going to accumulate all of the GPA of every student and store it as a sum. To find the average, we're going to divide it by the count, the number of students. We'll do that within a class

[7:44:02] method. To create a class method, again, we need to use the class method decorator. I will define a method of get average GPA. The first parameter is cls

[7:44:15] for class. I will check if cls count the count variable of my class is equal to zero. That means if we have no students.

[7:44:29] If that's the case, if there's no students, we're going to return zero because otherwise we're going to divide by zero and we'll get an error. else we're going to return an f string. Follow this formula. We're going

[7:44:45] to take the total GPA of my class. Class dot total GPA divided by class.c count the number of students we have. That's

[7:44:55] how to calculate the average GPA. After getting the count of the number of students to access a class method, we take the name of the class student call the class method get average GPA. Then I will print it. Total number of students is three.

[7:45:18] The average GPA is 3.06 repeating. After calculating the average, I'm going to add a format specifier of 2F just to round to two decimal places. And I'll add average GPA

[7:45:34] colon space. Then we'll calculate the average. All right, everybody. Those are

[7:45:41] class methods. Instance methods are best for operations on instances of the class, any objects. Static methods are best for general utility functions which do not need access to class data. Class

[7:45:56] methods are best used when we're working with class level data or we require access to the class itself such as when we're working with class variables rather than using self as the first parameter. We're going to use cls meaning class. And well everybody those are class methods in Python. Yo, what's going on people? So

[7:46:18] today I'm going to explain magic methods in Python. Magic methods are also known as dunder methods meaning double underscore. You typically find these within classes. We're already familiar

[7:46:29] with one of them. Our dunder init method. We have double underscores on the left and double underscores on the right, but there are others. I'll cover

[7:46:38] a few of the more beginner friendly ones. So, what these methods do is that they're automatically called by using some of Python's built-in operations such as printing an object, seeing if two objects are equal, greater than, or less than. When we use many of Python's built-in operations with objects, we can define and customize the behavior of those objects. So, in this

[7:47:01] demonstration, I'm going to create a class of book. We will construct some book objects. We will define a magic method, a dunder method of init. To

[7:47:12] initialize these objects for a book, we need a title, an author, and the number of pages. We'll say num pages. self.title equals

[7:47:28] title. Self.author equals author.

[7:47:34] self dot number of pages equals number of pages. When we call the class of book, we are automatically calling done a nit. So let's create a book object. Book one

[7:47:47] equals book. We need a title, an author, and number of pages. So since we're dealing with this topic of magic methods, I'll pick some fantasy related books. For my

[7:47:58] first book, I'll pick The Hobbit. That's the title. The author is JRR Tolken. The number of pages is

[7:48:10] 310. So for my next book, book two, I will pick Harry Potter and the Philosopher Stone. The author is JK Rowling.

[7:48:31] The number of pages is 223. Then we have book three. For my third book, I will pick The Lion, The Witch, and The Wardrobe. The author is CS

[7:48:53] Lewis. The number of pages is 172. Okay, here are my three book objects. When we

[7:49:00] call the class of book and pass in arguments, we will call the dunder init method. It's a magic method. It's automatically called behind the scenes.

[7:49:10] Within this magic method, we can define and customize the behavior of objects. And in this example, we're just assigning the attributes of title, author, and number of pages. That is one built-in operation of Python. What would

[7:49:24] happen if I was to print book one directly to the console? Here's what happens. Well, we're given a memory address. Here's book two and book

[7:49:37] three. Well, we can customize this behavior. We will use the dunder string method. Double underscore str meaning

[7:49:49] string double underscore. Again, we have one parameter of self. Instead of returning a memory address, we can customize this behavior.

[7:49:59] Let's instead return an fstring. I'll add two placeholders. We will display self.title, the title of

[7:50:07] the book by self.author. And I'll place the title within single quotes. Now, let's print book one. We

[7:50:18] have The Hobbit by JRR Tolken. Let's print book two. Harry Potter and the Philosopher Stone by JK Rowling and book three, The Lion, the Witch, and the Wardrobe by CS Lewis.

[7:50:33] So that is dunder string. We can return a string representation of the object when we print it directly to the console. Here's another dunder method.

[7:50:43] We can check to see if two objects are equal. I will print is book one equal to book two. That gives me false. If they were to have the same

[7:50:59] title, the same author, and the same number of pages, then Python would say they're not equal still. So, let's customize this behavior. We will define a method of dunder equals, which is just EQ. For parameters, we have self, the

[7:51:22] first book we're examining. In this case, book one and other. Other means the other book. We're examining two

[7:51:29] objects for equality. To do that, we'll see if the title of two books and the author is the same. We'll disregard the number of pages. You can have two different

[7:51:42] versions of the same book. They might have different font sizes or the dimensions of the physical pages might be different. So, we will return a boolean value. We will examine if self that's

[7:51:55] the first book is the title attribute equal to our other book's title and is the author of the first book self.author equal to our other book's author. If I were to run this we get false. Book one does not equal book two.

[7:52:16] But if they have the same title, I'm going to replace these and the same author, then they would be equal. And we'll disregard the number of pages. Let's say that with this version of The Hobbit, they're using a smaller font size, so there's less pages. We're using dunder equals to

[7:52:38] compare if two objects are equal. What if I was to print book two is less than book three? Like what does that even mean? And I'm just going to get rid

[7:52:50] of these two lines. Type error less than is not supported between instances of book and book. So we can't use less than on two objects. But we can customize that

[7:53:04] behavior by using dunder less than which is just lt. We're examining one book and the other book self and other. Let's compare the number of pages. We'll compare if the pages of

[7:53:20] book two is less than book three. We will return a boolean value is self dot number of pages less than other number of pages. So now this should not give us an error. Book two does not have less pages

[7:53:41] than book three. Another would be greater than. I'll just copy what we have. Dunder GT for greater than for our

[7:53:51] first book of self. Is it greater than the number of pages of the other book? Well, that's true. The number of

[7:54:02] pages of book two is greater than book three. Let's use dunder add to add the pages of two books together. What would happen if I were to add two books together? Book two plus book

[7:54:15] three. Well, we get a type error. Unsupported operand for book and book.

[7:54:21] Well, to customize the behavior of addition, we will define dunder add. We have self and other for the other object. Let's add the pages together of two books. Maybe we need a summer reading

[7:54:36] list and we would like to see what the total number of pages is. I will return self dot number of pages attribute plus our other books number of pages. That would give me 395. That's 223 + 172. Heck, I'll even

[7:54:58] put this within an F string cuz why not? Then I will add the word pages 395 pages. Within an object, we can search for a keyword within one of the attributes. So let's find the word lion

[7:55:21] within book three. To do that, I would write a statement like this. Lion in book three type error argument of type book is not iterable. We will define dunder

[7:55:40] contains besides self we will pass in a keyword a keyword that we're searching for. I will return. Then we'll use the in membership operator is our keyword in self.title. I'm looking for the word

[7:55:58] lion. That's going to return true. If lion is in the title of this book or is our keyword in self.author, maybe we're

[7:56:09] searching for an author. Let's try that again. That returns true. Lion is in

[7:56:17] book three. However, Lion is not within book one. That's false. Is Rolling in book two? That's

[7:56:27] the author. That is true. Is rolling in book three? That is false. That is

[7:56:36] dunder contains. We are searching for a keyword in an object. Now, we could search for a key given an object. For book one, we'll use the

[7:56:47] index operator and look up an attribute. Let's get the title of book one. The default behavior is that we get a type error. Book object is not

[7:57:01] subscriptable. So to customize this behavior, we will use dunder get item. Besides self, we have one parameter of key. We're accessing book

[7:57:15] attributes by indexing. With this object, return the value at this key. What's that attribute? We will check if our key that

[7:57:26] we receive is equal to title, which it is in this case. We will return self.title. What's the title of the

[7:57:36] book? So that would give me the Hobbit. Here's book two and book three. What if the key is

[7:57:49] author? None. We didn't set that up yet. If key is equal to

[7:57:58] author, then return self.author. The author of book three is CS Lewis.

[7:58:08] Two is JK Rowling. Book one is JRR Tolken. What about number of pages? Num

[7:58:19] pages. Well, we're not set up for that yet. I'm going to turn this into an else- if statement.

[7:58:27] Else if key is equal to num pages then we will return self.num pages. The number of pages in book one is 310. Book two is

[7:58:47] 223. Book three is 172. What if there is no key? Otherwise, if there is no

[7:58:54] matching key, I'll add an else statement. Let's return an fstring key placeholder. Our key that we pass in as an argument was not found. What do books not have? Well,

[7:59:13] they don't have audio, I guess, unless it's an audio book. Is there a key of audio in book three? There is not. key

[7:59:22] audio was not found. And I'll place that within single quotes. Much better. All right,

[7:59:29] everybody. So, those are magic methods, also known as dunder methods, meaning double underscore. They are automatically called by many of Python's built-in operations. They allow

[7:59:40] developers to define or customize the behavior of objects when we use those built-in operations. And well, everybody, those are magic methods in Python. Hey everybody. So in today's video, I

[7:59:53] got to talk about the property decorator in Python. The property decorator allows us to define a method as a property. We can access it like it's an attribute.

[8:00:02] One of the benefits is that when reading, writing, or deleting attributes, we can add additional logic. The property decorator gives us a getter method to read, a setter method to write, and a deleter method to delete when working with attributes. In this example, we'll create a class of rectangle. We need a constructor. Let's

[8:00:23] define that. When constructing a rectangle object, we will need a width and a height. We will assign the attribute of width equal to the width that we receive when constructing this object.

[8:00:39] Self.height equals height. Let's construct a rectangle object. rectangle equals

[8:00:49] rectangle. We need to pass in a width and a height. Then I will print my rectangle's width rectangle.width and the

[8:00:59] height. Rectangle.height. With my rectangle, the

[8:01:04] width is three, the height is four. Using the property decorator, when reading these attributes of width or height, I can write some additional logic. Let's say that when accessing the width or the height, I would like to display one digit after the decimal, then add centimeters. Here's one way in

[8:01:22] which I can do that. For each of these attributes, I'm going to create a method. We will define a method of width, no parameters besides self. For

[8:01:32] now, I'll write pass and define height. Preceding each of these methods, I will use the property decorator. So at property now when accessing the width or the height we'll be returned with whatever is within these methods of width and height. But there's one change we're

[8:01:54] going to make to these attributes. We'll set these attributes to be private. Prefix each of these attributes with an underscore. This tells you and other

[8:02:04] developers that these attributes, they're meant to be protected. They're internal. We shouldn't access the width or the height directly outside of this class. Technically, we could. I will

[8:02:15] access the internal version of width and height. We get three and four, but we do have a warning. Access to a protected member width of a class. That applies to

[8:02:26] height as well. Our width and our height are only meant to be used inside of this class. If we need to get the width and the height, we will do so through these getter methods provided by the property decorator. So when accessing the width,

[8:02:40] let's return an fstring I will access self dot private width add a format specifier to display one digit after the decimal.1f followed by centimeters. We'll do this with the height as well. We will return self.private

[8:03:05] height. So now when we access the width or the height we will do so using these getter methods. If I access these private width and height attributes instead again they will be three and four. It's kind of like they're raw.

[8:03:23] These attributes are meant to be used internally inside of the class. So that's the point of a getter method. We can add additional logic when reading one of these attributes when we try to get them. We can also add setter methods

[8:03:37] if we would like to set or write these attributes. Here's how. Let's take our width. We will create a decorator of at

[8:03:45] width setter. When attempting to set the width, we will do so using this method. We will define our method name of width.

[8:03:54] We will have one parameter, a new width. We don't want the parameter name to be the same as the method name. That's why we're naming it something different.

[8:04:05] When setting the width, let's check to see if the new width is greater than zero. If so, we will take self.private width equals our new width. Else, let's print something.

[8:04:22] Let's print width must be greater than zero. And let's do this with the height. Heights setter define height.

[8:04:41] Pass in a new height. If our new height is greater than zero, assign self.private height equals the new height. Else print height

[8:04:55] must be greater than zero. Before printing the width and the height, let's take our rectangles width, set it to be zero. Then see what happens. Well, we get that message width

[8:05:10] must be greater than zero. If I were to set width to be five. Well, that does work. Our width is

[8:05:17] now five. Let's change the height. Rectangle. I will set this to be -1.

[8:05:27] height must be greater than zero and the height hasn't changed. What about six? Six does work. When using these

[8:05:36] setter methods, we can add additional logic when writing or changing one of these attributes. These are setter methods. Now, if you need to delete an attribute, here's how. There is a delete keyword. We will

[8:05:52] delete our rectangle's width and delete our rectangle's height. In this series, we really won't be using the delete keyword, but you should still know that it exists. So, we will create a deleter method at take one of the attributes. In

[8:06:09] this example, width. We will create a deleter method. The method name will be width. The name of the

[8:06:17] attribute. There will be no parameters besides self. We will delete self.private private width. Then

[8:06:28] let's print something just to confirm that this was deleted. Width has been deleted. Same thing applies to height. Take the attribute of height.

[8:06:43] Define height. Delete private height. Height has been deleted.

[8:06:55] When deleting our width or our height, we get that confirmation message. Width has been deleted and height has been deleted. All right, everybody. So that

[8:07:04] is the property decorator. We can define a method as a property. Meaning it can be accessed as if it was an attribute.

[8:07:12] One of the benefits is that we can add additional logic when we read, write, or delete attributes. The property decorator gives us a getter, setter, and deleter method. Getter methods to read, setter methods to write and deleter methods to delete. And well everybody

[8:07:30] that is the property decorator in Python. What is going on everybody? So today I got to talk about decorators in Python. A decorator is a function that

[8:07:40] extends the behavior of another function without modifying that base function. We pass the base function as an argument to the decorator function. For example, let's say we have a base function of get ice cream and you can pass in a flavor of ice cream. Well, some people might

[8:07:56] want sprinkles on their ice cream and others may not. They might just want plain vanilla. Well, we could add sprinkles by using a decorator. We're

[8:08:04] extending the behavior of a function where we get ice cream where we're adding sprinkles, but we may not want to change the base function because some people don't like sprinkles. Think of decorators that way. We're adding something to a base function without changing it. Here's how to create a

[8:08:19] decorator. Let's start with the base function. We will create a function to get ice cream. There will be no

[8:08:27] parameters for now. All we're going to do is print the following message. Here is your ice cream. And for

[8:08:36] fun, I'll add an emoji because I like emojis. I'll add an ice cream emoji. To call this function, all I got to do is call the get ice cream function. Here is

[8:08:48] your ice cream. Here's how to create a decorator. A decorator is a function.

[8:08:55] We'll need to define it. Define add sprinkles. Our decorator function is going to have one parameter, a function, but we'll just rename it to funk for short. We're going to pass a function to

[8:09:10] our decorator function. Within our decorator function, we will define an inner function of wrapper. Currently, there's no parameters. We'll set that up

[8:09:24] later. Within this wrapper function, we will call the function that we receive this parameter. Then we will return our wrapper function. Up until this point,

[8:09:37] we've been returning values, but now we're going to return an entire function. Here's the basic formula to create a decorator. To apply a decorator to a base function, preceding that function, you're going to add at the name of the decorator. So add sprinkles

[8:09:54] is a decorator. The base function is get ice cream. Within our decorator, how do we want to add sprinkles exactly?

[8:10:02] Currently, our decorator doesn't do anything. Here's what happens. We just print here is your ice cream. Let's say

[8:10:10] that before we're given our ice cream, we'll print a statement that we add sprinkles within our decorator. Imagine that we're replacing calling function with this print statement. Let's create another print statement where we add sprinkles before it. I will print the following

[8:10:33] message. You add sprinkles and I'll add an emoji. How about confetti? That could resemble

[8:10:42] sprinkles. Okay, let's see what happens. You add sprinkles. Here is your

[8:10:48] ice cream. We're decorating our base function of get ice cream with a decorator of add sprinkles. We're not modifying the base function. We're extending it. Now, we

[8:11:01] have a nested function of wrapper within our decorator. It is necessary to have this. Here's why. So, I'm not going to

[8:11:08] call the get ice cream function quite yet. So, nothing should happen. If I was to remove this wrapper, well, we'll end up calling this function as soon as we apply the decorator. We're not even calling the

[8:11:27] get ice cream function at all. We only want to execute this code when we want ice cream, not whenever we apply the decorator. That's why we need that wrapper function. We'll get ice cream and add

[8:11:42] sprinkles only when we call that function. Then at any point in my program, if I call the get ice cream function, then we get ice cream with sprinkles. Let's apply more than one decorator. We'll create a decorator to

[8:12:01] add fudge. Define add fudge. We have one parameter a function which we will rename as funk. We need an inner

[8:12:11] wrapper function. This is so that we don't call this function when we apply a decorator. I will print you add fudge. Close enough. We'll add a bar of

[8:12:31] chocolate. then call the base function that we receive. Then we need to return the wrapper function. All right. Given our base

[8:12:43] function, we can apply more than one decorator. Let's say that after adding sprinkles, we will apply the decorator where we add fudge. So now we have the following output. You add sprinkles, you add

[8:12:59] fudge. Here is your ice cream. So with decorators, you can apply more than one decorator to a base function. What if your base function

[8:13:08] accepts arguments? For example, when we get our ice cream, we need to pass in a flavor like vanilla. I will set up one parameter, a flavor. I will convert our print

[8:13:21] statement to be an string. Here is your add a placeholder flavor of ice cream. Let's run this and see what happens. All right, we have a type

[8:13:36] error. Our wrapper function isn't set up to accept arguments. What you'll see within wrapper functions is that they'll have parameters of args and quarks to accept any number of arguments and keyword arguments.

[8:13:51] Then when you call your base function, in this case get ice cream, we will also set this up to accept any number of arguments and keyword arguments. Let's do that within our add fudge decorator too. Our wrapper function will accept any number of arguments and keyword arguments. Same

[8:14:10] thing goes with the base function. And now this should work. You add sprinkles, you add fudge. Here

[8:14:17] is your vanilla ice cream or any other flavor of your choosing like chocolate. You add sprinkles, you add fudge. Here is your chocolate ice cream.

[8:14:30] All right, everybody. So, those are decorators. They're a function that extend the behavior of a base function.

[8:14:37] In this case, get ice cream. Decorators extend a function without modifying it. If you would like to apply a decorator to a function, you preede that function when you define it with at the name of the decorator and you can apply more than one. And well everybody, that is an

[8:14:54] introduction to decorators in Python. Hey everybody. So today I got to talk about exception handling in Python.

[8:15:01] An exception is an event that interrupts the normal flow of a program. There are many different types of exceptions which include but are not limited to zero division error exceptions when you attempt to divide a number by zero. For example, 1 divided by 0. That would

[8:15:17] interrupt our program. We have a zero division error. Another is a type error.

[8:15:22] That's if we attempt to perform an operation of a value that's of the wrong data type. For example, one plus a string of one. That would give us a type error. unsupported operand for int and

[8:15:35] string. Value errors tend to happen when you attempt to type cast a value of the wrong data type. So let's say we attempt to type cast the word pizza as an integer. Well, pizza isn't a number. We

[8:15:49] have a value error invalid literal for int base with 10. Pizza. So exceptions will interrupt our program if they're not handled gracefully. And here's how

[8:16:00] we can do that. There's three steps. We can write a try, accept, and finally block. Any code that's dangerous where

[8:16:09] it could cause an error, you'll place within a try block. For example, anytime we accept user input, that is considered dangerous code because a user can type in anything. So, let's say we have a number. Number equals we will accept

[8:16:24] some user input. We will tell a user to enter a number. Then we're going to type cast it as an integer. Then I'm going to

[8:16:37] print 1 / whatever the user types in. If I were to type in zero, we get a zero division error. If I type in the word pizza, we get a value error. We would like to

[8:16:51] prevent our program from stopping. This code is considered dangerous. A user can really type in anything. So, we're going

[8:16:59] to surround this code within a try block. We'll type try colon and then indent any code underneath it. We're going to try this code. If an exception

[8:17:11] happens, we will move on to step two. Subsequently, following the try block, we will add an accept block. If we run into one of these exceptions, we can execute some alternative code. For example, a zero

[8:17:25] division error. If somebody attempts to divide a number by zero, we can take a different course of action. Instead of our program crashing and coming to a halt, let's print you can't divide by zero. Idiot. Let's attempt to divide by

[8:17:46] zero. Enter a number zero. You can't divide by zero, idiot.

[8:17:53] We have gracefully handled this exception. So now let's say somebody types in the word pizza when we're asking for a number. Well, we have a value error. Well, we can chain accept

[8:18:04] blocks. If we encounter a value error, let's add an accept block for that. Accept value error. We're going to

[8:18:16] print enter only numbers. Please enter a number. I'll type in the word pizza. Enter only numbers, please.

[8:18:28] That's good. We're not interrupting our program. Now, what you may see some people do is they will just catch all exceptions.

[8:18:37] Except exception. Now, this is actually considered bad practice. Exception will catch all exceptions. However, it's too

[8:18:46] broad of a clause. It's good practice to tell the user what went wrong exactly. If we resort to just catching all exceptions, you may see an error message such as something went wrong. I'm looking at

[8:19:01] you, Microsoft. We want to tell the user what went wrong exactly. I would only catch all exceptions as a last resort.

[8:19:09] First, let's try and tell the user what went wrong exactly. So, I'm going to undo all this code. If there's an exception that occurs, it's not a zero division error and it's not a value error, then we can add that catch all where we catch any unseen exceptions. Now, lastly, we have the

[8:19:29] finally block. The finally block always executes regardless if there's an exception or not. It's usually used for any sort of cleanup that you need to do, such as if you're handling files. You

[8:19:42] may try and open a file and then you want to be sure to close that file when you're done with it. that would be handled within the finally block. But we'll get to file handling pretty soon in the next topic. So just for the time

[8:19:54] being, I'm going to print do some cleanup here. All right, let's test this. Enter a number. I'm going to divide by zero.

[8:20:07] You can't divide by zero. And we still execute the finally block. Enter a number. I'll enter in

[8:20:14] one. 1 / 1 is 1 and we still execute that finally block. The finally block will be more useful in future videos. All you

[8:20:24] need to know is that it always executes regardless if there's an exception or not. All right, everybody. So, that's exception handling. An exception is an

[8:20:32] event that interrupts the normal flow of a program. There are many different types of exceptions. You can always look under the official Python documentation for an extensive list. And well

[8:20:42] everybody that's exception handling in Python. Hey, what's going on everybody? Today I'm going to show you how we can handle basic file detection using Python. This topic is the first of many

[8:20:53] involving a minieries on file handling using Python. First we'll need to cover file detection. Before we read and write files to work with files using Python, we will import the OS module. OS means

[8:21:06] operating system. This module provides a way for Python programs to interact with the operating system. Be sure to import the OS module at the top. For my

[8:21:16] demonstration, within my project folder, I'm going to create a new file, new file. I will name this file test. And this will be a plain text file. It will

[8:21:27] have the file extension of .txt. This file really doesn't need to say anything. I'm just going to type I

[8:21:34] like pizza because I do. The context doesn't matter. We're not going to be reading files in this video.

[8:21:42] For convenience, I'm going to assign a variable of file path. This will be a string. For file detection, we can either use a relative file path or an absolute file path.

[8:21:54] We'll cover relative file paths first. These two files are right next to each other. My main Python file and my test file. If we're using a relative file

[8:22:04] path, I only need the file name, including the extension test.txt. We'll be passing in the string of file path as an argument. To check to

[8:22:15] see if this file exists, I will use an if statement. If access the OS module access the path, there is a built-in method of exists. We'll pass in our file path as the argument. This method returns a

[8:22:32] boolean value of true or false if this file exists. So if this file does exist, test.txt, let's print the following. I'll use an

[8:22:46] fstring. The location I'll add a placeholder exists. I will place my file path within that placeholder and I'll surround it with single quotes to make it look nice. If

[8:23:02] this method returns true, do this else we'll do something else. I will print that location doesn't exist. All right, let's see what happens. The location test.txt txt

[8:23:23] exists. Now, what if I get the extension wrong? Let's say that I'm looking for a PDF, but it's really a txt file. Well, that location doesn't exist.

[8:23:35] You do have to be sure to get the file extension correct. What if this file was in a folder within my Python project? I will create a new directory. I will name this directory

[8:23:48] stuff. Then I will place my test file within the stuff folder. PyCharm wants me to refactor my code because the location changed. I'm

[8:23:59] not going to do that. I'm going to be sure that this box is unchecked and press refactor. We're using a relative file path. That test file is no longer

[8:24:08] next to my main Python file. Here's what happens. That location doesn't exist. With our relative file path,

[8:24:17] we'll have to navigate to our stuff folder. then find the test file. So preceding this file name, I will access the stuff folder stuff/ the name of the file test.txt. And now we can locate that

[8:24:32] file. The location stuff/est exists. When working with relative file paths, you may need to open up a folder, then find your file. You also could work with absolute

[8:24:46] file paths. So for this demonstration on my desktop I'm going to create a new file new text document test. If I were to look at the properties this is a txt file a text document. I'm going to copy the

[8:25:09] location within my file path. I will paste it. Then list the name of the file test.txt.

[8:25:17] This is an absolute file path. One problem we're running into when working with strings, a backslash does serve as an escape sequence. Python thinks we're trying to print a tab character. We can

[8:25:30] solve this with double backslashes or we could use a forward slash. Either one works. All right, let's see if that file exists. That

[8:25:44] does. the location of that absolute file path does exist. If I were to get the extension wrong, let's say this is a PDF, well, that location doesn't exist. There is a built-in method of is

[8:26:00] file to check to see if that file is in fact a file and not a directory. Let's add the following. After we detect this file, we'll write a nested if statement. If

[8:26:14] Oos.path dot is file then pass in our file path as an argument. If this file is in fact a file and not a directory, I will print that is a file. The location of that absolute file

[8:26:35] path does exist. That is a file. What if it was a directory, a folder?

[8:26:42] I'm going to delete this. Go to new folder. I will name this folder test. To check to see if a location is a

[8:26:53] directory, let's add an else- if statement. Else if ospath dot is dur meaning is directory. This is a method. We'll pass

[8:27:06] in our file path. If this is a directory, a folder, I will print that is a directory. Let's run this again. That

[8:27:19] location doesn't exist. Oh, we have to get rid of the file extension. It is not a plain text file. The location of that absolute file

[8:27:31] path exists. That is a directory, a folder. All right, everybody. That's

[8:27:38] basic file detection. In the next few videos, we're going to be reading and writing files. And well everybody, that is basic file detection using Python.

[8:27:47] Hey, what's going on everybody? In today's video, I'm going to show you how we can write and output files using Python. We'll cover plain text, JSON, and CSV files, but we'll start with plain text because it's the easiest.

[8:28:00] Suppose we have some data that we would like to output. I'll create a variable of text data. Think of a food you like. I will output

[8:28:09] I like pizza. For convenience, we'll create a variable, a file path. This can be a relative file path or an absolute file path. Within this file path, we'll need

[8:28:21] a name for this file. I will name this output. Then include the file extension.

[8:28:27] This will be a .txt file, a plain text file. This is a relative file path. When

[8:28:33] I generate this file, it will be within the same project folder as my main Python file. To create a file, we'll write the following with open function pass in our file path and a character of W to write as file. And for now, I'll write pass.

[8:28:56] There's a few things going on here. Width is a statement. It's used to wrap a block of code to execute. If we open a

[8:29:04] file, the width statement will also close that file when we're done with it. So, we don't need to manually close files. When you open a file, it is good practice to close it because if you don't, you may run into unexpected behavior. The width statement takes care

[8:29:18] of that for you. The open function will return a file object. The first parameter is the file path. The second

[8:29:26] parameter is the mode. W is write. X will also write if this file doesn't exist. If it already does exist, we'll

[8:29:35] receive an error. A is for append to append a file and R is to read, but we'll take care of reading in the next video. So, we will stick with W to write a file. The open function returns a file

[8:29:47] object. The first argument is the file. The second argument is the mode.

[8:29:54] You can set these to be keyword arguments if it's easier for you to read. When the open function returns a file object for us, we're using the as keyword to give it a name as file. It's kind of like we're instantiating a file object. File equals file. File is the

[8:30:13] name of the file object. To write to this file, we're going to take our file object, use the built-in write method, then pass in our text data. Then when this is done, I'm going to print a confirmation message. I'll use an fring. Let's say

[8:30:31] text file. I'll add our file path. Place it within single quotes was created. Let's see what

[8:30:44] happens. text file output.txt was created. And here's that file. I like

[8:30:53] pizza. We also have the capability of setting an absolute file path. Let's say I would like to output this file to my desktop. I would just need that

[8:31:02] location. Let me just get the location from one of these folders by going to properties. I will copy this location.

[8:31:10] This is the location to my desktop. But for you, it's probably going to be different. Then I will paste the absolute file path. A backslash is an

[8:31:20] escape sequence within a string. We either could use double backslashes or a forward slash. Now, let's see if this outputs to my desktop. Text file. Here's the file path

[8:31:39] was created. And here's that file. It's a plain text file and it says I like pizza. So when working with the file

[8:31:52] path, it can be a relative file path or an absolute file path. All right. Now for our text data. There are different

[8:32:00] modes as well. W is for write. If we use X, we'll write a file if that file doesn't already exist. In this case, it

[8:32:09] does. On my desktop, we already have a file named output and it's a plain text file. So when I run this with the mode of X, we get a file exists error. That

[8:32:21] file already exists. We could catch this exception so that our program isn't interrupted. I will copy the name of this error. I will place my code within a try

[8:32:34] block. We will try this code and catch any exceptions. except file exists error. If this file

[8:32:44] already exists, let's take a different course of action. Let's print that file already exists. So now when I run this again, our program isn't interrupted. We

[8:32:59] receive this message. That file already exists. If I were to delete that file, bye-bye. Then run this

[8:33:11] again. Well, we create a new file. Text file that absolute file path was created. And here it is

[8:33:19] again. Now for the mode, there's also a a to append. Any new data will be appended to that file. We get I like pizza. I like pizza.

[8:33:33] When appending data, if you would like that data on a new line, we can add a new line character. W will overwrite a file. So, we're back to the original. When appending, either before

[8:33:49] or after we write our text data, we could add a new line character. Let's say let's do that before. New line plus our text data.

[8:34:00] Here's the output. Again, we're appending, not writing. I like pizza. I like pizza. Our

[8:34:07] second sentence is on a new line. Let's run this a couple times. We should have several lines now. Let's work with a collection. Let's

[8:34:20] say we have a list of employees. We'll pick some employees at the Krusty Krab. So, we have Eugene. I

[8:34:28] guess he's technically the manager. I don't know if that counts as an employee. Squidward, Spongebob, and Patrick. Patrick worked

[8:34:39] at the Krusty Krab in one episode. He counts. Then we'll have to be sure we're writing our employees. This is what's going to

[8:34:49] happen. We have a type error. Write argument must be a string, not a list.

[8:34:55] In order for us to write each item within a list, we'll need to iterate over it using some sort of loop. We can't write a list or any other collection directly. Here's what we'll change. For

[8:35:08] every employee in our collection of employees, we're iterating over something that is iterable. We will access our file object. Use the write method. Then write each

[8:35:27] employee. Here's the result. We get one long string of each item in this list. If you prefer, after writing each

[8:35:39] employee, we could add a new line character after. And here's the output. We get each item in our list on a new line. Or rather than a new line

[8:35:55] character, we could use a space. This would output all the employees but space them out. Now we'll be outputting a JSON file. In summary, a JSON file is made of

[8:36:08] key value pairs. For our data, let's say we have a dictionary of employee. A dictionary is made of key value pairs.

[8:36:18] We'll have a name of Spongebob. Spongebob's age will be 30. His job, his position is that he is a cook. So this is the data I would like

[8:36:36] to output. I'll keep the file path the same. We'll change the file extension to JSON.

[8:36:44] We will need the help of the JSON module. Let's be sure to import that. import JSON. Within our width block, we'll make

[8:36:52] the following change. We're going to access our JSON module. Use the dump method. The dump

[8:37:00] method will convert our dictionary to a JSON string to output it. So we have to pass in our JSON data of employee our file as the second argument. Then for a confirmation message let's print JSON file was created. Here's the result. JSON file at

[8:37:22] this location was created. And here's my JSON file. I'll go to properties. We'll confirm it is a

[8:37:30] JSON file. It is. And I'll open it.

[8:37:34] Here's the result. Now, you could add indentation after each key value pair. Here's how. After our second argument, our

[8:37:45] file, we can pass in a keyword argument of indent. For each key value pair, by how many spaces do we want to indent each? Let's say four. And let's take a look. I think

[8:38:00] that's more readable. We're indenting each key value pair by four spaces. So that is a JSON file. It's a

[8:38:08] collection of key value pairs. A dictionary or anything that uses key value pairs is a great candidate to be output to a JSON file. All right. Now we're going to work

[8:38:20] with CSV files. CSV means commaepparated values. CSV files are pretty common with a spreadsheet of data like an Excel spreadsheet. We will create a 2D data

[8:38:31] structure of employees. This will be a list of lists. Let's add four. We'll need the help of the CSV

[8:38:49] module. Import CSV. Think of our 2D data structure as a table of rows and columns. So for the

[8:38:58] first row I will add name, age, comm, job. The second row will have a name of Spongebob age 30, job cook. For the next row, we'll have Patrick. Patrick will be

[8:39:22] 37. What is Patrick's job? I don't know.

[8:39:26] He's unemployed. Then we'll have Sandy. Sandy will be 27. Sandy is a

[8:39:39] scientist. Okay. Now with our file path, the file extension is going to be a CSV file, commaepparated values. Within the

[8:39:48] context of our width block, we're going to create a writer object to write to a file. writer equals access the CSV module. Use the writer method of that module. Then pass in our

[8:40:04] file. Writer is an object. It provides methods for writing data to a CSV file. And then we'll print a

[8:40:12] confirmation message of CSV file was created. Here's the output. Currently we have a CSV file. I'll go to

[8:40:22] properties to confirm it. Well, we have no output. We have to iterate over all the rows in our 2D collection. We'll write the following.

[8:40:35] For every row in our data of employees, we'll take our writer object, use the write row method, and pass in that row that we're iterating over. Now, let's take a look. That's better. However, the writer

[8:40:58] method gives us a new line after each row. So, if we would like to prevent that, when we open this file, I will set the keyword argument of new line equal to no characters, an empty string. Let's take a look again. Yeah, that's much better. So this

[8:41:22] is a CSV file. It's made of commaepparated values. All right everybody. So that is

[8:41:29] an introduction to writing files using Python. What's going on everybody? Today I'm going to show you how we can read files using Python. We'll cover plain

[8:41:39] text, JSON and CSV files. In the previous topic we have created some sample files to work with. Here is my plain text file. my JSON

[8:41:51] file and my CSV file. They're all named input. They each have a different file extension. For convenience, I will

[8:42:00] create a variable of file path. We can list a relative file path or an absolute file path. I'll use an absolute file path. I'm going to right

[8:42:10] click on the file I would like to read, go to properties, copy the location, then paste it, then add the file name, including the extension input, and this is a .txt file. Within the context of a string, backslashes are escape sequences for special characters. We would either need

[8:42:32] to use double backslashes or a forward slash. Here is the absolute file path to the file I would like to read. To read this file, I will add a width block. Width is a statement. It's

[8:42:48] going to wrap a block of code within a context manager and it'll close a file if we open it. It is good practice to close a file if you do open it. If you don't, it can lead to unexpected behavior. We will use the open function.

[8:43:02] The open function has two arguments. our file path and a mode. To read a file, we'll set the mode to be R for read. The open function is going to

[8:43:15] return a file object which we will give a nickname of file as file. When we read our file object, it's going to return one long string which we will assign to a variable named content. content equals file. Use the read method

[8:43:36] and assign it to this variable. Then I'm going to print the content. Print our content, the content of the file. Here's the

[8:43:47] result. That is the content of my file. I like pizza. It's really

[8:43:54] good. Let's say we can't find this file. Perhaps I forget the file extension.

[8:44:00] We'll run into a file not found error. This will interrupt our program. We can catch exceptions when they happen. Any

[8:44:08] dangerous code that may cause an exception, we can wrap within a try block. If there's an exception, we will catch them by stating except the name of the exception. In this case, file not found error. Instead of our program

[8:44:25] being interrupted, let's take a different course of action. We will print that file was not found. Let's try this again. That file was not found. At least

[8:44:41] our program isn't being interrupted. Let's add the file extension back. What if we don't have permission to read this file? To demonstrate that, I'm going to

[8:44:51] rightclick on that file, go to properties, go to security, edit the permissions. I will deny any sort of control. I will attempt to read this file. And we get a permission error.

[8:45:07] Permission denied. We could handle this exception as well. If we encounter a permission error, I will print the following.

[8:45:18] You do not have permission to read that file. Let's run this again. You do not have permission to read that file. Those are a few exceptions we can

[8:45:32] handle in case they appear. File not found errors and permission errors. Let's say we would like to read a JSON file. We will need the help of the JSON

[8:45:41] module. I will import the JSON module. At the top of my program, I need to get the file path of this JSON file. It's pretty much the same as

[8:45:52] before. In this case, the file extension is a JSON file. There's only one change we're going to make. We will assign our variable of

[8:46:06] content equal to access the JSON module. Use the load method and load our file. And that should read the contents of my file. Here's my JSON file. Name

[8:46:20] Spongebob age 30 job cook with the data of your JSON file. You could access a value given a key. I will access our content by its key of name that will return the value of Spongebob.

[8:46:37] age 30 job cook. Now, here's how to read a CSV file. We will import the CSV module. The

[8:46:49] file extension is going to be CSV. Again, this is on my desktop in the same location as the previous files. My content will equal access the CSV module. Access the reader method and

[8:47:04] pass in our file. Here's the content. Currently, we're given a memory address. With a CSV file, what we need

[8:47:14] to do is read the CSV file line by line. All of the data is within a collection, which we need to iterate over. So to do that, we're going to create a for loop. For every line in my

[8:47:30] content, I will print each line That's much better. The format resembles a spreadsheet, like an Excel spreadsheet. There's rows and columns. To get a specified column, we

[8:47:51] can access an index. In my example, our line at index of zero would give me the first column, name, Spongebob, Patrick, Sandy. The next index would be all the ages of each person 30, 35, 27. And index two would be the job

[8:48:12] positions, cook, unemployed, and scientist. If you need a specific column of data from a CSV file, you can use an index as one possibility. All right, everybody. So, those are a few ways in

[8:48:26] which we can read files using Python. Hey, what's going on everybody? So, in today's video, I'm going to show you how we can work with dates and times using Python. We will import the date

[8:48:38] time module. This allows us to work with dates and times using our system clock, our computer's clock. This video serves as more of an introduction. To create a

[8:48:48] date object, we will assign an object of date. Let me zoom in a little bit. We will access the datetime module.

[8:48:56] Call the date method. Within the date method, we will pass in the following arguments. A year of our choosing. So

[8:49:04] for me, I'll say 2025, a month, one corresponds to January. These are numeric months. And a day, a day of the month. I will say the

[8:49:15] second. If I was to print the state object, here's what it outputs. The year is 2025, January 2nd. to get the date right now. Let's

[8:49:28] say today. This will return a date object that represents today. Access the date time module. Access the class of date. Then

[8:49:40] call the today method to return the date of today. Let's print today. Currently, I'm recording this video July 14th, 2024. For me, that is the result of my

[8:49:53] today object when I print it. Now we'll work with time. I will create a time object. Access the datetime

[8:50:01] module. Call the time method. We have to pass in hours, minutes, and then seconds. So for the hour, let's say 12,

[8:50:11] 30, and 0 seconds. I will print the current time. It is 12:30.

[8:50:19] Now to get the time right now on our system clock I will create a datetime object of now equals access the datetime module now within the datetime module there is a datetime class we have to access we will access that I know it looks kind of silly datetimed datetime dot the now method so we're accessing the datetime module there is a built-in datetime class we have access. Then within that class, there's a now method. What is the time right now according to my system clock? This returns a date and a time.

[8:51:00] July 14th, 2024. It is just after 9:00 a.m. We can format the appearance of the

[8:51:08] string. Here's how. I'm going to reassign our datetime object of now. Our datetime object has a string

[8:51:19] format time method strf time. We're going to pass in a string and include some format specifiers. Let's say I would like to display the hour first. I'm going to add

[8:51:32] a percent. These format specifiers you can find according to the datetime documentation online. So I will display the hours. That would be percent

[8:51:44] H, percent M for minutes, percent S for seconds. Let's see what we're working with. We have the hours, the minutes, and the seconds. I will separate each of

[8:51:59] these with a colon. That's better. Now I'll add the date. I'll

[8:52:07] start with the month. I will add a format specifier of lowercase M then the day a format specifier of D then the year format specifier capital Y here's the result we have the month the day and the year I'll add a dash to separate these better or if you prefer the day first rather than the We can switch this around. It depends on how you read dates in your country. Now, we're going to

[8:52:44] cover an exercise. We're going to see if the current date and time has passed a target date and time. So, we are going to create a target date time equals access the datetime module. We will create a new date time.

[8:53:04] So now we have to pass in a date and a time. For my date time, let's say it's something far into the future like the year 2030, January 2nd. For the hour, it will be 12 30 and 1 second. I'm going to get the time

[8:53:23] right now which I will name current datetime equals access the datetime module access the datetime class call the now method to return the current date and time right now using an if statement I will see if our target date time is less than the current date time. Have we already passed this date? If our target date is less than the current date, that means this date and time has already passed. I will print

[8:54:02] the following if that's the case. Target date has passed. else I will print target date has not passed. Here's the

[8:54:23] result. Target date has not passed. What if I set the target date to the year 2020? Well, then the target date has

[8:54:33] passed. So, that's how we can check to see if a date and time has already passed. Has it elapsed?

[8:54:40] All right, everybody. So, that is an introduction to working with dates and times using Python. All right, everybody. So, in

[8:54:48] today's video, we're going to create a working alarm clock using [Music] Python. For this project, we will need the following imports. We will import time. We'll be updating our clock every

[8:55:05] second. The time module is going to help us with that as well as import date time. The datetime module allows us to work with string representations of a time. In my opinion, the easiest way to

[8:55:18] work with sound effects is to actually use pygame. So we will import pygame. Now you may need to download the pygame package. Here I'm getting a

[8:55:29] message that there's no module named pygame. There might be a link to install it even too. One way in which you can download the Pygame package is to open up a terminal then use pip. Pip is

[8:55:41] Python's package manager. pip install Pygame. All right, we have our three imports. Let's create a function to set

[8:55:54] alarm. We have one parameter an alarm time. And for now I'll write pass. Our alarm time parameter is going

[8:56:05] to be a string representation of a time in military time. I would like to start this program if I'm running my main Python file directly. I can add the following if statement. If dunder name is equal to a

[8:56:21] string of dunder main. If we are running this main Python file directly then we will set the alarm. But first we have to prompt the user what they would like to set the alarm to. So we will define a

[8:56:34] variable of alarm time equals ask for some user input using the input function. We will prompt the user to enter the alarm time and give a format hours, minutes and seconds. Again this is going to be in military time. Once we have our alarm

[8:56:58] time, we will call the set alarm function and pass in our alarm time. All right, we are now within the set alarm function. When we call this function, let's print the following.

[8:57:11] I'll use an fstring alarm set for then include the alarm time. You will need an MP3 file to work with. If you don't have one available, here's one recommendation. You could use YouTube's

[8:57:28] audio library and then search for sound effects or some music. These audio files are only allowed for non-commercial use outside of YouTube. So, you can search for a song or some sound effects. Find one that you

[8:57:42] like and download it. Once you find a song that you like, move it to your project folder. Now I will create a variable of sound file equals. This will be a relative or

[8:57:58] absolute file path. My MP3 file is right next to my main Python file. I only need to list the file name. I named mine my

[8:58:07] music and this is an MP3 file. I'm going to perform a test run. We're not going to play our sound quite yet.

[8:58:15] We do have this output that displays that says hello from the Pygame community. Let's say I set my alarm to 9:00 a.m. Then enter alarm set for 9:00

[8:58:26] a.m. If you would like to suppress this output for Pygame, we can navigate to our virtual environment. Go to library

[8:58:34] Pygame underneath this file named dunder init. Let's scroll all the way to the bottom. And we should have this if statement. We

[8:58:48] display the version of Pygame we're using and a print statement of hello from the Pygame community. We could comment this out or even just delete it. That is the most simple solution. So we shouldn't get that

[8:59:01] message anymore. We're going to create a boolean variable of is running. Is our alarm clock running? I will set that to be

[8:59:12] true. While is running while this is true, we will continue the alarm clock. We need to get the current time.

[8:59:24] Current time equals we will access the datetime module. Access the class of date time. Call the now method to get the time and date. Right now we could method

[8:59:39] chain the string format method strf time I would like the hours minutes and seconds but not the date. So we will type percent h colon let me zoom out a little percent m for minutes and percent s for seconds. We're getting the hours, minutes, and seconds of the date and time right now and storing it within this variable of current time. Then I'm going to print the

[9:00:13] current time. We'll perform a test run. However, currently we're within an infinite loop.

[9:00:20] At the end of the while loop, I'll set is running to be false. Okay. Enter the alarm time. Let's

[9:00:28] say 10:00 a.m. Alarm set for 10:00 a.m. and the

[9:00:34] time for me right now is 9:42 and 16 seconds. We'll get rid of this line where we set is running to be false. Instead, I'm going to access the time module and call the sleep method. We

[9:00:48] will pass in a number of seconds to sleep. So, 1 second. I'll set the alarm to be 10:00 a.m. Now, the time should update every

[9:00:58] second, which it is. However, when the current time is equal to the alarm time, we have to trigger the alarm. So, after printing the current time, we will write an if statement to check if the current time is equal to the alarm time.

[9:01:22] If this is true, then let's print the following. Wake up. And I'll add an emoji cuz it's silly. Once our alarm triggers, we will

[9:01:37] set is running to be false within this if statement. Let's do a test run. We're not going to play the sound quite yet. I will set the alarm to 9:45.

[9:01:51] and then I'll come back a little bit later. All right. Once the current time matches the alarm time, we print wake up and set is running to be false to exit the while loop and then subsequently exiting the program. Now we need to play an MP3

[9:02:15] file. We will access our package of Pygame. access the module of mixer. So mixer is a module for loading

[9:02:25] and playing sounds, but we have to initialize it, but we're going to initialize it with init to initialize. The initialize method is another way to call the constructor. We can pass in some keyword arguments for the frequency, size, channels, buffer, all that, but that might be a little too complicated for us at this level. We'll

[9:02:47] use the default settings by not passing in anything. The next step is to load our sound file. Access the package of pygame. Access the module of

[9:02:59] mixer. Access the module of music. Then call the load method. We will load our

[9:03:06] sound file. Our sound file contains the file path to our MP3 file. Once we load our music, we have to play it.

[9:03:21] Pygamemixer music call the play method. Our MP3 file is only going to play for a brief second. I'll demonstrate that. I will set the alarm

[9:03:32] to 949 and just give it a few seconds. Our sound file stops playing when the program terminates. What we need to do next is continue playing our sound file while that sound file is busy. We will

[9:03:55] add a while loop. file access pygamemixer dot music call the get busy method. This returns a boolean. If our song is busy, if it's

[9:04:15] still playing, then we will call the time modules sleep method and sleep for 1 second. Once the song finishes or we terminate the program prematurely, the sound file will no longer be busy. So, this should be the finished product.

[9:04:32] Let's test it. I will set the alarm for 952. And we just have to give it some time.

[9:04:49] [Music] So, uh, yeah, I'm going to talk about multi-threading in Python today. Multi-threading is used to perform multiple tasks concurrently. Think of it like we're multitasking. We're

[9:05:14] performing a few different actions at once. For example, I could study and listen to music and eat something at the same time. Multi-threading is good for IO bound tasks. IO meaning input output,

[9:05:27] such as reading files or fetching data from an API, things that may take some time to do and we don't know when it's going to end exactly. To use multi-threading, we'll import the threading module. Import threading. We access the threading

[9:05:44] module, then call the thread constructor and pass in a target function. What we'll do for this demonstration, let's say we have a bunch of chores to do. We have to walk the dog, get the mail, and take out the trash. Let's define some

[9:05:56] functions to handle that. We have a function to walk the dog. Then I will print the following message. You finish walking the dog.

[9:06:12] Let's create a function to take out trash. Then we will print you take out the trash. Then another function of get mail as in get the mail from the mailbox. Then I will

[9:06:36] print you get the mail. Just to simulate these functions taking an indeterminate amount of time, I'm going to import the time module to help us. Let's say walking the dog takes 8 seconds. I will access the time module,

[9:06:59] call the sleep method, and pass in 8 for 8 seconds. When we call the walk dog function, we'll wait around for 8 seconds, then finish walking the dog. This chore will take quite a bit of time to complete. Taking out the trash, it's

[9:07:15] fairly quick. Taking out the trash will take 2 seconds. Getting the mail will take 4 seconds. Let's call these functions and

[9:07:28] see what happens. We will begin by walking the dog. I will call the walk dog function followed by take out trash function and the get mail function. Here's the

[9:07:48] result. We're going to wait around for 8 seconds until the walk dog function is complete. Right about now you finish walking the dog, you take out the trash.

[9:08:02] and you get the mail. These functions are running on the same thread, the main thread, our main Python program. We have to complete these chores in order one by one because they're all running on the same thread.

[9:08:18] Instead of walking the dog and then when we're done taking out the trash and then when that's done, we get the mail. We could accomplish all three tasks at the same time. Let's say we have a thread object.

[9:08:31] We could say thread one. Or to be more descriptive, let's say we have chore one. Let me zoom in a little bit. Chore one is going to contain a

[9:08:42] thread. We will access the threading module. Call the constructor for a thread. We have to pass in a keyword

[9:08:51] argument of target. What is the first chore that we have to do? Let's walk the dog.

[9:08:58] To start this thread, we will take our thread object of chore one and call the start method to start it. Okay, let's do this with chore 2. Access the threading module. Call the thread constructor.

[9:09:16] Pass in a target. Then the name of a function. Take out trash. Chore 2.

[9:09:25] Start. And then we have chore three. I'll just copy what we have because I'm feeling lazy. Chore three will be get

[9:09:35] mail. Here's the result. Now we finish taking out the trash first, then we get the mail. Then we finish walking the dog. So

[9:09:49] we're executing these functions concurrently. We're multitasking. We're taking out the trash and getting the mail and walking the dog all at the same time. One thing that I did want to point

[9:10:01] out, notice how we finish taking out the trash first, followed by getting the mail, then walking the dog. These tasks finished in a different order compared to when we weren't multi-threading. That's because taking out the trash finished first. It took 2 seconds.

[9:10:17] Getting the mail took 4 seconds. And walking the dog took the longest. It took 8 seconds.

[9:10:23] Previously, we finished walking the dog first, then took out the trash, then got the mail. When all the chores are complete, I would like to print a message. I will print the following. All

[9:10:36] chores are complete. Here's what happens. Currently, we get this message that all chores are complete, but we haven't finished any yet. We're still completing

[9:10:48] them. There may be at times you want your program to wait for all threads to finish. Before we print that confirmation message that all chores are complete, we're going to use the join method. Take each thread, use the join

[9:11:08] method. We'll do this with chore 2 and chore 3 as well. With the join method, we will wait for these threads to finish before continuing with the rest of the program.

[9:11:19] Here's the result. Now you take out the trash, you get the mail, and you finish walking the dog, all chores are complete. When constructing a thread object and we have a keyword argument of target if some of these functions take parameters for example with the function of walk dog let's say we have a first name I will convert this print statement to an fstring we will display first for the first name you finish walking whatever your dog's name is. So when we're creating a thread and

[9:12:01] the target is that function and that function accepts arguments, we need one more keyword argument and that is args. We will send this function a tpple. We need a set of parenthesis within this tpple. We will list our arguments. Let's

[9:12:17] say that our dog's first name is Scooby. Now, since this is a tpple, if we only have one argument, we have to end that tpple with a comma to let Python know that this is a tpple. Here's the result. You take out the trash. You get

[9:12:36] the mail. You finish walking Scooby. All chores are complete. If we were missing

[9:12:45] this comma, this is what would happen. We're no longer passing in a tpple. What if we have multiple parameters? We have first for first name

[9:12:57] and last for last name. You finish walking first and last. We have first name of Scooby, last name of do. You take out the trash. You get the

[9:13:14] mail. You finish walking Scooby-Doo. All chores are complete. All right, everybody. So, that

[9:13:24] is multi-threading. It's used to perform multiple tasks concurrently. As if we're multitasking, we're executing multiple functions at the same time.

[9:13:34] Multi-threading is good for IO bound tasks such as reading files or fetching data from APIs. And well everybody, that is an introduction to multi-threading in Python. Hey everybody. In this video, I'm going

[9:13:47] to show you how we can connect to an API using Python. In this demonstration, we're going to connect to the Poke API to get some information on a Pokémon of our choosing. I'm assuming that most of us are familiar with Pokémon. I thought

[9:13:59] it'd be a fun example. So, according to this API, we can look up a Pokémon such as Pikachu. Then we can get the stats for Pikachu, such as Pikachu's name, height, ID number, and all sorts of moves and abilities that a Pikachu may have. We will need this URL, but

[9:14:22] we'll handle that later. Our first step is that we're going to import the requests library to make an API request. However, when I run this, I have a module not found error.

[9:14:36] No module named requests. Requests is one package we'll have to install. It's not normally included with the standard Python download. If I was to go to my project

[9:14:46] folder, go to my virtual environment library site packages. There is no package for requests. We'll have to download that. With PyCharm and VS Code,

[9:14:57] there is a built-in terminal that we can use to download the request package. We can use pip. Pip is a package manager for Python. It's normally included when

[9:15:07] you install Python. We'll type pip install requests. It'll take just a second. And now we have that package of

[9:15:18] requests within our project folder. If I run this again, that error goes away. process finished with exit code zero. That means

[9:15:27] there were no errors. Going back to our Pokemon API, we will need this URL. Let me zoom in so you can see it. I'm going to store that as a base

[9:15:43] URL so it's easier to work with. For convenience, I'm going to create a function name. Get Pokemon info. To get some info on a Pokemon,

[9:15:57] we'll have to pass in the name of a Pokemon. For now, I'll write pass. Outside of this function, let's say we have a variable of Pokemon name. Pick a

[9:16:09] Pokemon. I will pick Pikachu for now. Then I will call the get Pokemon info function. then pass in my Pokemon

[9:16:18] name. Remember that your parameters can be named different than your arguments. When you send data to a function, you can rename it to something else temporarily. Now that we have the name

[9:16:29] of the Pokémon we would like to look up, we can complete the URL. This will be an string. So with our Pokemon API, we have the base URL followed by the word Pokemon, then the name of a Pokemon. So we have the base URL. I'll

[9:16:49] add a placeholder and insert it forward slash the word Pokémon slash the name of that Pokémon. In this example, it's going to be Pikachu. We now have the full URL.

[9:17:04] We'll access the request module, use the get method and pass in that URL. This method is going to return a response object which I will assign to response. Response is a response object. And I'm just going to print our

[9:17:22] response just to see what we're working with. Here's our response object. It has a status code. This is an HTTP status

[9:17:32] code of 200. 200 means the response was okay. Here's a few examples of response codes. You're probably familiar with

[9:17:41] 404. Not found. So, we are looking for 200. The

[9:17:49] response is okay. After we get our response, I'll add an if statement. If our response our response object does have an attribute of status code to read what the status code is. If this status

[9:18:06] code is equal to 200 that means the response is okay. But for now I'll write pass. Else I'm going to print the following. else I'm going to print

[9:18:19] failed to retrieve data and I will print the status code of the response object. So temporarily I will print data retrieved if it was successful. I can't spell.

[9:18:42] Okay, we have our data. Data was retrieved. If our status code of our response object is equal to 200, I will take our response object and use the JSON method. Our response is a JSON format.

[9:18:59] Using this method, we'll convert it to a Python dictionary. It will consist of key value pairs much like a JSON file, but I'm going to assign that to a variable of Pokemon data so it's easier to work with. Then I will print our Pokemon data. So here's the data on Pikachu.

[9:19:26] It's really difficult to read all this. You can see some keywords. We have abilities, base experience. This is an

[9:19:35] extremely large dictionary. Once we have our dictionary, I will return that dictionary of Pokemon data back to the place where we call this function and I will store that as a variable. Pokemon info equals get Pokemon info. Pass in a Pokemon's

[9:19:58] name. And now we should have a dictionary that we can work with. Let me zoom out.

[9:20:06] If our dictionary exists, we can use the if keyword. If Pokemon info, if that's true. If it exists, this will be true. I

[9:20:16] will print the following. I'll use an f string. To access the value of a dictionary, we can access it by a key.

[9:20:25] We'll take our dictionary of Pokémon info. Access the key of name. Let's see what happens exactly.

[9:20:35] we get Pikachu. Let's get Pikachu's ID number. We will access the key of ID.

[9:20:43] The given value is 25. Pikachu is the 25th Pokémon in the franchise. Let's get Pikachu's height. Pikachu's height is four. I

[9:20:58] don't know what unit of measurement they use in that franchise. 4 feet or 4 in. I don't know.

[9:21:04] Let's get Pikachu's weight. Pikachu's weight is 60 60 lb 60 kg. I don't know. Just to make this look

[9:21:16] nice, I'm going to add name, ID, height, and weight. That looks much better. Let's pick a different Pokemon. I will pick my

[9:21:33] favorite Pokemon of Tyloian. Failed to retrieve data. Does that have to be a lowercase T? Yes, it does. Okay. So, name

[9:21:49] Tyloian. I'll follow the name with the capitaliz method to make it capital. There we go. So, my favorite

[9:22:01] Pokemon is Typhloian. ID is 157. Typhloian's height is 17 and weight is 795. All right,

[9:22:10] everybody. That is one way in which we can connect to an API using Python. Also, tell me what your favorite Pokémon is in the comment section down below. All right, everybody. In today's

[9:22:20] video, we're going to get started working with the PIQT5 graphical user interface, also known as a GUI GUI. In this topic, we'll be creating a basic window. So, let's get started. All

[9:22:32] right. The first step is that using pip, we're going to install the PIQT5 package. Open up a terminal. Both

[9:22:39] PyCharm and VS Code have a built-in terminal that you can use. We're going to use pip, that is Python's package manager. pip install PIQT5. Enter. And this might just take a

[9:22:53] second. Once your download has finished, you should have a package within your site packages folder named piqt5. We can work with it as long as we import it. First, we are going to import the

[9:23:08] module of CIS. CIS meaning system. This module provides access to variables used and maintained by the Python interpreter. Then from the package of pi

[9:23:20] QT5, do pay attention to the capitalization. It's easy to mess that up. Use dot to access the module of QT widgets. Widgets are the building

[9:23:32] blocks of a PIQT5 application. They begin with Q. That helps distinguish them from widgets from other libraries.

[9:23:39] They typically begin with Q. From this module, import the following widgets. Q application and Q main window. Here's

[9:23:54] some boilerplate code that we have to write in order to get this application up and running. First, we will create a class of main window which will inherit from the class of Q main window by inheriting from the parent of Q main window. We can customize our own windows to display to the user. We will

[9:24:14] need a constructor. Let's define that. Define innit. There will be no

[9:24:20] arguments currently besides self. And in case we have to pass any arguments to the parent of Q main window, we will access the superass that's the parent and call the parents constructor. But currently we don't have any arguments to pass in. We will return to this class

[9:24:39] momentarily. Let's define a function of main. When we begin this program, we will call the function of main to begin the application. For now, I'll write

[9:24:49] pass. If we are running this file directly, let's add the following if statement. If dunder name is equal to a string of dunder main. If we are running this file

[9:25:03] directly, call the main function in order for us to begin. If that's true, we will call the function of main. Within the main function, we will create an app object.

[9:25:15] app equals we will call the constructor for Q application that class but there's one argument that we have to pass in we will access our module of cis argv meaning arguments so by passing in this argument this allows piqt to process any command line arguments intended for it that's if we use command prompt or terminal we won't be doing that in this series but you may someday in the future it would be a good idea for us to futureproof our code. Otherwise, you may see people pass in an empty list. So, we now have an app object. Next, we will create a window

[9:25:55] object. Window equals call the constructor for our class of main window. Currently, we don't have any arguments to pass in. We have an app

[9:26:05] object and a window object by calling their respective constructors. Now if I run this program currently, our window is not going to show. The default behavior for a window is to hide it. In

[9:26:18] order to show our window, we will access our window. Call the show method to show it. It's only going to appear for a brief second when I run this script. I don't know if you saw it, but

[9:26:32] it pops up for a brief second. We need to ensure that the window stays until we interact with it or close it. After we show our window, we will access our module of CIS call the exit method. The exit

[9:26:48] method ensures a clean exit of our program. Within our exit method, we will pass in as an argument our app object. Our app object has a built-in method of exec. And this is a method so we can

[9:27:04] call it. This is the execute method. There is an underscore character after exec for execute that distinguishes it from the execute method. There is a

[9:27:15] separate version of this execute function that ends with an underscore. Our apps execute method. It waits around for user input and handles events such as if we click buttons, press keys, or close the window. Now that we're calling

[9:27:29] this method, when we run our program, this window should stay in place. We can maximize it, minimize it, or close it. That's all the boilerplate code that we need for a basic window. Let's

[9:27:44] customize it. Within our constructor for our main window, what would we like to add? Let's set the title for our window. self dot set window title

[9:27:58] method. We will pass in a string. Think of a title for your program. My cool first GUI

[9:28:09] guey. And now we have a new title. My cool first guey graphical user interface. When this window appears, we

[9:28:18] can set the geometry of where the window appears and the size of the window. access self dot set geometry method. There's four arguments. X and Y for the X and Y

[9:28:34] coordinates, a width of the window, and a height of the window. If I were to set X and Y to be both zero, this window will appear in the top left corner of my screen. I'll also need a width and a height. Let's say, I don't

[9:28:51] know, 500 for each. So now my window is now a square. The width and the height are both the same. They're both 500. The width is 500

[9:29:01] pixels. The height is 500 pixels. With the first two arguments, we set the initial placement of our window to be where x is 0 and y is zero. That

[9:29:11] corresponds to the top left corner. If I set the first argument to be 100, well then the window is going to move to the right by 100 pixels. There are ways to center your window in the very center of your screen, but that's a little too advanced for us right now.

[9:29:28] For the time being, I'll pick something roughly near the middle of my screen. 700 pixels on the xaxis and 300 on the y-axis. It should appear roughly in the middle, but feel free to adjust these values based on the size of your screen. We'll

[9:29:45] discuss layouts in the future. Now, if you would like a window icon, we can change that. You will need an image to work with. So, within my project

[9:29:56] folder, I have a profile picture for my YouTube channel. I'll set that to be the icon. Find an image that you like, then add it to your project folder.

[9:30:06] In order to work with icons, we'll need to make the following import. From piqt5, that's the package. Access the module of qt gui. import the following Q icon. Now we

[9:30:25] can work with icons. After we set the geometry for our window, access this object of self, this main window, call the method of set window icon. Within this method, we will call the constructor of Q icon. We'll pass in

[9:30:47] either a relative file path or an absolute file path. My main Python file is right next to my profile picture, that image. I only need the file name within a string. So the name of my

[9:31:00] image, it's going to be different for you depending on what the name of your image is. My image is named profile_pic and this image is a JPEG jpg. Then when I run this program, I'm using my image as an icon for this window. All right, everybody. That is

[9:31:21] how to create a window using PIQT5. And in the next topic, we will be creating some labels. What's up everybody? In today's

[9:31:29] topic, we're going to create some labels using PIQT5. We will import the widget of Q label. This label class is used to create label widgets that can display text or images. Within the constructor

[9:31:45] of our main window, this is where we'll create a label. We will declare a label object. label equals call the constructor for Q label. For the text of the label, we'll

[9:31:59] pass in a string. That's the first argument. Let's say the word hello. For the second argument, we will

[9:32:06] pass in self. Self refers to this window object that we're calling and instantiating. All right, let's do a test run. Here is my label. Although you can

[9:32:19] barely see it, the font is really small, but it does say hello. Let's set the font. We'll need another import from pi qt5 dot qt gui import q font. By importing the qfont class, we

[9:32:44] can begin working with fonts. We're going to take our label call the set font method. Within this method, we will call the constructor of Q font. Pick a font that you would like. I

[9:32:59] will pick Ariel, but feel free to choose really any font. Then the second argument is a font size. I'll pick 30. Let's do another test

[9:33:11] run. That's much better. Let's increase this to 40 for the font size. Now I'm going to set the geometry

[9:33:20] of this label such as the positioning and the width and the height. Let's take our label. Use the set geometry method. We

[9:33:33] will pass in X and Y coordinates. 0 corresponds to the top left corner. For the width, let's set the width to be 500 and the height to be 100. That's better. I'll cover more

[9:33:48] advanced alignments momentarily. Let's add a stylesheet. PIQT does have styles that are very similar to CSS. If you would

[9:33:57] like to learn more about CSS, I do have a full course on that topic. We will add some CSS like properties by accessing our label object. call the method of set style sheet. Within this method, we will pass

[9:34:15] in some CSS like properties such as a color. For the color, let's say blue. These CSS like properties should end with a semicolon. And now the font color is

[9:34:28] blue. You could also use RGB values or hexodimal values. You could always look up a color picker and pick a very specific color. Let's pick something

[9:34:42] green. We can either use RGB values or hexodimal values. So I will copy this value. So I will paste that hexodimal

[9:34:54] value. And now we have a very specific shade of green. But I think I'll go with something dark.

[9:35:03] such as that. So this color is going to be a dark gray color. We could set a background color.

[9:35:13] This will be a new string. Background dash color. And I will pick a new color. I will pick something blue.

[9:35:32] That's a decent color. We have a blue background with dark gray text. We can set the font to be bold.

[9:35:44] Font weight will be bold. So the font is now bold. The font style can be italic. font

[9:35:57] style italic. So our font is italic and we can underline text decoration underline. The text on our label is now underlined. Let's work on positioning

[9:36:17] next. Currently my text is left justified and set to the center vertically. To work with alignments, we need this import from piqt5 QT core import QT. The class of QT is used for

[9:36:41] alignments. To center the text of our label at the top vertically, we will take our label use the set alignment method. Then pass in a flag access the class of Qot access the flag of align top. This will align our text vertically

[9:37:04] to the top. So then our text is aligned vertically to the top rather than the center. For the bottom, we will use the flag of align bottom. We will align vertically on the

[9:37:27] bottom. The text is now on the bottom. to align vertically in the center. Align V

[9:37:38] center. This will be vertically center which it was originally. Now for horizontal alignment we can add the following. Okay. To align right we will

[9:37:52] pass in a flag of align right. horizontally align right. The text is now all the way to the right for the center. Align H. H for

[9:38:14] horizontal. Center. The text is now horizontally aligned in the center. for the

[9:38:30] left. Align left. The text will be aligned to the left. We could combine both horizontal

[9:38:42] and vertical positioning. Here's how. Take our label, call the set alignment method.

[9:38:53] We will align horizontally in the center. Follow this with the or bitwise operator which is a vertical bar. This allows us to combine flags. We will

[9:39:03] align horizontally in the center. Then vertically let's align to the top. So our text should be aligned horizontally. We're aligned in the

[9:39:14] center. And vertically we're aligned to the top. align bottom vertically. Horizontally, we are in the

[9:39:25] center. Vertically, we're aligned on the bottom. Then for the very center of our label, align horizontal center and align vertical center.

[9:39:49] Our text will now be in the very middle of our label, both horizontally and vertically. Now, there is a shortcut for the very center. We don't need both of these flags. The shortcut is the

[9:40:04] following. Set alignment align center. that will align the text both horizontally and vertically. So that is center and

[9:40:17] center. All right everybody, so that is an introduction to labels in PIQT5. What is going on everybody? In

[9:40:25] today's video, I'm going to show you how we can add images to PIQT5. You will need an image to work with me. I'll be using my profile picture for my YouTube channel. Feel

[9:40:34] free to take a moment to find a picture of your own, maybe a profile picture of yourself. We will need the following imports. Q label. The most common and

[9:40:44] straightforward approach to displaying an image is to add an image to a label in order to display it. Then we will need this other import from piqt5. That's the package. Then the

[9:40:57] module of qt gui import the class of qpix map. The class of qpix map it's used for handling images and provides functionality for loading, manipulating and displaying images. We will load our image to a qixmap object. Then add this

[9:41:18] qpix mapap object to a label in order to display it within our constructor of our main window. We will create a label. Label equals call the Q label constructor. Then pass in self. self

[9:41:34] refers to the window object. Our window will be the parent widget. Our label widget is one of its children. Once we

[9:41:41] have our label, we'll set the geometry of the label. Label set geometry method. We have to pass in x and y coordinates as well as a width and height of the label. For the coordinates, let's say

[9:41:56] zero for each. The label will appear in the top left corner. For the width, 250 is good. and the height 250 as

[9:42:05] well. Here's my window. The label is going to appear in the top left corner.

[9:42:10] However, there's nothing added to the label. That's where the widget of qpix map comes in. We will create a pix map object equals call the constructor of q pix mapap. We have to pass in a string

[9:42:25] that represents a relative file path or an absolute file path to our image. My image is right next to my main Python file. I just need the file name. The

[9:42:35] name of my image is profile_pic and this is a JPEG. When I run this, we don't see our image. We have to add the pixmap object to the label. We have to set it. Here's

[9:42:50] how. Take our label, use the set pixmap method, and pass in our pix map object. And now we can see the image. However,

[9:43:02] the image doesn't scale according to the size of the label. To enable that, we have to call the following method. Take our label, call the set scaled contents method, then pass in true. Our image will now scale to the

[9:43:20] size of the label. If we were to change the size of the label, let's say it's 100 pixels, it will scale down even further. Or I could even increase it to 500. So now the image takes up the

[9:43:37] entire width and height of the window. Let's set that back to 250. There's a few tricks that we can do with positioning of the image. We've set

[9:43:49] our label with an image. We can move the label within the confines of the window. Currently, it's set in the top left corner, but here's a few tricks that we can do with positioning. With our label,

[9:44:01] we will set the geometry again. So, the top left corner is 0 0 for the coordinates. We could pass in 250 and 250 again for the width and the height.

[9:44:15] But if we were to change that here when we initially create this label, we would have to manually change that here as well. I think it would be better if we were to get the current width and height of the label. Take our label, call the width method to get the width. Same

[9:44:31] thing applies with the height. Label height method. And that should work fine. Let's say we would like to take

[9:44:41] our image and move it to the right side of our window. Here's how. With the x-coordinate, we're going to access self. That means our window called the

[9:44:52] width method. Here's what we have currently. We can't see the label. It was placed outside of the

[9:45:00] confines of the window. Let's subtract our label's width. Label.width. I'll put each of these

[9:45:10] arguments on a new line just to help with readability. So now our image is right justified within our window. For the bottom right corner, we will take the second argument access self.height. That's the height of the

[9:45:29] window that we're instantiating minus our labels height. And now our image is in the bottom right corner. For the bottom left corner, we will set X to be zero. Now, here's the tricky part. To

[9:45:49] have our image placed in the center of our window, we will take the width of the window minus the width of the label divided by two. For integer division, we'll be using double forward slashes. We need our pixels to be whole integers, so we're going to be using integer division and not standard division.

[9:46:09] We will round to the nearest whole pixel. Then we will do this with the height as well. And now our image should be in the middle of our window. All right everybody. And that is

[9:46:24] how to add an image to your PIQT5 application. Well, hello again friends. Today I got to explain layouts in PIQT5.

[9:46:33] We'll discuss vertical, horizontal, and grid layouts. But we'll need the following imports. We will be importing Q label Q widget. I'm going to put these imports

[9:46:46] on a new line just because we have a lot. Q V for vertical box layout. And I'm just going to copy this. Q H for horizontal box

[9:47:02] layout and Q grid layout. Let's be sure that we have all these imports. These classes deal with layout managers. They aren't widgets. We'll be

[9:47:14] writing a majority of the code within our main window class. However, it can get disorganized really quick. What will help keep things organized is if we declare a separate function within the main window class. This is a common practice that

[9:47:28] you'll see within PIQT5. There will be a function for init for initialize UI for user interface. no other arguments besides self. And for now, I'll write

[9:47:40] pass. When we construct a window object, we will call self dot init UI to initialize the user interface. So, anything that deals with the user interface, we're going to be writing within this function to help keep our code clean and organized.

[9:47:58] Normally, we can't add a layout manager to a main window object. Main window widgets have a specific design and layout structure that's normally incompatible with layout managers. What we would need to do is create a generic widget, add a layout manager to that widget, then add that widget to the main window in order to display the layout.

[9:48:20] Within our method to initialize our user interface, we are going to create what is called a central widget called the constructor for Q widget. This is a generic widget. Then we will take self. Self is our

[9:48:38] window. Call the set central widget method. Then pass in our central widget. When working with layout

[9:48:49] managers, we will add that layout manager to the central widget. The central widget is then added to the main window. So currently this is what we're working with. We will need some widgets to

[9:49:02] organize because right now it's empty. Let's create a few labels. Let's say label 1 equals Q label. I'll pass in some text. Number

[9:49:15] one. Okay. Let's create four additional labels 1 through 5. I'll just do some

[9:49:22] copying and pasting. All of our labels are overlapping. Let's add some colors.

[9:49:33] Let's take label one, use the set stylesheet method, then pass in a background color as a CSS property. Background dash color will be red. Let's copy this line of code. paste

[9:49:53] it four additional times. For labels 1 through 5, we'll have a label that is yellow, another that is green, blue, then purple. Here are the labels. They're all

[9:50:14] overlapping one another. That's why we can only see five. This is where a layout manager comes in.

[9:50:21] We'll start with the vertical layout. We will create a vertical layout manager which we will name vbox vbox equals call the constructor for QV box layout. We are calling the constructor.

[9:50:40] We will take our layout manager, call the add widget method, then pass in a widget such as label one near the top here. We'll do this with the other labels. We'll do some copying and pasting. Add label 2, 3, 4, and

[9:51:01] five. There's one last step. We will take our central widget which we have declared at the top of this function. Call the set layout

[9:51:15] method. We are setting the layout of our central widget with the layout manager of Vbox vertical box. Here's the new layout. All

[9:51:26] of our labels, all of our widgets are arranged vertically. For horizontal, we will use QH box layout. For horizontal, replace any instance of Vbox with Hbox. For the set layout method, pass in

[9:51:46] Hbox. This allows for a horizontal layout. Then we have grid. Q grid layout. Replace Hbox with

[9:52:02] grid. So what we have to do with grids after adding a widget we have to specify a row and column with separate arguments. The row and column both begin with zero. So row one column 1 would be

[9:52:16] row 0 column 0. For label two let's say row 0 column 1. Label three will be row 1 column 0.

[9:52:29] Four will be row one, column 1. Then five, row one, column 2. So here's the current layout. We have labels 1 and two, both

[9:52:41] within row zero. Labels 3, 4, and 5 are both within the second row. Let's say label 5 is row 2, column 2. That would

[9:52:51] result with something like this. We have label five, which is purple, in row two, column 2. So it depends on how you want to arrange your widgets. All right

[9:53:01] everybody. So that is an introduction to layout managers in PIQT5. Today I'm going to show you how we can create push button widgets in PIQT5. To begin we will need the

[9:53:13] following imports. Q push button as well as Q label for this demonstration. During the previous topic on layout managers, within our constructor for our main window, we defined a method of initialize UI for user interface. Let's

[9:53:31] be sure that we're calling that method within our constructor. Within this method is where we'll be handling managing the user interface. To create a button, we will call the push button constructor. Normally, when creating

[9:53:42] widgets, we would want to prefix that widget with self, then follow the name of the widget, for example, button. However, I'm going to demonstrate what happens when we don't do that because without self, we're declaring a local variable. We'll get back to that in just a moment. Let's create a local button

[9:54:00] object by calling the Q push button constructor. We can pass in some text such as click me. We will add this to our window self.

[9:54:12] Self refers to our window object. Let's set the geometry of the button. button set geometry. We could use a layout manager,

[9:54:23] but I do want to keep this lesson as simple as possible. So, let's pick some coordinates. I've picked the following.

[9:54:30] For the X and Y coordinates, 150 and 200. For the width, 200, and the height, 100. Here's our button. Currently, the

[9:54:39] font is a little small, so I'm going to set the stylesheet. Set style sheet. I'll just increase the font size. We

[9:54:50] could use Q font, but that might be overkill for this demonstration. Let's just say the font size will be 30 pixels. Now we can read it. So we have

[9:55:02] our button. We're going to be connecting our button to a function, but we need to define that function. We'll do so within our main window class.

[9:55:12] So we will define a function of on click. There are no parameters besides self. When we click on the button, what would we like to do? Let's print a test

[9:55:24] message. Let's say button clicked. And that's it. When we click this button, nothing

[9:55:34] happens. We have to set up a signal and slot for the button. Here's how.

[9:55:41] We will take our button dot list a signal. A signal is emitted when a widget is interacted with. We have to list the type of signal. So the signal

[9:55:52] we're looking for is clicked. When we click this button, we will perform a slot an action. We will take the signal of clicked connect it to a slot. Connect is a method.

[9:56:07] The slot will be self dot the name of the method on click. When we press this button, we perform this slot this method of on click. Each time I press the button, we perform that action. Not only should we print a

[9:56:27] message for this demonstration, let's set the text of the button. So, we have button set text. Let's change the text to clicked. So, this actually isn't going

[9:56:44] to work because we're not prefixing self. Let me demonstrate what happens. We print button clicked. But

[9:56:53] then we have a problem. We have an exit code. Our program was interrupted. Button is considered local

[9:57:00] to our initializer method. Our on click function doesn't recognize what our button is. That's why we're going to prefix our button with self. So it

[9:57:09] belongs to the class of main window and not this method. Any instance of button we're going to prefix with self. And now this should work. The text

[9:57:22] on my button is going to change when I click it. Clicked. You don't have to do this, but with my personal coding style, whenever I create a variable or an object within a class, I like to do so within the constructor.

[9:57:38] Even PyCharm is giving me a warning. When we declare this button, I'm going to move it to the constructor. And let me just rearrange everything. self dotbutton equals a Q

[9:57:55] push button widget within my initializer method. That's when I like to rearrange everything and style it. We can also disable buttons when we click on them.

[9:58:06] To do that, we will take self.button, call the set disabled method, then pass in true. When I click the button, it will be disabled. I can

[9:58:19] no longer click on it. For the last part of this demonstration, when we click on our button, let's change the text of a label. Let's declare self label within our constructor equals a Q label. The text of the label will be

[9:58:39] hello. We will add this label to self the window. When we set up the user interface, let's set the geometry of the label self.l

[9:58:50] lab set geometry. We could use a layout manager, but just to keep things simple, I'm going to set some coordinates. 150 for X, 300 for Y. The width will be 200, and

[9:59:04] the height 100. Let's change the font size. self.label set style

[9:59:15] sheet. I will set the font size to be 30. Maybe 50 better. All right. Within our on

[9:59:28] click function, let's instead take self.label set text method. Then pass in some new text to display. We're saying

[9:59:40] hello. But when we click the button, let's say goodbye. So now when I click the button we will change the text on a separate widget my label which now says goodbye. So with buttons you need a

[9:59:57] signal that's connected to a slot. The signal is an event. The slot is an action that this widget is going to take when this signal occurs. And well

[10:00:07] everybody that is an introduction to push buttons in piqt5. Hey y so today I got to explain a checkboxes in piqt5. To work with checkboxes we will need the following import from the module of widgets from piqt5. import q

[10:00:27] checkbox to work with different states. We will also need the following import from piqt5qt core importqt. this module of QT core it contains non-geuey classes relevant to piqt5 applications so be sure that you get this import as well to create a checkbox I will create this within the constructor of my main window we will create a checkbox with self the name of the checkbox which I will name checkbox equals call the constructor of the Q checkbox class the first argument is going to be the text of the checkbox.

[10:01:12] What do you want the checkbox to say? Let's ask, do you like food? The second argument is the parent widget where we will be adding this checkbox. Let's say self. Self will

[10:01:27] apply to this window. We could use a layout manager, but I want to keep this lesson as simple as possible. We're just going to focus on checkboxes and their functionality. So, we should have a

[10:01:38] checkbox. However, we can barely see it. The font is really small. I have a

[10:01:44] method to initialize the user interface. That's where we'll set the stylesheet and the geometry of our checkbox. Let's set the stylesheet. self

[10:01:54] dot the name of the checkbox. Checkbox dot set style sheet method. Then we can pass in some CSS like properties. Let's set the font size to

[10:02:09] be 30 pixels. And I will pick a font family. Font family Ariel. Oh, and we should change the

[10:02:23] geometry of the label. It's getting cut off. self dot the name of the checkbox, which is checkbox.

[10:02:33] Let's set the geometry. Pass in some X and Y coordinates for the placement as well as a width and a height. I will pick 500 and 100. Maybe I'll move it a little more to

[10:02:48] the right by 10 pixels. That's pretty good. Our checkbox has an initial state. It's normally

[10:02:56] unchecked. That's the default behavior, but we could set that to be checked with the following method when the window loads. Let's take our checkbox self.checkbox, call the set checked

[10:03:10] method, then pass in true. So then when the window loads, the checkbox is already checked. But let's keep that as false. Now this checkbox, it doesn't do

[10:03:24] anything when I check it. Let's add some functionality. We'll take our checkbox, connect a signal to a slot. The slot can be a function or a

[10:03:36] method. Let's define a method within our main window class. Let's name this method checkbox changed. We will call this

[10:03:47] method when the state of our checkbox changes. There is one parameter beside self a state. Now the state parameter is going to be provided to us when we interact with our checkbox. When we

[10:04:00] check the checkbox, let's print something like a test message. You like food. We have to connect a signal of state changed to a slot of checkbox changed. We will take self dot the name

[10:04:17] of the checkbox which is checkbox. The signal will be state changed. To connect a slot to a signal, we use the connect method. Then pass in a

[10:04:30] function or method name. So we are working with methods. This method belongs to the window class. We'll prefix the method

[10:04:39] name with self. self.checkbox changed. So when I run this program,

[10:04:46] when I check the checkbox, we execute this method. You like food. Now when I uncheck it, I instead would like to display you do not like food. So that's where our state is going

[10:05:00] to come in. I'm going to print our state just to see what it is. Our state is going to be a value. When we check the check box, our

[10:05:13] state has a value of two. When we uncheck it, it has a value of zero. Zero means unchecked. two means checked.

[10:05:22] There's also one for partially checked, but that's not going to be relevant to this topic. So, zero or two. We could add an if statement such as if state is equal to two, then print you like food.

[10:05:37] However, that's not really readable. Other developers looking over your code aren't going to understand what two is by looking at it. Instead, let's use the following. We will access the class of

[10:05:48] QT. There's a built-in constant of checked. This also equals to, but it's more readable. It's a constant. So, if

[10:06:00] state is equal to QT checked, print you like food. I will check the checkbox. You like food. When I uncheck it, nothing

[10:06:11] happens. Let's add an else statement. else. Let's

[10:06:17] print you do not like food. So then when I check the check box, we print you like food. When I uncheck it, we print you do not like food. You like food. You do not like

[10:06:33] food. You like food. You do not like food. All right, everybody. So that is

[10:06:38] an introduction to checkboxes in PIQT5. All right, let's do this thing. Today I got to talk about radio buttons in PIQT5. To work with radio buttons, we

[10:06:49] will need the following imports. From the module of QT widgets, we will need the class of Q radio button as well as Q button group. To group together different buttons, let's create three radio buttons within the constructor of my main window. We will construct three

[10:07:10] radio buttons. For the first radio button, this will be named radio one. We will call the constructor of the class Q radio button. Then we can pass in some

[10:07:21] text. What is the radio button going to say? Let's say that we're working with payment options. Let's say visa for the

[10:07:29] first option. Then for the second argument, I will pass in self. We will add this radio button directly to our window. That would be self. Let's create

[10:07:40] two more additional radio buttons. Radio 2 and radio 3. The text of radio button two will be masterard and three will be a gift card.

[10:07:51] We are selecting different payment options. We need to set the geometry of these radio buttons because we're not using a layout manager. I have a method to initialize my user interface. This is

[10:08:04] where I will set the geometry of my radio buttons. So let's say self.radio 1. We will call the set

[10:08:12] geometry method. Pass in some coordinates. 0 0 is good. That applies

[10:08:18] to the top left corner of my window. For the width 300, and the height 50 is good. Let's do this with radio buttons two and three. Radio 2, radio 3. We'll

[10:08:31] just move each radio button down on the y-axis by 50 pixels each. So 50, then 100. Here are the three radio buttons.

[10:08:41] However, the font is kind of small. We can barely see it. So, let's apply a stylesheet. Here's a trick that we can

[10:08:48] do with stylesheets. We can apply multiple CSS like properties to an entire group of widgets. Rather than having to type them and apply them individually, we will select our window of self. set the stylesheet of our

[10:09:03] window with the set stylesheet method. We will add a selector. The selector is going to be the name of the widget. Q radio button in this case.

[10:09:14] Then add a set of curly braces. We can apply CSS like properties to an entire group of widgets this way. So let's set the font size of all radio buttons to be 40 pixels.

[10:09:34] better. Let's set the font family to be aerial. Then I will add a little bit of padding around each radio button. Padding 10

[10:09:49] pixels. That's pretty good. So with radio buttons, we can only select one from any one radio button group. If I

[10:09:57] was making a payment, I can't pay with a Visa and a Mastercard at the same time. I can only select one option. That's the point of radio buttons. We're limited to

[10:10:07] just one option. With the default behavior of PIQT5, all radio buttons, unless explicitly stated, are all part of the same group. To demonstrate that, let's create two additional radio buttons.

[10:10:22] Radio 4 and radio 5. Radio button four will be for a payment method rather than a payment type. For example, we could say we're paying in store. Radio button five will be we're

[10:10:35] paying online. Radio buttons 1 through 3 will be for the payment type. Radio buttons four and five will be for the payment method. We're either paying in

[10:10:45] store or we're ordering something online. We do need to set the geometry for these two radio buttons. I'll just copy these two lines. Add radio 4. Radio 5. We'll set

[10:10:58] the y-coordinate of four to be 150 and five to be 200. All radio buttons will be within the same button group. If I was to select in store, we deselect one of these options. What I would like is

[10:11:12] one option from this first group and another option from this other group. These buttons are all in the same group. I can only select one. If I would like

[10:11:22] to pay with the visa in store and I click the in store radio button, we unselect the radio button for visa. I would like these radio buttons within different groups. We need to create two different groups and add them accordingly. Here's

[10:11:39] how. Within our constructor, we will access self. Declare a button group.

[10:11:45] Let's name it button group one for simplicity. Equals call the constructor of the class Q button group. Then pass in self to set the parent widget to be the window. Then we will create button group

[10:12:03] two. We're going to access self. Select the radio button group. Button group one. Call the add

[10:12:14] button method. Then pass in a radio button self.radio one. Then we'll add radio 2 and radio

[10:12:26] 3. We'll select button group two this time. Button group two. Add radio button four and radio

[10:12:35] button five. The first three radio buttons are within the same group. Radio buttons four and five are within a different group. We can only select one radio

[10:12:47] button from any one radio button group. Maybe I would like to pay with a Visa card in store or a master card online or a gift card in store. These radio buttons are within different button groups. We're limited to one

[10:13:03] selection in any one radio button group. When we select these radio buttons, they don't quite do anything. For each radio button, we have to connect a signal to a slot. Here's

[10:13:15] how. Let's define a method of radio button changed. There will be no parameters besides self temporarily. I'll write pass. We'll

[10:13:28] fill this in in a moment. We will take each radio button. Let's start with radio one. Radio one.

[10:13:37] The signal will be toggled. When this radio button is toggled, we will connect a slot. We will pass in a function or a method self radio button changed. Then we will

[10:13:53] do this with the other radio buttons 1 through 5. Let's print a test message. You selected something just to be sure that everything is working. You selected

[10:14:13] something. Okay, we know that that works currently. What we're going to need to do is get the sender widget which radio button sent the signal of toggled.

[10:14:27] I will create a local radio button to store that radio button whichever one emitted the signal. We can determine that with selfender method. The sender method is going to return the widget that sent the signal. So if we select radio button

[10:14:46] one, our radio button will be radio button one. If it was five, then it's five in this case. Then we'll determine if our radio button is checked. Take our radio button. Use

[10:15:00] the is checked method. This will return a boolean true or false. If it's checked, if this returns true, then let's print the following. I'll use an

[10:15:12] fring. We will get the text of the radio button. radio button. Call the text

[10:15:19] method to return the text of the radio button. is selected. All right, then let's see if this works. Let's select Visa. Visa is

[10:15:32] selected, Mastercard is selected, gift card is selected, in store is selected, and online is selected. That's how to determine which radio button was selected, which one is the sender, which one sent the signal. All right, everybody. So that is an

[10:15:50] introduction to radio buttons in PIQT5. Why hello everybody. Today I got to explain lineedit widgets in PIQT5.

[10:16:00] Also known as text boxes in pretty much anything ever made ever. Why are they called lineedit widgets? I really don't know. Let's begin. From the module of QT

[10:16:10] widgets, we will import the following class of Q lineedit to create a text box. I mean a line edit widget. We are accessing our window of self. We will call this line ededit

[10:16:26] widget lineedit equals call the constructor of the class q lineedit. Then we will pass in self to add this lineedit widget to the window. Let's set the geometry but we do have a text box in which we can type in stuff.

[10:16:49] I have a method to initialize the user interface. Within this method, I will access self dot the line edit widget and set the geometry. Let's set it in the top left corner where X is 10, Y is 10. Set a

[10:17:09] width, 200 is good, and a height 40. That's not too bad. Now the text is really small. We can change that by

[10:17:20] applying a stylesheet. Access our window with self. Access our line edit widget. Then call

[10:17:28] the set stylesheet method. We can pass in some CSS like properties including a font size. Let's pick 25 pixels.

[10:17:44] And here's my new text box. We can read the text. Now, let's also change the font family. Font family, I will pick

[10:17:56] Ariel. This text box by itself, it really doesn't do anything. We need some way to get the text from the text box.

[10:18:05] Let's add a button. When we click on the button, we will get the text from the text box and do something with it because right now it doesn't do anything. We will need to import Q push button. Let's create one button

[10:18:23] self.button equals call the constructor of the class q push button. Let's say that this is a submit button. I will pass in a string of

[10:18:34] submit. And we are adding this button to our window. And we do need to set the geometry of the button. We're not using

[10:18:43] a layout manager right now. Access our window with self. Access our button that we have previously created in our constructor. Then call the set geometry

[10:18:57] method. We'll place our button where X is 210, Y is 10, the width will be 100, and the height will be 40. Not too bad. Let's change the font

[10:19:11] size of the button. I'll copy these two lines of code because I'm lazy. Instead of selecting our line edit widget, we will select our button. That's better. If I were to

[10:19:27] click on the button, it doesn't do anything. We'll set up the signal of clicked to connect to a method that will do something. Let's define a method of submit. We're submitting something.

[10:19:41] We're submitting the text within the text box. And for now, I'll write pass. We'll get back to this in a second. We're going to take our button

[10:19:51] self.button. We'll connect the signal of clicked clicked dot connect method we will connect the method of submit self.submit. So when we click on the

[10:20:06] button we will call this method. Let's print a test message. You clicked the button. Let's type in

[10:20:17] something. Press submit. And we get our test message. You clicked the

[10:20:24] button. Let's get the text from the text box, then do something with it. Let's create a local variable of text. Text equals. Now we have to get

[10:20:36] the text from our lineedit widget. self dot lineedit. That's the widget. To get the

[10:20:45] text, we can use the text method to return the text. Then let's print the text. I'll use an fstring. We'll say hello, add a

[10:20:56] placeholder, then display the text. So now after typing in something, why don't you type in your name, then press submit. We will display hello, your name. You could add some placeholder

[10:21:12] text, too. Let's do that here. Let's take self do.Eedit line edit

[10:21:20] widget set placeholder text and let's say enter your name. When I run this program, we have some placeholder text that says enter your name. This time I will type in Spongebob. Then press submit. Hello

[10:21:43] Spongebob. All right everybody. So those are lineedit widgets also commonly referred to as text boxes and well everybody those are lineedit widgets in piqt5. Hello everybody. So in today's

[10:21:57] video I'm going to explain setting stylesheets in piqt5. CSS means cascading stylesheets. If you're not familiar with CSS you can still follow along but knowing CSS is helpful. As a

[10:22:09] reminder, I do have a full free course on YouTube on HTML and CSS if you would like to learn more. Let's begin. For this demonstration, we will need the following imports. We will be designing

[10:22:21] some buttons. We will import Q push button. We'll be working with the layout manager. We will import Q

[10:22:29] widget. And for a horizontal layout manager, we will need QH box layout. So import these three from the module of QT widgets. Now in

[10:22:42] previous topics, we've set the geometry of our window. Since we're using a layout manager, we don't necessarily need that anymore. So I'm going to delete it. In the past, I have also

[10:22:53] created a method to initialize our user interface and we are calling that within the constructor of our main window. We will create three push button widgets. Self do.button Button one will

[10:23:04] be the first button equals take our Q push button class and call the constructor. We can add text to the button. We will pass that as an argument. Now since we're using a layout

[10:23:16] manager, we don't need to add this button to self our window. We don't need to do that. Let's create two more buttons. We'll have button two and

[10:23:26] button three. Button two will say number two. Button three will say number three.

[10:23:31] Now we'll create a layout manager. Under normal circumstances, we can't add a layout manager to our main window. With main window widgets, there's already a specified layout and format. We're going

[10:23:42] to add a layout manager to a central widget. And this widget will be added to the main window. Let's take care of that within our initialize user interface method. We will create a central

[10:23:56] widget equals call the constructor of Q widget. Then we will take self that means our window and set the central widget. Set central widget then pass in our central widget to set it. Then we

[10:24:16] will create a layout. We will call the constructor within the class of qhbox layout. Let's name this layout hbox for a horizontal box.

[10:24:28] Equals call the constructor within this class. We will take our layout of horizontal box. Then add the following widgets. Add widget self.button

[10:24:43] one. We'll do this with two and three. Then the last thing we need to do is take our central widget, call the set layout method, then pass in our layout manager. And now we should have those

[10:25:01] three buttons. They're all arranged horizontally. Now we're going to apply some CSS like styling using the method of set style sheet. Here's how. Rather

[10:25:12] than apply the CSS properties individually such as self.button button one set stylesheet. And in the past, we've passed in individual CSS properties.

[10:25:24] We're instead going to set the stylesheet of our window self. We have a lot to write. Instead of double quotes, we're going to use triple quotes. Triple quotes are used to write

[10:25:39] very long strings in a more organized way. All of the CSS properties that we're going to write are going to be within this set of triple quotes. So, let me give you a demonstration. We

[10:25:49] could individually apply CSS like properties to each of these widgets, but we could select an entire class of widgets, too. Let's select the class of Q push button, then add a set of curly braces. The following CSS properties will apply to all Q push button widgets.

[10:26:10] So currently this is what we have. We'll increase the font size for every push button. So we will add the following property of font size. Then set it to be 40 pixels each.

[10:26:23] Be sure to end each CSS property with a semicolon. So the font size is now 40 for every button. Let's set the font. Font family.

[10:26:36] I will pick Ariel. Let's add some padding. We can add some space around the text and the button itself. So with padding, if I was to set

[10:26:50] this to 75 pixels, we would have 75 pixels worth of space between the text and the border of the button. I would like to change the dimensions of the padding. So, let's apply 15 pixels to the top and bottom of the button and 75 to the sides. That's

[10:27:12] better. Margin is the space around a button. Let's set the margin to be 25 pixels. Now, the buttons are more spread

[10:27:21] out. If this was 250, they would really be spread out. That's margin. It's the

[10:27:28] space around a widget. Let's set that back to 25. I'm going to change the border.

[10:27:38] Border 3 pixels solid. This would change the border of the buttons. We now have a black border that's 3 pixels in width. If you would

[10:27:50] like to round the corners, we can use border radius. I will set that to be 15 pixels. With all the buttons, the corners are now rounded.

[10:28:00] Within our set stylesheet method, we're applying all of these CSS like properties to every push button. Now, what if you would like to apply CSS properties to only one widget rather than all of them? Here's how. With each

[10:28:15] of our widgets, buttons 1, 2, and three, we need to set an object name. Let's do that before we call the set stylesheet method. We will take our buttons self.button button

[10:28:27] one. Call the set object name method. Then pass in a name for this widget.

[10:28:36] We'll keep the name the same as button one. So let's do this with button two and button three, button two, button three. Within the context of set stylesheet, we will refer to these widgets by their object name. Buttons 1,

[10:28:54] 2, and three. And now we can select them individually. Let's say that with button one, I would like the background color to be red. We're going to access our

[10:29:05] class of Q push button. Follow this with a pound sign. I like to call it a hashtag. Then we need the object name

[10:29:14] button one. Button one refers to the widget of button one. Again, I kept the name the same. Then we need a set of

[10:29:21] curly braces. Between the set of curly braces, we can list one or many different CSS properties. Let's change the background color. I will set it to be

[10:29:34] red. And now the background color of only that button is red and not all of them. If I was to set the background color within the class, well then all of them would be red. Okay. Okay, so with button two,

[10:29:50] I'll just copy what we have and paste it. We are selecting the ID of button two. Let's set the background color to be green. So then the background color is

[10:30:02] now green and button three. Button three will be blue. If you would like a greater variety of colors, I recommend looking up a color picker, you can just Google color picker. So, if I would like a very

[10:30:23] specific shade of red, I can pick that. Let's go with that. There are a few options provided to you. You can use hex

[10:30:35] values. Now, we have a very specific shade of red. You can use RGB RGB enclose it within a set of parenthesis and then paste those numbers or my favorite which is HSL. HSL

[10:30:55] means hue, saturation and lightness. We will enclose our values within HSL. If you copy these values directly from Google, you would have to remove this degree symbol. I like HSL because I can also

[10:31:13] control the saturation and the lightness pretty easily. Okay, let's pick a very specific shade of green. That's good. I would say I'll use

[10:31:22] the HSL values. HSL. Remove the degree symbol. And now we have a very specific

[10:31:33] shade of green and blue. That's good. I would say that's not too bad. If you're

[10:31:52] already familiar with CSS, we can apply pseudo classes such as when we hover over one of the buttons. Here's how. Let's copy these three blocks, then paste them again. We can add CSS properties. When

[10:32:09] we hover over something, we have to use the hover pseudo class. After the ID of each of our buttons, we will add colon hover. We can apply the following CSS properties when we hover over the buttons. All I'm going to do is up the

[10:32:26] lightness, let's say by 20% each. Then when we hover over one of the buttons, the lightness is going to change. We apply the new CSS properties. All right, everybody. So

[10:32:41] that is a more in-depth explanation of the set stylesheet method in PIQT5. All right, everybody. In today's video, we're going to build a digital clock widget using Python's PIQT5 library. At the top of our Python file,

[10:32:57] we will need the following imports. Import CIS. CIS means system. This

[10:33:02] module provides variables used and maintained by the Python interpreter. We would also need widgets. Widgets are the building blocks of a guey application.

[10:33:12] From the package of pi QT5, we need to access the module of QT widgets. Import the following. Q application Q widget. This is a generic

[10:33:29] widget. We'll turn our digital clock into its own widget. And Q label to work with labels. We will be using a layout

[10:33:38] manager, more specifically QV box layout. There's another import we'll need too from the package of piqt5. Access the module of QT core. The

[10:33:53] QT core module, it provides functionality not related to GUI components. This is where we'll get a timer to keep track of the time. From this module, we will import Q timer, Q time, and QT. QT is for

[10:34:10] alignment. We will create a class of digital clock. Instead of inheriting from the main window widget, we will inherit from the base class of Q widget.

[10:34:22] Q widget is a base class to create our own widgets. Our digital clock will be a widget. We will need a constructor. So,

[10:34:29] let's define that. define init pass in self. If there are any arguments to send to the parent, we will call the constructor of the parent the superass super call the init method. At the end of the constructor,

[10:34:46] what I like to do is call a method of initialize UI. Init UI. This will be a separate method. Define init UI. There

[10:34:59] are no parameters besides self. And for now, I'll write pass. It's within this method that we will be designing the layout of the digital clock. Within the

[10:35:07] constructor, that's where we will be constructing all of the different entities for the clock. At the end of my Python file, I will add the following statement. If dunder name is equal to a string of dunder main. This statement will be true if we

[10:35:25] are running this program directly. To create an application, we will create an app object equals call the constructor within the class Q application. As an argument to the constructor, we will pass in the following argument. Access the module of

[10:35:41] CIS argv, which means arguments. This would apply if we're running from command prompt or terminal, but we won't be doing that in this video, but it's nice just to set it up in case we do in the future. Now we are going to create a clock object clock equals we will call the constructor of our digital clock class.

[10:36:03] There are no arguments. Now the window doesn't appear. That's because we have to use the show method of our clock.

[10:36:10] Take our clock call the show method. Now it's only going to appear for a brief second just momentarily. I don't know if you saw that.

[10:36:21] To ensure a clean and proper exit of our application, we need to call the following method. Access our module of CIS. Call the exit method. Then pass in

[10:36:31] the following. We will take our app object. Then call the following method exec underscore and then a set of parenthesis. It's a method. It's the

[10:36:44] execute method. It starts the main event loop of the application. It also handles events such as key presses, mouse clicks, or other user interactions. So

[10:36:54] then we should have a window that stays in place until we exit. Okay, now we have the base functionality all set up. We have a class of digital clock that inherits from the Q widget base class.

[10:37:07] We're not going to be using main window in this video. Within the constructor of my digital clock, I will create a label self dot time label. This will be a label that displays the time. We will

[10:37:20] call the constructor within the class q label. Then be sure to pass in self. We will be adding this label directly to our widget of clock. We will need a

[10:37:31] timer self.time timer equals call the constructor of q timer. then pass in self. We are adding the timer to the

[10:37:42] clock. Now with designing the layout of our clock, I'll handle that within the initialize user interface method. We're going to set a title for the window. self set window title

[10:37:56] method. Pass in a string that will be used for the title of the window. Let's say digital clock. Then our window

[10:38:05] should say digital clock. Let's set the geometry of the window. self set geometry. The first two arguments are

[10:38:16] going to be for the placement of the window. Where will it appear within your screen? So I'll pick something approximately in the middle for me, but feel free to change these values. Then

[10:38:27] we need a width for the window. Let's say 300. And a height 100 for the height. So my window should appear

[10:38:35] approximately in the middle of my screen. The base width is 300. The base height is 100. Now we're going to need a

[10:38:42] layout manager. I will name this layout manager VBOX for a vertical box. vbox equals call the constructor within the class QVbox. This will arrange all of our

[10:38:56] widgets vertically. But we only have one widget, a time label. So we will take our layout manager of vbox add widget that's a method we will pass in selftime label as an argument we're adding our label to this layout manager of vbox then to set the layout we will take self that applies to our clock call the set layout method then pass in our layout manager of vbox. So currently if I run this we

[10:39:30] don't see anything. Temporarily within our label I will add some text just as a placeholder so we can see what we're working with. Let's say 12:00. So then we should see something

[10:39:45] at least although the font is kind of small. We will be getting rid of this later. We just want to be sure that we can see everything. All right. So after our

[10:39:56] layout, I would like the label to be center aligned horizontally. Here's how we can set that up. We will take our label self.time label. Call the set alignment

[10:40:13] method. Access the class of Qot. Access align center. This should center align our

[10:40:25] time. Now let's work on the font. I can barely read it. We will take our label

[10:40:34] selftime label set style sheet. We can pass in multiple CSS like properties. Let's set the font size. I'll set it to be 150

[10:40:49] pixels. Now we can read it. You could pick a font, but we're going to change that at the end of this video.

[10:40:56] We'll import a custom font. But temporarily, let's say font family Ariel. You could change the color, too. So, if I set the color to be

[10:41:13] green, then the font color is going to be green, but I would like a very specific shade of green. You could always Google a color picker, then pick a very specific color. Uh, let's go with that. Something that's

[10:41:29] bright green. You can copy the hex value, RGB, or HSL. HSL means hue, saturation, and lightness. I'll use HSL

[10:41:41] values. For the color, we will type HSL. Add a set of parenthesis. Then paste

[10:41:47] those values. But there is a degree symbol. You do have to get rid of that.

[10:41:51] Now the font color is going to be bright green. Let's change the background color. Here's how. We will take self

[10:41:59] that applies to our clock. Then call the set stylesheet method. Pass in a background color. We will set the background color

[10:42:10] property to be black. I think that looks pretty good, but it doesn't quite do anything quite yet. That's the next step. Let's create

[10:42:21] a method to update time. No arguments besides self. I will create a local variable of current time equals. Now to

[10:42:32] get the current time, we can access the class of Q time. Q time dot call the method of current time. We will need to convert it to a string. We will method chain the tworing

[10:42:49] method. Within the two-string method, we will design the layout of the time. So, I would like hours first. I will type

[10:42:57] two h's colon minutes. That's 2 m's colon 2 s's. To set the text of the label, we will take selftime label. Call the set text method. Then

[10:43:11] pass in our current time. So if I run this currently, we still have our placeholder time. Let's update it with the current time. We can get rid

[10:43:22] of our placeholder text of 12. We can delete it. After we set the font, let's call the method of update time. self.update

[10:43:36] time. Now we should display the current time. So me, I'm recording this video at 7:44 in the morning.

[10:43:43] If you would like to add AM or PM after your time, here's how. After our string format specifiers, we will add capital A. A means anteridium and P means post meridian. So then we should display A.M.

[10:44:00] or P.M. depending on when you're coding this. Currently, the time for me is 7:45

[10:44:06] a.m. To get the clock to update every second, we need to connect our timer widget to a slot of update time. We will

[10:44:15] take our timer self.time timer. This isn't the time label, it's the timer to keep track of the time. During a signal

[10:44:23] of time out, we will connect the following slot of self.update time self.update time. With our timer, we

[10:44:36] need to trigger a timeout signal every 1,00 milliseconds. Every second, that is. To handle that, we will take our timer self.time timer, call the start

[10:44:47] method, then pass in 1,00 for 1,00 milliseconds. So then when we run this program, our clock should update every second and display the new current time. As an added bonus, if you would like to download a custom font, here's how.

[10:45:06] Using Google or another search engine, I would recommend looking up a font of your choosing. So, one font that I like is DS Digital. What we need is a TTF file, meaning true type font. I'll just

[10:45:20] pick this first link. So, these fonts are pretty good. So, I'm going to download them.

[10:45:28] I'll pick this specific font, DS Digit. And again, the file extension is TTF. So once you have your font, move it to your project folder. So for

[10:45:39] convenience, we have that TTF file right next to our main Python file. Okay. To work with specific fonts, we will need the following. Import from piqt5.

[10:45:53] QT gui import Q font as well as Q font data base. Since we're going to use our own custom font, we can delete that from the set stylesheet method of our time label. So let's set the font right here. We

[10:46:17] will assign a local variable of font id equals q font database. Q font database is a class for managing and querying fonts available to the application. To add a custom font, we will call the following method within it. Add

[10:46:38] application font. Within the set of quotes, we're going to pass in a file path. This can be a relative file path or an absolute file path. This TTF file is right next

[10:46:50] to my main Python file. I only need the file name. My font file is named DS digit and get the file extension of TTF. We will create a local variable of

[10:47:04] font family. We will retrieve the name of the font family from this ID. Again we will access Q font database dot call the application font families method. So

[10:47:23] this method returns a list of font names. We will pass in our font ID. But there's another step. We're

[10:47:32] going to use the index of operator and get the index of zero. This will retrieve the first element of the font family. That's because we're working with a list. We will need just the first

[10:47:43] element at index zero. Now we'll have a font family to work with. Now to set the font, we will create a local variable of my font equals call the class. Call the

[10:47:57] constructor within the class Q font. Pass in the following arguments. our font family, that's the first argument, and then a font size, let's say 150. To set the font, we will take

[10:48:13] our time label, self dot time label, call the set font method, then pass in my font, our custom font. So then we should have our custom font, that digital font that we've downloaded. All right, everybody. So

[10:48:33] that is how to create a digital clock widget using PIQT5. Hey yeah everybody. So in today's video we're going to create this stopwatch program using Python's PIQT5 library. Once that's out of the way you

[10:48:46] will need the following imports. Import cis. CIS means system.

[10:48:51] It handles system variables for your Python interpreter. We will need the following widgets from piqt5. Access the module of QT widgets.

[10:49:04] Widgets are the building blocks of a PIQT5 application. We will import the following widgets. Q application.

[10:49:14] Q widget. Q label. Q push button. QV box

[10:49:26] layout. and QH box layout. Let me put these on a new line just so we can read everything from the package of PIQT5. Access QT core. We will

[10:49:40] import Q timer. Our timer will emit a signal after a given interval, which is what we need for a stopwatch. Q time to keep track of the time and QT for alignment. Let's do a test run to be

[10:49:55] sure that there's no errors. Looks like L and label should be capital. There we go. No errors. Once

[10:50:04] you have the following imports, we will construct a class, a class of stopwatch, which will inherit from the base class of Q widget. Our stopwatch will be a widget. We will need a constructor. We'll define that dunder

[10:50:22] init. No arguments besides self. If we have arguments to pass to the parent of Q widget, we will call the superass the parent. Call the constructor of the

[10:50:33] parent. No arguments currently. Now if we are running this file directly, we'll use an if statement to verify that if dunder name is equal to a string of dunder main. If this is

[10:50:48] true, if we are running this file directly, then we will construct a stopwatch. We will create an app object. Call the constructor within the Q application class. Pass in the following

[10:51:01] access cis our system access argv which means arguments. This is if we're using command line arguments, which we won't be using, but it's nice to futureroof our code just in case we do in the future. We will create a stopwatch object. Stopwatch equals call the

[10:51:22] constructor within our class of stopwatch. Our window is not going to show unless we call the show method. Take our stopwatch. Call the show

[10:51:32] method. Now our window is only going to show for a brief second. We need to ensure a clean exit.

[10:51:40] We can access cis. Call the exit method. pass in the following app then call the exec method. This method starts the main

[10:51:54] event loop and handles events. So then we should have a basic window which stays in place until we close it. We now have the main skeletal structure of a PIQT5 application set up.

[10:52:06] If you're one of the people that have jumped ahead up until this point, we have a class of stopwatch which inherits from the Q widget class. We've constructed a stopwatch object and we're showing it. So now we can begin designing our stopwatch. We will create

[10:52:22] a time object. self dot time equals call the constructor within the class of Q time. For arguments, we'll pass in the hours, minutes, seconds, and milliseconds all zero. We need a label for the

[10:52:39] stopwatch. self.time time label equals call the constructor of Q label. What would we like the text

[10:52:48] to say? I'll display some placeholder text. A bunch of zeros. 0 hours, minutes, seconds, and

[10:52:58] milliseconds. We will add this label to self, our stopwatch. We need a start button.

[10:53:05] Self.st Start button equals call the constructor within Q push button. What would we like the text of the button to say? Let's say start. We are adding this

[10:53:19] button to self. Our stopwatch. We need a stop button. Let's

[10:53:26] replace start with stop. Change the text from start to stop and reset. The name of this button will be the reset button. The text will be

[10:53:39] reset. We will need a timer to emit a signal at a given interval. self.time

[10:53:46] timer equals call the constructor within the class Q timer. Then pass in self. We're going to call a method of initialize UI self.init UI.

[10:54:02] But we still have to define this method. All right. Within our stopwatch class, we need the following methods. A method of init UI. This is

[10:54:13] where we'll be designing the user interface. I'll write pass for now as a placeholder. We need a method to start to start the stopwatch. That is a

[10:54:26] method to stop the stopwatch. a method to reset the stopwatch. We'll create a method to format our time. Format time. Besides

[10:54:41] self, there's one parameter. We have to pass in a time to format. We will be returning a string, a string representation of the current time and a method to update our display.

[10:54:55] Update display. Here are the six methods we'll need. Within our initialize user interface method, we will set the title of the window because right now it says Python. We will take self our stopwatch.

[10:55:14] Call the set window title method and we will pass in stopwatch. That should change the title of the window to stopwatch. We're going to use a vertical layout manager for the label and the buttons. We will create a layout manager

[10:55:34] named VBox. vbox equals call the constructor of QV box layout. We will take our layout manager and add the following widgets. self.time

[10:55:54] label. Then our start, stop and reset buttons, start button, stop button and reset button. We will take self set the layout pass in our vertical layout manager.

[10:56:23] So, we have all of our buttons. We have our widgets arranged in a column. We're going to take our time label and also center it horizontally. We will take our time

[10:56:34] label self.time label. Call the set alignment method. Access our class of QT.

[10:56:45] access the flag of align center. That's going to center align the time. It should be aligned both vertically and horizontally. Now with your buttons,

[10:56:58] they're arranged in a column. We could group them together horizontally. Here's how. We will create

[10:57:05] a horizontal layout manager of HBox. hbox equals call the constructor of QHBOX layout. Instead of adding these buttons directly to our vertical layout manager, let's cut them. Paste them underneath

[10:57:26] HBox. Replace Vbox with HBox. Then with our vertical layout manager Vbox, we will add our layout of Hbox. This group of buttons is arranged

[10:57:45] vertically with the time label. Now we'll be applying a stylesheet. Access self our stopwatch.

[10:57:54] Call the set style sheet method. We can pass in one extremely long string with a set of triple quotes. All of the CSS like properties we'll add will do so between the set of triple quotes. Let's

[10:58:09] select our buttons. Q push button. We are selecting an entire class. Within a set of curly braces,

[10:58:19] let's add the property a font size. The font size of all buttons will be 50 pixels. Let's customize our label. Select the

[10:58:30] class of Q label within a set of curly braces. Let's add the following properties. Font size will be 120. If you would like, we can add a

[10:58:44] background color too to the label. We can select a background color temporarily. I will select blue.

[10:58:54] But we can pick more specific shades of blue or another color. Here's how. You can look up a color picker and select a very specific color. You can

[10:59:05] use hex values, RGB, or HSL. I've already selected a color. I'm going to copy these HSL values. So, instead of a

[10:59:14] color name, we will select HSL. Then paste those values. If you have a degree symbol, you will need to remove that.

[10:59:24] And now we have a very specific shade of blue. I will also round the corners of our label. Add the property of border radius. I will set that to be 20

[10:59:37] pixels. This will round the corners between each button and label. We'll add some padding. We're going to use multiple

[10:59:45] selectors. We will select all push buttons and all labels. apply the following properties to each.

[10:59:55] I will add padding of 20 pixels around these widgets. And I will also make the font weight bold. Font weight will be bold. All right, I think that looks

[11:00:13] pretty good. Hey, this is Bro from the future. I am currently editing this video. If you would like, you can add a

[11:00:19] font family. One font that I think looks really good is Calibri. We'll apply that to all push buttons and Q labels. I really like this font. I think

[11:00:30] it fits a stopwatch, but it's up to you if you would like to change the font. I just thought I would mention that. Now, we just have to add some functionality because these buttons don't do anything. For each of our buttons, we

[11:00:43] have to connect a signal to a slot. We will take our start button self. Start button with the signal of clicked. We

[11:00:54] will connect the following slot. We will call the start method self.st start method. Let's do this with the stop

[11:01:03] button. Change start to stop clicked connect self.s stop method reset self.reset reset button called the

[11:01:17] reset method. At a given interval, we're going to update our display self.time timer during a signal of timeout. We will connect the following

[11:01:34] method. self.update display self.update

[11:01:40] display. Within our start method, we will take our timer self.time a timer.

[11:01:46] Call the start method. Pass in 10 for 10 milliseconds. We will set an interval for a timeout every 10 milliseconds. Within our stop method, we

[11:01:59] will take our timer and instead call the stop method. We'll get back to reset in just a moment. Let's work on the format time method.

[11:02:11] From our time that we pass in, we have to get the hours, minutes, seconds, and milliseconds. We will create some local variables. Hours equals access our time that we pass in. Call the hour method to

[11:02:24] return hours. We have variable minutes. Time dot call the minute method to return the minutes. We have a variable of seconds.

[11:02:35] seconds seconds equals take our time. Call the second method. Then for milliseconds access our time call the mc which means milliseconds and call it this is a method. I'm going to return a string an

[11:02:55] string to represent the time. We will add four placeholders hours and milliseconds. Each will be separated with a colon except for milliseconds which will be a dot a period. We will display the

[11:03:15] hours. I'll add some leading zeros. Two leading zeros. Let's do this for

[11:03:23] minutes. We're using a format specifier for two leading zeros as well. Seconds and milliseconds.

[11:03:39] Now we will work on the update display method. We have to get the time self dot time equals we will take our time but call the add milliseconds method mcs then pass in 10 for 10 milliseconds. We're going to take our time label self.time

[11:04:06] label and set the text of it. We will call our format time method. But we have to pass in a time.

[11:04:16] We will be passing in selftime. Let's see what we have currently. We can start the stopwatch and we can stop it.

[11:04:29] However, we're displaying three digits for the milliseconds. We can eliminate that within format time. When we get the milliseconds, we will use integer division. We will divide by 10. This

[11:04:44] will convert our milliseconds from three digits to two. We're basically dividing by 10. So, here's our stopwatch. currently

[11:04:52] we can start, we can stop, we can start again and we can stop again. Now we just need to reset. Here's how. Within the reset

[11:05:04] method, we will take our timer self.time timer use the stop method to stop. We will reassign our time call the constructor of Q time. We have to pass

[11:05:17] in hours, minutes, seconds, and milliseconds. They're all going to be zero. We're resetting our time. And then

[11:05:25] we'll reset the text again of our time label. self.time label. Call the set text

[11:05:32] method. When we set the text, we will first format it with the format time method. But we have to pass in a time.

[11:05:40] We will pass in selftime. And now we should be able to reset our stopwatch. We can start, we can stop, we can reset, start again, and stop again. All right, everybody. So, that is

[11:06:01] a cool stopwatch that you can make using Python. Hey, uh, what's going on everybody? So, in today's video, we're going to create a working weather app that fetches real-time weather data from an API. This is a massive project, so

[11:06:15] feel free to take your time. take several days or even weeks if you need to complete this. Heck, you can even add this project to your portfolio. Well,

[11:06:23] let's get started, everybody. All right, let's get started, everybody. This is a fairly useful API to get real-time weather data. The

[11:06:34] website is openweathermap.org. You will need your own API key, but signing up for an account is free. To create an account,

[11:06:42] we'll go to sign in, create an account, enter your information, and then sign in. Once you're signed in, to find your API key, go to this drop-own menu, go to my API keys, and you would just need to copy this API key. If the status is inactive, you'll need to toggle it to active, like so. Now, it may take several minutes for

[11:07:08] your API key to become active. Hopefully by the time of this project where we will need it, it'll be active. I would either leave up this window or copy this key and paste it somewhere. We will need the following

[11:07:21] imports. We will import CIS. CIS means system. It handles system variables for

[11:07:27] your Python interpreter. We will import the request module to make a request to an API. Then we'll need widgets. Widgets

[11:07:36] are the building blocks of a PIQT5 application. From the package of PIQT5, access the module of QT widgets. Import the following widgets. Q

[11:07:52] application, Q widget, Q label, Q lineedit, Q push button. Let me put some of these on a new line for readability. QV box layout. This is a vertical layout

[11:08:16] manager. To work with alignment, we'll need the following. From the package of piqt5, from the module of QT core, import the following class QT, which is used for alignment. So, these are the imports

[11:08:32] that you'll need. Just to be sure that I didn't misspell anything or get the capitalization wrong, I'm just going to do a test run. No problems. Processed

[11:08:42] finished with exit code zero. Sometimes I make one of these characters lowercase and then it doesn't work. Okay, we have our imports. We will

[11:08:53] need to create a class of weather app. Weather app is going to inherit from the parent of Q widget. We will need a constructor. So we'll

[11:09:06] define that under init arguments besides self. In case we have arguments to send to the parent, we will call the parent with super meaning the superass then call the constructor. But currently we don't have any arguments. If we are running our main

[11:09:25] Python file directly, we can verify that with an if statement. If dunder name is equal to a string of dunder main. If we are running this file directly then we will create a weather app object. Otherwise we won't. If this

[11:09:45] statement is true we will do the following. We will create an app object app equals call the constructor within our Q application class. But we will pass in the following. Access the module

[11:09:59] of CIS then access a argv which means arguments. If we have command line arguments to send to our application, this is how we would take care of that. But we're not going to be using command line arguments in this video, but it's nice to futureroof our code just in case we do. We will construct a weather app

[11:10:19] object. Weather app equals call the constructor of our weather app class. Now this window isn't going to show. We

[11:10:27] have to call the show method of our weather app. Weather app show. And now it's going to show for a brief second. We need to ensure a clean exit.

[11:10:39] Access cis. Call the exit method. Within this method, we will pass in the following.

[11:10:46] Take our app. Call the execute method which is execore. It is a method. So we have to

[11:10:54] call it. This method handles events within our application such as closing the window. So now our window should stay in place until we close it. If you're one of the people that

[11:11:08] have jumped ahead, we have created a class of weather app which inherits from the parent of Q widget. We've constructed a weather app object and we're showing it. If you've made some PIQT5 projects in the past, you would just have to change some of these around. Within the constructor of our

[11:11:27] class weather app, we will declare the different widgets that belong to our weather app object. We will create a label that prompts the user to enter in a city. We will name this city label equals this is a Q label widget. We can

[11:11:43] set the initial text of the label. Let's say enter city name. Then the second argument is going to be self. We are adding this label to

[11:11:55] our weather app object. Here's what we have currently. We still have to do some CSS formatting, but we'll take care of that soon. We will need a line edit widget,

[11:12:08] basically a text box. We will name it city input. The widget is line edit. No parameters besides

[11:12:24] self. Here is our line edit widget. We're not currently using a layout manager. These widgets are going to

[11:12:32] overlap. We need a button self.get weather button.

[11:12:40] This is a Q push button. The text on this button will be get weather. We are adding this to self, our weather app object. Here's our

[11:12:54] button. When we click on this button, we'll make a request to an API. For the next following widgets, we're going to add some placeholders just so that we can see what we're doing when we apply CSS styling. We need a temperature label to

[11:13:08] display the temperature. temperature label equals a Q label temporarily for the label. Let's say that the temperature is 70° F or pick something else in Celsius. So to

[11:13:26] add a degree symbol, if you're using Windows, make sure num lock is on, hold alt, then on the numpad, type 0176. I will pick 70° F. And then we will add this to self. Again, we're just using this

[11:13:41] temperature as a placeholder. We'll delete it when we do a test run. If you would like to include an emoji or some other image, we can create a label for that. I will name this emoji

[11:13:55] label equals a Q label. I will add an emoji of a sun as a placeholder. Again, we're going to delete this when we do a test run.

[11:14:07] We are adding this to self again. Everything is overlapping. That is fine. And we need a description of the

[11:14:19] weather. Description label equals a Q label as a placeholder. Let's say that it's sunny and we are adding this label to self. Okay. Here are all the widgets.

[11:14:36] They're all overlapping. So, we need to fix that. All right, moving on everybody.

[11:14:44] So, now we have to design the layout of our web app. Right now, all of our widgets are gravitating to the top left corner. So, I will define a method to initialize our user interface. At the end of this

[11:15:02] constructor, we will call this method self.initialize initialize UI, then call it. Once we've constructed our widgets, we'll format them and design the layout. So, we are now within our

[11:15:17] initialize user interface method. First, let's set the title of our window. Self set window title. Let's say that the title is

[11:15:30] weather app. So that should change, which it does. We're going to use a vertical layout manager to handle all the widgets. Let's name the layout manager

[11:15:44] VBox equals call the constructor of the class QVox layout. We're going to take our layout manager of VBox. Then add a widget. We will start with the city

[11:15:58] label. That's first. We will pass in self.c city

[11:16:04] label. And we'll do this with the other widgets too. We have city input, get weather button, temperature label, emoji label, and then a description label.

[11:16:36] take self our weather app set the layout. We will pass in the layout manager of VBox. And here's what we have currently. All the widgets are arranged

[11:16:51] in a column. Now we just have to center align them horizontally. Here's how. We will take self.c city

[11:17:02] label. Call the set alignment method. Access the class of QT. Access

[11:17:11] the flag of align center. We're going to align all of our widgets in the center except for our weather button. Currently, our button expands to take up the width of the window. So, we don't need to

[11:17:26] horizontally align that. So we have five widgets to align. We have city label, city input, temperature label, emoji label, and description label. All of the widgets are going to

[11:17:42] be arranged in a column horizontally. Now we just have to apply some CSS styling because right now it's kind of ugly. We will apply styles based on an object name, but we have to set that object name. So let's start with our

[11:17:58] city label self. city label. Call the set object name method. Pass in a unique ID for this

[11:18:11] widget. I will name it city label. I'll keep it the same. Okay. We have to do

[11:18:17] this with the other widgets too. We have a total of six. We have city label, city input. We have the get weather

[11:18:33] button, temperature label, emoji label, and description label. Then we're going to set a stylesheet. Take self, our weather app.

[11:18:48] Apply a stylesheet with set style sheet. We have a lot of properties to write. I will do so within a set of triple quotes just to keep everything more organized. We can apply CSS styles based

[11:19:03] on a class. So the class is going to be Q label. Within a set of curly braces, we can list multiple CSS properties. I

[11:19:12] will set the font family to be Calibri. as well as all push buttons. Q push button. So here's the font, although

[11:19:26] it's still kind of small. Let's select our ID of city label. It's good practice to preede this ID with the name of the class. So Q label pound sign the

[11:19:39] ID. We preede the ID with the name of the class. Just so we're only applying these CSS properties to any ID that's a city label that falls within the class of Q label. Let's set the font size to be 40

[11:19:55] pixels. Let's set the font size to be 40 pixels. That's better. I'll set the font style to be

[11:20:05] itallic. Font style itallic. That's pretty good.

[11:20:14] Let's select the ID of city input. This is a line edit widget. Q lineedit pound the ID of city input within a set of curly braces. Let's set the font size to be 40

[11:20:32] pixels. We will select our push button which is named get weather button. The class is Q push button pound. The ID of get weather

[11:20:50] button within a set of curly braces. We will apply the following. Let's set the font size to be 30 pixels. And let's make it bold. font

[11:21:04] weight bold. Let's select our temperature label. The ID is temperature label and this is a Q label pound temperature label. We will increase the font

[11:21:25] size. Font size 75 pixels. better. Let's work on our emoji.

[11:21:39] Next, we will select the ID of emoji label. The class is Q label. The ID is emoji label. We'll set the font size first.

[11:21:53] Font size 100 pixels. I would like a large image. To display emojis properly, we're going to use a very specific font. We're

[11:22:04] going to set the font family to be, now I don't know if I'm saying this right, segi emoji. I probably pronounced this word wrong, but I don't care. So then our emoji should display correctly using this font. It's

[11:22:27] colorful. Then we have the description label of the weather. That is the last widget description label. The class is Q

[11:22:35] label. The ID is description label. Let's take the font size and set it to be 50 pixels. All right. So this is what our

[11:22:48] weather app is going to look like. We have the city label, a text box to enter in a city, the get weather button, the temperature label, an emoji label, and a description of the weather currently. Now, we just have to add some functionality because currently this doesn't do anything. All right, so now we just have

[11:23:10] to add some functionality to our weather app. Temporarily, I'm going to collapse our initialize user interface method. We will define a few extra methods. Let's

[11:23:20] declare a method of get weather. No parameters besides self. I'll write pass for now as a placeholder. We will need a method to

[11:23:32] display any errors. Display error. There's going to be one argument besides self, a message. We will pass in

[11:23:41] an error message if there is one. and a method to display weather. That's if there's no errors. We will

[11:23:52] need some data, our weather data. So, be sure that you write these three methods. Back within our initialize user interface method at the bottom, we have to connect a signal to a slot. When we click on the button with

[11:24:12] the signal of clicked, we will connect a slot of get weather. We will access self. Take our get weather button with a signal of clicked. We will

[11:24:28] connect a slot of self.get weather. And I will print a test message just to be sure that it's working.

[11:24:38] You get the weather. So I press the button and we will display you get the weather. We can get rid of our placeholder text for the temperature, our emoji, and the weather description. So we can delete these

[11:24:58] strings, but be sure to keep self. Scrolling down to our get weather method. When we click the button, we're going to create a few local variables.

[11:25:14] The first is going to be our API key equals. This will be a string. Back to the open weather API, you will copy your API key and make sure that it's active. You can use the toggle

[11:25:30] button to make it inactive and active. So, make sure that it's active. Paste your API key within a string.

[11:25:40] Please use your own. It still may take several minutes for your key to be active. Just keep that in mind. We will need to get the city that

[11:25:49] we're looking up. So let's say we type in Miami. I have to get the text from this widget.

[11:25:57] This line ededit widget. We will create a local variable of city. city equals access our line edit widget. It had a

[11:26:07] name of city input. So self.c city input to get the text we will call the text method. We have the API key and the

[11:26:20] city. Now we will create a URL. This will be an fstring using the request module. we

[11:26:28] will pass in a URL to make a request to. So, back to our open weather API. To get the URL for a city, we have to go to the tab of API, scroll down to current weather data, and there's going to be some API documentation. To the right, we have a

[11:26:48] link for built-in API request by city name. We will copy this URL and paste it within our F string. There's two changes we're going to make.

[11:27:01] We will replace city name with city, the name of that variable, and API space key with API_key. It doesn't matter what you name these. Just make sure they're consistent with your variables. When we make an API request,

[11:27:19] we will be returned with a response object. response equals access our module of requests call the get method then pass in our URL with our response object we have to convert it to a JSON format we will be returned with an object we will name this object data it's going to be readable to us data equals take our response object and use the JSON method to convert it to a JSON format at. So, let's print our data to see what we're working with. Let's say I look up the city of

[11:28:04] Miami. So, we have one gigantic object. This is our weather data. We

[11:28:11] have coordinates such as longitude and latitude, a weather description. Currently in Miami, there's broken clouds. There's an ID of the weather.

[11:28:24] This is the temperature, but it's in Kelvin. If we scroll all the way to the end, we are looking for an HTTP status code, which is named Cood, short for code. 200 means that the response was successful. Depending on what this

[11:28:41] number is, we will display one of the few error messages. If our status code is 404, that means the city wasn't found. And there's many others. So 200

[11:28:52] means that the request was successful. So let's write the following. If our data object at key of COD, if this is equal to 200, if the request was successful, then we will call the display weather method self.

[11:29:13] display weather, but we do have to pass in our data. Now, temporarily, I'm just going to print our weather data. We'll do some more complex stuff later, but I just want to be sure that everything is working. So, let's look up Los

[11:29:34] Angeles. So, here's the weather in Los Angeles. There is currently broken clouds. And again, the status code is

[11:29:44] 200. The request was successful. I'll write an else statement for now. We will print our data. What if

[11:29:54] we can't find a city? For example, I will look up the city blah blah blah and get the weather. So, here's our weather data. We

[11:30:06] have an error code of 404 and a message of city not found. Let's do some exception handling in case we run into one of these status codes that's not 200. We can get rid of our else statement. What we'll do is enclose all

[11:30:23] of our dangerous code. That means any code that might cause an exception within a try block. We will try all of this code and handle any exceptions with an accept block.

[11:30:37] There's two types of exceptions we're looking for. The first is an HTTP error. HTTP error is an exception raised by the request module when an HTTP request returns a status code that's 400 or 500. However, this exception is found

[11:30:59] within the request module that we've imported. So, we can't simply just say accept HTTP error. We first have to access the request module then access exceptions. Then we can list the

[11:31:17] specific exception of HTTP error. will encounter this exception if the status code is between 400 and 500. And for now, I'll write pass. So there's one more step within

[11:31:33] our try block. If we're going to handle any HTTP errors, we have to raise an exception within our try block because our try block by itself normally doesn't catch these. We will take our response object and call the raise for status method. This method will raise an

[11:31:57] exception if there's any HTTP errors. Normally our try block doesn't do that. So we have to manually type this. There's another type of exception

[11:32:08] we'll catch and that's the request exception. We'll add another block for accept request exception. This is found within the request module.

[11:32:24] Requests exceptions. Request exception. With a request exception, this can be due to network problems, invalid URLs, exceptions of that nature.

[11:32:37] In case we run into one of those types of exceptions, we will execute this block of code. But for now, I'll write pass. We'll get back to it later. Going back to our accept block

[11:32:48] where we handle any HTTP errors. Let's use a match case statement, we need to get the status code of our response. I'll print that temporarily.

[11:32:59] Let's print our response objects status code and see what it is. Again, let's make up a city. Get the weather. We have a status code of 404.

[11:33:13] That means the city wasn't found. Depending on what this number is, the status code, we'll use a match case statement. So we will match our response objects status code. The first case will be

[11:33:35] 400. That means there's a bad request. So let's print the following. Bad request. I'll add a new

[11:33:46] line character. Please check your input. We'll create a total of I believe eight cases. We'll copy what we

[11:34:01] have. So we have 400 401 403 404. That one we're familiar with.

[11:34:12] 500 502 503 504. So for case 401, that means we're unauthorized. Maybe our API key isn't active yet. So let's say

[11:34:36] unauthorized. Invalid API key. for 403 that means access is denied. It's

[11:34:48] forbidden. So let's print forbidden. Access is denied. 404 is for something that's not

[11:35:01] found. Not found. City not found.

[11:35:10] 500 is for an internal server error. Internal server error. Please try again later. 502 is for a bad

[11:35:25] gateway. Bad gateway. Invalid response from the server.

[11:35:38] 503 is for service unavailable. Service unavailable. Server is down. Then 504 is for a gateway

[11:35:55] timeout. Gateway time out. No response from the server.

[11:36:08] In case there's any unexpected error, we can add a wild card of an underscore with our HTTP error. Let's give it a name as HTTP error. And then we'll just print it. In

[11:36:25] case there are no matching cases, let's print the following. HTTP error occurred. I'll add a new line. Let's convert this to an

[11:36:39] string. Add a placeholder. And then I will print our HTTP error. All right, let's do a test

[11:36:48] run. So, in case we can't find our city, we should encounter a 404 error. Not found. City not found.

[11:36:57] Eventually, we will display this message within our app, but we know that it works. What if my API key is invalid? So, I will take my API key, set it to be inactive, but it might take a few minutes to take effect. The status code of our response

[11:37:17] object should be 401. So, this time I'm going to look up a city. I have an invalid API key and I get that error message of unauthorized invalid API key. All right, everybody. So, I am on

[11:37:33] day three of working on and recording this topic. Over the course of the day, I thought of one change that I can make. We're going to add a few extra accept blocks. So, we will accept access

[11:37:45] requests access exceptions. We will handle any connection error exceptions. as well as any timeout exceptions and any redirects. Too many

[11:38:15] redirects. So if we run into a connection error, let's say that our internet gets disconnected. Well, we can print something. So let's print the

[11:38:24] following. Let's print connection error. I'll add a new line character. Check your internet

[11:38:36] connection. If we encounter a timeout, then we will print the following. We have a timeout error.

[11:38:48] the request timed out. If we have a too many redirects error, that M should be capital, by the way. Let's state too many redirects. Check the

[11:39:12] URL. And if there's anything else we don't anticipate, I'll give this exception a name of as wreck error. And then we'll just print it.

[11:39:25] This is a last resort. I'll use an f string request error. I'll add a new line. I'll add a

[11:39:35] placeholder. Then display our request error. So I'm actually going to turn off my internet. I'll see if I can get a

[11:39:42] connection error intentionally. So, my internet is currently off. I will attempt to look up a city, get the weather, and we get a connection error. Check your internet

[11:39:56] connection. All right, my internet is connected again. Let's perform a test run. And we get the weather in Miami.

[11:40:08] Now what we're going to do is if we have an error, we'll display the error message within the app and not within our console. So we're going to replace print with a call to our display error method. Let me zoom out a little bit. So replace

[11:40:27] print with self dot display error. And we're passing in a message. So, let's replace those. One thing I forgot to add,

[11:40:46] although it's not necessary, I'm going to add a colon after each initial message. I think it'll look better. You don't have to do this, but I'm OCD about the appearance.

[11:41:00] If we encounter one of these exceptions, we'll pass along a message to our display error method and display it within the app. Let's take our temperature label self. Temperature label and set the text to be our message that we pass in. Let's do a test run.

[11:41:26] Let's look up a city that doesn't exist. Get the weather. So, we get that error message. Not found. City not found.

[11:41:34] While we're within this method, I'm going to change the font size just so that it's a little bit smaller. So, let's take our temperature label. Self dot temperature label. I'm

[11:41:49] just going to copy this because I'm lazy. I will call the set stylesheet method. and pass along a new property. Let's set

[11:41:59] the font size to 30 pixels. Let's look up North Pole. I don't think that's a city. Oh, I guess it is.

[11:42:15] Interesting. The North Pole is a city, I guess. Let's look up blah blah blah. Not found. City not found.

[11:42:25] Let's do another test. What if our API key is invalid? I'll just delete one of the digits. Let's look up Los

[11:42:36] Angeles. Unauthorized. Invalid API key. Let's change that back again. I

[11:42:43] will turn off my internet. Then look up Miami. Connection error. Check your

[11:42:51] internet connection. All right. So we know that our exception handling works. Okay. Now we're within the

[11:42:58] display weather method. We'll receive an object to represent our data. We have to get the temperature. But first I'm going to

[11:43:07] print our data. So let me zoom in a little bit. Let's look up Houston. Houston,

[11:43:16] Texas. I need the temperature. Within our data object, we are looking for a key of main and that is right here. Main

[11:43:26] contains a dictionary with key value pairs. Once we've accessed main, we have to access temp to get the temperature. And this temperature is in Kelvin. We'll

[11:43:36] have to convert it to Celsius or Fahrenheit. It's your choice. So, we need to extract this value. I will store it as a local

[11:43:45] variable. temperature let's say temperature K for Kelvin equals take our data object access the key of main that's right here then we have to go one level deeper and get the temperature the key is temp then give me the value at the key of temp and that should return the current temperature so to test it let's print it Let's print the temperature in Kelvin. So what is the weather in Houston, Texas? The temperature that

[11:44:25] is 309 Kelvin. Let's convert it to Celsius and Fahrenheit. Let's create temperature C if you want to use Celsius. If you would

[11:44:38] rather use Fahrenheit, you can skip this step. To convert from Kelvin to Celsius, we will take our temperature in Kelvin, subtract 273.15. Then for

[11:44:52] Fahrenheit, let's take temperature F for Fahrenheit equals, this is a little more complicated. Take our temperature in Kelvin times 9 / 5 subtract 459.67.

[11:45:10] 67. Okay. So, let's print the temperature in Celsius. Let's look up

[11:45:21] Houston. 36.46° C. Then in Fahrenheit, that would

[11:45:31] be 97.6° F. That's pretty hot. All right. So once we have our

[11:45:39] temperature, let's change the temperature label. self. Temperature label. I'll just copy this. Then we will

[11:45:47] set the text. I'll use an F string. Add a placeholder. I'll use

[11:45:54] Fahrenheit, but feel free to use Celsius. Then I will add a degree symbol. With Windows, make sure num lock is on. Hold alt. Then on your numpad,

[11:46:04] type 0176 for a degree symbol. Then F for Fahrenheit. Let's look up Miami. Get the weather. And here's the

[11:46:16] temperature. 94.964. Now, let's say I would like no

[11:46:21] digits after the decimal. I can add a format specifier after our temperature. I'll add a colon 0F to display no decimals. Let's try that again. I will

[11:46:34] look up Miami. Get the weather. The current temperature in Fahrenheit is 95° F. Now, here's one issue. Let's say we

[11:46:45] display an air, then display the weather. If we display an error, we're going to be changing the font size. So, let's look up blah blah blah.

[11:46:54] Got the weather, city not found. Then, let's look up Miami again. Got the weather. And the font size is a lot

[11:47:03] smaller. So, if we display the weather, let's reset the font size, we can really just copy this line. So, within the display weather method, let's set the font size back to 75, what it was originally. Let's try that

[11:47:23] again. Let's look up a city that doesn't exist. Get the weather. City not found.

[11:47:28] Then, we'll look up a city that does exist, like Miami, and get the weather. 95° F. Now, let's get a description of the weather. We'll display that at the

[11:47:39] bottom. In the center, we'll display a picture or an emoji, but we'll handle that last. Now, we need a description of the weather, like, is it sunny? Is it

[11:47:49] cloudy? Is it raining? So, after we calculate the temperature, so I'm going to print our data again. Let's look up Los Angeles.

[11:48:04] So currently it's 85° F. So for the weather description that is found at the key of weather. We're now within a list at index zero within our list. We'll look up the key of

[11:48:19] description which states clear sky. So we will create a local variable of weather description equals access our data at the key of weather. There's layers to this. We're

[11:48:43] then within a list and actually it's a list with only one item in it. So at the index of zero then at the key of description that's going to return this description of clear sky. So we will take our description label self.escription label. Let me just

[11:49:10] copy it. This one right here. Then we will set the text and then pass in our weather description. What is the weather

[11:49:25] description of Los Angeles? 86° F and there's a clear sky. Okay. Now, the last thing we're

[11:49:36] going to do is add an emoji. We'll add it right to the center between the temperature and the weather description. You don't necessarily have to, but I think it'll look cool and that's a good enough reason. So, let's create another method

[11:49:50] to handle that. We will define a method of get weather emoji or a picture if you would rather use a picture. We don't need self necessarily. We're going to need a

[11:50:04] weather ID. This method isn't going to rely on any class data or instance data. We could make it a static method. I'll add a

[11:50:15] decorator of static method. In summary, a static method, we haven't covered these for a little bit. They belong to a class but don't require any instance specific data or any other methods. They're used as more of a

[11:50:30] utility tool. We're going to be passing in a weather ID and returning an emoji. I'm going to show you where we can find that weather ID. I'll use a print

[11:50:43] statement. I will print our data. Let's look up Miami again. That's

[11:50:50] the first thing that came to mind. Now, at the key of weather, there's a key of ID, and the value is a three-digit number. I'll show you this chart.

[11:51:03] Depending on what this three-digit number is, that corresponds to a certain group of weather. So the 200 range is a thunderstorm. 300 is a drizzle. 500 is

[11:51:15] rain. 600 is snow. 700 is atmosphere, like if there's a tornado or there's a volcanic eruption. 800 exactly is a clear sky.

[11:51:29] Anything that's 801 or above refers to clouds. So this ID is 803. We have broken clouds. Depending on what this ID is, I

[11:51:39] would like to return a certain emoji based on the weather. So we need this ID. I'll delete our print statement. We

[11:51:47] no longer need it. Let's say before our weather description, we will create a local variable of weather ID equals access our data object. then access the key of weather. The value at weather is a list

[11:52:08] but this list only has one item in it. So we need the index of operator at zero and then we will access the key of ID. The key is ID. So our weather ID is

[11:52:23] going to be a number, a three-digit number. Okay everybody, we're near the end. So after setting the temperature, we're going to set the emoji label self.oji

[11:52:37] label and call the set text method. Within the set text method, we will call self.get weather emoji method. This will return a string, an

[11:52:51] emoji within a string. But we have to pass in our weather ID. It's that three-digit number. So now we

[11:53:00] are within our get weather emoji method. Depending on the range of that three-digit number, we will return one of a few emojis. We could use a match case statement. I think it's more

[11:53:11] complicated with the match case statement. We'll use else if statements for simplicity. So if our weather ID is greater than or equal to 200 and our weather ID is less than or equal to 232. Now we have two conditions here

[11:53:33] linked with the and logical operator. There is a shortcut to this and actually PyCharm is telling me that there is. We can simplify these expressions. Instead of two separate

[11:53:45] conditions, we can combine them into one. If 200 is less than or equal to our weather ID and our weather ID is less than or equal to 232, if this one combined condition is true, then we will return an emoji. So to add an emoji on Windows, you can hold down the window key and press semicolon.

[11:54:10] So 200 to 232, that's for a thunderstorm. Depending on the font style of your IDE, some of these emojis might not display properly. You can always just copy them from someplace else. I think that's better. It's more

[11:54:27] colorful. Then else if 300 is less than or equal to our weather ID and our weather ID is less than or equal to 321. This is for a partially cloudy sky. We will

[11:54:48] return some clouds. A partially cloudy sky. And again I don't like that one. So

[11:54:54] let's use this one instead. Else if 500 is less than or equal to our weather ID which is less than or equal to 531 we will return rain eh that's better 600 to 622 Else if 600 is less than or equal to our weather ID which is less than or equal to 622 we will return snow. So 701 to 741 is mist or fog. Else

[11:55:52] if 701 is less than or equal to our weather ID which is less than or equal to 741. We will return some mist or fog. 762 specifically is for ash like from a volcano. So else if our weather

[11:56:19] id is directly equal to 762 we will return let's return a volcano 771 is for a squall that's a violent gust of wind else if our weather ID is directly equal to 771 one we will return. Let's return that. A violent gust of wind, a squall. 781 is for a

[11:56:58] tornado. Else if our weather ID is equal to 781, return a tornado. 800 exactly is for a clear sky. Else if our weather ID is equal to

[11:57:20] 800 return a sun a sun emoji. Else if 801 is less than or equal to our weather ID which is less than or equal to 804. We will return some clouds. Now, if there are no matches,

[11:57:52] let's return an empty string to not display anything. Okay, let's do a test run. Let's look up Miami. We get scattered clouds. It's

[11:58:06] 94°. Los Angeles. Got the weather. We have a

[11:58:12] clear sky and a sun. Now, there's one fix we need to make. Let's say that I make up a city again. Blah blah blah.

[11:58:22] Got the weather. We should clear our emoji label and the weather description. But we still get that error message.

[11:58:31] So after we display our error within the display error method, after we set the text of the temperature label, let's take the emoji label self.oji label and call the clear method to clear it. Then we have to do this with the description label self.escription

[11:58:55] label and call the clear method. Now we should be able to clear it when we get an error. Okay, let's look up Houston. Get

[11:59:07] the weather. Few clouds. 98°. Let's make up a city. Pizza City.

[11:59:15] Get the weather. Not found. City not found. And the emoji label and the

[11:59:20] weather description are cleared. Okay. What if I type in nothing? What happens? Let's get the

[11:59:27] weather. We have a bad request. Please check your input. That's if we have an HTTP status

[11:59:34] code of 400. We handled this exception. Bad request. All right, one last city. What

[11:59:42] about Paris? Let's get the weather. It is 68 degrees Fahrenheit and there's light rain. All right, everybody. So,

[11:59:51] that is a weather app that you can make using Python. Add it to your portfolio and thanks for watching.

