def solution(n):
    cnt = 0
    for i in range(1, n+1):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                cnt += 1
                break
    return cnt          
