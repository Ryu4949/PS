N = int(input())
points = []
for _ in range(N):
    a, b = map(int, input().split())
    points.append((a, b))

points.sort(key=lambda x: (x[1], x[0]))

for point in points:
    print(*point)