"""

왕실의 나이트

8*8 좌표 평면의 정원, 특정한칸에 나이트가 서있음
나이트는 말을 타기때문에 L자 형태로만 이동 가능
1. 수평 두칸 이동 후 수직 한칸 이동
2. 수직 두칸 이동 후 수평 한칸 이동

나이트 위치가 주어졌을 때 한 번에 이동할 수 있는 경우의 수를 출력
행 위치는 1~8
열 위치는 a~h로 표현함

"""

location = input()

row = int(ord(location[0])) - int(ord('a')) + 1 # 알파벳을 1~8로 변환
col = int(location[1])

x = [2, 2, 1, -1, -2, -2, 1, -1]
y = [1, -1, 2, 2, 1, -1, -2, -2]

cnt = 0
for i in range(8):
    nx = row + x[i]
    ny = col + y[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8 :
        continue
    cnt += 1

print(cnt)