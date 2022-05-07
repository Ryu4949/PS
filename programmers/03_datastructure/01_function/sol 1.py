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