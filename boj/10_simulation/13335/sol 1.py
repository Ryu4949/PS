import sys
from collections import deque
input = sys.stdin.readline

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

        if waiting and w+waiting[0] <= weight:
            truck = waiting.popleft()
            w += truck
            on_bridge.append(truck)
        else:
            on_bridge.append(0)

    return time

N, W, L = map(int, input().split())
weights = [*map(int, input().split())]

print(solution(W, L, weights))