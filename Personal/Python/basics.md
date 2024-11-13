# PYTHON BAISCS

## 1. List Comprehension

- Concise way to create lists based on iterables and conditions.
- `new_list = [expression for item in iterable if condition]`
- `evens = [x for x in range(10) if x % 2 == 0]`

## 2. Generators

- Efficient way to create iterator object that generate values on-the-fly (runtime) rather than storing them all in memory at once.
- Uses Python's iterator protocol, implementing `__iter__()` and `__next__()` methods behind the scenes.
- Generator Functions (using `yield`):
```py
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Using the generator
counter = count_up_to(3)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
```
```py
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 5 Fibonacci numbers
fib = fibonacci()
for _ in range(5):
    print(next(fib))  # 0, 1, 1, 2, 3
```
- Generator Expressions (similar to list comprehensions):
```py
squares_gen = (x**2 for x in range(1000))
```
- Key benefits of generators:
	- Memory efficient (values generated on-demand), perfect for working with large datasets.
	- Lazy evaluation (compute values only when needed).
- Differences between generators and regular functions:
	- Generators use yield instead of return.
	- They maintain state between calls.
	- They return an iterator object.
- Common Pitfalls:
	- Can't access previous values unless explicitly stored.
	- No len() function, since values are generated on-the-fly.

## 3. Lamda Function

- Also known as anonymous functions - these are one line functions that can have multiple arguments and one expression.  
Syntax: `lambda arguments: expression`.
```py
# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
add = lambda x, y: x + y

# Usage
print(add(5, 3))  # 8

# One-liner without assignment
print((lambda x, y: x + y)(5, 3))  # 8
```
- Common Uses with Built-in Functions
```py
# With map() - apply function to each item
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# With filter() - keep items that return True
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]

# With sorted() - custom sorting
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # [(1, 'one'), (3, 'three'), (2, 'two')]
```

## 4. Dictionary Comprehension

- Similar to list comprehensions but it creates dictionary instead of list.  
Basic Syntax: `{key_expression: value_expression for item in iterable}`.
- Example usage:
```py
# Create a dictionary of squares
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Using if condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

## 5. File Handling

- Basic File Operations using with statement.
```py
# Reading a file
with open('example.txt', 'r') as file:
    # Read entire file as string
    content = file.read()
    
    # OR read line by line
    for line in file:
        print(line.strip())

# Writing to a file
with open('output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.writelines(['Line 1\n', 'Line 2\n'])

# Appending to a file
with open('output.txt', 'a') as file:
    file.write('Appended text\n')
```
- File Open Modes:
```
'r'  - Read (default)
'w'  - Write (overwrites)
'a'  - Append
'x'  - Exclusive creation
'b'  - Binary mode
't'  - Text mode (default)
'+'  - Read and write
```

## 6. Serialization

- This is a process of converting an object into a format that can be transmitted over network. The transmitted data can be deserialized or reconstructed into the obejct.
- Serialization is useful in several scenarios:
    - **Data Persistence:** Serializing objects allows you to save their state to a file or database, so they can be recreated later.
    - **Data Exchange:** Serialized data can be easily shared between different systems or programming languages. In distributed systems, serialization is often used to pass method arguments and return values between client and server.
    - **Caching and Messaging:** Serialized data can be cached or sent as messages between different components of a system.
- Popular serialization formats include:
    - **JSON (JavaScript Object Notation):** A text-based format that is human-readable and widely supported but does not stores the datatype of the variable.
    - **Pickle:** Converts objects into byte array format and it stores information about variable's datatypes. It can also serialize functions.

## 7. Copying object

- Assignment operator (=) does not create a copy of the object, but it creates new reference to same object.
- Two ways to actually copy an object in python:
    - **Shallow Copy:** `y = copy.copy(x)`, this creates a clone of the object. In case of nested objects such as `[1,[1,2],3]`, it only clones the top layer of the object, the inner nested layers will be referenced.
    - **Deep Copy:** `y = copy.deepcopy(x)`, this creates a clone of the whole object, including the nested objects recursively. This ensures that the copied object is entirely independent of the original object.

## 8. Dunder methods

- Also known as "magic methods" or "special methods", are a set of predefined methods that you can use to enrich python classes.
- These methods are surrounded by double underscores, such as `__init__` or `__str__`, and are automatically called when certain operations are performed on the objects of your class.
- Example:
```py
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __len__(self):
        return 2

# Usage
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
print(v1)  # Output: (1, 2)
print(len(v1))  # Output: 2
print(v1 + v2)  # Output: (4, 6)
```

## 9. `__repr(self)__` vs `__str__(self)`

- Both dunder methods used for string representation of object.
- `__repr__(self)`:
    - This method is used for string representation of objects for other programmers.
    - The output of this method is what you see when you evaluate an object in the interactive Python console or when the object is displayed in a debugger.
    - This method should aim to provide a detailed representation of the object, which is typically used for debugging and logging purposes.
- `__str__(self)`:
    - This method is used for string representation for users of the module.
    - The output of this method is what you see when you print an object or use the str() function on it.
    - If __str__ is not defined, Python will use the __repr__ method as a fallback.

## 10. Properties of datatypes

- **Dictionary:**
    - Key:Value pair store.
    - Ordered insertion of keys after v3.6.
    - Mutable datatype.
    - Keys are of immutable datatype e.g. integer, string or tuple.
    - Unique keys.
- **Sets:**
    - Mutable datatype.
    - Unordered insertion.
    - Unique Elements.
    - No indexing.
- **Frozen Sets:**
    - Immutable datatype.
    - Other properties same as Sets.
- **Lists:**
    - Mutable datatype.
    - Ordered insertion.
    - Indexing.
