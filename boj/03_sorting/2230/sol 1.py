import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()

answer = 10**10
i = 0
j = 1

while i < N and j < N:
    tmp = nums[j] - nums[i]
    if tmp == M:
        answer = M
        break
    elif tmp > M:
        answer = min(answer, tmp)
        i += 1
    else:
        j += 1

print(answer)