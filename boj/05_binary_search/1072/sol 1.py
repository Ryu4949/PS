# z = int(y/x * 100)
#앞으로 n게임을 더한다고 치면 그 때의 z는
# z = int((y+n)/(x+n) * 100))
#시작전에 z가 99이상이라면 -1
x, y = map(int, input().split())
z = int(y/x * 100)

def binary(total, win, start, end):
    games = 0
    while start <= end:
        mid = (start + end) // 2
        if int((win + mid)/(total + mid) * 100) > z:
            games = mid
            end = mid - 1
        else:
            start = mid + 1
    return int(games)

if z >= 99:
    print(-1)
else:
    print(binary(x, y, 0, x**2))

#end점을 설정하는법? 일단은 대충 크게 x**2로 했더니 됐음
#부동소수점으로 인해 소수값이 정확하지 않을 수 있다는건 아는데, z = int(y/x * 100)으로 쓰면 답이 틀릴정도로
#차이가 있는건가?