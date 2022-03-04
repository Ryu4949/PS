import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1e9)
distance = [INF] * (N+1)
graph = []

for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

#음의 간선 사이클이 존재하는지를 판단하는 함수
def bellman_ford(start):
    distance[start] = 0
    #N번 반복할건데
    for i in range(N):
        #그 반복마다 모든 간선을 다볼거야
        for j in range(M):
            cur_node, next_node, cost = graph[j]

            #확인하는 간선의 출발노드로의 최단거리가 한번이라도 계산된 경우에만
            #더 짧은 거리가 있다면 최단거리 갱신
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + cost:
                distance[next_node] = distance[cur_node] + cost

                #만약 N번째 반복에서 최단거리가 갱신된다면 음의 간선 사이클이 존재!
                if i == N-1:
                    return True
    #N번째 반복에서 최단거리가 갱신되지 않았다면 음의 간선 사이클 존재 X
    return False

#출발점에서 함수 돌려주고
negative_cycle = bellman_ford(1)

#반환값이 True면 음의 간선 사이클이 존재하므로 -1 출력
if negative_cycle:
    print('-1')
else:
    for i in range(2, N+1):
        if distance[i] == INF:
            print('-1')
        else:
            print(distance[i])