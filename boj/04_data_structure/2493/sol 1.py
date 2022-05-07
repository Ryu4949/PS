N = int(input())
tower = [*map(int, input().split())]
towers = list(enumerate(tower, start=1))
answer = []
stack = []
for i in towers:
    while stack:
        if i[1] > stack[-1][1]:
            stack.pop()
        else:
            break

    if not stack:
        stack.append(i)
        answer.append(0)
    else:
        answer.append(stack[-1][0])
        stack.append(i)

print(*answer)