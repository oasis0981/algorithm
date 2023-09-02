"""
큐를 구현하고 명령을 처리하는 프로그램 작성
* push X: 정수 X를 큐에 넣는 연산
* pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력.
* size: 큐에 들어있는 정수의 개수를 출력.
* empty: 큐가 비어있으면 1, 아니면 0을 출력.
* front: 큐의 가장 앞에 있는 정수를 출력. 만약 큐에 들어있는 정수가 없는 경우 -1을 출력.
* back: 큐의 가장 뒤에 있는 정수를 출력. 만약 큐에 들어있는 정수가 없는 경우 -1을 출력.
"""

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
l = deque()
for _ in range(n):
    order = input().rstrip()

    if 'push' in order:
        w, n = order.split()
        l.append(int(n))

    elif order == 'pop':
        if len(l) > 0:
            pop = l.popleft()
            print(pop)
        else:
            print(-1)

    elif order == 'size':
        print(len(l))

    elif order == 'empty':
        if len(l) > 0:
            print(0)
        else:
            print(1)

    elif order == 'front':
        if len(l) > 0:
            print(l[0])
        else:
            print(-1)

    elif order == 'back':
        if len(l) > 0:
            print(l[-1])
        else:
            print(-1)