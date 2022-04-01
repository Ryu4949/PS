def preorder(v):
    if v:
        print(v, end=' ')
        preorder(ch1[v])
        preorder(ch2[v])

def inorder(v):
    if v:
        inorder(ch1[v])
        print(v, end= ' ')
        inorder(ch2[v])

def postorder(v):
    if v:
        postorder(ch1[v])
        postorder(ch2[v])
        print(v, end=' ')

V, E = map(int, input().split())
edges = list(map(int, input().split()))
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
for i in range(E):
    if ch1[edges[2*i]] != 0:
        ch2[edges[2*i]] = edges[2*i+1]
    else:
        ch1[edges[2*i]] = edges[2*i+1]

print('전위 순회 :', end=' ')
preorder(1)
print()
print('중위 순회 :', end=' ')
inorder(1)
print()
print('후위 순회 :', end=' ')
postorder(1)