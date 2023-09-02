from collections import deque
import sys
input = sys.stdin.readline

l = deque()
for i in range(1, int(input())+1):
    l.append(i)

while len(l) > 1:
    l.popleft()
    l.append(l.popleft())
print(l[0])