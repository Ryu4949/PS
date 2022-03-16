def inorder(v):
    if v <= N:
        inorder(v * 2)
        print(tree[v], end='')
        inorder(v * 2 + 1)

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    for _ in range(N):
        data = list(input().split())
        tree[int(data[0])] = data[1]

    print(f'#{tc} ', end='')
    inorder(1)
    print()