import sys
input = sys.stdin.readline

def mode(lst):
    cnt = [[0]*2 for _ in range(8001)]
    for n in lst:
        cnt[n][0] = n
        cnt[n][1] += 1

    cnt.sort(key=lambda x:(-x[1],x[0]))
    if cnt[0][1] == cnt[1][1]:
        return cnt[1][0]
    else:
        return cnt[0][0]

N = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()

print(round(sum(nums)/N))
print(nums[N//2])
print(mode(nums))
print(nums[-1]-nums[0])
