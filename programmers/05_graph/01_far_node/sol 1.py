from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for S, E in edge:
        graph[S].append(E)
        graph[E].append(S)

    q = deque([1])
    visited[1] = 1
    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1

    return visited.count(visited[v])

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 9.93MB)
테스트 3 〉	통과 (0.04ms, 10.1MB)
테스트 4 〉	통과 (0.24ms, 10.1MB)
테스트 5 〉	통과 (0.56ms, 10.3MB)
테스트 6 〉	통과 (1.64ms, 10.6MB)
테스트 7 〉	통과 (15.32ms, 16.8MB)
테스트 8 〉	통과 (25.86ms, 20.2MB)
테스트 9 〉	통과 (25.97ms, 20MB)
'''

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))