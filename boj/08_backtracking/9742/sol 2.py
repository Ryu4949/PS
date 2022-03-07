def factorial(N):
    fac = 1
    i = 1
    while i < N:
        i += 1
        fac *= i
    return fac

def perm(string, i):
    global cnt

    #문자열 하나 완성되면 cnt 1 증가
    if i == len(word):
        cnt += 1
        #cnt가 찾는 순번과 같아지면 해당 문자열 반환
        if cnt == N:
            return string
    else:
        #문자열 앞에서부터
        for j in word:
            #아직 추가하지 않은 문자열 추가
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