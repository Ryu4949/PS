N = int(input())

memo = [0] * (N+1)

def paper():
    if N == 1:
        return 1
    elif N == 2:
        return 3
    else:
        memo[1] = 1
        memo[2] = 3

        for i in range(3, N+1):
            memo[i] = memo[i - 1] + memo[i - 2] * 2
        return memo[N]

print(paper()%10007)