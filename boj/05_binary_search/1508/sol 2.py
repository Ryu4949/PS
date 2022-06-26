def check(n):
    cnt = 1
    tmp = 0
    ans = ['0'] * K
    ans[0] = '1'
    for i in range(K-1):
        if tmp >= n:
            cnt += 1
            tmp = 0
            ans[i] = '1'
        tmp += intervals[i]
    if tmp >= n:
        cnt += 1
        ans[-1] = '1'

    if cnt >= M:
        while cnt > M:
            for i in range(K-1, -1, -1):
                if ans[i] == '0':
                    ans[i] = '1'
                    cnt -= 1

        return (True, ans)
    return (False,)

N, M, K = map(int, input().split())
referees = [*map(int, input().split())]
answer = [0] * K
intervals = []
for i in range(K-1):
    intervals.append(referees[i+1]-referees[i])

start = 1
end = referees[-1] - referees[0]

answer = None
while start <= end:
    mid = (start+end)//2
    a = check(mid)
    if a[0]:
        answer = a[1]
        start = mid + 1
    else:
        end = mid - 1

print(''.join(answer))