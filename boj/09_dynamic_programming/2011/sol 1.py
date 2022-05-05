def find_code(i):
    cnt = 0
    if code[i] != '0':
        cnt += dp[i-1]

    if 10<= int(code[i-1]+code[i]) <=26:
        cnt += dp[i-2]

    return cnt

code = input()
N = len(code)
dp = [0] * (N+2)

if code[0] == '0':
    print(0)
    exit()
else:
    dp[0] = 1

if N>=2:
    if code[1] != '0':
        dp[1] += 1

    if 10<=int(code[0]+code[1])<=26:
        dp[1] += 1

for i in range(2, N):
    dp[i] = find_code(i)
    if dp[i] == 0:
        print(0)
        exit()

print(dp[N-1]%1000000)
