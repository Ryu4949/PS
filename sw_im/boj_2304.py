n = int(input())
pillars = []
for _ in range(n):
    pillars.append(list(map(int, input().split())))

#기둥을 위치 순으로 정렬.
pillars.sort(key=lambda x: x[0])

#2. 가장 높은 기둥의 idx와, 그 기둥의 높이
idx = pillars.index(max(pillars, key=lambda x:x[1]))
highest = pillars[idx][1]
total_area = highest * (pillars[-1][0]+1 - pillars[0][0])

#시작점무터 가장 높은 기둥까지
height = pillars[0][1]
start = pillars[0][0]
for i in range(1, idx+1):
    if pillars[i][1] > height:
        total_area -= (highest - height) * (pillars[i][0] - start)
        height = pillars[i][1]
        start = pillars[i][0]

#마지막 위치부터 가장 높은 기둥까지
height = pillars[-1][1]
start = pillars[-1][0]+1
for i in range(n-2, idx-1, -1):
    if pillars[i][1] > height:
        total_area -= (highest - height) * (start - pillars[i][0]-1)
        height = pillars[i][1]
        start = pillars[i][0]+1

print(total_area)

