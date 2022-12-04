word = input()
N = len(word)

for i in range(N):
    print(word[i], end='')
    if i%10 == 9:
        print()
