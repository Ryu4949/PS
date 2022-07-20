from collections import defaultdict

room = input()
nums = defaultdict(int)
for i in room:
    if i == '9':
        nums['6'] += 1
    else:
        nums[i] += 1

nums['6'] = nums['6']//2+1 if nums['6']%2 else nums['6']//2

print(max(nums.values()))