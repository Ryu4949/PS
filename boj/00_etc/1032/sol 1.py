N = int(input())
words = [input() for _ in range(N)]
pattern = ''
for i in range(len(words[0])):
    for j in range(N-1):
        if words[j][i] != words[j+1][i]:
            pattern += '?'
            break
    else:
        pattern += words[0][i]

print(pattern)