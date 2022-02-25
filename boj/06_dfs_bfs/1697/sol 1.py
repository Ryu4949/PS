#수빈이의 위치가 X일 때
#걸으면 1초후에 X-1 or X+1
#순간이동 하면 2*X
from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001
loc = [0] * 100001

def bfs():
    queue = deque([N])
    visited[N] = True
    loc[N] = 0

    while queue:
        x = queue.popleft()
        for i in range(3):
            if i == 0:
                xx = x - 1
            elif i == 1:
                xx = x + 1
            else:
                xx = 2 * x
            if 0<=xx<100001 and visited[xx] == False:
                queue.append(xx)
                visited[xx] = True
                loc[xx] = loc[x] + 1
        if visited[K] == True:
            return loc[K]

print(bfs())
