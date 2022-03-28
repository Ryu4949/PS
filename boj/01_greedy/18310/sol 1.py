'''
위치상 가운데 있는 곳
'''

N = int(input())
antenna = list(map(int, input().split()))
antenna.sort()

if N % 2:
    print(antenna[N//2])
else:
    print(antenna[N//2 - 1])