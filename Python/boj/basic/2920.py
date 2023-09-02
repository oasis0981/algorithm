#음계 판별하기

melody = list(map(int, input().split()))

if sorted(melody) == melody:
    print("ascending")
elif sorted(melody, reverse=True) == melody:
    print("descending")
else:
    print("mixed")