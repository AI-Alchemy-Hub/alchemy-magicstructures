
# MagicArray – API Reference

The `MagicArray` class provides a complete pedagogical implementation of array operations, enriched with benchmarking and visualization hooks.  
This page documents each method in detail, with usage examples and expected outputs.

---

## Class Signature
```python
class MagicArray:
    def __init__(self, data=None):
        ...
```

- **Parameters**
  - `data` (list, optional): Initial array contents. Can include integers, strings, objects, or nested structures.
- **Behavior**
  - Initializes with dynamic capacity.
  - Supports expansion/shrinkage with overflow/underflow simulation.

---

## Construction & Access

### `append(item)`
Add an element to the end of the array.

**Example**
```python
arr = MagicArray([1, 2, 3])
arr.append(4)
print(arr.traverse())
```

**Output**
```
[1, 2, 3, 4]
```

---

### `insert(index, item)`
Insert an element at a specific position.

**Example**
```python
arr = MagicArray([10, 20, 30])
arr.insert(1, 15)
print(arr.traverse())
```

**Output**
```
[10, 15, 20, 30]
```

---

### `delete(index)`
Remove an element at a specific position.

**Example**
```python
arr = MagicArray([5, 6, 7])
arr.delete(1)
print(arr.traverse())
```

**Output**
```
[5, 7]
```

---

### `get(index)`
Retrieve element at position.

**Example**
```python
arr = MagicArray(['a', 'b', 'c'])
print(arr.get(2))
```

**Output**
```
c
```

---

### `set(index, item)`
Update element at position.

**Example**
```python
arr = MagicArray([1, 2, 3])
arr.set(0, 99)
print(arr.traverse())
```

**Output**
```
[99, 2, 3]
```

---

## Search & Traversal

### `linear_search(item)`
Return index if found, else `-1`.

**Example**
```python
arr = MagicArray([4, 8, 12])
print(arr.linear_search(8))
```

**Output**
```
1
```

---

### `binary_search(item)`
Return index if found (requires sorted array).

**Example**
```python
arr = MagicArray([1, 3, 5, 7, 9])
print(arr.binary_search(7))
```

**Output**
```
3
```

---

### `traverse()`
Return list of all elements.

**Example**
```python
arr = MagicArray([100, 200, 300])
print(arr.traverse())
```

**Output**
```
[100, 200, 300]
```

---

## Sorting Algorithms

Each sorting method returns a sorted array and records benchmarking metrics.

### `bubble_sort()`
**Example**
```python
arr = MagicArray([9, 2, 5])
arr.bubble_sort()
print(arr.traverse())
```

**Output**
```
[2, 5, 9]
```

---

### `quick_sort()`
**Example**
```python
arr = MagicArray([10, 7, 8, 9, 1])
arr.quick_sort()
print(arr.traverse())
```

**Output**
```
[1, 7, 8, 9, 10]
```

---

## Benchmarking

### `benchmark(algorithm)`
Run algorithm and return metrics.

**Example**
```python
arr = MagicArray([3, 1, 2])
metrics = arr.benchmark('bubble_sort')
print(metrics)
```

**Output**
```
{'algorithm': 'bubble_sort', 'time': 0.0001, 'comparisons': 3, 'swaps': 2}
```

---

## Visualization

### `visualize()`
Generate chart (PNG) of current array state.

**Example**
```python
arr = MagicArray([4, 2, 7])
arr.visualize()
```

**Output**
- Creates `demo_int.png` showing array contents.

---

### `export(filename)`
Save array contents to JSON/CSV.

**Example**
```python
arr = MagicArray([1, 2, 3])
arr.export("array.json")
```

**Output**
- File `array.json` created with contents `[1, 2, 3]`.

---

## Exceptions
- **`IndexError`** → Raised for invalid index access.  
- **`ValueError`** → Raised for invalid operations (e.g., searching non‑comparable types).  

---

## Next Steps
- MagicMatrix2D API Reference  
- MagicMatrix3D API Reference  
- MagicLinkedList API Reference
 

--- 