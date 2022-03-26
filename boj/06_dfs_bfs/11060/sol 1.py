from collections import deque

N = int(input())
maze = list(map(int, input().split()))
visited = [-1] * len(maze)

def bfs():
    queue = deque([0])
    visited[0] = 0

    while queue:
        v = queue.popleft()

        for i in range(1, maze[v]+1):
            vv = v + i

            if vv < len(maze) and visited[vv] == -1:
                visited[vv] = visited[v] + 1
                queue.append(vv)

bfs()

print(visited[-1])