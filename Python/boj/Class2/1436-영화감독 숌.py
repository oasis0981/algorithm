# https://www.acmicpc.net/problem/1436

n = int(input())

# 666부터 1씩 더해가며 순서대로 종말의 수를 찾는다.
# 브루트포스
result = 0
temp = 666
for i in range(n):
    while True:
        if ('666' in str(temp) and (temp > result)):
            result = temp
            break
        temp += 1

print(result)
