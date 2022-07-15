def cal_distance(a, b):
    ax, ay = a
    bx, by = b
    return ((ax-bx)**2 + (ay-by)**2)**(1/2)

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

min_distance = 10**9
answer = None

for i in range(N):
    max_distance = 0
    max_point = None
    for j in range(N):
        if cal_distance(points[i], points[j]) > max_distance:
            max_distance = cal_distance(points[i], points[j])
            max_point = points[j]

    if max_distance < min_distance:
        min_distance = max_distance
        answer = points[i]

print(*answer)