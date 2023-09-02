N = int(input())

i = 1
while True:
    if N <= 1 + 6 * (i * (i - 1) / 2):
        print(i)
        break
    else:
        i += 1