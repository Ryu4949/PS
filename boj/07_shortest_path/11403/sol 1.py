INF = int(1e9)

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
graph = [[INF] * N for _ in range(N)]

#이 문제에서는 한 노드에서 같은 노드로는 연결이 안되어있는걸로 쳐서 여기를 없애야 답이 나오더라구요
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             graph[i][j] = 0

#여기는 그래프 입력받는 부분(0이면 INF고 간선이 있으면 1)
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            graph[i][j] = board[i][j]

for k in range(N):
    for r in range(N):
        for c in range(N):
            graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])

for i in range(N):
    for j in range(N):
        if graph[i][j] != INF:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()