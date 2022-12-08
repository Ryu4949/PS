N, M = map(int, input().split())
K = list(map(int, input().split()))
max_num = -1

def make_number(n, current_num):
    global max_num

    if current_num > N:
        return

    max_num = max(max_num, current_num)

    for i in range(M):
        make_number(n+1, current_num+(10**n)*K[i])

make_number(0, 0)
print(max_num)