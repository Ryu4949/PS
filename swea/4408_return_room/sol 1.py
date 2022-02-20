#1, 2를 1, 3, 4를 2 ... 이런 식으로 400개의 방을 1~200으로 압축
#
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    route = [0] * 201
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a

        for i in range((a+1)//2, (b+1)//2 + 1):
            route[i] += 1

    time = 0
    for i in range(201):
        if route[i] > time:
            time = route[i]

    print(f'#{tc} {time}')