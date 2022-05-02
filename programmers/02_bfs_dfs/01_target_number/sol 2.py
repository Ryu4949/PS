def solution(numbers, target):
    N = len(numbers)
    ans = 0
    stack = [(0, 0)]

    while stack:
        summ, cnt = stack.pop()
        if cnt == N:
            if summ == target:
                ans += 1
            continue

        for i in [1, -1]:
            stack.append((summ + numbers[cnt] * i, cnt + 1))

    return ans