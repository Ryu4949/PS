import heapq

def solution(scoville, K):
    answer = 0
    if scoville.count(0) >= 2:
        return -1

    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1:
            if scoville[0] >= K:
                return answer
            else:
                return -1

        scv1 = heapq.heappop(scoville)
        scv2 = heapq.heappop(scoville)
        if scv1 >= K:
            return answer

        heapq.heappush(scoville, scv1+2*scv2)
        answer += 1

print(solution([1, 2, 3, 9, 10, 12], 7))

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.44ms, 10.2MB)
테스트 7 〉	통과 (0.37ms, 10.2MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.29ms, 10.4MB)
테스트 11 〉	통과 (0.19ms, 10.2MB)
테스트 12 〉	통과 (0.66ms, 10.2MB)
테스트 13 〉	통과 (0.36ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.46ms, 10.4MB)
테스트 16 〉	통과 (0.01ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (179.65ms, 16.2MB)
테스트 2 〉	통과 (379.09ms, 21.9MB)
테스트 3 〉	통과 (1543.64ms, 49.8MB)
테스트 4 〉	통과 (142.22ms, 14.9MB)
테스트 5 〉	통과 (1841.13ms, 51.8MB)
'''