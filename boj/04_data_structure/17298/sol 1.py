N = int(input())
data = list(map(int, input().split()))

def NGE(idx):
    for i in range(idx+1, N):
        if data[i] > data[idx]:
            return data[i]
    return -1

for i in range(N):
    print(NGE(i), end=' ')