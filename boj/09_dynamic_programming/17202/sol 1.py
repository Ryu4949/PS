A = input()
B = input()
dp = [0] * 16
for i in range(8):
    dp[2*i] = int(A[i])
    dp[2*i + 1] = int(B[i])

while True:
    dp2 = []
    for i in range(len(dp)-1):
        dp2.append((dp[i]+dp[i+1])%10)

    dp = dp2[:]

    if len(dp) == 2:
        break

print(str(dp[0])+str(dp[1]))
