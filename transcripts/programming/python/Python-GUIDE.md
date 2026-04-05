# Python

Most Python code works. The gap between code that works and code that scales, tests cleanly, and reads well years later is almost entirely a matter of a few foundational habits — function design, type awareness, and consistent formatting — that most beginners never consciously develop.

This guide synthesizes core Python patterns from the ground up: how CPython actually executes code, how Python's type system behaves at its edges, and how to structure functions and loops that are composable rather than just functional. The goal is a foundation that holds up in production Django backends, data pipelines, and automation scripts.

---

## Return Values Over Side Effects

The most consequential design decision in Python function writing is one that Mosh Hamedani calls the "two types of functions" distinction, but which the broader Python community frames as the side-effect/pure-function divide. [^1]

A **Type 1 function** performs a task: it prints to console, writes to a file, sends an HTTP request. The work happens inside the function and nothing comes out. A **Type 2 function** calculates and returns a value — the caller decides what to do with that value. The difference sounds minor until you try to test the code, reuse it in a different context, or compose two functions together.

> **Key insight**: A function that returns a value can be used anywhere — passed to another function, stored in a variable, printed, logged, or sent over an API. A function that only prints can only print. [^1]

Consider a scraper utility that processes extracted markdown:

```python
# Type 1 — locked into one output
def process_bill(text):
    print(text.upper())

# Type 2 — composable
def process_bill(text):
    return text.upper()
```

The Type 2 version can be passed to `write_to_file()`, returned from a Django view, or fed into another transformation. The Type 1 version can only print. In practice, most functions that developers write as Type 1 should be Type 2.

- **Rule**: If a function produces a result, return it — don't print or write it inside the function [^1]
- **Exception**: Top-level orchestration functions (the ones that coordinate other functions) are typically Type 1 by design
- **Testing implication**: Pure functions (Type 2) have no external dependencies — they are trivially testable with `assert process_bill("hello") == "HELLO"`

**The takeaway**: Default to returning values; let the caller decide what to do with them.

---

## Python's Type System at the Edges

Python is dynamically typed and readable, but its truthiness rules contain several traps that cause subtle bugs, especially in conditional logic and form validation. [^1]

The **falsy values** in Python are: `0`, `""` (empty string), `None`, empty collections (`[]`, `{}`), and `False` itself. Every other value evaluates to `True` when tested in a boolean context. This rule is frequently misunderstood in one critical direction: a non-empty string is always truthy — even if its content represents falsehood. `bool("False")` returns `True`. `bool("0")` returns `True`. The string is non-empty, so it passes. [^1]

```python
# Common trap in form validation
is_active = request.POST.get("is_active")  # returns "False" (string)
if is_active:  # evaluates to True — the string is non-empty!
    activate_user()
```

This matters in Django form processing, API input validation, and any system that receives string representations of boolean values from external sources.

> **Key insight**: Truthiness is about the value's content and type, not its semantic meaning. `"False"` is truthy. `0` is falsy. Test the right thing. [^1]

Additional type-system patterns worth knowing:

- **Integer division** — `/` always returns a float; `//` returns an int: `7 / 2 = 3.5`, `7 // 2 = 3` [^1]
- **String comparison** uses Unicode code points — `"B" < "b"` because uppercase letters have lower Unicode values (`ord("B") = 66`, `ord("b") = 98`) [^1]
- **Chained comparisons** — Python supports `18 <= age < 65` as a single readable expression, equivalent to `age >= 18 and age < 65` [^1]
- **Boolean anti-pattern** — `if is_active == True:` is redundant; write `if is_active:` [^1]

**The takeaway**: Trust Python's truthiness rules for values you control; validate and convert string inputs from external sources before using them in boolean contexts.

---

## Automated Formatting with PEP 8

PEP 8 is Python's official style guide — a community document that defines spacing, indentation, naming conventions, and line length. The practical implication is not that developers need to memorize every rule, but that there is an automated tool — **autopep8** — that enforces the rules on save. [^1]

The setup is a one-time VS Code configuration:

1. Install the autopep8 extension (or via `pip install autopep8`)
2. Enable **"Editor: Format on Save"** in VS Code settings
3. All Python files are automatically reformatted to PEP 8 on every save

