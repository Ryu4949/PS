import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = [*map(int, input().split())]

prefix_sum = [0] * (N+1)
for i in range(1, N+1):
    prefix_sum[i] = num_list[i-1] + prefix_sum[i-1]

for _ in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])