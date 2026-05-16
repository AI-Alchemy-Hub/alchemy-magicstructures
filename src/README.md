 
# Source Code — Alchemy MagicStructures

This folder contains the core implementation of the **Alchemy-MagicStructures** library.

## Structure
- `alchemy_magicstructures/`
  - `__init__.py` — package initializer
  - `magicarray.py` — main implementation of the `MagicArray` class

## Purpose
The `src/` directory is the canonical location for the library’s source code.  
It follows the modern Python packaging convention where all importable modules live under `src/`.

## Usage
To use the library in your project:

```bash
pip install alchemy-magicstructures
```

Then import in Python:

```python
from alchemy_magicstructures.magicarray import MagicArray

arr = MagicArray([1, 2, 3])
print(arr.traverse())
```

## Notes
- Keep all new modules inside `alchemy_magicstructures/`.
- Do not place test files here — use `/tests/` instead.
- Ensure docstrings follow the EN_IN style for consistency.
 