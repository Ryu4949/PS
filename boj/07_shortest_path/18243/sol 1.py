#모든 사람들이 6단계 이내로 연결되어있는지 보고 싶으므로 플로이드-와샬 알고리즘을 이용한다

#마지막에 작은 세상 네트워크를 만족하는지 판단해줄 함수
def is_small_word(array):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if array[i][j] > 6:
                return "Big World!"

    return "Small World!"

N, K = map(int, input().split())
INF = int(1e9)

#그래프의 기본값은 INF, 사람의 번호와 인덱스를 맞춰주기 위해 N+1만큼 만들어줌
graph = [[INF] * (N+1) for _ in range(N+1)]

#자기 자신과의 거리는 0
for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0

#따로 방향이 없으므로 양쪽 모두를 바꿔주고, 몇명을 거치는지를 세주기 위해서 거리는 1로 설정
for _ in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

print(is_small_word(graph))