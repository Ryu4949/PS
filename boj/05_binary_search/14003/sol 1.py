import sys
input = sys.stdin.readline

def LIS(n):
    if not L or n > L[-1]:
        location.append(len(L))
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
    location.append(idx)
    return

N = int(input())
nums = [*map(int, input().split())]

L = []
location = []
lis = []

for num in nums:
    LIS(num)

print(len(L))
l = len(L)-1
for i in range(N-1, -1, -1):
    if location[i] == l:
        lis.append(nums[i])
        l -= 1

lis.reverse()
print(*lis)

