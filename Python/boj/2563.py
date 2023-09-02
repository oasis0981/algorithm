matrix = [[0]*100 for _ in range(100)]

n = int(input())
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(0,10):
        for j in range(0,10):
            if matrix[x+i][y+j] == 0:
                matrix[x+i][y+j] = 1
                cnt += 1

print(cnt)