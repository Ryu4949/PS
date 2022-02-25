from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
cnt = [0] * (N+1)

#[start]번 컴퓨터를 해킹했을 때
#최종적으로 해킹된 컴퓨터의 개수를 True를 세서 반환
def bfs(start, graph):
    visited = [False] * (N+1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return visited.count(True)

#모든 컴퓨터에서 bfs를 실시해서 해킹된 컴퓨터의 개수 저장
for i in range(1, N+1):
    cnt[i] = bfs(i, graph)

#최대개수와 개수가 같은 컴퓨터의 번호를 모두 출력
max_cnt = max(cnt)
for i in range(1, N+1):
    if cnt[i] == max_cnt:
        print(i, end=" ")
