T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    a_last_num = a % 10
    new_b = b % 4
    if b % 4 == 0:
        new_b = 4
    for j in range(1, 5):
        if a_last_num == 0:
            print(10)
            break
        elif new_b == j:
            computer_num = a_last_num ** j % 10
            print(computer_num)


