T = int(input())
for tc in range(1, T+1):
    string = input()
    steel = ''
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            if string[i+1] == '(':
                stack.append(i)