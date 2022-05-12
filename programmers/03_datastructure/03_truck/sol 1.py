from collections import deque
def solution(bridge_length, weight, truck_weights):
    N = len(truck_weights)
    waiting = deque(truck_weights)
    on_bridge = deque([0]*bridge_length)
    w = 0
    cnt = 0
    time = 0

    while cnt != N:
        time += 1
        down = on_bridge.popleft()
        w -= down
        if down > 0:
            cnt += 1

        if waiting and w+waiting[0] <= weight:    #트럭이 더이상 못올라감감
            truck = waiting.popleft()
            w += truck
            on_bridge.append(truck)
        else:
            on_bridge.append(0)

    return time

print(solution(2, 10, [7,4,5,6]))

'''
정확성  테스트
테스트 1 〉	통과 (0.50ms, 10.3MB)
테스트 2 〉	통과 (8.10ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (6.08ms, 10.2MB)
테스트 5 〉	통과 (60.46ms, 10.3MB)
테스트 6 〉	통과 (18.14ms, 10.4MB)
테스트 7 〉	통과 (0.38ms, 10.3MB)
테스트 8 〉	통과 (0.08ms, 10.2MB)
테스트 9 〉	통과 (2.22ms, 10.4MB)
테스트 10 〉	통과 (0.10ms, 10.4MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.15ms, 10.4MB)
테스트 13 〉	통과 (0.63ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
'''