# 부녀회장이 될테야

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    # k-1층의 n호까지 인원수 합
    floor = list(i for i in range(1, n+1))
    num = 0
    for i in range(k):
        for i in range(1, n): #인덱스
            floor[i] += floor[i-1]
    print(floor[n-1])