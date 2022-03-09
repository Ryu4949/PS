'''
증량 증가량이 주어지면 각각에서 K를 뺀 리스트를 새로 생성
0에서부터 하나씩 더해줄건데 음수가 되는 순간 return
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weight = list(map(int, input().split()))
for i in range(N):
    weight[i] -= K
cnt = 0
sum_weight = 0
visited = [False] * N

def perm(i):
    global cnt, sum_weight

    if sum_weight < 0:
        return

    if i == N:
        if sum_weight >= 0:
            cnt += 1
            return

    for j in range(N):
        if not visited[j]:
            sum_weight += weight[j]
            visited[j] = True
            perm(i+1)
            sum_weight -= weight[j]
            visited[j] = False

perm(0)
print(cnt)