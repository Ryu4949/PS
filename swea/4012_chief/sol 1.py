def synergy(food):
    synergy_food = 0
    for i in range(len(food)):
        for j in range(len(food)):
            synergy_food += S[food[i]][food[j]]
    return synergy_food

def dfs(i):
    if len(A) > N // 2 or len(B) > N // 2:
        return

    if i == N:
        rlt.append(abs(synergy(A) - synergy(B)))
        return

    A.append(i)
    dfs(i + 1)
    A.pop()
    B.append(i)
    dfs(i + 1)
    B.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    A = [0]
    B = []

    rlt = []

    dfs(1)

    print(f'#{tc} {min(rlt)}')