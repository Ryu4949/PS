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

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]
    ans = 0

    for _ in range(M):
        a, b = map(int, input().split())
        if find(a) != find(b):
            union(a, b)
            ans += 1

    print(ans)
