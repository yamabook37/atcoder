# https://qiita.com/maebaru/items/53a30c78bad8d0df92af

# Make tree as follows:
#     1
#    / \
#   2   3
#  / \ / \
# 4  5 6  7

from collections import deque

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

node1 = Node(1) # Root node
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# キューを作成して初期ノード(root)を入れる
q = deque()
q.append(node1)

# キューが空になるまで繰り返す
while len(q) > 0:
    # キューの先頭（左端）からnodeを取り出す
    node = q.popleft()

    if node is not None:
        print(node.val)
        # nodeの子要素をキューの末尾（右端）に入れる
        q.append(node.left)
        q.append(node.right)