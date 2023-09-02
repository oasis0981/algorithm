# 빠른 소수 판별
import sys
import math


m,n = map(int,sys.stdin.readline().split())

for i in range(m, n+1): # i는 m과 n 사이의 수
    if i == 1:
        continue
    for j in range(2,int(math.sqrt(i)+1)): # j는 나누는 수
        if i % j == 0: break
    else:
        print(i)