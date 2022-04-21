import sys
input = sys.stdin.readline

N = int(input())
costs = [[*map(int, input().split())] for _ in range(N)]
INF = int(1e6)

dp = [INF] * (1<<N)

dp[0] = 0

for i in range(1<<N):   #i는 일의 진행 상황을 나타냄. i를 이진수로 나타냈을 때 101이라면 1번일, 3번일이 처리된 것
    # k는 이번에 일해야 할 일꾼을 나타냄. 일꾼이 일하는 순서는 상관이 없기 때문에,
    # 현재까지 2개의 일이 처리됐다면 세번째 일꾼이 일해야 할 차례로 보는 것
    k = bin(i).count('1')

    for j in range(N):  #0~N-1번까지 모든 일을 확인하면서
        #아직 j번 일이 처리되지 않았고, 그 일을 k번 일꾼이 했을 때 비용이 절감된다면 dp 테이블을 갱신
        if i & (1<<j) == 0 and dp[i|(1<<j)] > dp[i] + costs[k][j]:
            dp[i|(1<<j)] = dp[i] + costs[k][j]

print(dp[-1])