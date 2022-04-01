N = int(input())
inorder = [*map(int, input().split())]
postorder = [*map(int, input().split())]

def preorder(inorder, postorder):
    if not inorder:
        return

    root = postorder[-1]
    idx = inorder.index(root)

    left_in = inorder[:idx]
    right_in = inorder[idx+1:]
    left_post = postorder[:idx]
    right_post = postorder[idx:-1]

    print(root, end=' ')
    preorder(left_in, left_post)
    preorder(right_in, right_post)

preorder(inorder, postorder)