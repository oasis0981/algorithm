# 체스판 다시 칠하기
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [input().rstrip() for _ in range(n)]

# 8*8로 자르는 경우의 수 : (n -7)*(m - 7)
cnt = []
for x in range(n-7): # 세로 이동 경우의 수
    for y in range(m-7): # 가로 이동 경우의 수
        start_w = 0
        start_b = 0
        for i in range(x, x+8): #
            for j in range(y, y+8):
                if (i+j) % 2 == 0: # i+j 짝수인 칸에 대해서
                    if board[i][j] != 'W':
                        start_w += 1 # 시작점이 W일때 고쳐야하는 개수 cnt
                    if board[i][j] != 'B':
                        start_b += 1 # 시작점이 B일때 고쳐야하는 개수 cnt
                else: # i+j가 홀수인 칸에 대해서
                    if board[i][j] != 'B':
                        start_w += 1 # 시작점이 W일때 고쳐야하는 개수 cnt
                    if board[i][j] != 'W':
                        start_b += 1 # 시작점이 B일때 고쳐야하는 개수 cnt
        cnt.append(min(start_w, start_b))

print(min(cnt))