import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# 1번선수는 start팀에 넣고 시작
start = [0]
link = []

# 두 팀의 능력치 차이를 담아줄 리스트
rlt = []

# 팀이 결정됐을 때 각 팀의 능력치를 계산하는 함수
def stat(team):
    stat_team = 0
    for i in range(len(team)):
        for j in range(len(team)):
            stat_team += S[team[i]][team[j]]
    return stat_team

def dfs(i):
    # 도중에 한팀의 인원이 전체인원의 절반을 초과하면 중단
    if len(start) > N // 2 or len(link) > N // 2:
        return

    # 팀을 절반씩 나눠줬다면
    if i == N:
        # rlt에 두팀 능력치 차이를 담아줌
        rlt.append(abs(stat(start) - stat(link)))
        return

    # 1번선수는 무조건 start팀에 넣었으니까 2번부터 시작할건데
    # 일단 start팀에 넣고 다음단계 진행
    start.append(i)
    dfs(i + 1)

    # 원상복구 해주고 link팀에 넣고 다음단계 진행하고 원상복구
    start.pop()
    link.append(i)
    dfs(i + 1)
    link.pop()

# 1번 선수는 이미 start팀이니까 2번선수부터 시작
dfs(1)

# 최소값 출력
print(min(rlt))