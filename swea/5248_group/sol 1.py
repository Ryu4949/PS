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
for tc in range(1, T+1):
    N, M = map(int, input().split())
    buddy = [*map(int, input().split())]
    parent = [i for i in range(N+1)]

    for i in range(M):
        union(buddy[2*i], buddy[2*i+1])

    rlt = []
    for i in range(1, N+1):
        rlt.append(find(i))

    print(f'#{tc} {len(set(rlt))}')