import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
num_list = list(set(lst))
lst.sort()
rlt = []

for i in num_list:
    if lst.count(i) > M:
        for _ in range(lst.count(i)-M):
            lst.remove(i)

visited = [False] * len(lst)

def perm(i):
    if i == M:
        print(*rlt)
        return

    for j in range(len(lst)):
        if not visited[j]:
            rlt.append(lst[j])
            visited[j] = True
            perm(i+1)
            rlt.pop()

perm(0)

