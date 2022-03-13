import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 바이러스를 놓을 수 있는 위치를 저장하는 리스트
virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i, j))

# virus에서 M개를 뽑는 조합의 리스트
virus_comb = list(combinations(virus, M))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(arr):
    # arr에 있는 좌표들의 시간을 0으로
    queue = deque(arr)
    for i in queue:
        check[i[0]][i[1]] = 0

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r + dr[i], c + dc[i]

            # 다음 이동 위치가 범위내이고 아직 방문하지 않은 경우
            if 0 <= rr < N and 0 <= cc < N and check[rr][cc] == -1:
                # 그 위치가 벽이 아니라면
                if graph[rr][cc] == 0 or graph[rr][cc] == 2:
                    # 시간을 기존 위치에서 +1 한 값으로 갱신해주고 좌표를 큐에 추가
                    check[rr][cc] = check[r][c] + 1
                    queue.append((rr, cc))

    # 탐색을 끝냈는데 벽이 아니면서 바이러스가 퍼지지 않은 곳이 있다면 큰 수를 반환
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 1 and check[i][j] == -1:
                return float('inf')

    # 벽이 아닌 모든 곳에 퍼졌다면 최종적으로 걸린 시간을 반환
    # 이때 비활성 바이러스가 활성으로 바뀌는데는 시간이 소요되지 않으므로 여기는 제외하고 찾는다
    time = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 2:
                time = max(time, check[i][j])

    return time

# 각 조합마다 bfs를 실행하면서 최소 시간 찾기
ans = float('inf')
for i in virus_comb:
    check = [[-1] * N for _ in range(N)]
    ans = min(ans, bfs(i))

# 최소 시간이 큰 수라면 어떤 조합으로 바이러스를 놓아도 모든 칸에 퍼질 수 없다는 뜻이므로 -1 출력
if ans == float('inf'):
    print(-1)
else:
    print(ans)