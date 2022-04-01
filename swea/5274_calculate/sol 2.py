from collections import deque

def bfs():
    queue = deque([N])
    visited[N] = 0

    while queue:
        n = queue.popleft()

        for i in [1, -1, n, -10]:
            rlt = n+i

            if 0<rlt<=1000000 and visited[rlt] == -1:
                queue.append(rlt)
                visited[rlt] = visited[n]+1

            if rlt == M:
                return

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [-1] * 1000001

    bfs()

    print(f'#{tc} {visited[M]}')
