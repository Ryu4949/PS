from collections import deque

N = int(input())
command = []
for _ in range(N):
    command.append(list(input().split()))

q = deque()

for i in command:
    if 'push' in i:
        q.append(i[1])
    elif 'pop' in i:
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif 'size' in i:
        print(len(q))
    elif 'empty' in i:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in i:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    else:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
