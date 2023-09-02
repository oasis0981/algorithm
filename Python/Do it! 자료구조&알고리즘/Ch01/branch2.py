# 4개로 분기하는 조건문

n = int(input("정수를 입력: "))

if n ==1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')
# else:
#     pass

'''
위 프로그램은 3개로 분기하는 것 같지만, 사실 마지막 else부분이 생략된것
사실상 4개로 분기하는 프로그램이다.
'''