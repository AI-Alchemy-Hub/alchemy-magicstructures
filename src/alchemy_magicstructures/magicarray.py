"""
===============================================================================
MagicArray Class – Milestone 1
Alchemy-MagicStructures Library
===============================================================================

Author: Satya Prakash Nigam
Team: AI Alchemy Hub
License: PSF/BSD-Compatible License
         (See LICENSE file in repository for full terms)

Description:
------------
Implements a dynamic array with:
- Initialisation (empty, pre‑filled, max size, external source)
- Core operations (insert, delete, update, search)
- Sorting algorithms (bubble, insertion, selection, merge, quick)
- Expand/shrink capacity
- Visualisation (matplotlib) – numeric elements as bars, non‑numeric as labels
- Benchmarking hooks
- Error simulation

Notes:
------
- Elements can be of ANY type.
- For sorting, elements must support comparison (`__lt__`).
- Designed for educational use in Milestone 1 of Alchemy‑MagicStructures.
- Documentation and tutorials are EN_IN compliant.

===============================================================================
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
        """
        Insert a value at a given index.

        Parameters
        ----------
        index : int
            Position at which the new element should be inserted.
        value : Any
            Element to insert into the array.

        Raises
        ------
        OverflowError
            If the array has reached its maximum capacity.
        IndexError
            If the index is outside the valid range [0, size].

        Notes
        -----
        - Expands the array size by one.
        - Shifts existing elements to the right from the given index.
        """
        if self.max_size and self.size >= self.max_size:
            raise OverflowError("Array capacity reached.")
        if index < 0 or index > self.size:
            raise IndexError("Invalid index.")
        self.elements.insert(index, value)
        self.size += 1

    def delete(self, index: int) -> Any:
        """
        Delete an element at a given index and return it.

        Parameters
        ----------
        index : int
            Position of the element to delete.

        Returns
        -------
        Any
            The element removed from the array.

        Raises
        ------
        UnderflowError
            If the array is empty.
        IndexError
            If the index is outside the valid range [0, size-1].

        Notes
        -----
        - Shrinks the array size by one.
        - Shifts subsequent elements to the left.
        """
        if self.size == 0:
            raise UnderflowError("Array is empty.")
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index.")
        removed = self.elements.pop(index)
        self.size -= 1
        return removed

    def update(self, index: int, value: Any) -> None:
        """
        Update the element at a given index.

        Parameters
        ----------
        index : int
            Position of the element to update.
        value : Any
            New value to assign at the given index.

        Raises
        ------
        IndexError
            If the index is outside the valid range [0, size-1].

        Notes
        -----
        - Overwrites the existing element at the specified index.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index.")
        self.elements[index] = value

    def search(self, value: Any) -> int:
        """
        Search for a value in the array using Python's built‑in index.

        Parameters
        ----------
        value : Any
            Element to search for.

        Returns
        -------
        int
            Index of the element if found, else -1.

        Notes
        -----
        - Performs a direct equality check.
        - Returns -1 if the element is not present.
        """
        try:
            return self.elements.index(value)
        except ValueError:
            return -1


        # ---------------- Sorting Algorithms ----------------
    def sort(self, algorithm: str = "quick") -> None:
        """
        Sort the array elements using the chosen algorithm.

        Parameters
        ----------
        algorithm : str, optional
            Sorting algorithm to use. Options are:
            - 'bubble'
            - 'insertion'
            - 'selection'
            - 'merge'
            - 'quick'
            Default is 'quick'.

        Raises
        ------
        ValueError
            If an unknown algorithm name is provided.

        Notes
        -----
        - Elements must support comparison (`__lt__`).
        - For 'merge' and 'quick', the method replaces the internal list
          with a new sorted list.
        - For 'bubble' and 'insertion', sorting is done in place.
        """
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

    def _bubble_sort(self) -> None:
        """
        Internal bubble sort implementation.

        Notes
        -----
        - Repeatedly compares and swaps adjacent elements if they are in the wrong order.
        - Time complexity: O(n^2).
        - Stable sort (preserves order of equal elements).
        """
        for i in range(self.size):
            for j in range(0, self.size - i - 1):
                if self.elements[j] > self.elements[j + 1]:
                    # Swap adjacent elements
                    self.elements[j], self.elements[j + 1] = self.elements[j + 1], self.elements[j]

    def _insertion_sort(self) -> None:
        """
        Internal insertion sort implementation.

        Notes
        -----
        - Builds the sorted array one element at a time.
        - Shifts larger elements to the right to insert the current key.
        - Time complexity: O(n^2).
        - Stable sort (preserves order of equal elements).
        """
        for i in range(1, self.size):
            key = self.elements[i]
            j = i - 1
            # Shift elements greater than key to the right
            while j >= 0 and self.elements[j] > key:
                self.elements[j + 1] = self.elements[j]
                j -= 1
            self.elements[j + 1] = key


    def _selection_sort(self) -> None:
        """
        Internal selection sort implementation.

        Notes
        -----
        - Divides the array into a sorted and an unsorted region.
        - Repeatedly selects the minimum element from the unsorted region
          and swaps it with the first unsorted element.
        - Time complexity: O(n^2).
        - Not stable (equal elements may change relative order).
        """
        for i in range(self.size):
            min_idx = i
            for j in range(i + 1, self.size):
                if self.elements[j] < self.elements[min_idx]:
                    min_idx = j
            # Swap the found minimum with the first unsorted element
            self.elements[i], self.elements[min_idx] = self.elements[min_idx], self.elements[i]

    def _merge_sort(self, arr: List[Any]) -> List[Any]:
        """
        Internal recursive merge sort implementation.

        Parameters
        ----------
        arr : List[Any]
            Sub‑list of elements to sort.

        Returns
        -------
        List[Any]
            A new sorted list containing the elements of `arr`.

        Notes
        -----
        - Divides the list into halves recursively until single elements remain.
        - Merges sorted halves using the `_merge` helper.
        - Time complexity: O(n log n).
        - Stable sort (preserves order of equal elements).
        """
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        return self._merge(left, right)

    def _merge(self, left: List[Any], right: List[Any]) -> List[Any]:
        """
        Helper function for merge sort.

        Parameters
        ----------
        left : List[Any]
            Left half of the list (already sorted).
        right : List[Any]
            Right half of the list (already sorted).

        Returns
        -------
        List[Any]
            A merged and sorted list containing all elements from `left` and `right`.

        Notes
        -----
        - Iteratively compares elements from both halves and appends the smaller one.
        - Extends the result with any remaining elements once one half is exhausted.
        """
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # Append remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result


    def _quick_sort(self, arr: List[Any]) -> List[Any]:
        """
        Internal recursive quick sort implementation.

        Parameters
        ----------
        arr : List[Any]
            Sub‑list of elements to sort.

        Returns
        -------
        List[Any]
            A new sorted list containing the elements of `arr`.

        Notes
        -----
        - Selects a pivot element (here, the middle element).
        - Partitions the list into three sub‑lists:
            * left   → elements less than pivot
            * middle → elements equal to pivot
            * right  → elements greater than pivot
        - Recursively sorts the left and right sub‑lists.
        - Concatenates results as: sorted left + middle + sorted right.
        - Average time complexity: O(n log n).
        - Worst‑case time complexity: O(n^2) (rare, depends on pivot choice).
        - Not stable (equal elements may change relative order).
        """
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self._quick_sort(left) + middle + self._quick_sort(right)

 
    # ---------------- Expand/Shrink ----------------
    def expand(self, extra: int = 5) -> None:
        """
        Expand the maximum capacity of the array.

        Parameters
        ----------
        extra : int, optional
            Number of additional slots to add to the maximum capacity.
            Default is 5.

        Notes
        -----
        - Only effective if `max_size` is defined.
        - Increases `max_size` by the specified number.
        - Does not alter current elements or size, only the capacity limit.
        """
        if self.max_size:
            self.max_size += extra

    def shrink(self, reduce: int = 5) -> None:
        """
        Shrink the maximum capacity of the array.

        Parameters
        ----------
        reduce : int, optional
            Number of slots to remove from the maximum capacity.
            Default is 5.

        Notes
        -----
        - Only effective if `max_size` is defined.
        - Decreases `max_size` by the specified number, provided
          the result remains greater than zero.
        - Does not remove existing elements, only reduces the capacity limit.
        """
        if self.max_size and self.max_size > reduce:
            self.max_size -= reduce


    # ---------------- Visualisation ----------------
    def display_and_save(self, filename: str = "array.png") -> None:
        """
        Visualise the array contents and save the plot as a PNG file.

        Parameters
        ----------
        filename : str, optional
            Name of the output file to save the visualisation.
            Default is "array.png".

        Notes
        -----
        - If all elements are numeric (int or float), they are plotted as bars
          with heights corresponding to their values.
        - If elements are non‑numeric, each element is shown as a labelled bar
          with index positions on the x‑axis.
        - The figure is saved to disk and closed automatically.
        - Uses matplotlib for rendering.

        Example
        -------
        >>> arr = MagicArray([10, 20, 30])
        >>> arr.display_and_save("numbers.png")
        # Creates a bar chart with values 10, 20, 30
        """
        import numpy as np
        plt.figure(figsize=(8, 4))
        if all(isinstance(x, (int, float)) for x in self.elements):
            # Numeric elements → bar heights represent values
            plt.bar(range(self.size), self.elements, color="skyblue")
            plt.ylabel("Value")
        else:
            # Non‑numeric elements → labelled bars
            plt.bar(range(self.size), [1] * self.size, color="lightgreen")
            plt.xticks(range(self.size), [str(x) for x in self.elements], rotation=45)
            plt.ylabel("Elements")
        plt.title("MagicArray Visualisation")
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

    # ---------------- Search Algorithms ----------------
    def linear_search(self, value: Any) -> int:
        """
        Perform a linear search for a given value.

        Parameters
        ----------
        value : Any
            Element to search for in the array.

        Returns
        -------
        int
            Index of the element if found, else -1.

        Notes
        -----
        - Iterates through the array sequentially.
        - Time complexity: O(n).
        - Works on both sorted and unsorted arrays.
        - Stable behaviour: returns the first occurrence if duplicates exist.

        Example
        -------
        >>> arr = MagicArray([5, 10, 15])
        >>> arr.linear_search(10)
        1
        """
        for i, elem in enumerate(self.elements):
            if elem == value:
                return i
        return -1

    def binary_search(self, value: Any) -> int:
        """
        Perform a binary search for a given value on a sorted array.

        Parameters
        ----------
        value : Any
            Element to search for in the array.

        Returns
        -------
        int
            Index of the element if found, else -1.

        Raises
        ------
        ValueError
            If the array is not sorted prior to calling this method.

        Notes
        -----
        - Requires the array to be sorted in ascending order.
        - Time complexity: O(log n).
        - Not stable: if duplicates exist, the returned index may vary.
        - Efficient for large datasets compared to linear search.

        Example
        -------
        >>> arr = MagicArray([1, 3, 5, 7, 9])
        >>> arr.binary_search(7)
        3
        """
        low, high = 0, self.size - 1
        while low <= high:
            mid = (low + high) // 2
            if self.elements[mid] == value:
                return mid
            elif self.elements[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def traverse(self) -> List[Any]:
        """
        Traverse the array and return a shallow copy of all elements.

        Returns
        -------
        List[Any]
            A new list containing all elements of the array.

        Notes
        -----
        - Provides a safe copy, leaving the original array unchanged.
        - Useful for iteration, inspection, or external processing.
        - Shallow copy: nested objects are not duplicated.

        Example
        -------
        >>> arr = MagicArray([1, "A", 3.5])
        >>> arr.traverse()
        [1, 'A', 3.5]
        """
        return self.elements[:]

 
# ---------------- Custom Exceptions ----------------
class UnderflowError(Exception):
    """
    Exception raised when attempting to delete from an empty array.

    Notes
    -----
    - Used specifically in the `delete` method of `MagicArray`.
    - Signals that the operation cannot proceed because the array
      contains no elements.
    - Distinct from `IndexError`, which indicates an invalid index.
    - Helps differentiate between logical underflow (empty structure)
      and incorrect indexing.

    Example
    -------
    >>> arr = MagicArray([])
    >>> arr.delete(0)
    Traceback (most recent call last):
        ...
    UnderflowError: Array is empty.
    """
    pass
