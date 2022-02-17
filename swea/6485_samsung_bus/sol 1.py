T = int(input())
for tc in range(1, T+1):
    N = int(input())
    route = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stop = []
    for _ in range(P):
        stop.append(int(input()))

    bus_stop = [0] * 5001

    for i in route:
        for j in range(i[0], i[1]+1):
            bus_stop[j] += 1

    print(f'#{tc}', end=" ")
    for i in stop:
        print(bus_stop[i], end=" ")
    print()