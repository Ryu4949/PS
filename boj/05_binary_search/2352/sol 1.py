import sys
input = sys.stdin.readline

def find_lowerbound(n):
    if not L or n > L[-1]:
        return -1

    start = 0
    end = len(L) - 1
    idx = 0
    while start <= end:
        mid = (start + end) // 2
        if n <= L[mid]:
            idx = mid
            end = mid - 1
        else:
            start = mid + 1
    return idx

N = int(input())
codes = [*map(int, input().split())]

L = []

for code in codes:
    loc = find_lowerbound(code)
    if loc == -1:
        L.append(code)
    else:
        L[loc] = code

print(len(L))