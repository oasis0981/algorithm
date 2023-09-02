# 행렬 덧셈

n, m = map(int,input().split())
matrix = [[0] * m for _ in range(n)]

for i in range(n*2):
    nums = list(map(int, input().split()))
    for j in range(m):
        matrix[i%n][j] += nums[j]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end = ' ')
    print()
