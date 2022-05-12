def solution(money):
    answer = 0
    N = len(money)
    dp1 = [0] * N  # 첫번째 집 털때
    dp2 = [0] * N  # 첫번째 집 안털 때

    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2, N - 1):
        dp1[i] = max(dp1[i - 2] + money[i], dp1[i - 1])

    dp2[1] = money[1]
    for i in range(2, N):
        dp2[i] = max(dp2[i - 2] + money[i], dp2[i - 1])

    print(dp1)
    print(dp2)
    return max(dp1[-2], dp2[-1])

print(solution([1, 2, 3, 1]))
print(solution([1, 2, 3, 1, 5]))
print(solution([1, 1, 4, 1, 4]))
print(solution([1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000]))
print(solution([1000, 1, 0, 1, 2, 1000, 0]))

'''
정확성  테스트
테스트 1 〉	통과 (0.45ms, 10.1MB)
테스트 2 〉	통과 (0.60ms, 10.1MB)
테스트 3 〉	통과 (0.31ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.1MB)
테스트 5 〉	통과 (0.15ms, 10.2MB)
테스트 6 〉	통과 (0.54ms, 10.1MB)
테스트 7 〉	통과 (0.46ms, 10.1MB)
테스트 8 〉	통과 (0.20ms, 10.1MB)
테스트 9 〉	통과 (0.57ms, 10.1MB)
테스트 10 〉	통과 (0.21ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (582.09ms, 92.4MB)
테스트 2 〉	통과 (541.09ms, 87MB)
테스트 3 〉	통과 (569.86ms, 90.4MB)
테스트 4 〉	통과 (570.21ms, 91.1MB)
테스트 5 〉	통과 (471.92ms, 77.1MB)
테스트 6 〉	통과 (537.73ms, 87.6MB)
테스트 7 〉	통과 (337.46ms, 55.5MB)
테스트 8 〉	통과 (301.17ms, 56.7MB)
테스트 9 〉	통과 (387.69ms, 64.7MB)
테스트 10 〉	통과 (585.08ms, 88.5MB)
'''