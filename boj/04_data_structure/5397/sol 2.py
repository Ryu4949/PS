from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    keylogs = input().rstrip()
    left = []
    right = deque()

    for k in keylogs:
        if k == '<':
            if left:
                right.appendleft(left.pop())
        elif k == '>':
            if right:
                left.append(right.popleft())
        elif k == '-':
            if left:
                left.pop()
        else:
            left.append(k)

    print(''.join(left)+''.join(right))