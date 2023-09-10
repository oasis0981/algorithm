from collections import deque

def find_print_order(priorities, target_idx):
    print_order = 0
    queue = deque([(idx, priority) for idx, priority in enumerate(priorities)])

    while queue:
      current_doc = queue.popleft()
      index, priority = current_doc

      if any(priority < doc[1] for doc in queue):
        queue.append(current_doc)
      else:
        print_order += 1
        if index == target_idx:
          return print_order

test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    result = find_print_order(priorities, m)
    print(result)
