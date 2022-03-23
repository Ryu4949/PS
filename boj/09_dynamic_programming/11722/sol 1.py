'''
뭔소리여? 아 이해함
'''

N = int(input())
nums = list(map(int, input().split()))
#무조건 수열의 길이는 1 이상이니까 1로 초기화
d = [1] * N

for i in range(1, N):
    for j in range(i):
        if nums[j] > nums[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))
