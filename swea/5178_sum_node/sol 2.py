T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    #노드의 현재 값 - 왼쪽 자식 - 오른쪽 자식 - 부모노드
    tree = [0] * (N+1)

    #리프노드의 값 입력받기
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    #끝에서부터 현재 값을 부모 노드의 값에 더하기
    for i in range(N, 1, -1):
        tree[i//2] += tree[i]

    print(f'#{tc} {tree[L]}')