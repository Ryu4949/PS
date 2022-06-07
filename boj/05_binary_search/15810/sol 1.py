import sys
input = sys.stdin.readline

def check(limit):
    cnt = 0
    for i in time:
        cnt += limit//i
    if cnt >= M:
        return True
    else:
        return False

N, M = map(int, input().split())
time = [*map(int, input().split())]

start = 0
end = 10**12

answer = 0
while start <= end:
    mid = (start+end)//2
    if check(mid):
        answer = mid
        end = mid-1
    else:
        start = mid+1

print(answer)