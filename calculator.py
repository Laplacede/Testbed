def add(a, b):
    """返回两个数的和"""
    return a + b

def divide(a, b):
    """返回两个数的商，处理除以零的情况"""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
