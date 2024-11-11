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
