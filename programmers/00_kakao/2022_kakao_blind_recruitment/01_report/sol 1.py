from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_list = defaultdict(list)
    reported = defaultdict(int)

    report = set(report)

    for i in report:
        a, b = i.split(' ')
        report_list[a].append(b)
        reported[b] += 1

    print(report_list)
    print(reported)

    for i in range(len(id_list)):
        for j in report_list[id_list[i]]:
            if reported[j] >= k:
                answer[i] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))