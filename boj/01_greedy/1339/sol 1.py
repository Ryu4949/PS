N = int(input())
words = [0] * 26
for _ in range(N):
    word = input()
    L = len(word)
    for i in range(L):
        words[ord(word[i])-65] += 10**(L-i-1)

words.sort(reverse=True)

answer = 0
for i in range(10):
    answer += words[i] * (9-i)

print(answer)