# Make tree as follows:
#     1
#    / \
#   2   5
#  / \ / \
# 3  4 6  7

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.left = node2
node1.right = node5
node2.left = node3
node2.right = node4
node5.left = node6
node5.right = node7

def traverse(node):
    if node is not None:
        print(node.val)
        # 子要素に対して再帰的に呼び出していく
        traverse(node.left)
        traverse(node.right)

traverse(node1)