'''
리스트를 입력받을 때 시간을 유의미하게 줄여주는 방법
일차원 뿐만 아니라 N x N 차원에도 적용
'''

#1. 일반적인 방법
N = 30
lst = [list(map(int, input().split())) for _ in range(N)]

#2. 효과적인 방법
lst2 = [[*map(int, input().split())] for _ in range(N)]
