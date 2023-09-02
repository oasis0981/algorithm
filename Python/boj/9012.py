import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x = input().rstrip()
    while True:
        if '()' in x:
            idx = x.find('()')
            new_x = x[:idx] + x[idx+2:]
            x = new_x
            if len(x) == 0:
                print('YES')
                break
        else:
            print('NO')
            break
