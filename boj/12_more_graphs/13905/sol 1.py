def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
s, e = map(int, input().split())
edges = [[*map(int, input().split())] for _ in range(M)]
parent = [i for i in range(N+1)]

edges.sort(reverse=True, key=lambda x: x[2])

ans = 10**7
for i in edges:
    if find(i[0]) != find(i[1]):
        union(i[0], i[1])
        ans = min(ans, i[2])

    if find(s) == find(e):
        break

if find(s) != find(e):
    print(0)
else:
    print(ans)