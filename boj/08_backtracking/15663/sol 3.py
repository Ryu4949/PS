import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
rlt = []
visited = [False] * N

def perm(i):
    if i == M:
        print(*rlt)
        return

    #트리 형태를 생각했을 때, 가로 방향으로 같은 순열이 나오는 것을 방지
    last = 0
    for j in range(len(lst)):
        if not visited[j] and lst[j] != last:
            rlt.append(lst[j])
            visited[j] = True
            last = lst[j]
            perm(i+1)
            rlt.pop()
            visited[j] = False

perm(0)
