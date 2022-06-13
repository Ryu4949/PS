from collections import defaultdict

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
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

N = int(input())
ids = Trie()
ids_cnt = defaultdict(int)
for _ in range(N):
    user_id = input()
    nickname = ''
    for i in user_id:
        nickname += i
        if not ids.startsWith(nickname):
            break
    ids.insert(user_id)
    ids_cnt[user_id] += 1

    if user_id == nickname:
        print(nickname if ids_cnt[user_id] == 1 else nickname+str(ids_cnt[user_id]))
    else:
        print(nickname)