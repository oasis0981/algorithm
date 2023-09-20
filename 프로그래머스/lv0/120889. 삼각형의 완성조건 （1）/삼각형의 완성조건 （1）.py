def solution(sides):
    maxNum = sides.pop(sides.index(max(sides)))
    if maxNum < sum(sides):
        return 1
    return 2
