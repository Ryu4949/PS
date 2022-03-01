N = int(input())
INF = int(1e9)
friends = [list(input()) for _ in range(N)]
graph = [[INF] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0
        if friends[i][j] == 'Y':
            graph[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

max_2_friends = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        #직접 친구인 경우와 한단계 건너 친구인 경우
        if 0<graph[i][j]<=2:
            cnt += 1
    max_2_friends = max(cnt, max_2_friends)

print(max_2_friends)