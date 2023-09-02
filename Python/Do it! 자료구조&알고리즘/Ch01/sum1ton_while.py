# 1부터 n까지 정수의 합 (while)

n = int(input('n입력: '))

sum = 0
i = 0

while i <= n:
    # 명령문 = 루프 본문
    sum += i
    i += 1

print(f"1부터 n까지의 합은? {sum}")
print(f"i값은? {i}") # i = n+1일때 종료됨