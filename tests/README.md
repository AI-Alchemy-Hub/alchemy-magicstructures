 
# Tests — Alchemy MagicStructures

This folder contains the **unit tests** for the Alchemy-MagicStructures library.

## Structure
- `test_magicarray.py` — pytest suite covering all functionality of `MagicArray`.

## Coverage
The tests validate:
- Initialization with different element types
- Core operations: insert, delete, update, search
- Sorting algorithms: bubble, insertion, selection, merge, quick
- Expand and shrink capacity
- Visualization and saving plots
- Benchmarking performance
- Search algorithms: linear, binary, traverse
- Custom exceptions: `UnderflowError`, overflow, invalid index

## Running Tests
From the project root:
```bash
pytest -v tests/
```

## Notes
- All 73 tests currently pass (M1 milestone).
- Add new test files here for future modules.
- Keep test names descriptive and aligned with functionality.
 

