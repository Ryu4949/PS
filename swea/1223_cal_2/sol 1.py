for tc in range(1, 11):
    n = int(input())
    data = input()
    stack = []
    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
    rlt = ''

    def push(sign):
        global rlt
        if not stack:
            stack.append(sign)
        elif icp[sign] > isp[stack[-1]]:
            stack.append(sign)
        elif sign == '(':
            stack.append(sign)
        else:
            rlt += stack.pop()
            push(sign)

    for i in data:
        if i.isdigit():
            rlt += i
        elif i == ')':
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    rlt += stack.pop()
        else:
            push(i)

    while stack:
        rlt += stack.pop()

    def cal(exp):
        for i in exp:
            if i.isdigit():
                stack.append(int(i))
            elif i == '+':
                stack.append(int(stack.pop())+int(stack.pop()))
            elif i == '*':
                stack.append(int(stack.pop())*int(stack.pop()))
            elif i == '-':
                stack.append(-int(stack.pop())+int(stack.pop()))
            else:
                stack.append(int(stack.pop())/int(stack.pop()))

    cal(rlt)
    print(f'#{tc} {stack.pop()}')