import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.length = 0
        self.pointer = 0

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end="")
            cur = cur.next

    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next

T = int(input())
for tc in range(T):
    if tc:
        print()
    keylogs = input().rstrip()
    password = LinkedList('')


    for k in keylogs:
        if k == '<':
            password.pointer = max(1, password.pointer-1)
        elif k == '>':
            idx = min(password.pointer+1, password.length)
        elif k == '-':
            pass
        else:
            pass


    password.print_all()