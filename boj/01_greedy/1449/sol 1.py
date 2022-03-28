'''
테이프로 누수를 막을 때 간격을 좌우 0.5씩 줘야하기 때문에
길이 L인 테이프로 한번에 막을 수 있는 거리는 L-1
'''

N, L = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()

cnt = 0
start = 0
for i in range(N):
    if leak[i] - leak[start] >= L:
        cnt += 1
        start = i

print(cnt+1)