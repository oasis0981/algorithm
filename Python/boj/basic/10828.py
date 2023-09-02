# 스택 처리 프로그램
import sys

n = int(input())
stack_list = []

for _ in range(n):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == 'push':
        stack_list.append(int(order[1]))
    elif order[0] == 'pop':
        if not len(stack_list): print(-1)
        else:
            print(stack_list[-1])
            stack_list.pop()
    elif order[0] == 'size':
        print(len(stack_list))
    elif order[0] == 'empty':
        if not len(stack_list): print(1)
        else: print(0)
    elif order[0] == 'top':
        if not len(stack_list): print(-1)
        else: print(stack_list[-1])

