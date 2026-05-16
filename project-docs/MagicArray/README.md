 
# MagicArray Documentation

## 📘 Introduction
`MagicArray` is the foundational class in the **Alchemy‑MagicStructures** library.  
It is designed as an educational tool to teach data structures with a focus on:
- Dynamic array operations (insert, delete, update, search).
- Sorting algorithms (bubble, insertion, selection, merge, quick).
- Visualization of array contents using Matplotlib.
- Benchmarking of algorithm performance.

This class is the **Milestone 1 (M1)** deliverable in the course syllabus, serving as the entry point for learners to explore advanced data structures with practical examples.

---

## 📚 Prerequisites
Before using `MagicArray`, ensure you have:
- Python **3.8 or higher**.
- Installed dependencies:
  - `matplotlib >= 3.0`
  - `numpy >= 1.20`
- Basic knowledge of Python lists and comparison operators (`__lt__`).

---

## ⚙️ Installation Guide
Clone the repository and install the package in editable mode:

```bash
git clone https://github.com/your-repo/Alchemy-MagicStructures.git
cd Alchemy-MagicStructures
pip install -e .
```

Verify installation:

```bash
pip list | findstr alchemy-magicstructures
```

Run the demo script:

```bash
python examples/magicarray_demo.py
```

---

## 🔧 API Documentation

### Class: `MagicArray`
```python
MagicArray(elements: list, max_size: int = None)
```

#### Methods

| Method | Syntax | Description | Exceptions |
|--------|--------|-------------|------------|
| **Initialization** | `arr = MagicArray([1,2,3], max_size=10)` | Creates a new array with optional max size. | — |
| **Insert** | `arr.insert(index, value)` | Inserts `value` at `index`. | `OverflowError` |
| **Delete** | `arr.delete(index)` | Removes element at `index`. | `UnderflowError`, `IndexError` |
| **Update** | `arr.update(index, value)` | Replaces element at `index`. | `IndexError` |
| **Search** | `arr.search(value)` | Returns index of `value` if found, else `-1`. | — |
| **Sort** | `arr.sort(algorithm="quick")` | Sorts using bubble, insertion, selection, merge, or quick. | `ValueError` |
| **Expand Capacity** | `arr.expand_capacity(new_size)` | Increases max size. | `ValueError` |
| **Shrink Capacity** | `arr.shrink_capacity(new_size)` | Decreases max size. | `ValueError` |
| **Display & Save** | `arr.display_and_save("array.png")` | Saves visualization as PNG. | — |
| **Benchmark** | `arr.benchmark("quick", trials=5)` | Returns average runtime for sort algorithm. | `ValueError` |

---

## 📝 Tutorial Section

### Example 1: Integers
```python
from alchemy_magicstructures.magicarray import MagicArray

arr = MagicArray([5, 3, 8, 1])
arr.sort("quick")
print(arr.elements)  # [1, 3, 5, 8]
arr.display_and_save("int_array.png")
```

### Example 2: Strings
```python
arr = MagicArray(["pear", "apple", "banana"])
arr.sort("selection")
print(arr.elements)  # ['apple', 'banana', 'pear']
```

### Example 3: Custom Objects
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __lt__(self, other): return self.grade < other.grade
    def __repr__(self): return f"{self.name} ({self.grade})"

students = [Student("Alice", 90), Student("Bob", 85)]
arr = MagicArray(students)
arr.sort("bubble")
print(arr.elements)  # [Bob (85), Alice (90)]
```

### Example 4: Benchmarking
```python
arr = MagicArray([5, 3, 8, 1])
print(arr.benchmark("quick", trials=3))
```

---

## 📖 Notes
- Mixed types (e.g., ints + strings) may raise `TypeError`.  
- Visualization adapts automatically:
  - Numeric → bar chart.
  - Non‑numeric → labels.  
- Benchmarks provide approximate runtime, not precise profiling.  
- All visualizations are saved as PNG files in the current working directory.

---

## 🎯 Course Integration
- `MagicArray` is the **first milestone** in the Alchemy‑MagicStructures syllabus.  
- Learners should practice:
  - Implementing new sorting algorithms.
  - Extending visualization styles.
  - Benchmarking with larger datasets.  
- This class sets the foundation for subsequent milestones (e.g., stacks, queues, trees).

---

## 📎 References
- NumPy Documentation  
- Matplotlib Documentation  
- PyTorch Documentation  

---
 