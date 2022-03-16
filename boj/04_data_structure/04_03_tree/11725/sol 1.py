#?틀림

N = int(input())
nodes = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    if a == 1 or nodes[a] != 0:
        nodes[b] = a
    else:
        nodes[a] = b

for i in range(2, N+1):
    print(nodes[i])