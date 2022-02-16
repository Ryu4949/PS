#set을 활용한 풀이
#그 중에서도 교집합을 이용한 풀이
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data_set = [list(map(int, input().split())) for _ in range(n)]

    red = set()
    blue = set()

    for data in data_set:
        r1, c1, r2, c2, color = data

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if color == 1:
                    red.add((r,c))
                else:
                    blue.add((r,c))

    rlt = len(red & blue) # red.intersection(blue)
    print(f'#{tc} {rlt}')
