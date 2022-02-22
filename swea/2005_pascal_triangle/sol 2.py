T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = [[0]*(i+1) for i in range(N)]

    array[0][0] = 1
    for i in range(1, N):
        for j in range(len(array[i])):
            #왼쪽 위에 값이 있으면 더해주고 없으면 pass
            if j-1 >= 0:
                array[i][j] += array[i-1][j-1]
            #오른쪽 위에 값이 있으면 더해주고 없으면 pass
            if j < len(array[i])-1:
                array[i][j] += array[i-1][j]

    print(f'#{tc}')
    for i in array:
        for j in i:
            print(j, end=" ")
        print()