import sys
from collections import Counter

n = int(input())

# 입력받은 숫자 개수만큼 리스트 생성, 값 입력
num_list =[]
sum_num = 0
cnt_list = Counter()
for i in range(n):
  num_list.append(int(sys.stdin.readline()))
  sum_num += num_list[i]

for num in num_list:
  cnt_list[num] += 1

# 리스트 오름차순 정렬
num_list.sort()

# 최빈값 리스트 생성
max_list = [k for k,v in cnt_list.items() if max(cnt_list.values()) == v]

# 여러개일 경우 두번째로 작은값을 max_num에 넣음
if len(max_list) == 1:
  max_num = max_list[0]
else:
  max_list.sort()
  max_num = max_list[1]

print(round(sum_num / n))
print(num_list[n//2])
print(max_num)
print(max(num_list)-min(num_list))