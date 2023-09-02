# 분해합

n = int(input())

i = 1   # n의 자리수
first_num = 0   # n의 첫번째 숫자
while True:
    if n // (10 ** (i - 1)) >= 10:
        i = i + 1
    else:
        first_num = n // (10 ** (i - 1))
        break

generator = n - (first_num + (9 * (i - 1)))
while generator < n:
    j = generator
    each_sum = 0
    while j > 0:
        digit = j % 10
        each_sum += digit
        j = j // 10
    if each_sum + generator == n:
        print(generator)
        break
    else:
        generator += 1
else:
    print(0)
