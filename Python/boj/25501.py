def recursion(s, l, r):
    global cnt # 함수 내에서 전역변수 선언, 밖에서 global로 선언하더라도 함수 내에서 한번더 해줘야함
    cnt += 1

    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1) # 0, len(s)-1은 인덱스

t = int(input())
for _ in range (t):
    s = input()
    cnt = 0
    print(isPalindrome(s),cnt)

