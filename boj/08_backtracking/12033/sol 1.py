T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    #정상가격표와 할인가격표를 담아줄 리스트
    normal = []
    discount = []
    
    #체크했는지 확인
    visited = [False] * 2 * N

    #2중 for문으로 전체를 다 돌면서
    for i in range(2*N):
        for j in range(2*N):
            #정상-할인 관계 발견하면 각각 리스트에 추가해주고 반복 중단하고 다음 가격표 탐색
            if i != j and not visited[i] and not visited[j] and price[i] == price[j] * 3 // 4:
                visited[i] = True
                visited[j] = True
                normal.append(price[j])
                discount.append(price[i])
                break

    print(f'Case #{tc}:', *discount)

