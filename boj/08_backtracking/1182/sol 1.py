import sys
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

def subtotal(i, total):
    global cnt
    if i == N:
        if total == S:
            cnt += 1
        return

    subtotal(i+1, total)
    subtotal(i+1, total + lst[i])

subtotal(0, 0)

if S == 0:
    cnt -= 1

print(cnt)