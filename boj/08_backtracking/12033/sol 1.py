T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    normal = []
    discount = []
    visited = [False] * 2 * N

    for i in range(2*N):
        for j in range(2*N):
            if i != j and not visited[i] and not visited[j] and price[i] == price[j] * 3 // 4:
                visited[i] = True
                visited[j] = True
                normal.append(price[j])
                discount.append(price[i])
                break

    print(f'Case #{tc}:', *discount)

