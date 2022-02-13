N = int(input())
command = []
for _ in range(N):
    command.append(list(input().split()))

stack = []

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0

def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]

for i in command:
    if 'push' in i:
        push(i[1])
    elif 'pop' in i:
        print(pop())
    elif 'size' in i:
        print(size())
    elif 'empty' in i:
        print(empty())
    else:
        print(top())
