D, N, M = map(int, input().split())
stone = [int(input()) for _ in range(N)]
stone.extend([0, D])
stone.sort()

def check(array, gap):
