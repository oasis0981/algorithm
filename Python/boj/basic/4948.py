"""
베르트랑 공준
임의의 자연수 n에 대하여, n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재함
"""
import math
import sys

n = 123456 * 2
arr= [True for i in range(n+1)]
arr[0] = False
arr[1] = False

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(n)+1)):
    if arr[i] == True: # i가 소수인 경우
        # i 제외한 i의 모든 배수 지우기
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

while True:
    data = int(sys.stdin.readline())
    if data == 0:
        break
    cnt = 0
    for i in range(data+1, data*2+1):
        if arr[i] == True:
            cnt += 1
    print(cnt)