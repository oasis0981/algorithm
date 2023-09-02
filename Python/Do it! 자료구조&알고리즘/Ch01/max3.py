# 세 정수의 최댓값 구하기

print('세 정수의 최댓값을 구합니다')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

max = a
if b > max : max = b
if c > max : max = c

print(f'최댓값 : {max}')
