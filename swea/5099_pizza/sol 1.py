from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    #치즈양을 번호와 함께 추가
    cheese = deque()
    for i in range(1, M+1):
        cheese.append([i, lst[i-1]])

    #화덕 크기만큼 넣기
    pizza = deque()
    for i in range(N):
        pizza.append(cheese.popleft())

    while True:
        #이번 피자를 꺼내서 치즈를 반으로 줄이고
        pizza_now = pizza.popleft()
        pizza_now[1] //= 2

        #치즈가 0이 되었는데
        if pizza_now[1] == 0:
            #새로 넣을 피자가 남아있다면 새로 넣어줌
            if cheese:
                pizza.append(cheese.popleft())

        #치즈가 0이 아니라면 다시 끝에다가 넣기
        else:
            pizza.append(pizza_now)

        #화덕에 있는 피자의 개수가 1개면 중단
        if len(pizza) == 1:
            break

    #그때의 피자번호 출력
    print(f'#{tc} {pizza[0][0]}')