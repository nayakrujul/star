# star
Powerful arrays in Python

## Documentation

### Install from PIP

```
$ pip install star-array
```

### Import library

```python
import star
```

### Define array from Iterable

```python
a = star.Array(range(10))
print(a)
```

Output: `Array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`

### Define array from type

```python
x = star.Array(int)
print(x)
```

Output: `Array([])`

### Perform operations to the array

```python
print(a + 5)
```

Output: `Array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14])`

Supported operations: `+`, `-`, `*`, `/`, `//`, `%`, `<<`, `>>`, `&`, `|`, `~`

### Perform comparisons to the array

```python
print(a % 3 == 0)
```

Output: `Array([True, False, False, True, False, False, True, False, False, True])`

Supported operations: `==`, `!=`, `>`, `>=`, `<`, `<=`

### Get indexes of matches

```python
print(star.Array.where(a % 3 == 0))
```

Output: `Array([0, 3, 6, 9])`

Note: the second parameter, match, is the element which it looks for. It defaults to `True`.

```python
print(star.Array(['a', 'b', 'a', 'b', 'a']).where('a'))
```

Output: `Array([0, 2, 4])`

### Get methods of elements

```python
b = star.Array(['foo', 'bar', 'baz'])
print(b.el.startswith('b'))
```

Output: `Array([False, True, True])`

### Use list methods, but with multiple arguments

```python
b.append('something', 'else')
print(b)
```

Output: `Array(['foo', 'bar', 'baz', 'something', 'else'])`

### Notes

All elements in the array must be of the same type. A `StarError` may be raised if this condition is not met.
