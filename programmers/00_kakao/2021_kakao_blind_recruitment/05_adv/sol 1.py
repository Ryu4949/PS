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

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))