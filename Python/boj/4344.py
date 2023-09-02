C = int(input())
for i in range(C):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]
    cnt = 0
    for k in range(1, scores[0]+1):
        if scores[k] > avg:
            cnt += 1
    rate = cnt / scores[0] * 100
    print("%0.3f%%" %rate)
