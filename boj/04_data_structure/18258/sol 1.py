from collections import deque
import sys

N = int(input())
q = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        q.append(command[1])