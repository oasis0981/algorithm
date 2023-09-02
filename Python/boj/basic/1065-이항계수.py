def Hansu(x):
    if x//10 == 0 or x//100 == 0:
        return True
    else:
        digits = []
        num = x
        for i in range(3,0,-1):
            digit = num // 10 ** (i-1)
            digits.append(digit)
            num = num - (digit * 10 ** (i-1))
        if digits[0]-digits[1] == digits[1]-digits[2]:
            return True
        else:
            return False


n = int(input())
cnt = 0
for i in range(1, n+1):
    if Hansu(i) == True:
        cnt += 1

print(cnt)