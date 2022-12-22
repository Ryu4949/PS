problems = []
for i in range(1, 9):
    score = int(input())
    problems.append((i, score))

problems.sort(key=lambda x: -x[1])

total_score = 0
total_score_nums = []

for i in range(5):
    total_score += problems[i][1]
    total_score_nums.append(problems[i][0])

total_score_nums.sort()

print(total_score)
print(*total_score_nums)