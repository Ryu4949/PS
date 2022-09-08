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

N, M, t = map(int, input().split())
roads = []
for _ in range(M):
    s, e, d = map(int, input().split())
    roads.append((s, e, d))

roads.sort(key=lambda x: x[2])
parent = [i for i in range(N+1)]

ans = 0

for i in roads:
    if find(i[0]) != find(i[1]):
        union(i[0], i[1])
        ans += i[2]

ans += (N-2)*(N-1)*t//2

print(ans)