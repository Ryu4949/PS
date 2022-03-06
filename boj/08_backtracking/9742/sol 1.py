#메모리초과?

def factorial(N):
    rlt = 1
    i = 1
    while i < N:
        i += 1
        rlt *= i
    return rlt

def perm(i):
    if i == len(word_list):
        rlt.append(''.join(word_list))
    else:
        for j in range(i, len(word_list)):
            word_list[i], word_list[j] = word_list[j], word_list[i]
            perm(i+1)
            word_list[i], word_list[j] = word_list[j], word_list[i]

def find_perm(word, N):
    if N > factorial(len(word)):
        return "No permutation"
    else:
        perm(0)
        rlt.sort()
        return rlt[N-1]

while True:
    try:
        word, N = input().split()
        word_list = list(word)
        N = int(N)
        rlt = []
        print(f'{word} {N} = {find_perm(word_list, N)}')
    except:
        break
