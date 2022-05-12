from collections import deque

def solution(progresses, speeds):
    answer = []
    work = deque(progresses)
    N = len(speeds)
    while work:
        M = len(work)
        cnt = 0
        for i in range(M):
            work[i] += speeds[i + N - M]

        while True:
            if work and work[0] >= 100:
                work.popleft()
                cnt += 1
            else:
                break
        if cnt > 0:
            answer.append(cnt)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.42ms, 10.2MB)
테스트 3 〉	통과 (0.57ms, 10.1MB)
테스트 4 〉	통과 (0.20ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.1MB)
테스트 7 〉	통과 (1.01ms, 10.3MB)
테스트 8 〉	통과 (0.06ms, 10.2MB)
테스트 9 〉	통과 (0.35ms, 10.2MB)
테스트 10 〉	통과 (0.37ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
'''