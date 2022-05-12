def solution(triangle):
    N = len(triangle)
    for i in range(1, N):
        for j in range(i+1):
            if 0 < j < i:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            elif j == 0:
                triangle[i][j] += triangle[i-1][j]
            else:
                triangle[i][j] += triangle[i-1][j-1]

    return max(triangle[N-1])

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.1MB)
테스트 4 〉	통과 (0.29ms, 10.2MB)
테스트 5 〉	통과 (1.05ms, 10.2MB)
테스트 6 〉	통과 (0.59ms, 10.3MB)
테스트 7 〉	통과 (2.12ms, 10.2MB)
테스트 8 〉	통과 (0.38ms, 10.4MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.27ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (37.71ms, 14.1MB)
테스트 2 〉	통과 (27.44ms, 13.1MB)
테스트 3 〉	통과 (40.72ms, 14.7MB)
테스트 4 〉	통과 (38.19ms, 14.1MB)
테스트 5 〉	통과 (34.02ms, 13.9MB)
테스트 6 〉	통과 (44.59ms, 14.7MB)
테스트 7 〉	통과 (47.25ms, 14.4MB)
테스트 8 〉	통과 (34.81ms, 13.7MB)
테스트 9 〉	통과 (33.33ms, 13.9MB)
테스트 10 〉	통과 (42.20ms, 14.5MB)
'''