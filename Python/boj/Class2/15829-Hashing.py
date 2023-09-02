# https://www.acmicpc.net/problem/15829
# 문자열이 주어졌을 때 해싱 함수 결과 출력하기

l = int(input())
words = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
r = 31
m = 1234567891
result = 0

for i in range(l):
    idx = alphabet.index(words[i])+1
    hash = idx * (r ** i)
    result += hash

print(int(result) % m)
