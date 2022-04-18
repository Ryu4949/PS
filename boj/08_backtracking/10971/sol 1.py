def travel(i, start, last, c):
    global ans
    if c > ans:
        return

    if i == N-1:
        if costs[last][start]:
            ans = min(ans, c+costs[last][start])
        return

    for j in range(N):
        if not visited[j] and costs[last][j]:
            visited[j] = True
            travel(i+1, start, j, c+costs[last][j])
            visited[j] = False

N = int(input())
costs = [[*map(int, input().split())] for _ in range(N)]
visited = [False] * N

ans = 10**8

for i in range(N):
    visited[i] = True
    travel(0, i, i, 0)
    visited[i] = False

print(ans)