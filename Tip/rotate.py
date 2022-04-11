#큰 2차원 배열에서 일부만 90도 회전시킬 경우
def rotate(r, c, interval): #왼쪽 위 좌표가 (r, c)이고 가로세로 길이가 interval인 배열을 회전
    for i in range(interval):
        for j in range(interval):
            graph[r+j][c+interval-i-1] = base[r+i][c+j]