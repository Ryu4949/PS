T = int(input())
for _ in range(T):
    N = int(input())
    candidates = [[*map(int, input().split())] for _ in range(N)]
    candidates.sort()

    interview = candidates[0][1]
    cnt = 1
    for i in range(1, N):
        if candidates[i][1] > interview:
            pass
        else:
            cnt += 1
            interview = candidates[i][1]

    print(cnt)