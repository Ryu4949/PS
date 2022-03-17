'''
부모-자식 2행으로 리스트 만들고
어떤 노드의 가장 먼 부모? 조상?이 선택된 노드면 cnt + 1
'''

#루트노드를 찾는 함수. 해당 노드의 루트 노드가 설정된 루트노드와 같으면 cnt 1 증가
def find_root(v):
    global cnt
    if v == N:
        cnt += 1
        return
    for i in range(1, V + 1):
        if child_1[i] == v or child_2[i] == v:
            find_root(i)

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    V = E+1

    #왼쪽 자식과 오른쪽 자식의 노드번호를 저장할 리스트
    child_1 = [0] * (V+1)
    child_2 = [0] * (V+1)

    #간선정보로부터 자식노드 입력하기. 리스트의 인덱스가 부모노드의 번호
    for i in range(len(edges)//2):
        parent_node = edges[2*i]
        child_node = edges[2*i+1]

        if child_1[parent_node] == 0:
            child_1[parent_node] = child_node
        else:
            child_2[parent_node] = child_node

    cnt = 0
    for i in range(1, V+1):
        find_root(i)

    print(f'#{tc} {cnt}')