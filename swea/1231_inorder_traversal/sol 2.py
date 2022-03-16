def inorder(v):
    if v:
        inorder(ch_1[v])
        print(tree[v], end='')
        inorder(ch_2[v])

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    ch_1 = [0] * (N+1)
    ch_2 = [0] * (N+1)

    for _ in range(N):
        data = list(input().split())
        tree[int(data[0])] = data[1]

        if len(data) == 3:
            ch_1[int(data[0])] = int(data[2])
        elif len(data) == 4:
            ch_1[int(data[0])] = int(data[2])
            ch_2[int(data[0])] = int(data[3])

    print(f'#{tc} ', end='')
    inorder(1)
    print()