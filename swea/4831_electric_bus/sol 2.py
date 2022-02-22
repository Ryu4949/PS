#DP

#정류장 0 ~ 10
#충전기 위치[1, 3, 5, 7, 9]
K, N, M = map(int, input().split())
memo = [0] * (N+1)
charge = list(map(int, input().split()))

def dp(charge):
    for i in range(K+1):
        memo[i] = 0

    for i in range(K+1, N+1):
        for j in charge:
            if j in range(i-K, i+1):
                memo[i] = memo[i-K] + 1
                print(f'i: {i}, j: {j}')
                print(memo)
                print('--------------------------')
                break
        else:
            print(f'i: {i}, j: {j}')
            return 0
    return memo[N]

print(dp(charge))



