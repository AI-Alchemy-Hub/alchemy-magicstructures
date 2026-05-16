"""
MagicArray Demo Script
Demonstrates usage with ints, floats, strings, tuples, custom objects
"""

from alchemy_magicstructures.magicarray import MagicArray, UnderflowError

# ---------------- Example 1: Integers ----------------
print("\n--- Example 1: Integers ---")
arr_int = MagicArray([5, 3, 8, 1])
print("Original:", arr_int.elements)
arr_int.sort("quick")
print("Sorted:", arr_int.elements)
arr_int.display_and_save("demo_int.png")

# ---------------- Example 2: Floats ----------------
print("\n--- Example 2: Floats ---")
arr_float = MagicArray([2.2, 1.1, 3.3])
print("Original:", arr_float.elements)
arr_float.sort("merge")
print("Sorted:", arr_float.elements)
arr_float.display_and_save("demo_float.png")

# ---------------- Example 3: Strings ----------------
print("\n--- Example 3: Strings ---")
arr_str = MagicArray(["pear", "apple", "banana"])
print("Original:", arr_str.elements)
arr_str.sort("selection")
print("Sorted:", arr_str.elements)
arr_str.display_and_save("demo_str.png")

# ---------------- Example 4: Tuples ----------------
print("\n--- Example 4: Tuples ---")
arr_tuple = MagicArray([(2,3), (1,4), (3,1)])
print("Original:", arr_tuple.elements)
arr_tuple.sort("insertion")
print("Sorted:", arr_tuple.elements)
arr_tuple.display_and_save("demo_tuple.png")

# ---------------- Example 5: Custom Objects ----------------
print("\n--- Example 5: Custom Objects ---")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __lt__(self, other: "Student") -> bool:
        return self.grade < other.grade
    def __repr__(self):
        return f"{self.name} ({self.grade})"

students = [Student("Alice", 90), Student("Bob", 85), Student("Charlie", 95)]
arr_obj = MagicArray(students)
print("Original:", arr_obj.elements)
arr_obj.sort("bubble")
print("Sorted:", arr_obj.elements)
arr_obj.display_and_save("demo_obj.png")

# ---------------- Example 6: Benchmarking ----------------
print("\n--- Example 6: Benchmarking ---")
arr_bench = MagicArray([5, 3, 8, 1])
print("Quick Sort Avg Time:", arr_bench.benchmark("quick", trials=3))
print("Merge Sort Avg Time:", arr_bench.benchmark("merge", trials=3))


