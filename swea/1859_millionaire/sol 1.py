#fail

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    price = list(map(int, input().split()))
    act = ['sell'] * n

    for i in range(len(price)):
        for j in range(i+1, n):
            if price[i] < price[j]:
                act[i] = 'buy'
                break

    cnt = 0
    money = 0
    for i in range(n):
        if act[i] == 'buy':
            cnt += 1
            money -= price[i]
        else:
            money += cnt * price[i]
            cnt = 0

    print(f'#{tc} {money}')