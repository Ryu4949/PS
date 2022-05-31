word = input()
bomb = input()

N = len(bomb)
stack = []
last = bomb[-1]

for i in word:
    stack.append(i)
    if i == last:
        try:
            for j in range(-1, -1-N, -1):
                if bomb[j] != stack[j]:
                    break
            else:
                for _ in range(N):
                    stack.pop()
        except:
            pass

if stack:
    print(''.join(stack))
else:
    print("FRULA")