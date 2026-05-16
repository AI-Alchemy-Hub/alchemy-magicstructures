
# Alchemy-MagicStructures

A Python library providing **MagicArray** — a dynamic array structure with extended functionality, visualization, and benchmarking.

## 🚀 Features
- Support for multiple data types (int, float, str, tuple, object)
- Core operations: insert, delete, update, search
- Sorting algorithms: bubble, insertion, selection, merge, quick
- Expand/shrink capacity dynamically
- Visualization with plots
- Benchmarking performance
- Custom exceptions for underflow/overflow

## 📦 Installation
From PyPI:
```bash
pip install alchemy-magicstructures
```

## 🔧 Usage
```python
from alchemy_magicstructures.magicarray import MagicArray

arr = MagicArray([1, 2, 3])
print(arr.traverse())
```

## 📖 Documentation
- Public docs: see `/docs/` (served via MkDocs, deployable to GitHub Pages)
- Internal docs: see `/project-docs/`

## 🧪 Testing
Run all tests:
```bash
pytest -v tests/
```

## 📋 Requirements
See [requirements.txt](requirements.txt) for dependencies.

## 📌 Milestone
- **M1 complete**: 73 tests passed, documentation prepared, packaging ready.

## 📜 License
Licensed under the terms of the [LICENSE](LICENSE) file.


--- 
