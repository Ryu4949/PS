import heapq
T = int(input())
for _ in range(T):
    N = int(input())
    max_heap = []
    min_heap = []
    visited = []
    idx = 0

    for _ in range(N):
        i = input()

        if i[0] == "I":
            num = int(i[2:])
            heapq.heappush(max_heap, (-num, idx))
            heapq.heappush(min_heap, (num, idx))
            idx += 1
            visited.append(False)
        else:
            if max_heap and len(i) == 3:
                while max_heap:
                    mx = heapq.heappop(max_heap)
                    if not visited[mx[1]]:
                        visited[mx[1]] = True
                        break
            elif min_heap and len(i) == 4:
                while min_heap:
                    mn = heapq.heappop(min_heap)
                    if not visited[mn[1]]:
                        visited[mn[1]] = True
                        break
    INF = 10**10
    max_value = INF
    min_value = INF
    while max_heap:
        a = heapq.heappop(max_heap)
        if visited[a[1]] == False:
            max_value = -a[0]
            break

    while min_heap:
        b = heapq.heappop(min_heap)
        if visited[b[1]] == False:
            min_value = b[0]
            break

    if max_value == INF:
        print('EMPTY')
    else:
        print(max_value, min_value)
