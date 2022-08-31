N = int(input())
INF = 10**10

start = -INF
end = -INF
total = 0

def add_line(s, e):
    global start, end, total

    #일부가 겹치는 선분인 경우
    if s <= end and e > end:
        end = e

    #새로운 선분인 경우
    if s > end:
        total += (end-start)
        start = s
        end = e

    #기존 선분에 포함되는 선분인 경우
    if s <= end and e <= end:
        pass

for _ in range(N):
    s, e = map(int, input().split())
    add_line(s, e)

total += end-start

print(total)