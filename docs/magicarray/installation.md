
# MagicArray – Installation Guide

## Step 1: Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/AI-Alchemy-Hub/alchemy-magicstructures.git
cd alchemy-magicstructures
```

---

## Step 2: Local Editable Install
Install in editable mode so changes are reflected immediately:
```bash
pip install -e .
```

This will also install required dependencies:
- **NumPy ≥ 1.20**
- **Matplotlib ≥ 3.0**

---

## Step 3: Verify Installation
Check that the package is installed:
```bash
pip list | findstr alchemy-magicstructures
```

Or test import in Python:
```python
from alchemy_magicstructures import MagicArray
print("MagicArray ready!")
```

---

## Step 4: Run Demo Scripts
Try the examples provided:
```bash
python examples/magicarray_demo.py
```

Expected outcome:
- A sample `MagicArray` is created.  
- Sorting algorithms run on test data.  
- PNG charts (`demo_int.png`, `demo_str.png`, etc.) are generated in the project root.  

---

## Step 5: Troubleshooting
- If dependencies are missing, reinstall:
  ```bash
  pip install numpy matplotlib
  ```
- If using multiple Python versions, ensure you are running the correct interpreter (`python3` vs `python`).  
- For Windows users, run commands in **Git Bash** or **PowerShell**.  

---

## Next Steps
- Detailed method documentation  
- Guided examples with code and outputs