> **Key insight**: Code formatting is not a style preference — it is a team coordination mechanism. Consistent formatting eliminates entire categories of code review comments and makes diffs meaningful rather than noisy. [^1]

The key PEP 8 rules enforced by autopep8:

- **4 spaces** for indentation (never tabs)
- **Spaces around operators**: `x = 1` not `x=1`; `x += 3` not `x+=3`
- **No alignment of equal signs** across variable declarations
- **Two blank lines** between top-level function definitions
- **snake_case** for variable and function names; `UPPER_CASE` for constants

One naming convention PEP 8 enforces that matters more than it appears: **variable names should be descriptive**. `students_count` over `sc`. This is enforced by convention, not the linter, but the discipline compounds over a large codebase — `sc` in a 500-line Django view is a maintenance hazard. [^1]

**The takeaway**: Enable autopep8 on save once and never think about formatting again — use the freed attention for logic.

---

## String Manipulation Toolbox

Python strings are objects, and their built-in methods cover the large majority of text processing needs without importing anything. Understanding the full surface area prevents developers from writing manual loops for operations that are already built in. [^1]

Three string features that unlock compact, readable code:

**f-strings** (formatted string literals): prefix any string with `f` and embed any valid Python expression inside `{}`. Not just variables — full expressions including function calls, arithmetic, and method calls.

```python
name = "Mosh"
items = 5
# Variables
print(f"Hello, {name}")
# Expressions
print(f"Total: {items * 2.5:.2f}")
# Function calls
print(f"Upper: {name.upper()}")
```

**Slicing**: `string[start:stop:step]` — returns a substring without modifying the original. The end index is exclusive; negative indices count from the end; omitting start defaults to 0; omitting end defaults to the string's length. [^1]

```python
course = "Python Programming"
course[0:6]    # "Python"
course[-11:]   # "Programming"
course[::2]    # every second character
```

**Escape sequences**: `\n` (new line), `\\` (literal backslash), `\"` and `\'` (quotes inside matching delimiters). For multi-line strings without escape sequences, use triple quotes: `"""..."""`. [^1]

String methods return new strings — the original is never modified. Python strings are immutable. [^1]

**The takeaway**: Before writing a loop to process a string, check whether `.split()`, `.join()`, `.strip()`, `.replace()`, or a slice already solves the problem in one line.

---

## Loop Control Patterns

Python's loop constructs include several features beyond basic `for` and `while` that make common patterns more expressive. Two in particular — `for...else` and `while True` with `break` — solve problems that beginners typically work around with boolean flags. [^1]

**`for...else`**: the `else` block on a `for` loop executes only if the loop completed without hitting a `break`. This is Python's built-in "search completed with no match" pattern.

```python
# Without for...else — requires a flag variable
found = False
for item in items:
    if item.id == target_id:
        found = True
        break
if not found:
    handle_missing()

# With for...else — no flag needed
for item in items:
    if item.id == target_id:
        process(item)
        break
else:
    handle_missing()
```

This is particularly useful in scrapers and search functions where "not found" is a meaningful outcome that requires different handling from "found." [^1]

**`while True` with `break`**: the standard pattern for loops that must run at least once and whose exit condition can only be evaluated after the first iteration — typically interactive input loops and polling loops.

```python
while True:
    command = input("Enter command: ").lower()
    if command == "quit":
        break
    process(command)
```

**Nested loops and coordinate iteration**: outer loop runs once, inner loop runs fully for each outer iteration. For generating all combinations of two ranges, this is more readable than list comprehension for beginners and equally correct.

```python
for x in range(width):
    for y in range(height):
        render_cell(x, y)
```

**`range()` patterns**:
- `range(n)` — 0 to n-1
- `range(start, stop)` — start to stop-1
- `range(start, stop, step)` — with step; step can be negative for countdown [^1]

**The takeaway**: Use `for...else` for search loops to eliminate boolean flag variables; use `while True` + `break` for interactive loops that need at least one iteration.

---

## How CPython Executes Code

Understanding Python's execution model is not just theory — it explains why Python is cross-platform, why `import` takes time on cold starts, and why `.pyc` files appear in `__pycache__` directories. [^1]

