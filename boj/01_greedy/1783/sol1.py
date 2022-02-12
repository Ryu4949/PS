n, m = map(int, input().split())
#세로가 3이상이고 가로가 7이상이면 1~4를 한번씩 이동하고 나머지는 오른쪽으로 1씩만 이동가능하고
#이 때가 최대로 방문 가능
#그 외의 경우 가로/세로에 따라 이동이 제약되는 점과 이동횟수에 대한 제약을 고려해서 나눠봄

if n >= 3:
    if m >= 6:
        print(m-2)
    elif m == 5:
        print(4)
    else:
        print(m)
elif n == 2:
    if m >= 7:
        print(4)
    elif m >= 5:
        print(3)
    elif m >= 3:
        print(2)
    else:
        print(1)
else:
    print(1)
