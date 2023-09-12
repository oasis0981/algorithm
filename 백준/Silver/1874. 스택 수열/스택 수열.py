from collections import deque

test_cases = int(input())
target_arr = deque()

for _ in range(test_cases):
  target_arr.append(int(input()))

stack = []
result = []
for i in range(1, test_cases + 1):
  stack.append(i)
  result.append('+')
  while (len(stack) != 0 and stack[-1] == target_arr[0]):
    stack.pop()
    target_arr.popleft()
    result.append('-')

if len(stack) == 0:
  print("\n".join(result))
else:
  print("NO")