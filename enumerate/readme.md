# Enumerate

The Python [enumerate](https://docs.python.org/3/library/functions.html#enumerate) function is useful when you need to iterate over a list and access both the elements and their indexes.

```python
my_list = ["Frodo", "Sam", "Pippin", "Merry"]
for i, v in enumerate(my_list, 1):
    print(i, v)
# 1 Frodo
# 2 Sam
# 3 Pippin
# 4 Merry

```

The second parameter is optional and specifies the starting index for the first element.
When omitted, it defaults to 0.

## Enumerate Object

Under the hood, `enumerate` returns an enumerate object that yields tuples of the form `(index, element)`.
This object can be converted directly to a list of tuples.

```python
my_list = ["Frodo", "Sam", "Pippin", "Merry"]
new_list = list(enumerate(my_list, 1))
print(new_list)
# [(1, "Frodo"), (2, "Sam"), (3, "Pippin"), (4, "Merry")]
```

## Assignment

Some of our players are having trouble clearly seeing how healthy their party is.
We need a way to identify which party members are injured below a threshold so they can be highlighted.

Complete the `get_injured` function.
It takes as input the party's health as a list of integers and a threshold.

Return a list of party member indexes that are below the threshold and have not fainted.
A party member faints if their health reaches 0 or less.

Example:

```python
party = [25, 20, 35, 30, 15]
result = get_injured(party, 25)
# result = [1, 4]
```