CPython (the default and reference Python implementation) follows a two-step execution process: it first compiles Python source code (`.py` files) into **Python bytecode** (`.pyc` files, stored in `__pycache__`), then executes that bytecode on the **Python Virtual Machine (PVM)**. The PVM translates bytecode to native machine code at runtime. This is why Python is platform-independent — the same bytecode runs on any operating system that has a Python VM installed. [^1]

Alternative implementations follow the same principle but target different runtimes:

- **Jython**: compiles Python → Java bytecode → JVM; allows importing Java libraries into Python programs
- **IronPython**: compiles Python → .NET bytecode; allows importing C# libraries
- **PyPy**: alternative CPython with JIT compilation for performance-critical use cases [^1]

The practical implication: `.pyc` files in `__pycache__` should be added to `.gitignore` — they are generated artifacts, not source code. The Python VM regenerates them automatically when source files change. [^1]

**The takeaway**: Python's platform independence comes from its two-stage compilation to bytecode — understanding this demystifies `__pycache__`, import times, and the behavior of alternative Python distributions.

---

## Object-Oriented Programming — Classes and Inheritance

The transition from procedural to object-oriented Python is where the language's full power becomes available. A **class** is a blueprint; an **object** is an instance of that blueprint. Every Django model, every serializer, every view is a class — understanding OOP at the Python level demystifies the Django framework. [^2]

The `__init__` method runs automatically when constructing an object. Instance variables (prefixed with `self.`) belong to each object independently; class variables are shared across all instances. This distinction matters in Django models: class-level field declarations (`name = models.CharField(...)`) are class variables that Django's ORM reads at import time. [^2]

```python
class Student:
    school = "Moro University"   # class variable — shared by all
    
    def __init__(self, name, gpa):
        self.name = name          # instance variable — unique per object
        self.gpa = gpa
```

**Inheritance** allows a child class to inherit all methods and attributes of a parent. Python supports **multiple inheritance** (one child, multiple parents) and **multi-level inheritance** (grandparent → parent → child). The `super()` function calls parent methods from within a child — critical for extending constructors without duplicating code. [^2]

**Magic methods (dunder methods)** customize how objects behave with Python's built-in operators: `__str__` controls `print()`, `__eq__` controls `==`, `__add__` controls `+`. Django uses dunder methods extensively — `__str__` in models controls how objects display in the admin panel. [^2]

> **Key insight**: OOP is not about structure for its own sake — it's about reducing the blast radius of changes. When color validation logic lives in a `Shape` class, changing it changes it everywhere. [^2]

**The takeaway**: Learn the four pillars — encapsulation (`self._private`), inheritance, polymorphism, and abstraction — and the Django framework becomes readable rather than magical.

---

## Exception Handling — Failing Gracefully

Exceptions are runtime errors. Unhandled exceptions crash programs; handled exceptions allow programs to recover, log, and continue. The `try/except` block is Python's mechanism for separating the happy path from error handling. [^2]

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Always runs — good for cleanup.")
```

The `finally` block runs whether or not an exception occurred — use it for cleanup (closing connections, releasing locks). The `else` block runs only if no exception occurred — use it for code that depends on the try block succeeding. [^2]

File operations are the most common exception source for beginners: `FileNotFoundError` when a path doesn't exist, `PermissionError` when access is denied. Any file I/O should be wrapped in `try/except`. [^2]

**The takeaway**: Wrap external operations (file I/O, API calls, type casting of user input) in `try/except`. Let internal code fail loudly — only catch exceptions at system boundaries.

---

## File I/O — Reading and Writing Data

Python's `with` statement (context manager) handles file opening and closing automatically. The `open()` function takes a file path and a mode: `"r"` (read), `"w"` (write, overwrites), `"a"` (append), `"x"` (create, fails if exists). [^2]

```python
# Writing
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# Reading
with open("output.txt", "r") as file:
    content = file.read()
