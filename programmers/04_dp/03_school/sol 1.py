from collections import deque


def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)]
    for i in puddles:
        graph[i[1] - 1][i[0] - 1] = -1
    dr = [0, 1]
    dc = [1, 0]
    dp = [[0] * m for _ in range(n)]

    queue = deque([(0, 0)])
    dp[0][0] = 1

    while queue:
        r, c = queue.popleft()
        for i in range(2):
            rr, cc = r + dr[i], c + dc[i]
            if 0 <= rr < n and 0 <= cc < m and graph[rr][cc] != -1:
                if dp[rr][cc] == 0:
                    queue.append((rr, cc))
                dp[rr][cc] += dp[r][c]

    return dp[n - 1][m - 1] % 1000000007

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 9.99MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.27ms, 10.1MB)
테스트 6 〉	통과 (0.12ms, 10.1MB)
테스트 7 〉	통과 (0.11ms, 10.1MB)
테스트 8 〉	통과 (0.44ms, 10.2MB)
테스트 9 〉	통과 (0.11ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (7.79ms, 10.4MB)
테스트 2 〉	통과 (3.44ms, 10.3MB)
테스트 3 〉	통과 (4.15ms, 10.2MB)
테스트 4 〉	통과 (6.04ms, 10.4MB)
테스트 5 〉	통과 (4.66ms, 10.3MB)
테스트 6 〉	통과 (7.74ms, 10.3MB)
테스트 7 〉	통과 (3.71ms, 10.4MB)
테스트 8 〉	통과 (5.72ms, 10.5MB)
테스트 9 〉	통과 (6.05ms, 10.5MB)
테스트 10 〉	통과 (6.50ms, 10.4MB)
'''