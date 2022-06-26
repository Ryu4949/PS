def check(n):
    cnt = 1
    tmp = 0
    for i in range(K-1):
        if tmp >= n:
            cnt += 1
            tmp = 0
        tmp += intervals[i]
    if tmp >= n:
        cnt += 1

    if cnt >= M:
        return True
    return False

N, M, K = map(int, input().split())
referees = [*map(int, input().split())]
answer = ['0'] * K
intervals = []
for i in range(K-1):
    intervals.append(referees[i+1]-referees[i])

start = 1
end = referees[-1] - referees[0]

intv = 0
while start <= end:
    mid = (start+end)//2
    if check(mid):
        intv = mid
        start = mid + 1
    else:
        end = mid - 1

answer[0] = '1'
itv = 0
c = 1
for i in range(K-1):
    itv += intervals[i]
    if itv >= intv:
        answer[i+1] = '1'
        c += 1

        if c == M:
            break
        itv = 0

print(''.join(answer))