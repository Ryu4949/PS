import sys
input = sys.stdin.readline

def log_to_point(p):
    return (int(p[1])-1, ord(p[0])-65)

def point_to_log(x, y):
    return chr(y+65)+str(x+1)

direction = {'B': 0, 'T': 1, 'L': 2, 'R': 3, 'LB': 4, 'RB': 5, 'RT': 6, 'LT': 7}
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]

board = [[0]*8 for _ in range(8)]
king, stone, N = input().rstrip().split()
kx, ky = log_to_point(king)
sx, sy = log_to_point(stone)

for _ in range(int(N)):
    d = input().rstrip()
    nkx = kx+dr[direction[d]]
    nky = ky+dc[direction[d]]
    nsx = sx+dr[direction[d]]
    nsy = sy+dc[direction[d]]

    if nkx == sx and nky == sy:
        if 0<=nsx<8 and 0<=nsy<8:
            sx, sy, kx ,ky = nsx, nsy, nkx, nky

    else:
        if 0<=nkx<8 and 0<=nky<8:
            kx, ky = nkx, nky

print(point_to_log(kx, ky))
print(point_to_log(sx, sy))