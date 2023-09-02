# 소수찾기 2

m = int(input())
n = int(input())
sosu = []
for i in range(m, n+1):
    if i == 1:
        continue
    elif 2 <= i <= 3:
        sosu.append(i)
        continue
    for j in range(2, i):
        if i%j == 0: break
    else:
        sosu.append(i)

if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))
