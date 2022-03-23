D, N, M = map(int, input().split())
rock = [0, D]
for _ in range(N):
    rock.append(int(input()))

rock.sort()

#점프거리 최소값이 주어졌을 때 그 최소값을 유지하면서 최대 몇번 점프할 수 있는지를 체크
def check(jump):
    cnt = 0
    i = 0
    j = 1
    while True:
        if j == len(rock):
            return cnt

        if rock[j] - rock[i] >= jump:
            cnt += 1
            i = j
            j = i+1
        else:
            j += 1

#시작값은 1로 잡고, 최대는 탈출구까지의 거리
start = 1
end = D

ans = 0
while start <= end:
    mid = (start + end) // 2

    #만약 중간값을 점프거리의 최소값으로 했을 때,
    #그 때 점프할 수 있는 횟수가 전체 돌섬에서 M개만큼 제거한 개수에 1을 더한것보다 크거나 같아야함
    #(마지막 탈출구도 밟아야 하니까 1을 더함)
    #이 조건을 만족한다면 ans에 값을 저장해놓고, 점프거리의 최소값을 늘려봄
    if check(mid) >= N-M+1:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)