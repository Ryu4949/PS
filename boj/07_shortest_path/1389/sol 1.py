#18243과 똑같은 문제?

N, M = map(int, input().split())
INF = int(1e9)

#그래프의 기본값은 INF, 사람의 번호와 인덱스를 맞춰주기 위해 N+1만큼 만들어줌
graph = [[INF] * (N+1) for _ in range(N+1)]

#자기 자신과의 거리는 0
for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0

#따로 방향이 없으므로 양쪽 모두를 바꿔주고, 몇명을 거치는지를 세주기 위해서 거리는 1로 설정
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

idx = 0
rlt = INF
for i in range(1, N+1):
    kevin = sum(graph[i]) - graph[i][0]
    if kevin < rlt:
        rlt = kevin
        idx = i

print(idx)