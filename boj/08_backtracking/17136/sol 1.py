paper = [list(map(int, input().split())) for _ in range(10)]
confetti = [5, 5, 5, 5, 5]
cnt = [0] * 5
rlt = []

#(r, c)위치에서 가로세로 n크기의 색종이를 붙였을 때
#붙일 수 있으면 True, 없으면 False
def possible(r, c, n):
    for i in range(r, r+n):
        for j in range(c, c+n):
            if paper[i][j] == 0:
                return False
    return True

#색종이 붙일 때 처리와 원상복구 할 때 처리
def reversal(r, c, n):
    for i in range(r, r+n):
        for j in range(c, c+n):
            paper[i][j] = 1-paper[i][j]

def dfs(r, c, n):
    for i in range(5):
        if cnt[i] > confetti[i]:
            return

    if n == 0:
        for i in range(10):
            for j in range(10):
                if paper[i][j] == 1:
                    return
        rlt.append(sum(cnt))
        return

    if r == 10-n and c == 10-n:
        if possible(r, c, n):
            cnt[5-n] += 1
            reversal(r, c, n)
            dfs(0, 0, n-1)
            cnt[5-n] -= 1
            reversal(r, c, n)
        else:
            dfs(0, 0, n - 1)

    elif c == 10-n:
        if possible(r, c, n):
            cnt[5-n] += 1
            reversal(r, c, n)
            dfs(r+1, 0, n)
            cnt[5 - n] -= 1
            reversal(r, c, n)
        else:
            dfs(r + 1, 0, n)

    else:
        if possible(r, c, n):
            cnt[5 - n] += 1
            reversal(r, c, n)
            dfs(r, c+1, n)
            cnt[5 - n] -= 1
            reversal(r, c, n)
        else:
            dfs(r, c + 1, n)

dfs(0, 0, 5)

if len(rlt) == 0:
    print(-1)
else:
    print(min(rlt))

