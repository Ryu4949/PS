from collections import defaultdict
import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a != b:
        parent[b] = a
        relations[a] += relations[b]

T = int(input())

for _ in range(T):
    F = int(input())
    parent = defaultdict(str)
    relations = defaultdict(int)

    for _ in range(F):
        friend_one, friend_two = input().rstrip().split()
        if not parent[friend_one]:
            parent[friend_one] = friend_one
            relations[friend_one] += 1
        if not parent[friend_two]:
            parent[friend_two] = friend_two
            relations[friend_two] += 1

        union(friend_one, friend_two)

        print(relations[find_parent(friend_one)])