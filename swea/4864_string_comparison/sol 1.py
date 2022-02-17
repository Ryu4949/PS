def BruteForce(p, t):
    #i: 패턴의 인덱스, j: 문자열의 인덱스
    i = 0
    j = 0
    while i < len(p) and j < len(t):
        if t[j] != p[i]:
            j = j - i
            i = -1
        i += 1
        j += 1

        if i == len(p):
            return j - len(p)
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    if BruteForce(str1, str2) != -1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
