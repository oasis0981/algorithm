# 펠린드롬수 판별하기
import sys
input = sys.stdin.readline

while True:
    num = input().rstrip()
    if num == '0': break
    if num[:len(num)//2] == num[-1:-(len(num)//2 + 1):-1]:
        print('yes')
    else:
        print('no')