n = int(input())

l = [None] * n
for i in range(n):
    l[i] = input().split()
    l[i][0] = int(l[i][0])

for people in sorted(l, key=lambda x:x[0]):
    print(*people)