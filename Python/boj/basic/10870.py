# n = int(input())
#
# p = [0, 1]
# for i in range(n-1):
#     p.append(p[i] + p[i+1])
#
# print(p[n])


# 재귀함수로 구현
def pivo(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return pivo(n-1)+pivo(n-2)

n = int(input())
print(pivo(n))