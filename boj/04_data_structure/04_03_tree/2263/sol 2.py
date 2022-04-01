N = int(input())
inorder = [*map(int, input().split())]
postorder = [*map(int, input().split())]

def preorder(si, ei, sp, ep):
    if si == ei:
        return

    root = postorder[ep]
    idx = inorder.index(root)

    print(root, end=' ')

    preorder(si, idx-1, sp, sp+idx-1-si)
    preorder(idx+1, ei, ei+1, ep-1)

preorder(0, N-1, 0, N-1)