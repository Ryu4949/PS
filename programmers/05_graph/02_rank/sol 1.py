def solution(n, results):
    answer = 0
    INF = 10*3
    distance = [[INF] * (n+1) for _ in range(n+1)]
    for S, E in results:
        distance[S][E] = 1

    for i in range(n+1):
        distance[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if distance[i][j] != INF or distance[j][i] != INF:
                cnt += 1

        if cnt == n:
            answer += 1

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.10ms, 10.3MB)
테스트 2 〉	통과 (0.23ms, 10.2MB)
테스트 3 〉	통과 (0.58ms, 10.1MB)
테스트 4 〉	통과 (3.83ms, 10.2MB)
테스트 5 〉	통과 (10.58ms, 10.2MB)
테스트 6 〉	통과 (34.10ms, 10.2MB)
테스트 7 〉	통과 (99.35ms, 10.2MB)
테스트 8 〉	통과 (217.23ms, 10.6MB)
테스트 9 〉	통과 (269.39ms, 10.5MB)
테스트 10 〉	통과 (274.69ms, 10.6MB)
'''


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))