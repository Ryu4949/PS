'''
최초의 사고 방향은 공통조상 찾기
먼저 루트 노드에서 각 리프노드로의 거리를 구하고,
리프 노드 두개를 잡고 전체 거리를 더한 다음에, 최초의 공통 조상을 찾아서
루트노드로부터 그 공통조상까지의 거리의 2배를 뺀다. 이 방법을 반복하고 거리가 최대가 되는 거리를 도출
하지만 말로만해도 복잡하기 때문에 안함

결국 1967번 그림에서 힌트를 받았다. 약간 모빌? 같이 생겨서 저걸 손으로 잡는 상상을 해봤는데,
예를 들어 두 노드 사이의 거리가 최대가 아닌 리프노드를 잡았다고 치자. 그러면 밑으로 주렁주렁 내려갈 것이다
정도에 차이는 있겠지만 내가 잡아서 당긴 두 리프노드가 지름이 아니라면, 내가 당기고 있는 그 길이보다 길게 늘어질 것이다
그래서 일단 지름을 이루는 두 노드 중 하나는 아무 두 리프노드나 잡아서 늘어뜨렸을 때 가장 밑으로 내려가는 것이 된다.
그렇게 한점을 특정하고 나면 나머지 하나는 그 점에서 탐색을 해서 거리가 가장 먼 노드를 택하면 된다
'''

from collections import deque

N = int(input())
tree = [[] for _ in range(N+1)]

def bfs(v):
    distance = [-1] * (N+1)
    queue = deque([v])
    distance[v] = 0

    while queue:
        v = queue.popleft()

        for i in tree[v]:
            if distance[i[0]] == -1:
                distance[i[0]] = distance[v] + i[1]
                queue.append(i[0])

    return (max(distance), distance.index(max(distance)))

for _ in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

one_end = bfs(1)[1]

print(bfs(one_end)[0])

