T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    #각각 내림차순 정렬
    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    #최대 무게
    rlt = 0

    #무거운순으로 컨테이너를 확인하면서, 그것을 실을 수 있는 트럭이 있다면 바로 실어주고
    #아니면 다음 컨테이너 확인
    j = 0
    for i in range(N):
        if containers[i] <= trucks[j]:
            rlt += containers[i]
            j += 1

        #모든 컨테이너를 확인하기 전에 트럭을 다 사용했다면 중단
        if j == M:
            break

    print(f'#{tc} {rlt}')