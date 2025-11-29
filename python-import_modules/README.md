# Python - Import & Modules

This project covers the basics of importing functions, using modules, and organizing code across multiple files in Python.  
It focuses on how to properly reuse functions from other files using the `import` and `__import__` statements.

---

## 📚 Learning Objectives

By the end of this project, you should be able to:

- Understand how modules work in Python  
- Import functions from another file  
- Use `import` and `__import__` correctly  
- Avoid executing code during import  
- Organize Python code into separate reusable files  
- Use string formatting with print  
- Understand how Python executes scripts vs imported modules  

---

## 📁 Project Structur
---

## 📝 Task 0: Import a simple function from a simple file

### 📌 Requirements:
- File **0-add.py** must contain a function `def add(a, b)` that returns the sum of two integers.
- File **0-import_add.py** must:
  - Import the function using `__import__("0-add").add`
  - Assign:
    - `a = 1`
    - `b = 2`
  - Print the result using:
    ```
    1 + 2 = <result>
    ```
- You are not allowed to use:
  - `from ... import ...`
  - `*` for importing
  - Any additional modules

---

## ✅ Example Output
---

## 🧠 How It Works

- Python treats every `.py` file as a module.
- Using `__import__("0-add")` allows importing a file name starting with a number.
- Code inside the imported file **does not run** unless it's inside a function or guarded by:

```python
if __name__ == "__main__":
