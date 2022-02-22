N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

#방문처리를 할 N x N 리스트
graph = [[False] * N for _ in range(N)]

#시작할 위치의 행과 열의 인덱스를 인자로 받고
def jelly(r, c):

    #만약 범위를 벗어난다면 False를 반환
    if r >= N or c >= N or r < 0 or c < 0:
        return False

    #인덱스가 범위 내인데 False라면 즉 아직 방문처리가 되지 않았다면
    if graph[r][c] == False:
        
        #해당 위치의 graph에 방문처리를 해주고
        graph[r][c] = True

        #그 위치의 값만큼 오른쪽, 아래로 이동한 곳을 계속해서 탐색
        jelly(r+board[r][c], c)
        jelly(r, c+board[r][c])

#(0, 0)을 시작 위치로 깊이 우선 탐색 시행
jelly(0, 0)

#시행을 마치고 (N-1, N-1) 위치에 방문처리가 되었다면 haruharu, 아니라면 hing
if graph[N-1][N-1] == True:
    print("HaruHaru")
else:
    print("Hing")