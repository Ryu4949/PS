def check(data):
    stack = []
    for i in data:
        #여는 괄호면
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False

data = input()
print(check(data))