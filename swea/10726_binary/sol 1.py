def binary(r, n):
    for _ in range(r):
        if n % 2 == 0:
            return "OFF"
        n //= 2

    return "ON"

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {binary(N, M)}')