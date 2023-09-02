# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
# 0! = 1! = 1
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1) # 수학식 n*(n-1)!를 그대로 코드로 작성