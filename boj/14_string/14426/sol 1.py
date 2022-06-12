import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

N, M = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
prefix = [input().rstrip() for _ in range(M)]

T = Trie()

for word in words:
    T.insert(word)

cnt = 0
for pre in prefix:
    if T.startsWith(pre):
        cnt += 1

print(cnt)

