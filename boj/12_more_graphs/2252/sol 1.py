from collections import deque

def topology_sort():    #위상정렬 함수
    result = []
    queue = deque()

    for i in range(1, N+1): #진입차수가 0인 노드 추가
        if indegree[i] == 0:
            queue.append(i)

    while queue:    #큐가 빌 때까지
        v = queue.popleft()
        result.append(v)

        for j in edges[v]:  #연결된 간선들 확인하면서 진입차수 1씩 감소
            indegree[j] -= 1

            if indegree[j] == 0:    #진입차수가 0이 되면 큐에 추가
                queue.append(j)

    for node in result: #순서대로 출력
        print(node, end=' ')

N, M = map(int, input().split())
indegree = [0] * (N+1)
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

topology_sort()