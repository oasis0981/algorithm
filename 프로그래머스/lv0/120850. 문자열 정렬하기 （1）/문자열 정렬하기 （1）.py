import string

def solution(str):
    alphabets = list(string.ascii_lowercase)
    numbers = []
    for s in str:
        if s not in alphabets:
            numbers.append(int(s))
    return sorted(numbers)