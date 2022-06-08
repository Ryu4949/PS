import sys
input = sys.stdin.readline

def check(h):
    cnt = 0
    for i in range(N):
        if not i%2:
            if obstacles[i] >= h:
                cnt += 1
        else:
            if H-obstacles[i] < h:
                cnt += 1
    return cnt

N, H = map(int, input().split())
obstacles = [int(input()) for _ in range(N)]

start = 1
end = H

min_destroy = N
while start <= end:
    mid = (start+end)//2
    new = check(mid)
    if new < min_destroy:
        min_destroy = new
        end = mid - 1
    else:
        start = mid + 1

sections = 0
for height in range(1, H+1):
    if check(height) == min_destroy:
        sections += 1

print(min_destroy, sections)