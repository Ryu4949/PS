T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = []
    for i in string:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    print(f'#{tc} {len(stack)}')