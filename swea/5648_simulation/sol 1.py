T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    #원자들이 이동하다가 n+0.5의 위치에서 만나는 경우가 있으므로 그런 상황 방지를 위해 모든 좌표에 곱하기 2
    for i in range(len(arr)):
        arr[i][0] *= 2
        arr[i][1] *= 2

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    ans = 0

    for _ in range(4001):   #좌표의 범위가 -2000 ~ 2000이므로 range(4001)
        for i in range(len(arr)):   #원자들 이동
            arr[i][0] += dx[arr[i][2]]
            arr[i][1] += dy[arr[i][2]]

        ddel, v = set(), set()  #이동 후 좌표가 같은 원자들이 있다면 충돌한 것. ddel는 지울 좌표들을 담을 용도
        for i in range(len(arr)):
            cx, cy = arr[i][0], arr[i][1]
            if (cx, cy) in v:   #이미 v에 해당 좌표가 들어있다면 ddel에 추가
                ddel.add((cx,cy))
            v.add((cx, cy))

        #arr를 역순으로 검토하면서 해당 좌표가 ddel에 들어있다면 그 에너지만큼 더해주고 arr에서 삭제
        for i in range(len(arr)-1, -1, -1):
            if (arr[i][0], arr[i][1]) in ddel:
                ans += arr[i][3]
                arr.pop(i)

        if len(arr) < 2:    #가지치기. arr에 원자 정보가 하나만 남아있다면 충돌할 일이 없기 때문에 중단
            break
    print(f'#{tc} {ans}')