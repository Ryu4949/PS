def post(v):
    if v:
        post(int(tree[v][2]))
        post(int(tree[v][3]))
        if tree[v][1].isdigit():
            stack.append(int(tree[v][1]))
        else:
            n = stack.pop()
            m = stack.pop()
            stack.append(cal(m, n, tree[v][1]))

def cal(num_1, num_2, sign):
    if sign == '+':
        return num_1 + num_2
    elif sign == '-':
        return num_1 - num_2
    elif sign == '*':
        return num_1 * num_2
    else:
        return num_1 / num_2

for tc in range(1, 11):
    N = int(input())
    tree = [[0]*4 for _ in range(N+1)]
    stack = []

    for i in range(1, N+1):
        data = list(input().split())
        for j in range(len(data)):
            tree[i][j] = data[j]

    post(1)

    print(f'#{tc} {int(stack[-1])}')