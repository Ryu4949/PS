N = int(input())
bi = bin(N)[2:][::-1]
answer = 0
for i in range(len(bi)):
    if bi[i] == '1':
        answer += 3**i

print(answer)