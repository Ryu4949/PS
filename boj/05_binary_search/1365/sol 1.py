import sys
input = sys.stdin.readline

N = int(input())
codes = [*map(int, input().split())]

L = []

for code in codes:
    if not L or L[-1] < code:
        L.append(code)
    else:
        start = 0
        end = len(L)-1
        idx = 0
        while start <= end:
            mid = (start + end) // 2
            if code <= L[mid]:
                idx = mid
                end = mid - 1
            else:
                start = mid + 1
        L[idx] = code

print(N-len(L))
