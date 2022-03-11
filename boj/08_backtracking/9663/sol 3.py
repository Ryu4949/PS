N = int(input())
cnt = 0

#queen[i]는 i번째 행에 queen이 몇번째 열에 있는지 나타냄
queen = [0] * N
visited = [False] * N

#유망한지 체크
def is_promising(depth):
    for j in range(depth):
        #열의 위치가 같은 퀸이 있거나, 대각선에 위치한 퀸이 있다면 False
        if queen[depth] == queen[j] or abs(queen[depth]-queen[j]) == depth-j:
            return False
    return True

def dfs(i):
    global cnt

    #끝까지 탐색했으면 cnt 1 증가
    if i == N:
        cnt += 1
        return

    else:
        for j in range(N):
            #아직 방문하지 않은 열이라면
            if not visited[j]:
                #i번째 행에서 j열에 퀸을 놓고 방문처리
                queen[i] = j
                visited[j] = True

                #퀸을 놓은 상태에서 유망하다면 다음단계 진행
                if is_promising(i):
                    dfs(i+1)
                #원상복구
                visited[j] = False

dfs(0)
print(cnt)