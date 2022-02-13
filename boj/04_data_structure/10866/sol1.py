from collections import deque

N = int(input())
command = []
for _ in range(N):
    command.append(list(input().split()))

q = deque()

for i in command:
    if 'push_front' in i:
        q.appendleft(i[1])
    elif 'push_back' in i:
        q.append(i[1])
    elif 'pop_front' in i:
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif 'pop_back' in i:
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
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
