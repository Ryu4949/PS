T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    info = list(map(int, input().split()))

    # 입력받은 가격 정보를 뒤에서부터 검토
    profit = 0

    # j는 판매 가격을 나타내는 인덱스인데, 뒤에서부터 앞으로 가면서
    # j번째 인덱스의 가격보다 낮은 가격에 대해서는 그 차이만큼 더해주고
    # j번째 인덱스의 가격보다 큰 가격을 만나면, j를 그 때의 인덱스로 교체해줌
    j = n - 1
    for i in range(n - 1, -1, -1):
        if info[i] <= info[j]:
            profit += info[j] - info[i]
        else:
            j = i

    print(f'#{tc} {profit}')