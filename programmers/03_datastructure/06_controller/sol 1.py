import heapq

def solution(jobs):
    answer = 0
    N = len(jobs)
    jobs.sort(reverse=True)
    waiting = []
    on_process = []
    time = 0
    while jobs or waiting or on_process:
        if on_process and on_process[0][2] == time:
            finish = on_process.pop()
            answer += finish[2]-finish[1]

        if jobs:
            job = jobs.pop()
            if job[0] > time:
                jobs.append(job)
            else:
                heapq.heappush(waiting, [job[1], job[0]])

        if waiting and not on_process:
            now = heapq.heappop(waiting)
            on_process.append(now+[now[0]+time])
        time += 1

    return answer//N

print(solution([[0, 3], [1, 9], [2, 6]]))

'''
정확성  테스트
테스트 1 〉	통과 (27.06ms, 10.3MB)
테스트 2 〉	통과 (25.25ms, 10.3MB)
테스트 3 〉	통과 (20.72ms, 10.1MB)
테스트 4 〉	통과 (19.39ms, 10.2MB)
테스트 5 〉	통과 (24.57ms, 10.2MB)
테스트 6 〉	통과 (1.11ms, 10.2MB)
테스트 7 〉	통과 (35.24ms, 10.3MB)
테스트 8 〉	통과 (18.63ms, 10.3MB)
테스트 9 〉	통과 (5.83ms, 10.2MB)
테스트 10 〉	통과 (27.64ms, 10.2MB)
테스트 11 〉	통과 (0.07ms, 10.3MB)
테스트 12 〉	통과 (0.10ms, 10.2MB)
테스트 13 〉	통과 (0.09ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.3MB)
테스트 15 〉	통과 (0.12ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.4MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.4MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
'''