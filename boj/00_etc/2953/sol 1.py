winner = -1
max_score = 0
for i in range(1, 6):
    scores = list(map(int, input().split()))
    score = sum(scores)
    if score > max_score:
        winner = i
        max_score = score

print(winner, max_score)