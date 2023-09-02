n = int(input())
cnt = 0

while n >= 0:
    if n % 5 == 0: # n=0일때(즉, 3으로만 나누어떨어질때)도 식이 성립한다.
        cnt += n // 5
        print(cnt)
        break
    n -= 3
    cnt += 1
else: # n<0
    print(-1)