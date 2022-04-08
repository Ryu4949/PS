N = int(input())
graph = [[0] * N for _ in range(N)]
friends = [[*map(int, input().split())] for _ in range(N**2)]
friends.sort()

print(friends)

def find_seat():
    like = 0
    empty = 0
