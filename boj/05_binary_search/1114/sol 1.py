def check(cri):
    if max(piece) > cri:    #자를 수 있는 지점간 길이가 기준으로 잡은 최대길이보다 길면 불가능
        return False

    cnt = 0 #자른 횟수
    log = 0 #통나무 길이. 자를 때마다 초기화함
    spot = 0    #처음 자른 위치
    for i in range(len(piece)-1, -1, -1):   #경우가 여러가지일 때 자른위치가 제일 앞에 있을때를 찾아야하니까 뒤에서부터 자른다
        log += piece[i]
        if log > cri:   #자르지 않고 유지한 통나무길이가 기준점 넘어서면 직전위치에서 자르고, 통나무길이 초기화
            cnt += 1
            log = piece[i]

            spot = i    #자른 위치 저장

    if cnt == C:    #이때 자른 횟수와 자를 수 있는 최대횟수가 일치한다면 바로 현재의 spot return
        return (spot,)
    elif cnt < C:   #만약 횟수가 남는다면 제일 첫지점 한번 더 자르기(경우가 여러가지면 자르는 위치가 작은 것을 출력해야 하므로)
        return (0, )
    else:
        return False

N, K, C = map(int, input().split())
cut = [*map(int, input().split())]
cut.extend([0, N])
cut = list(set(cut))
cut.sort()
piece = [cut[i+1]-cut[i] for i in range(len(cut)-1)]

start = 1
end = N

ans1 = 0    #통나무의 가장 긴 조각의 길이
ans2 = 0    #그 때의 처음 자르는 위치
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        ans1 = mid
        ans2 = check(mid)
        end = mid - 1
    else:
        start = mid + 1

print(ans1, cut[ans2[0]+1])
