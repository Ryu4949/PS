def check(string):
    stack = []
    for i in string:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')':
            if not stack:
                return 0
            elif stack.pop() != '(':
                return 0
        elif i == '}':
            if not stack:
                return 0
            elif stack.pop() != '{':
                return 0
    if not stack:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    string = input()
    print(f'#{tc} {check(string)}')