#1번 노드에서 다른 노드들까지 가는 최단 경로 저장하기
from pprint import pprint

N, M = map(int, input().split())
distance = [[float('inf')] * (N+1) for _ in range(N+1)]
path = [[[] for _ in range(N+1)] for _ in range(N+1)]

#간선 정보를 입력받으면서 경로에도 같이 추가
#이 문제의 경우 출발점은 경로에 포함시키지 않고 있으므로 그 점 고려
for _ in range(M):
    a, b, c = map(int, input().split())
    distance[a][b] = c
    path[a][b].append(b)
    distance[b][a] = c
    path[b][a].append(a)

#자기 자신으로의 거리는 0
for i in range(N+1):
    for j in range(N+1):
        if i == j:
            distance[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            #최단거리가 갱신될 때 경로도 바꿔준다
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                path[i][j] = path[i][k] + [j]

# pprint(path)
# pprint(distance)

for i in range(1, N+1):
    for j in range(1, N+1):
        if not path[i][j]:
            print('-', end =' ')
        else:
            print(path[i][j][0], end=' ')
    print()
