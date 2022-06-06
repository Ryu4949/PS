import sys
input = sys.stdin.readline

N = int(input())
nums_list = [*map(int, input().split())]
answer = 0

while True:
    cnt = 0

    if sum(nums_list) == 0:
        break

    for i in range(N):
        if nums_list[i]%2:
            nums_list[i] -= 1
            cnt += 1
    answer += cnt

    if cnt == 0:
        nums_list = list(map(lambda x: x//2, nums_list))
        answer += 1

print(answer)