def greeting(name: str) -> str:  # 这里提示有问题
    print(f"Hello { name }")


x: str = "xxx"
y: int = "yyy"  # 这里应该提示有问题
greeting(x)
greeting(y)  # 这里应该提示有问题


# * mypy test_mypy.py

"""
test_mypy.py:1: error: Missing return statement  [return]
test_mypy.py:6: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
test_mypy.py:8: error: Argument 1 to "greeting" has incompatible type "int"; expected "str"  [arg-type]
Found 3 errors in 1 file (checked 1 source file)
"""
