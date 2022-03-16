def inorder(v):
    if v != '.':
        inorder(ch[tree[v]][0])
        print(v, end='')
        inorder(ch[tree[v]][1])

def preorder(v):
    if v != '.':
        print(v, end='')
        preorder(ch[tree[v]][0])
        preorder(ch[tree[v]][1])

def postorder(v):
    if v != '.':
        postorder(ch[tree[v]][0])
        postorder(ch[tree[v]][1])
        print(v, end='')


N = int(input())
tree = dict()
ch = [[] for _ in range(N+1)]

for i in range(1, N+1):
    data = list(input().split())
    tree[data[0]] = i
    ch[i].append(data[1])
    ch[i].append(data[2])

preorder('A')
print()
inorder('A')
print()
postorder('A')
#
# print(tree)
# print(ch)