```

The `json` and `csv` modules extend this pattern to structured data. `json.dump()` serializes a Python dict to JSON; `json.load()` deserializes JSON back to a dict. For CSV, `csv.writer` and `csv.reader` handle row-based data. [^2]

> **Key insight**: The `with` statement is not optional style — it guarantees the file closes even if an exception occurs mid-write. Files left open cause data corruption and resource leaks. [^2]

**The takeaway**: Always use `with open(...)` for file operations; combine with `try/except FileNotFoundError` for robust file handling at system boundaries.

---

## For Your Work

These Python fundamentals map directly to five active areas of your stack — Django backends, standalone scripts, scrapers, data processing, and developer training. The patterns here aren't new to you conceptually, but applying them consistently across the `scripts/` directory and backend code would have compound returns.

### Applications

- **`scripts/` directory** (`generate_indexes.py`, `standardize_md.py`, `apply_standardization.py`) — Audit each utility function for the Type 1/Type 2 distinction. Functions that write files directly should likely return the generated content and let a thin top-level caller handle writing — this would make them testable without filesystem access and reusable in Django management commands [^1]
- **BTA Bills / Jurisprudence scrapers** — Apply `for...else` to the search loops that currently use boolean flags for "no results found" handling. This cleans up `scrape_bta_bills.py` and the jurisprudence scraper without changing logic [^1]
- **Django backends (e-Bangsamoro, Tarbiyyah-MS, OBCMS)** — Audit form/serializer validation logic for the `bool("False") == True` trap anywhere external string inputs are used in boolean conditions. This is a real risk in API views that receive JSON with string-encoded booleans [^1]
- **MoroAcademy / MoroDevelopers Community** — The course structure (setup → types → strings → loops → functions) is a ready-made 2-hour beginner Python curriculum. Adapt it as-is for the first MoroDevelopers training session — Mosh's sequencing is proven and the exercises (print even numbers, count iterations) are replicable [^1]
- **`/tdd` skill application** — The Type 2 function preference enables TDD. When next applying `/tdd` to Python work, start by refactoring target functions from Type 1 to Type 2 before writing tests — pure functions need no mocking [^1]
- **Django models** — `__str__`, `__eq__`, and other dunder methods covered in [^2] are used extensively in Django ORM. The `__str__` method on every model controls how objects display in the admin panel and in error messages [^2]
- **File I/O scripts** — Any `scripts/` utility that reads or writes files should use `with open(...)` + `try/except FileNotFoundError`. This pattern from [^2] replaces the current bare open() calls that crash on missing files [^2]
- **API integration** — The `requests.get()` + status code check + `.json()` pattern in [^2] (Pokémon API demo) is the same pattern used in the Weather App final project. Apply it in any Django view that calls an external REST API [^2]
- **Scraper multi-threading** — The `threading.Thread(target=..., args=(...))` pattern from [^2] can parallelize the BTA bills scraper — run multiple page fetches concurrently using threads, then join() before writing results [^2]

### Priority Actions

1. **This week**: Enable autopep8 "Format on Save" in VS Code for all Python workspaces — settings sync across projects. One-time setup, permanent returns.
2. **This week**: Open `scripts/generate_indexes.py` and identify the two or three functions that print or write directly. Convert them to return values. This is a 15-minute refactor that makes the scripts composable.
3. **This month**: Audit Django serializer validation in e-Bangsamoro and Tarbiyyah-MS for string-to-boolean coercion errors. Grep for patterns like `if request.data.get("field"):` where the field is expected to be a boolean.
4. **This month**: Add `try/except FileNotFoundError` + `PermissionError` to all bare `open()` calls in the `scripts/` directory. The BTA bills scraper and standardization scripts currently crash on missing files.
5. **This quarter**: Draft a MoroDevelopers Python Beginner Module outline using Mosh's sequence as the backbone, supplemented by Bro Code's project list. Two 1-hour sessions: Session 1 (setup, types, strings), Session 2 (loops, functions, exercises). Deliverable: a facilitator guide compatible with the `/training-assistant` skill.

---

## References

[^1]: Hamedani, Mosh. "Python Full Course for Beginners." *Programming with Mosh*, 122:20. YouTube, April 2026.
      https://youtube.com/watch?v=K5KVEU3aaeQ

[^2]: Bro Code. "Python Full Course for free." *Bro Code*, 720:00. YouTube, April 2026.
      https://youtube.com/watch?v=ix9cRaBkVe0
