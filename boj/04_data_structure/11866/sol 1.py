from collections import deque

N, K = map(int, input().split())
people = deque([i for i in range(1, N+1)])
rid = []

now = 0
while people:
    a = people.popleft()
    now += 1
    if now == K:
        now = 0
        rid.append(a)
    else:
        people.append(a)

if N != 1:
    for i in range(N):
        if i == 0:
            print(f'<{rid[i]}, ', end='')
        elif i == N-1:
            print(f'{rid[i]}>')
        else:
            print(f'{rid[i]}, ', end='')
else:
    print('<1>')