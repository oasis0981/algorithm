# a부터 b까지 정수 합 구하기(for)

'''
range(a,b,step)
이터러블 객체 : 반복할 수 있는 객체
이터러블 자료형 : list, str, tuple
'''

a = int(input('a: '))
b = int(input('b: '))

if a > b:
    a, b = b, a # a, b 오름차순 정렬

sum = 0
for i in range(a, b+1):
    sum += i

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')
