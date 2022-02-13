from itertools import permutations
N = int(input())
K = int(input())
nums = []
for _ in range(N):
    nums.append(input())

cards = []
for i in list(permutations(nums, K)):
    cards.append(''.join(i))

print(len(set(cards)))