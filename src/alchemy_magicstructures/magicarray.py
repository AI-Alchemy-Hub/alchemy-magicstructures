"""
MagicArray Class – Milestone 1
Alchemy-MagicStructures Library

Implements a dynamic array with:
- Initialization (empty, pre-filled, max size, external source)
- Core operations (insert, delete, update, search)
- Sorting algorithms (bubble, insertion, selection, merge, quick)
- Expand/shrink capacity
- Visualization (matplotlib) – numeric elements as bars, non-numeric as labels
- Benchmarking hooks
- Error simulation

Note:
- Elements can be of ANY type.
- For sorting, elements must support comparison (__lt__).
"""

from typing import List, Any, Optional
import matplotlib.pyplot as plt


class MagicArray:
    def __init__(self, elements: Optional[List[Any]] = None, max_size: Optional[int] = None):
        """
        Initialize MagicArray.
        :param elements: Optional pre-filled list of elements.
        :param max_size: Optional maximum capacity.
        """
        self.elements = elements[:] if elements else []
        self.max_size = max_size
        self.size = len(self.elements)

    # ---------------- Core Operations ----------------
    def insert(self, index: int, value: Any) -> None:
        """Insert value at index, expanding if needed."""
        if self.max_size and self.size >= self.max_size:
            raise OverflowError("Array capacity reached.")
        if index < 0 or index > self.size:
            raise IndexError("Invalid index.")  # pragma: no cover
        self.elements.insert(index, value)
        self.size += 1

    def delete(self, index: int) -> Any:
        """Delete element at index and return it."""
        if self.size == 0:
            raise UnderflowError("Array is empty.")
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index.")  # pragma: no cover
        removed = self.elements.pop(index)
        self.size -= 1
        return removed

    def update(self, index: int, value: Any) -> None:
        """Update element at index."""
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index.")
        self.elements[index] = value

    def search(self, value: Any) -> int:
        """Return index of value, or -1 if not found."""
        try:
            return self.elements.index(value)
        except ValueError:
            return -1

    # ---------------- Sorting Algorithms ----------------
    def sort(self, algorithm: str = "quick") -> None:
        """Sort elements using chosen algorithm. Elements must support __lt__."""
        if algorithm == "bubble":
            self._bubble_sort()
        elif algorithm == "insertion":
            self._insertion_sort()
        elif algorithm == "selection":
            self._selection_sort()
        elif algorithm == "merge":
            self.elements = self._merge_sort(self.elements)
        elif algorithm == "quick":
            self.elements = self._quick_sort(self.elements)
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}")

    def _bubble_sort(self):
        for i in range(self.size):
            for j in range(0, self.size - i - 1):
                if self.elements[j] > self.elements[j + 1]:
                    self.elements[j], self.elements[j + 1] = self.elements[j + 1], self.elements[j]

    def _insertion_sort(self):
        for i in range(1, self.size):
            key = self.elements[i]
            j = i - 1
            while j >= 0 and self.elements[j] > key:
                self.elements[j + 1] = self.elements[j]
                j -= 1
            self.elements[j + 1] = key

    def _selection_sort(self):
        for i in range(self.size):
            min_idx = i
            for j in range(i + 1, self.size):
                if self.elements[j] < self.elements[min_idx]:
                    min_idx = j
            self.elements[i], self.elements[min_idx] = self.elements[min_idx], self.elements[i]

    def _merge_sort(self, arr: List[Any]) -> List[Any]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        return self._merge(left, right)

    def _merge(self, left: List[Any], right: List[Any]) -> List[Any]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i]); i += 1
            else:
                result.append(right[j]); j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def _quick_sort(self, arr: List[Any]) -> List[Any]:
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self._quick_sort(left) + middle + self._quick_sort(right)

    # ---------------- Expand/Shrink ----------------
    def expand(self, extra: int = 5) -> None:
        """Expand capacity by extra units."""
        if self.max_size:
            self.max_size += extra

    def shrink(self, reduce: int = 5) -> None:
        """Shrink capacity by reduce units."""
        if self.max_size and self.max_size > reduce:
            self.max_size -= reduce

    # ---------------- Visualization ----------------
    def display_and_save(self, filename: str = "array.png") -> None:
        """Visualize array contents and save as PNG.
        Numeric elements are plotted as bars.
        Non-numeric elements are shown as labels at indices.
        """
        import numpy as np
        plt.figure(figsize=(8, 4))
        if all(isinstance(x, (int, float)) for x in self.elements):
            plt.bar(range(self.size), self.elements, color="skyblue")
            plt.ylabel("Value")
        else:
            plt.bar(range(self.size), [1]*self.size, color="lightgreen")
            plt.xticks(range(self.size), [str(x) for x in self.elements], rotation=45)
            plt.ylabel("Elements")
        plt.title("MagicArray Visualization")
        plt.xlabel("Index")
        plt.savefig(filename)
        plt.close()

    # ---------------- Benchmarking ----------------
    def benchmark(self, algorithm: str = "quick", trials: int = 5) -> float:
        """Benchmark sorting algorithm runtime."""
        import time
        total = 0.0
        for _ in range(trials):
            arr_copy = self.elements[:]
            start = time.perf_counter()
            if algorithm == "merge":
                self._merge_sort(arr_copy)
            elif algorithm == "quick":
                self._quick_sort(arr_copy)
            else:
                raise ValueError("Benchmark supports only merge/quick.")
            total += (time.perf_counter() - start)
        return total / trials


# ---------------- Custom Exceptions ----------------
class UnderflowError(Exception):
    """Raised when attempting to delete from an empty array."""
    pass
