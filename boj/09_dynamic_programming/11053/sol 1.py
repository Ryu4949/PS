'''
뭔소리여?
'''

N = int(input())
nums = list(map(int, input().split()))
d = [1] * N

for i in range(1, N):
    if d[i] >= d[i-1]:
        d[i] = d[i-1] + 1

print(max(d))
