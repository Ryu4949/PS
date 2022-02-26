N = int(input())
stone = [0] + list(map(int, input().split()))
S = int(input())
visited = [False] * (N+1)

dc = [-1, 1]

def dfs(c):
    visited[c] = True

    for i in range(2):
        cc = c + dc[i]*stone[c]
        if 1<=cc<N+1 and not visited[cc]:
            dfs(cc)

dfs(S)

print(visited.count(True))