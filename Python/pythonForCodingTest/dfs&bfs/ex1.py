'''

최대공약수 계산(유클리드 호제법)
- 두 자연수 a,b에 대해(a>b) a를 b로 나눈 나머지를 r이라고 한다.
- 이때 a,b 최대공약수는 b,r최대공약수와 같다

'''

# GCD : 최대공약수

def gcd(a,b):
    if a%b == 0:
        return b
    return(gcd(b, a%b))

print(gcd(164,144))