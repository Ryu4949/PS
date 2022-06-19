import sys
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]
X = int(input())

nums.sort()

i = 0
j = N-1
cnt = 0

while True:
    tmp = nums[i] + nums[j]
    if tmp == X:
        cnt += 1
        i += 1
        j -= 1
    elif tmp > X:
        j -= 1
    else:
        i += 1

    if i >= j:
        break

print(cnt)