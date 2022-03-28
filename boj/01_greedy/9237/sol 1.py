N = int(input())
trees = list(map(int, input().split()))

trees.sort(reverse=True)
for i in range(1, N+1):
    trees[i-1] += i

print(max(trees)+1)