T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [0] + list(map(int, input().split()))

    tree = [0] * (N+1)

    for i in range(1, N+1):
        #우선 새로운 노드를 추가하고
        tree[i] = data[i]

        #현재의 마지막 노드부터 돌면서 조건에 맞지 않으면 값을 서로 바꿔줌
        for j in range(i, 1, -1):
            if tree[j//2] >= tree[j]:
                tree[j//2], tree[j] = tree[j], tree[j//2]

    #v는 마지막 노드, ans에는 v의 조상노드에 저장된 값을 더해줄 변수
    v = N
    ans = 0

    #v노드는 포함되지 않으므로 먼저 부모노드를 찾기 위해 v는 2로 나눈 몫이되고
    #이때 v가 0이되면 중단
    #0이 아니면 그 노드에 저장된 값을 ans에 더함
    while True:
        v //= 2
        if v == 0:
            break
        ans += tree[v]

    print(f'#{tc} {ans}')