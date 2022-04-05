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

V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
edges = [[*map(int, input().split())] for _ in range(E)]
edges.sort(key=lambda x: x[2])
ans = 0

for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c

print(ans)
