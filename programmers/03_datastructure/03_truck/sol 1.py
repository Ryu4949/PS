from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting = deque(truck_weights)
    on_bridge = deque()
    w = 0
    cnt = 0
    time = 0
    while waiting:
        truck = waiting.popleft()
        on_bridge.append(truck)
        w += truck
        cnt += 1
        time += 1

        if cnt > bridge_length or w >

    return answer