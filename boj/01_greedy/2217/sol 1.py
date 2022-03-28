#주어진 로프를 내림차순으로 정렬했을 때, N번쨰 로프까지 사용해서 들 수 있는 최대 무게는
#N번째 로프가 견딜 수 있는 중량 x N

N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort(reverse=True)
weight = [0] * N
for i in range(N):
    weight[i] = (i+1) * rope[i]

print(max(weight))