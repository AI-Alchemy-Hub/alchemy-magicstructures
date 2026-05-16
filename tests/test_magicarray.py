"""
Unit Tests – MagicArray
Milestone 1
Covers multiple element types: ints, floats, chars, strings, tuples, custom objects
"""

import os
import pytest
from alchemy_magicstructures.magicarray import MagicArray, UnderflowError


# ---------------- Helper Class for Custom Objects ----------------
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __lt__(self, other: "Student") -> bool:
        return self.grade < other.grade

    def __repr__(self):
        return f"{self.name} ({self.grade})"


# ---------------- Initialization ----------------
@pytest.mark.parametrize("elements", [
    [], [1, 2, 3], [1.1, 2.2, 3.3], ['a', 'b', 'c'], ["apple", "banana"], [(1,2), (3,4)],
    [Student("Alice", 90), Student("Bob", 85)]
])
def test_initialization_various_types(elements):
    arr = MagicArray(elements)
    assert arr.size == len(elements)
    assert arr.elements == elements


def test_initialization_with_max_size():
    arr = MagicArray([1, 2], max_size=5)
    assert arr.max_size == 5
    assert arr.size == 2


# ---------------- Core Operations ----------------
@pytest.mark.parametrize("elements,value", [
    ([1, 2, 3], 99),
    ([1.1, 2.2], 3.3),
    (['a', 'b'], 'z'),
    (["apple"], "pear"),
    ([(1,2)], (5,6)),
    ([Student("Alice", 90)], Student("Charlie", 95))
])
def test_insert_valid(elements, value):
    arr = MagicArray(elements)
    arr.insert(1, value)
    assert value in arr.elements


def test_insert_overflow():
    arr = MagicArray([1, 2], max_size=2)
    with pytest.raises(OverflowError):
        arr.insert(1, 99)


def test_delete_valid():
    arr = MagicArray([1, 2, 3])
    removed = arr.delete(1)
    assert removed == 2
    assert arr.elements == [1, 3]


def test_delete_underflow():
    arr = MagicArray([])
    with pytest.raises(UnderflowError):
        arr.delete(0)


def test_update_valid():
    arr = MagicArray([1, 2, 3])
    arr.update(1, 42)
    assert arr.elements[1] == 42


def test_update_invalid_index():
    arr = MagicArray([1, 2, 3])
    with pytest.raises(IndexError):
        arr.update(5, 99)


def test_search_found():
    arr = MagicArray(["apple", "banana", "cherry"])
    assert arr.search("banana") == 1


def test_search_not_found():
    arr = MagicArray(["apple", "banana"])
    assert arr.search("pear") == -1


# ---------------- Sorting ----------------
@pytest.mark.parametrize("elements", [
    [5, 3, 8, 1],
    [2.2, 1.1, 3.3],
    ['d', 'a', 'c', 'b'],
    ["pear", "apple", "banana"],
    [(2,3), (1,4), (3,1)],
    [Student("Alice", 90), Student("Bob", 85), Student("Charlie", 95)]
])
@pytest.mark.parametrize("algorithm", ["bubble", "insertion", "selection", "merge", "quick"])
def test_sort_algorithms(elements, algorithm):
    arr = MagicArray(elements)
    arr.sort(algorithm)
    # Verify sorted order using Python's sorted()
    assert arr.elements == sorted(elements)


def test_sort_invalid_algorithm():
    arr = MagicArray([1, 2, 3])
    with pytest.raises(ValueError):
        arr.sort("unknown")


# ---------------- Expand/Shrink ----------------
def test_expand_capacity():
    arr = MagicArray([1, 2], max_size=5)
    arr.expand(3)
    assert arr.max_size == 8


def test_shrink_capacity():
    arr = MagicArray([1, 2], max_size=10)
    arr.shrink(4)
    assert arr.max_size == 6


# ---------------- Visualization ----------------
import matplotlib
matplotlib.use("Agg")   # Force non-interactive backend for tests

@pytest.mark.parametrize("elements", [
    [1, 2, 3], ["apple", "banana"], ['x', 'y', 'z'],
    [Student("Alice", 90), Student("Bob", 85)]
])
def test_display_and_save(tmp_path, elements):
    arr = MagicArray(elements)
    filename = tmp_path / "array.png"
    arr.display_and_save(str(filename))
    assert os.path.exists(filename)


# ---------------- Benchmarking ----------------
def test_benchmark_quick():
    arr = MagicArray([5, 3, 8, 1])
    avg_time = arr.benchmark("quick", trials=3)
    assert avg_time >= 0.0


def test_benchmark_merge():
    arr = MagicArray([5, 3, 8, 1])
    avg_time = arr.benchmark("merge", trials=3)
    assert avg_time >= 0.0


def test_benchmark_invalid_algorithm():
    arr = MagicArray([1, 2, 3])
    with pytest.raises(ValueError):
        arr.benchmark("bubble")


# ---------------- Mixed-Type Arrays ----------------
def test_sort_mixed_types_int_str():
    arr = MagicArray([1, "apple", 3])
    # Sorting should fail because int and str are not comparable
    with pytest.raises(TypeError):
        arr.sort("quick")


def test_sort_mixed_types_float_tuple():
    arr = MagicArray([1.1, (2, 3), 4.4])
    # Sorting should fail because float and tuple are not comparable
    with pytest.raises(TypeError):
        arr.sort("merge")


def test_sort_mixed_types_char_student():
    arr = MagicArray(['a', Student("Alice", 90)])
    # Sorting should fail because str and Student are not comparable
    with pytest.raises(AttributeError):
        arr.sort("bubble")
 
def test_visualization_mixed_types(tmp_path):
    arr = MagicArray([1, "apple", 3.14])
    filename = tmp_path / "mixed.png"
    # Visualization should still succeed (labels for non-numeric)
    arr.display_and_save(str(filename))
    assert os.path.exists(filename)
    
    
# ---------------- Search Algorithms ----------------

def test_linear_search_found():
    arr = MagicArray([10, 20, 30])
    assert arr.linear_search(20) == 1

def test_linear_search_not_found():
    arr = MagicArray([10, 20, 30])
    assert arr.linear_search(99) == -1

def test_binary_search_found():
    arr = MagicArray([1, 3, 5, 7, 9])
    assert arr.binary_search(7) == 3

def test_binary_search_not_found():
    arr = MagicArray([1, 3, 5, 7, 9])
    assert arr.binary_search(4) == -1

def test_traverse_returns_copy():
    arr = MagicArray([100, 200, 300])
    result = arr.traverse()
    assert result == [100, 200, 300]
    # Ensure it is a copy, not the same object
    result.append(400)
    assert arr.size == 3
    assert arr.elements == [100, 200, 300]

# ---------------- Exception Handling ----------------

def test_delete_underflow_error():
    arr = MagicArray([])
    with pytest.raises(UnderflowError):
        arr.delete(0)

def test_insert_overflow_error():
    arr = MagicArray([1, 2, 3], max_size=3)
    with pytest.raises(OverflowError):
        arr.insert(3, 4)

def test_update_index_error():
    arr = MagicArray([1, 2])
    with pytest.raises(IndexError):
        arr.update(5, 99)

def test_sort_invalid_algorithm():
    arr = MagicArray([1, 2, 3])
    with pytest.raises(ValueError):
        arr.sort("unknown")
