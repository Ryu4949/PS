N, M = map(int, input().split())
teammates = [0] * M
for i in range(M):
    questions = [*map(int, input().split())]
    q = 0
    for j in range(1, questions[0]+1):
        q += 2**(questions[j]-1)

    teammates[i] = q

ans = M+1
for i in range(1<<M):
    cnt = 0
    total = 0
    for j in range(M):
        if i & (1<<j):
            total |= teammates[j]
            cnt += 1

    if total == 2**N-1:
        ans = min(ans, cnt)

if ans == M+1:
    print(-1)
else:
    print(ans)