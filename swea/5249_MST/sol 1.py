T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [[*map(int, input().split())] for _ in range(E)]
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(V+1)]

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

    ans = 0
    for i in edges:
        if find(i[0]) != find(i[1]):
            union(i[0], i[1])
            ans += i[2]
    print(f'#{tc} {ans}')