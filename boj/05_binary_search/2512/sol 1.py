N = int(input())
budget = list(map(int, input().split()))
M = int(input())

start = 0
end = M

rlt = 0
while start <= end:
    sum_budget = 0
    mid = (start + end) // 2
    for i in budget:
        sum_budget += min(i, mid)
    if sum_budget <= M:
        rlt = mid
        start = mid + 1
    else:
        end = mid - 1

budget_list = []
for i in budget:
    budget_list.append(min(i, rlt))

print(max(budget_list))