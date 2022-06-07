#12015와 같은 풀이

import sys
input = sys.stdin.readline

def LIS(n):
    if not L or n > L[-1]:
        L.append(n)
        return

    start = 0
    end = len(L)-1
    idx = 0
    while start <= end:
        mid = (start+end)//2
        if n <= L[mid]:
            idx = mid
            end = mid-1
        else:
            start = mid+1
    L[idx] = n
    return

N = int(input())
nums = [*map(int, input().split())]

L = []

for num in nums:
    LIS(num)

print(len(L))
