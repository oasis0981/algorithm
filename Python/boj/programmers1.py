import sys

def solution(a, b):
    dates = 0
    if a == 1:
        answer = days[b % 7 - 1]
    else:
        for i in range(1, a):
            dates += date[i-1]
        answer = days[(dates + b) % 7 - 1]
    return answer

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

days = ('FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU')
date = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print(solution(a,b))