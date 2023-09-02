# 세 정수 중앙값 구하기 2

def med3a(a,b,c):
    if (b>=a and c<=a) or (b<=a and c>=a):
        return a
    elif (a>b and c<b) or (a<b and c>b):
        return b
    return c

print("세 정수의 중앙값")
a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))
print("중앙값: ", med3a(a,b,c))

"""
median.py보다 비효율적이다.
b>=a, b<=a 판단이 끝난 후에 elif에서 또다시 a와 b에 대한 판단을 하고 있기 때문
"""