J = input()
N = int(input())
answer = 0
for _ in range(N):
    if input() == J:
        answer += 1

print(answer)