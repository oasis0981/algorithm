a, b = input().split()

c = 0
d = 0
for i in range(2, -1, -1):
    c += int(a[i]) * (10 ** i)
    d += int(b[i]) * (10 ** i)

print(max(c, d))