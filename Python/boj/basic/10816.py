# 숫자 카드 2
from collections import Counter

n = int(input())
cards = dict(Counter(map(int,input().split())))
m = int(input())
find_list = list(map(int, input().split()))

for num in find_list:
    if num in cards.keys():
        print(cards[num], end = ' ')
    else: print(0, end = ' ')