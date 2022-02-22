T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = [[0]*(i+1) for i in range(N)]

    for i in range(0, N):
        n = len(array[i])
        for j in range(n):
            # 각행의 처음과 끝이면 1
            if j == 0 or j == n-1:
                array[i][j] = 1

            # 아니라면 왼쪽과 오른쪽 위의 숫자의 합
            else:
                array[i][j] = array[i-1][j-1] + array[i-1][j]

    print(f'#{tc}')
    for i in array:
        for j in i:
            print(j, end=" ")
        print()