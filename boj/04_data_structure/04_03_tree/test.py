def preorder(v):
    if v:
        print(v, end=' ')
        preorder(ch_1[v])
        preorder(ch_2[v])


N = int(input())
ch_1 = [0] * (N+1)
ch_2 = [0] * (N+1)

edge = list(map(int, input().split()))
for i in range(N-1):
    a = edge[2*i]
    b = edge[2*i + 1]
    if ch_1[a] == 0:
        ch_1[a] = b
    else:
        ch_2[a] = b

preorder(1)
