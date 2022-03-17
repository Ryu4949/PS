#이진탐색트리를 중위순회하면 오름차순 정렬이 된다는 성질 이용
#중위순회하는 함수인데 출력이 아니라 해당 노드에 현재까지 전체 트리에 저장된 값보다 1 큰 수를 저장함
def inorder(v):
    if v <= N:
        inorder(v * 2)
        tree[v] = max(tree) + 1
        inorder(v * 2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)

    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')