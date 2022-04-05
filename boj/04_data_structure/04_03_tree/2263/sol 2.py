import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
inorder = [*map(int, input().split())]
postorder = [*map(int, input().split())]

def preorder(si, ei, sp, ep):
    if si > ei or sp > ep:
        return

    root = postorder[ep]
    idx = inorder.index(root)

    print(root, end=' ')
    preorder(si, idx-1, sp, sp+(idx-1-si))
    preorder(idx+1, ei, sp+idx-si, ep-1)

preorder(0, N-1, 0, N-1)