N, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
n = len(str(N))
bit = [0]*K

def big_num(idx):
    idx = 0

    if idx == n:
        return
