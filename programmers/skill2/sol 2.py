def find_point(l, r):
    a, b, e = l
    c, d, f = r
    if not a*d-b*c:
        return False

    return ((b*f-e*d)/(a*d-b*c), (e*c-a*f)/(a*d-b*c))

def solution(line):
    N = len(line)
    points = []
    for i in range(N-1):
        for j in range(i+1, N):
            point = find_point(line[i], line[j])
            if point and point[0] == int(point[0]) and point[1] == int(point[1]):
                points.append((int(point[0]), int(point[1])))

    points = list(set(points))
    hs = max(points, key=lambda x: x[1])[1]
    he = min(points, key=lambda x: x[1])[1]
    we = max(points, key=lambda x: x[0])[0]
    ws = min(points, key=lambda x: x[0])[0]
    answer = [['.']*(we-ws+1) for _ in range(hs-he+1)]

    for p in points:
        answer[hs-p[1]][p[0]-ws] = '*'

    answer = list(map(lambda x: ''.join(x), answer))
    return answer

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))