from collections import defaultdict
import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return len(node.children.values())

def check(trie, arr):
    for i in arr:
        if trie.startsWith(i) > 0:
            return False
    return True

T = int(input())
for _ in range(T):
    trie = Trie()
    N = int(input())
    phone_nums = [input().rstrip() for _ in range(N)]

    for phone in phone_nums:
        trie.insert(phone)

    if check(trie, phone_nums):
        print("YES")
    else:
        print("NO")

