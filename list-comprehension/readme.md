# List Comprehension
A concise way to create a new list from an existing list in Python is with list comprehension.

```python
my_list = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in my_list]
print(squares)
# [1, 4, 9, 16, 25]
```

Optionally, you can also filter the elements of the original list at the same time.

```python
my_list = [1, 2, 3, 4, 5]
odds_squared = [x**2 for x in my_list if x % 2 == 1]
print(odds_squared)
# [1, 9, 25]
```

This is equivalent to the code:

```python
my_list = [1, 2, 3, 4, 5]
odds_squared = []
for x in my_list:
    if x % 2 == 1:
        odds_squared.append(x**2)
print(odds_squared)
# [1, 9, 25]
```

The full syntax is as follows:
```python
my_list = [expression for item in iterable if condition]
```

List comprehensions are great for simple transformations and filtering, but they become less readable once the expression and condition logic becomes more complex.
At that point, regular loops and if statements are preferred.

## Set and Dictionary Comprehension

"List" comprehension also works for sets and dictionaries!
Instead of using square brackets `[]` to indicate a list, you use `{}` instead to create a set.

```python
my_list = [1, 2, 3, 4, 5]
odds_squared = {x**2 for x in my_list if x % 2 == 1}
print(odds_squared)
# {1, 9, 25}
print(type(odds_squared))
# <class 'set'>
```

To create a dictionary, you still use `{}` but in the expression you give both the key and value as `key: value`.
In the example, the key is the original number and the value is the key squared.

```python
my_list = [1, 2, 3, 4, 5]
odds_squared = {x: x**2 for x in my_list if x % 2 == 1}
print(odds_squared)
# {1: 1, 3: 9, 5: 25}
print(type(odds_squared))
# <class 'dict'>
```

## Assignment

The player is overwhelmed by the number of items available in the shop and has requested a feature to filter the items they can afford.

Complete the `filter_shop_inventory` function.
It takes the shop items as a list of tuples and the player's balance as input.
The tuples are of the form `(item, price)`.

Return a new list containing the shop items the player can afford.

Example:

```python
items = [("Rag", 10), ("Vest", 20)]
result = filter_shop_inventory(items, 15)
# result = ['Rag']
```