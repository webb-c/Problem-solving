import sys
input = sys.stdin.readline

class Node() :
    def __init__(self, n, l, r):
        self.me = n
        self.left = l
        self.right = r

N = int(input())
tree = {}
for _ in range(N) :
    n, l, r = input().split()
    tree[n] = Node(n, l, r)

def preOrder(node) :
    print(node.me, end="")
    if node.left != '.' : preOrder(tree[node.left])
    if node.right != '.' : preOrder(tree[node.right])
def midOrder(node) :
    if node.left != '.': midOrder(tree[node.left])
    print(node.me, end="")
    if node.right != '.': midOrder(tree[node.right])
def latOrder(node) :
    if node.left != '.': latOrder(tree[node.left])
    if node.right != '.': latOrder(tree[node.right])
    print(node.me, end="")

preOrder(tree['A'])
print()
midOrder(tree['A'])
print()
latOrder(tree['A'])