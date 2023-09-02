N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
adj_scores = []
for i in range(N):
    adj_scores.append(scores[i] / M * 100)
adj_avg = sum(adj_scores) / N
print(adj_avg)