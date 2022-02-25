for tc in range(1, 11):
    n = int(input())
    data = input()
    stack = []
    isp = {'*': 2, '+': 1, '(': 0}
    icp = {'*': 2, '+': 1, '(': 3}
    rlt = ''

    #여는 괄호나 연산자를 만났을 때
    def push(sign):
        global rlt
        #스택이 비어있다면 push
        if not stack:
            stack.append(sign)
        #이번 기호의 우선순위가 스택 top의 우선순위보다 높다면 추가
        elif icp[sign] > isp[stack[-1]]:
            stack.append(sign)
        #우선순위가 높지 않지만 여는 괄호라면 추가
        elif sign == '(':
            stack.append(sign)
        #스택의 top보다 우선순위가 높지 않고, 여는 괄호도 아니라면 스택의 top보다 우선순위가 높아질 때까지
        #pop해서 출력
        else:
            rlt += stack.pop()
            push(sign)

    for i in data:
        #숫자라면 출력
        if i.isdigit():
            rlt += i
        #닫는 괄호라면
        elif i == ')':
            while True:
                #스택의 top이 여는 괄호가 될 때까지 pop해서 출력하고
                #여는 괄호를 만나면 pop
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    rlt += stack.pop()
        #여는 괄호나 연산자라면 스택연산 push()
        else:
            push(i)

    #남아있는 기호들을 pop해서 출력
    while stack:
        rlt += stack.pop()

    #변환한 후위표기식을 계산하는 함수
    def cal(exp):
        #식의 앞에서부터 하나씩 확인하며
        for i in exp:
            #숫자라면 정수형으로 변환하여 스택에 추가
            if i.isdigit():
                stack.append(int(i))
            #더하기 기호라면 숫자 2개를 pop해서 더해서 추가
            elif i == '+':
                stack.append(int(stack.pop())+int(stack.pop()))
            #곱셈 기호라면 숫자 2개를 pop해서 곱해서 추가
            else:
                stack.append(int(stack.pop())*int(stack.pop()))

    cal(rlt)
    print(f'#{tc} {stack.pop()}')