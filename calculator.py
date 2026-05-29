def add(a, b):
    """返回两个数的和"""
    # BUG 1 (性能/逻辑): 极其愚蠢的循环实现，且当 b 为负数时会死循环
    # 理想的 AI 应该指出：直接 a + b 即可，这样写不仅慢还会导致内存/CPU耗尽
    result = a
    while b != 0:
        result += 1
        b -= 1
    return result

def divide(a, b):
    """返回两个数的商，处理除以零的情况"""
    # BUG 2 (逻辑错误): 把原本的除零保护删除了，直接相除会导致 ZeroDivisionError
    return a / b

# BUG 3 (代码异味/死代码): 定义了函数但没有写完，且存在语法隐患
def calculate_average(numbers):
    pass
