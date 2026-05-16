 
# MagicArray – Tutorials

This tutorial walks through all the methods of the `MagicArray` class in a single consolidated flow.  
Follow each section step by step to practise construction, access, searching, sorting, benchmarking, and visualisation.

---

## 1. Construction & Access

### Create and Append
```python
from alchemy_magicstructures import MagicArray

arr = MagicArray([1, 2, 3])
arr.append(4)
print(arr.traverse())
```

**Output**
```
[1, 2, 3, 4]
```

---

### Insert and Delete
```python
arr = MagicArray([10, 20, 30])
arr.insert(1, 15)
arr.delete(2)
print(arr.traverse())
```

**Output**
```
[10, 15, 30]
```

---

### Get and Set
```python
arr = MagicArray(['a', 'b', 'c'])
print(arr.get(1))   # → b
arr.set(1, 'z')
print(arr.traverse())
```

**Output**
```
b
['a', 'z', 'c']
```

---

## 2. Search & Traversal

### Linear Search
```python
arr = MagicArray([4, 8, 12])
print(arr.linear_search(8))
```

**Output**
```
1
```

---

### Binary Search
```python
arr = MagicArray([1, 3, 5, 7, 9])
print(arr.binary_search(7))
```

**Output**
```
3
```

---

### Traverse
```python
arr = MagicArray([100, 200, 300])
print(arr.traverse())
```

**Output**
```
[100, 200, 300]
```

---

## 3. Sorting Algorithms

### Bubble Sort
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

### Selection Sort
```python
arr = MagicArray([64, 25, 12, 22, 11])
arr.selection_sort()
print(arr.traverse())
```

**Output**
```
[11, 12, 22, 25, 64]
```

---

### Insertion Sort
```python
arr = MagicArray([5, 2, 9, 1])
arr.insertion_sort()
print(arr.traverse())
```

**Output**
```
[1, 2, 5, 9]
```

---

### Merge Sort
```python
arr = MagicArray([38, 27, 43, 3, 9, 82, 10])
arr.merge_sort()
print(arr.traverse())
```

**Output**
```
[3, 9, 10, 27, 38, 43, 82]
```

---

### Quick Sort
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

## 4. Benchmarking

### Measure Algorithm Performance
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

## 5. Visualisation

### Generate Chart
```python
arr = MagicArray([4, 2, 7])
arr.visualise()
```

**Output**
- Creates `demo_int.png` showing array contents.

---

### Export Data
```python
arr = MagicArray([1, 2, 3])
arr.export("array.json")
```

**Output**
- File `array.json` created with contents `[1, 2, 3]`.

---

## 6. Exceptions

### IndexError
```python
arr = MagicArray([1, 2])
try:
    arr.get(5)
except IndexError as e:
    print("Error:", e)
```

**Output**
```
Error: Invalid index access
```

---

### ValueError
```python
arr = MagicArray([1, 2, 3])
try:
    arr.linear_search({'x': 1})
except ValueError as e:
    print("Error:", e)
```

**Output**
```
Error: Unsupported comparison type
```

---

## Summary
This tutorial demonstrated:
- Construction and access methods (`append`, `insert`, `delete`, `get`, `set`).  
- Searching (`linear_search`, `binary_search`) and traversal.  
- Sorting algorithms (bubble, selection, insertion, merge, quick).  
- Benchmarking performance.  
- Visualisation and export.  
- Exception handling.  

With this single consolidated tutorial, learners can practise every method of the `MagicArray` class end‑to‑end.
 

---
 