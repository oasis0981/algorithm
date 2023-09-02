"""

정수 n이 입력되면 00시 00분 00초부터 n시 59분 59초까지 모든 시각 중
3이 하나라도 포함되는 모든 경우의 숙 ㅜ하는 프로그램 구하기

"""

# 완전 탐색 : 가능한 모든 경우의 수 검사해보는 탐색 방법

n = int(input())

cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): # 시,분,초 나열한 문자열
                cnt+=1

print(cnt)