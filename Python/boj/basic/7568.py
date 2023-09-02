# 덩치
import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

ranks = []
for i in range(n):
    w, h = l[i][0], l[i][1]
    rank = 1
    for j in range(n):
        if j == i: continue
        if w < l[j][0] and h < l[j][1]:
            rank += 1
    ranks.append(rank)

print(*ranks)