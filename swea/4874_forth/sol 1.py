T = int(input())
for tc in range(1, T+1):
    command = list(input().split())
    stack = []  #빈 스택

    #입력받은 수식을 앞에서부터 확인
    for i in command:
        if i.isdigit(): #숫자라면 스택에 push
            stack.append(i)
        elif i == '.':  # '.'인 경우에는
            if len(stack) == 1: #스택의 size가 1이면 pop해서 출력
                print(f'#{tc} {stack.pop()}')
            else:   #size가 1이 아니면 error
                print(f'#{tc} error')
        elif len(stack) >= 2:   #숫자와 .이 아닌 경우 즉 연산자를 만났는데 스택의 size가 2이상이면 계산
            n1 = int(stack.pop())
            n2 = int(stack.pop())
            if i == '+':
                stack.append(str(n1 + n2))
            elif i == '-':
                stack.append(str(n2 - n1))
            elif i == '*':
                stack.append(str(n1 * n2))
            else:
                stack.append(str(n2 // n1))
        else:   #연산자를 만났는데 스택의 size가 2보다 작으면 연산이 불가능하므로 error
            print(f'#{tc} error')
            break