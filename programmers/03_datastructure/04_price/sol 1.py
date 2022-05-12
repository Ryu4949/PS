def solution(prices):
    N = len(prices)
    answer = [0] * N
    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            answer[i] += 1
            if prices[j] < prices[i]:
                break

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.66ms, 10.4MB)
테스트 4 〉	통과 (0.72ms, 10.4MB)
테스트 5 〉	통과 (0.97ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.84ms, 10.2MB)
테스트 8 〉	통과 (0.48ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.93ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (153.44ms, 18.8MB)
테스트 2 〉	통과 (106.65ms, 17.4MB)
테스트 3 〉	통과 (190.73ms, 19.2MB)
테스트 4 〉	통과 (134.59ms, 18.3MB)
테스트 5 〉	통과 (91.04ms, 16.8MB)
'''