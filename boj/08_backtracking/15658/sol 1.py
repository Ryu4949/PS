import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
cal = list(map(int, input().split()))
cnt = [0] * 4
ans = []

# 최초의 결과값은 맨 앞의 숫자
rlt = nums[0]


# i는 깊이를 가리키는 변수, k는 연산 대상 숫자를 가리키는 인덱스
def dfs(i, k):
    global rlt

    # 진행 도중에 각 연산자의 개수가 최대 연산자의 개수를 초과한다면 중단
    for j in range(4):
        if cnt[j] > cal[j]:
            return

    # 끝까지 계산했으면 결과값 추가
    if i == N - 1:
        ans.append(rlt)
        return

    for j in range(4):
        cnt[j] += 1
        # 연산 수행전 값 저장해놓고
        base = rlt
        if j == 0:  # 더하기
            rlt += nums[k]
        elif j == 1:  # 빼기
            rlt -= nums[k]
        elif j == 2:  # 곱하기
            rlt *= nums[k]
        else:  # 나누기
            # 기존 값이 양수일 때는 그냥 몫만 취하고
            if rlt >= 0:
                rlt //= nums[k]
            # 음수면 양수로 바꿔서 몫 취하고 다시 음수로
            else:
                rlt = (abs(rlt) // nums[k]) * (-1)
        dfs(i + 1, k + 1)

        # 원상복구
        cnt[j] -= 1
        rlt = base


dfs(0, 1)

print(max(ans))
print(min(ans))