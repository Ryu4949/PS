N = int(input())
for _ in range(N):
    sentence = input().split()
    sentence = list(map(lambda x: x[::-1], sentence))
    print(' '.join(sentence))