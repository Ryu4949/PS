def factorial(N):
    fac = 1
    i = 1
    while i < N:
        i += 1
        fac *= i
    return fac

def perm(string, i):
    global cnt
    if i == len(word):
        cnt += 1
        if cnt == N:
            return string
    else:
        for j in word:
            if j not in string:
                per = perm(string+j, i+1)
                if per:
                    return per

while True:
    try:
        word, N = input().split()
        N = int(N)
        cnt = 0

        if factorial(len(word)) < N:
            print(word, N, '=', "No permutation")
        else:
            print(word, N, '=', perm('', 0))

    except:
        break