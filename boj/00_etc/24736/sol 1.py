score = [6, 3, 2, 1, 2]
scores = []

for _ in range(2):
    s = 0
    points = [*map(int, input().split())]
    for i in range(5):
        s += score[i]*points[i]
    scores.append(s)

print(*scores)