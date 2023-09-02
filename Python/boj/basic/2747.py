#피보나치 수열

n = int(input())

fibo = [0, 1]

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(2, n+1):
        new_fibo = fibo[i - 2] + fibo[i - 1]
        fibo.append(new_fibo)
    print(fibo[n])