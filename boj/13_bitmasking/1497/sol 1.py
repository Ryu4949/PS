N, M = map(int, input().split())
songs = [0] * N
for i in range(N):
    a, b = input().split()
    for j in range(M):
        if b[j] == 'Y':
            songs[i] += (1<<j)

ans = M+1
song = 0
for i in range(1<<N):
    cnt = 0
    total = 0
    for j in range(N):
        if i & (1<<j):
            total |= songs[j]
            cnt += 1

    if total > song:
        song = total
        ans = cnt
    elif total == song:
        ans = min(ans, cnt)


if song == 0:
    print(-1)
else:
    print(ans)