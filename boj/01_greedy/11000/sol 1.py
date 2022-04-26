import heapq

N = int(input())
lectures = [[*map(int, input().split())] for _ in range(N)]
lectures.sort()

classrooms = []

for i in lectures:
    if not classrooms:
        heapq.heappush(classrooms, i[1])
    else:
        l = heapq.heappop(classrooms)
        if i[0] >= l:
            heapq.heappush(classrooms, i[1])
        else:
            heapq.heappush(classrooms, i[1])
            heapq.heappush(classrooms, l)

print(len(classrooms))