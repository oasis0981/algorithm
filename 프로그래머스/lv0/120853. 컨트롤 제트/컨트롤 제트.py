from collections import deque

def solution(s):
    num_list = []
    s_queue = deque(s.split(' '))
    for n in s_queue:
        if n.isdigit():
            num_list.append(int(n))
            continue
        if n.find('-') == 0:
            num_list.append(-int(n.replace('-','')))
            continue
        num_list.pop()
    return sum(num_list)