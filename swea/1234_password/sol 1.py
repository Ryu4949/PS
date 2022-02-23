for tc in range(1, 11):
    N, M = input().split()

    stack = []

    for i in M:
        if not stack or i != stack[-1]:
            stack.append(i)
        else:
            stack.pop()

    print(f'#{tc} {"".join(stack)}')