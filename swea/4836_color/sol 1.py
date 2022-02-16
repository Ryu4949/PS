t = int(input())
for num in range(1, t + 1):
    n = int(input())
    board = [[0] * 10 for _ in range(10)]
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    #입력받은 데이터에 해당하는 범위에 색칠할 색과 대응되는 수(각 줄의 마지막 값)를 더해줌
    #같은 색인 영역이 겹치지 않기 때문에 별도의 조건은 필요없음
    for i in data:
        for j in range(i[0], i[2] + 1):
            for k in range(i[1], i[3] + 1):
                board[j][k] += i[-1]

    #색을 다 칠하고 나면 빨간색과 파란색 모두 칠해진 곳은 값이 3이므로 3의 개수를 카운트
    cnt = 0
    for i in board:
        for j in i:
            if j == 3:
                cnt += 1
    print(f'#{num} {cnt}')