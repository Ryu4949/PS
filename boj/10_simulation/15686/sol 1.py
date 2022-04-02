from itertools import combinations
def chicken_dist(lst, loc):
    min_dist = float('inf')
    for i in lst:
        for j in lst:
            min_dist = min(min_dist, abs(loc[0]-i[0])+abs(loc[1]-i[1]))
    return min_dist

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])

ans = float('inf')
for i in range(1, M+1):
    chicken_lst = list(combinations(chicken, i))
    for j in chicken_lst:
        dist = 0
        for k in house:
            dist += chicken_dist(j, k)
        ans = min(ans, dist)

print(ans)
