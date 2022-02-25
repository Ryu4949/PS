T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bit = [[0] * N for _ in range(N)]
    for i in range(N):
        bit[i][i] = 1
    data = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9999999

    def sum_sub(i):
        global min_sum

        each_sum = 0
        for x in range(i):
            for y in range(N):
                each_sum += bit[x][y] * data[x][y]

        if each_sum > min_sum:
            return

        if i == N:
            min_sum = each_sum
            return

        else:
            for j in range(1, N):
                bit[i], bit[j] = bit[j], bit[i]
                sum_sub(i+1)
                bit[i], bit[j] = bit[j], bit[i]

    sum_sub(0)

    print(f'#{tc} {min_sum}')