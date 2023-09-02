import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))
num_list.sort()
m = int(input())
find_list = list(map(int,input().split()))

def binsearch(num_list, num):
    l = 0
    r = len(num_list) - 1
    while True:
        c = (l+r)//2
        if num_list[c] == num: return 1

        if num_list[c] < num: l = c + 1
        else: r = c - 1

        if l > r : break
    return 0

for num in find_list:
    print(binsearch(num_list, num))