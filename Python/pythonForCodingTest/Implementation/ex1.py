"""
<문제> 상하좌우

여행가 A는 정사각형 공간에 서있다.
왼쪽 위 좌표는 (1,1)이고 오른쪽 아래좌표는(n,n)이다.
상하좌우 이동가능하고, 시작좌표는 항상 (1,1)이다.

이동 계획서는 한 줄에 띄어쓰기를 기준으로 하여, L,R,U,D중 하나의 문자가 반복적으로 써있다.
- L: 왼쪽으로 한칸
- R: 오른쪽으로 한칸
- U : 위로 한칸
- D : 아래로 한칸

n*n 벗어나는 움직임은 무시됨
"""


# 시뮬레이션 유형 문제임

n = int(input())
x,y = 1,1
plans = list(input().split())

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if  nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x,y)