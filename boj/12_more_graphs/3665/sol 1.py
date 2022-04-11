from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        if len(queue) >= 2: #큐에 담긴 개수가 2개 이상이 되면 X
            return "IMPOSSIBLE"

        v = queue.popleft()
        result.append(v)

        for j in graph[v]:
            indegree[j] -= 1

            if indegree[j] == 0:
                queue.append(j)

    if len(result) != N:    #사이클이 발생하는 경우
        return "IMPOSSIBLE"

    return result

T = int(input())
for _ in range(T):
    N = int(input())
    indegree = [0] * (N+1)
    pre = list(map(int, input().split()))   #전년도 순위

    graph = [[] for _ in range(N+1)]
    for i in range(N-1):
        for j in range(i+1, N): #전년도의 모든 순위 관계를 그래프에 추가, 진입차수에 반영
            graph[pre[i]].append(pre[j])
            indegree[pre[j]] += 1

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        if b in graph[a]:   #상대순위 바뀐 두 번호는 간선정보 조정해주고, 진입차수도 조정
            graph[a].remove(b)
            graph[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1

    ans = topology_sort()
    if type(ans) == list:
        print(*ans)
    else:
        print(ans)