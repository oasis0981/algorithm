def solution(numbers):
    a = numbers.pop(numbers.index(max(numbers)))
    b = numbers.pop(numbers.index(max(numbers)))
    return a * b