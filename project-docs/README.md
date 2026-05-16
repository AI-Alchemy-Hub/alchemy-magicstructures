# Alchemy MagicStructures

## Overview
Alchemy‑MagicStructures is a pedagogical Python library designed to reimagine how learners engage with **Data Structures & Algorithms (DSA‑1)**. Each class begins with the prefix **Magic*** and implements all theoretically valid operations, dynamic capacity, benchmarking, visualization, and persistence.

## Documentation
- [vision.md](vision.md) – Philosophy and identity
- [executive_summary.md](executive_summary.md) – One‑pager overview
- [requirements.md](requirements.md) – Functional and non‑functional requirements
- [roadmap.md](roadmap.md) – Phased development plan
- [tutorials.md](tutorials.md) – Tutorial structure and principles
- [architecture.md](architecture.md) – Class hierarchy and design
- [testing.md](testing.md) – Testing strategy
- [contributing.md](contributing.md) – Contribution guidelines
- [changelog.md](changelog.md) – Version history
- [glossary.md](glossary.md) – Key terms
- [license.md](license.md) – Licensing terms
- [styleguide.md](styleguide.md) – Coding conventions

## Quick Start
```python
from magicstructures import MagicArray

arr = MagicArray([1, 2, 3], max_size=5)
arr.push(4)
arr.displayAndSave("array.png")
