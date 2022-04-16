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
univ = [0] + list(input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

parent = [i for i in range(N+1)]

ans = 0
cnt = 0
for i in edges:
    if univ[i[0]] != univ[i[1]] and find(i[0]) != find(i[1]):
        union(i[0], i[1])
        ans += i[2]
        cnt += 1

# for i in range(1, N):
#     if find(i) != find(i+1):
#         print(-1)
# else:
#     print(ans)

if cnt == N-1:
    print(ans)
else:
    print(-1)