# Python - Exceptions

This project focuses on using `try` and `except` in Python to handle errors safely without stopping the program.  
Each task must follow the rules of the project, including:
- No importing any module
- Using only `try` / `except`
- Avoiding built-in functions in some tasks (e.g., `len()`)

---

## 🔹 Task 0: Safe list printing

**Function:**  
`def safe_print_list(my_list=[], x=0):`

### Requirements:
- Print up to `x` elements from `my_list`
- Elements printed on the same line (no space)
- If `x` > length of list → print available elements only
- Return the number of elements printed
- Must use `try`/`except`
- Cannot use `len()`

### Example:
Input:
```python
my_list = [1, 2, 3, 4, 5]
safe_print_list(my_list, 7)
