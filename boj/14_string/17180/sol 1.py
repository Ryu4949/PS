N, M = map(int, input().split())
word1 = input()
word2 = input()

dp = [0]*2
dp[1] = abs(ord(word1[0])-ord(word2[0]))

i = 1
j = 1

while True:
    if i == N and j == M:
        break
    print(f'i, j: {i, j}')
    if word1[i] == word2[j]:
        dp.append(dp[-1])
        i += 1
        j += 1
    elif i == N-1 and j == M-1:
        dp.append(abs(ord(word1[i])-ord(word2[j])))
        break
    else:
        gap1 = abs(ord(word1[i-1])-ord(word2[j]))
        gap2 = abs(ord(word1[i])-ord(word2[j-1]))
        if gap1 >= gap2:
            dp.append(gap2)
            i += 1
        else:
            dp.append(gap1)
            j += 1

print(dp[-1])