N = int(input())
M = 1000-N
cnt = 0

money = [500, 100, 50, 10, 5, 1]
for i in money:
    cnt += M//i
    M %= i

print(cnt)