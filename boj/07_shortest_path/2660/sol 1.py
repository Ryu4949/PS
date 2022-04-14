N = int(input())
distance = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            distance[i][j] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    distance[a-1][b-1] = 1
    distance[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

candidates = []
for i in range(N):
    candidates.append((i+1, max(distance[i])))

score = min(candidates, key=lambda x: x[1])[1]
cnt = 0
for i in candidates:
    if i[1] == score:
        cnt += 1

print(score, cnt)
for i in candidates:
    if i[1] == score:
        print(i[0], end=' ')