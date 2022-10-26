N, K = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

costs = []
for i in range(N-1):
    costs.append(heights[i+1]-heights[i])

costs.sort()

print(sum(costs[:N-K]))