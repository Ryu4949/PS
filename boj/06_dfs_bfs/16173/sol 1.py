N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
graph = [[False] * N for _ in range(N)]

def jelly(r, c):
    if r >= N or c >= N or r < 0 or c < 0:
        return False

    if graph[r][c] == False:
        graph[r][c] = True

        jelly(r+board[r][c], c)
        jelly(r, c+board[r][c])

jelly(0, 0)

if graph[N-1][N-1] == True:
    print("HaruHaru")
else:
    print("Hing")