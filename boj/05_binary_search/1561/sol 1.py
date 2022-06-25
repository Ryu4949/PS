import sys
input = sys.stdin.readline

def check(t):   #마지막 학생이 놀이기구에 탑승하는 시간 찾기위한 함수
    cnt = 0
    for play in plays:
        cnt += (t//play)+1
    if cnt >= N:
        return True
    return False

N, M = map(int, input().split())
plays = [*map(int, input().split())]

start = 1
end = 10**11

last = 0
while start <= end:
    mid = (start + end)//2
    if check(mid):
        last = mid
        end = mid - 1
    else:
        start = mid + 1

if N <= M:  #학생이 놀이기구 수 이하이면, 앞에서부터 순서대로 탑승
    print(N)
else:
    cnt = 0
    idx = []    #마지막 학생이 탑승하는 시간에 놀이기구에 탑승할 수 있는 최대 학생수와 비교하여, 뒤에서부터 마지막으로 이용한 놀이기구가 어떤건지 찾음
    for i in range(M):
        cnt += (last//plays[i])+1
        if not last%plays[i]:
            idx.append(i+1)
    print(idx[N-cnt-1])