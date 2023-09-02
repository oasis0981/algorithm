import itertools

n, m = map(int, input().split())
cards = list(map(int, input().split()))
pick_three = list(itertools.combinations(cards, 3))

add_list = []
for i in range(len(pick_three)):
    add = sum(pick_three[i])
    if m - add >= 0:
        add_list.append(add)

print(max(add_list))