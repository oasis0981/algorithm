import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []

for _ in range(k):
  lines.append(int(input()))


def find_max_length(arr, target_count):
  left, right = 1, max(arr)

  while left <= right:
    mid = (left + right) // 2
    count = 0
    for length in arr:
      count += length // mid

    if count < target_count:
      right = mid - 1

    else:
      left = mid + 1

  return right


result = find_max_length(lines, n)

print(result)
