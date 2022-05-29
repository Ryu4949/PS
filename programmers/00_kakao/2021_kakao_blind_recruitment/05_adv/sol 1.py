def log_to_time(log):
    return 60*60*int(log[:2])+60*int(log[3:5])+int(log[6:8])

def solution(play_time, adv_time, logs):
    answer = ''
    total_time = [0] * 360000
    for log in logs:
        start = log[:8]
        end = log[9:]
        for i in range(log_to_time(start), log_to_time(end)):
            total_time[i] += 1
    max_value = 0
    max_s = 0
    for i in range(log_to_time(adv_time)):
        max_value += total_time[i]

    curr_value = max_value
    s = 0
    e = log_to_time(adv_time)-1
    while True:
        curr_value -= total_time[s]
        s += 1
        e += 1
        if e > log_to_time(play_time):
            break
        curr_value += total_time[e]
        if curr_value > max_value:
            max_value = curr_value
            max_s = s

    answer += (str(max_s//3600).zfill(2)+":")
    max_s %= 3600
    answer += (str(max_s//60).zfill(2)+":")
    max_s %= 60
    answer += (str(max_s).zfill(2))
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (6.13ms, 12.8MB)
테스트 2 〉	통과 (66.83ms, 13.3MB)
테스트 3 〉	통과 (225.42ms, 13.9MB)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	통과 (433.16ms, 21.3MB)
테스트 6 〉	통과 (260.27ms, 12.7MB)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	통과 (1930.13ms, 40.8MB)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	통과 (177.09ms, 12.8MB)
테스트 16 〉	실패 (시간 초과)
테스트 17 〉	실패 (시간 초과)
테스트 18 〉	통과 (751.72ms, 40.8MB)
테스트 19 〉	통과 (5.03ms, 12.7MB)
테스트 20 〉	통과 (13.05ms, 12.8MB)
테스트 21 〉	통과 (262.58ms, 21.2MB)
테스트 22 〉	통과 (247.86ms, 21.2MB)
테스트 23 〉	실패 (시간 초과)
테스트 24 〉	통과 (1009.64ms, 40.9MB)
테스트 25 〉	통과 (198.84ms, 12.8MB)
테스트 26 〉	통과 (108.57ms, 12.8MB)
테스트 27 〉	통과 (90.14ms, 12.8MB)
테스트 28 〉	통과 (56.58ms, 12.6MB)
테스트 29 〉	통과 (55.26ms, 12.7MB)
테스트 30 〉	통과 (53.98ms, 12.8MB)
테스트 31 〉	통과 (63.91ms, 12.8MB)
'''
print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))