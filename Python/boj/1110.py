# 더하기 사이클

N = int(input())
def split_number(n):
    if n >= 10:
        a = n // 10
        b = n - a * 10
    else:
        a = 0
        b = n
    return a, b


cnt = 0
a,b = split_number(N)

while True:
    sum = a+b
    if sum < 10:
        new_num = (b * 10) + sum
    else:
        new_num = (b * 10) + (sum % 10)

    cnt += 1

    a, b = split_number(new_num)

    if new_num == N:
        break

print(cnt)
