import sys
input = sys.stdin.readline

N = int(input())
homeworks = []

for _ in range(N):
    d, w = map(int, input().split())
    homeworks.append((d, w))

homeworks.sort(key=lambda x: (-x[0], -x[1]))
day = homeworks[0][0]
score = 0

while day > 0:
    max_score = 0
    idx = -1
    for i in range(len(homeworks)):
        if homeworks[i][0] >= day and homeworks[i][1] > max_score:
            max_score = homeworks[i][1]
            idx = i

    score += max_score
    day -= 1
    if idx >= 0:
        homeworks.pop(idx)

print(score)
