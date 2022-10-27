N = int(input())
seats = [0]*101
cnt = 0

people = list(map(int, input().split()))
for person in people:
    if not seats[person]:
        seats[person] = 1
    else:
        cnt += 1

print(cnt)