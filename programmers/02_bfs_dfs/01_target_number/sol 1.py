from collections import deque


def solution(numbers, target):
    N = len(numbers)
    ans = 0
    queue = deque()
    queue.append((0, 0))

    while queue:
        summ, cnt = queue.popleft()
        if cnt == N:
            if summ == target:
                ans += 1
            continue

        for i in [1, -1]:
            queue.append((summ + numbers[cnt] * i, cnt + 1))

    return ans