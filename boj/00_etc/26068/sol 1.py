N = int(input())
answer = 0
for _ in range(N):
    gift = input()
    if int(gift[2:]) <= 90:
        answer += 1

print(answer)