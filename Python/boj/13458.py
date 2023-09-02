import math
n = int(input())
stu_num = list(map(int, input().split()))
b, c = map(int, input().split())

invigilator_num = 0
for i in range(n):
    if stu_num[i] <= b:
        invigilator_num += 1
    else:
        invigilator_num += math.ceil(1 + (stu_num[i] - b) / c)

print(invigilator_num)