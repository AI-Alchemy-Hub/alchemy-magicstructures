# MagicArray Class Reference

## Overview
MagicArray is the foundational class in Alchemy‑MagicStructures. It demonstrates dynamic arrays with complete operations, visualization, and benchmarking.

## Constructors
- `MagicArray()` → empty array
- `MagicArray([elements])` → pre‑filled array
- `MagicArray(max_size=N)` → array with capacity constraint
- `MagicArray(source="file.csv")` → load from external source

## Methods
- `insert(index, value)`
- `delete(index)`
- `update(index, value)`
- `search(value)`
- `sort(algorithm="quick")`
- `expand()`, `shrink()`
- `displayAndSave(filename="array.png")`
- `benchmark(algorithm)`

## Attributes
- `size` → current number of elements
- `capacity` → maximum allowed size
- `elements` → internal storage list

## Usage Example
```python
arr = MagicArray([1, 2, 3], max_size=5)
arr.insert(2, 99)
arr.sort("merge")
arr.displayAndSave("array.png")
