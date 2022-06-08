import sys
input = sys.stdin.readline

N, H = map(int, input().split())
obstacles = [[] , []]
for i in range(N):
    obstacles[i%2].append(int(input()))

obstacles[0].sort()
obstacles[1].sort()

min_destroy = N+1
cnt = 0
for i in range(1, H+1):
    tmp = 0
    for j in range(2):
        height = i if j == 0 else H-i+1
        start = 0
        end = N//2-1
        loc = N//2
        while start <= end:
            mid = (start+end)//2
            if obstacles[j][mid] >= height:
                loc = mid
                end = mid-1
            else:
                start = mid+1
        tmp += (N//2)-loc
    if tmp < min_destroy:
        min_destroy = tmp
        cnt = 1
    elif tmp == min_destroy:
        cnt += 1

print(min_destroy, cnt)