import sys
input = sys.stdin.readline

M = int(input())
result = 0

for _ in range(M):
    operation = input().rstrip().split()
    if len(operation) == 2:
        j = 1 << int(operation[1])
        if operation[0] == 'add':
            if not result & j:
                result += j
        elif operation[0] == 'remove':
            if result & j:
                result -= j
        elif operation[0] == 'check':
            print(int(bool(result & j)))
        elif operation[0] == 'toggle':
            if result & j:
                result -= j
            else:
                result += j
    else:
        if operation[0] == 'all':
            result = (1<<22)-2
        else:
            result = 0