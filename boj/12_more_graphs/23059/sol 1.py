from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    result = []
    queue = deque()

    for item in indegree.keys():
        if not indegree[item]:
            queue.append((item, 0))

    while queue:
        now, order = queue.popleft()
        result.append((now, order))

        for i in items[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append((i, order+1))

    if len(result) == len(indegree):
        result.sort(key=lambda x: (x[1], x[0]))
        for i in result:
            print(i[0])
    else:
        print(-1)

N = int(input())
indegree = dict()
items = dict()

for _ in range(N):
    items_lst = input().rstrip().split()
    for item in items_lst:
        if item not in indegree:
            indegree[item] = 0
            items[item] = []

    if items_lst[1] not in items[items_lst[0]]:
        items[items_lst[0]].append(items_lst[1])
        indegree[items_lst[1]] += 1

topology_sort()
