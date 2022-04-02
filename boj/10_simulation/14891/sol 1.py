from collections import deque

#톱니바퀴 움직이는 함수
def move_saw(saw, direction):
    if direction == 1:
        saw.appendleft(saw.pop())
    else:   #direction == -1일 때
        saw.append(saw.popleft())

saws = []
for _ in range(4):
    saws.append(deque(input()))

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    visited = [False] * 4
    queue = deque([(a-1, b)])
    work = [(a-1, b)]
    visited[a-1] = True

    while queue:
        a, b = queue.popleft()

        for i in [-1, 1]:
            aa = a+i
            if 0<=aa<4:
                if i == -1 and not visited[aa] and saws[a][6] != saws[aa][2]:
                    queue.append((aa, -b))
                    visited[aa] = True
                    work.append((aa, -b))
                elif i == 1 and not visited[aa] and saws[a][2] != saws[aa][6]:
                    queue.append((aa, -b))
                    visited[aa] = True
                    work.append((aa, -b))

    for r, c in work:
        move_saw(saws[r], c)

ans = 0
for i in range(4):
    if saws[i][0] == '1':
        ans += 2**i

print(ans)