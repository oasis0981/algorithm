# 9*9 격자의 최댓값

max_num = {}

for i in range(9):
    num_arr = list(map(int, input().split()))
    max_num[max(num_arr)] = (i+1, num_arr.index(max(num_arr))+1)

result = max(max_num)
idx = max_num[result]

print(result)
print(idx[0], idx[1])