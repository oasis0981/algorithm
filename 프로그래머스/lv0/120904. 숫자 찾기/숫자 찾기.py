def solution(num, k):
    idx = str(num).find(str(k))
    if idx == -1:
        return idx 
    return idx + 1