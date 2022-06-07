import sys
input = sys.stdin.readline

N, M = map(int, input().split())
titles = []
for _ in range(N):
    a, b = input().split()
    titles.append((a, int(b)))

for _ in range(M):
    pow = int(input())
    start = 0
    end = N-1
    title = ''
    while start <= end:
        mid = (start+end)//2
        if pow <= titles[mid][1]:
            end = mid-1
            title = titles[mid][0]
        else:
            start = mid+1
    print(title)
