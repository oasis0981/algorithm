t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    if n % h != 0:
        room_num = (n // h) + 1
        room_floor = n % h
    else:
        room_num = n // h
        room_floor = h
    room = (room_floor * 100) + room_num
    print(room)