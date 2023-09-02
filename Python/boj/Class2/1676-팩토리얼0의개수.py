# https://www.acmicpc.net/problem/1676
# 실버 5

n = int(input())


def factorial(n):
    if (n <= 1):
        return 1
    return n * factorial(n-1)


strN = str(factorial(n))

result = 0
i = -1
while True:
    if strN[i] != '0':
        break
    result += 1
    i -= 1

print(result)
