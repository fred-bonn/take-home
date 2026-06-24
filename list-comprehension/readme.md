# List Comprehension

A concise way for creating a new list based on an existing list in Python is with list comprehension. 

```python
list = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in list]
print(squares)
# [1, 4, 9, 16, 25]
```

Optionally, you can also simultanously filter the elements of the original list.

```python
list = [1, 2, 3, 4, 5]
odds_squared = [x**2 for x in list if x % 2 == 1]
print(odds)
# [1, 9, 25]
```

This is equivalent to the code:

```python
list = [1, 2, 3, 4, 5]
odds_squared = []
for x in list:
    if x % 2 == 1:
        squares.append(x**2)
print(squares)
# [1, 9, 25]
```

The full syntax is as follows:
```python
my_list = [expression for item in iterable if condition]
```

List comprehensions are great for simple transformations and filtering, but are less readable once the expression and condition logic becomes more complex.
At that point, regular loops and if statements are prefered.

## Set and Dictionary Comprehension

"List" comprehension also works for sets and dictionaries!
Instead of using squares brackets `[]` to indicate a list, you use `{}` instead to create a set.

```python
list = [1, 2, 3, 4, 5]
odds_squared = {x**2 for x in list if x % 2 == 1}
print(odds_squared)
# {1, 9, 25}
print(type(odds_squared))
# <class 'set'>
```

To create a dictionary, you still use `{}` but in the expression you give both the key and value as `key: value`.
In the example, the key is the original number and the value is the key squared.

```python
list = [1, 2, 3, 4, 5]
odds_squared = {x: x**2 for x in list if x % 2 == 1}
print(odds_squared)
# {1: 1, 3: 9, 5: 25}
print(type(odds_squared))
# <class 'dict'>
```

## Assignment

The player is overwhelmned by the quantity of items available at the shops and have a requested a feature for filtering the items that they can afford.
Complete the `filter_shop_inventory` function.
It a takes the shop items as a list of tuples and the player's balance as input.
The tuples are of the form `(item, price)`.

Return a new list of the shop items the player can afford.

Example:

```python
items = [("Rag", 10), ("Vest", 20)]
result = filter_shop_inventory(items, 15)
# result = ['Rag']
```