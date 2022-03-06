N, M = map(int, input().split())
num_list = [str(x) for x in range(1, N+1)]

def perm(string, i):
    if i == M:
        print(string)
    else:
        for j in num_list:
            if j not in string:
                perm(string + j + ' ', i+1)

perm('', 0)