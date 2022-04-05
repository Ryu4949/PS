def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
planet = [[*map(int, input().split())] for _ in range(N)]
parent = [i for i in range(N)]

ans = 0
for i in range(N-1):
    for j in range(1, N):
        if set(planet[i]) & set(planet[j]):
            union(i, j)
            ans +=


print(ans)

'''
10000 * 10000 2차원 리스트 만들면 괜찮을까?
각 행성들 전부 어쨌든 연결이 가능하니까
거기서부터 방문처리 안된 곳중 하나씩 '''