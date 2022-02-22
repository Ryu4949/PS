T = int(input())
for tc in range(1, T+1):
    n = int(input())
    memo = [0] * 31
    memo[1] = 1
    memo[2] = 3

    for i in range(3, 31):
        memo[i] = memo[i-1] + memo[i-2] * 2
    print(f'#{tc} {memo[n//10]}')