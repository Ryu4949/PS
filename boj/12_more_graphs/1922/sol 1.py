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

N = int(input())
M = int(input())
wires = [[*map(int, input().split())] for _ in range(M)]
parent = [i for i in range(N+1)]

wires.sort(key=lambda x: x[2])

ans = 0
for i in range(M):
    if find(wires[i][0]) != find(wires[i][1]):
        union(wires[i][0], wires[i][1])
        ans += wires[i][2]

print(ans)