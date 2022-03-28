T = int(input())
for _ in range(T):
    N = int(input())
    info = list(map(int, input().split()))
    price = info[-1]
    profit = 0

    for i in range(N-2, -1, -1):
        if info[i] > price:
            price = info[i]
        else:
            profit += price-info[i]

    print(profit)