import sys

n = int(input())
nums = [0] * 10001

for i in range(n):
    nums[int(sys.stdin.readline())] +=1
    '''
    for문에서 append로 리스트에 값을 추가하게되면, 메모리 공간이 계속 확장되면서 낭비가 심해진다.
    가능한 리스트를 미리 선언하여 할당하는 것이 좋다.
    '''


for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)