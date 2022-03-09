import sys
input = sys.stdin.readline

ans = list(map(int, input().split()))
N = len(ans)
rlt = []
cnt = 0

def test(i):
    global cnt

    for j in range(2, len(rlt)):
        if rlt[j] == rlt[j-1] == rlt[j-2]:
            return

    if i == 10:
        scr = 0
        for j in range(10):
            if rlt[j] == ans[j]:
                scr += 1
        if scr >= 5:
            cnt += 1
        return

    for j in range(1, 6):
        rlt.append(j)
        test(i+1)
        rlt.pop()

test(0)

print(cnt)