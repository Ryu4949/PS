import heapq

N, D = map(int, input().split())
distance = [float('inf')] * (D+1)
graph = [[] for _ in range(D+1)]
nodes = [0, D]

for _ in range(N):
    a, b, c = map(int, input().split())
    #지름길의 길이가 두 지점보다 길지 않고, 지름길의 끝점이 고속도로의 끝을 벗어나지 않는다면
    if c < b-a and b <= D:
        #그래프에 추가해주고
        graph[a].append((b, c))

        #a와 b가 이미 노드 목록에 존재하는 게 아니라면 각각 추가해줌
        if a not in nodes:
            nodes.append(a)

        if b not in nodes:
            nodes.append(b)

#노드 목록 오름차순 정렬
nodes.sort()

#입력에 주어지는 지름길 외에, 각 노드들간의 거리 정보를 그래프에 같이 담아줌
for i in range(len(nodes)-1):
    graph[nodes[i]].append((nodes[i+1], nodes[i+1]-nodes[i]))

#다익스트라
def dijkstra():
    q = []
    distance[0] = 0
    heapq.heappush(q, (0, 0))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost

dijkstra()

#도착점까지의 최단거리는?
print(distance[-1])