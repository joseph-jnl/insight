import pytest
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.distance = 0


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    Find max depth of binary tree
    ie num of nodes along longest path from the root node 
    down to the farthest leaf node
    """

    marked = []
    max_distance = 1

    # Insert root into queue
    if root:
        breadth = deque()
        root.distance = 1
        breadth.append(root)

    # While q is not empty, mark and insert children into queue
    while breadth:
        current = breadth.popleft()
        print(current.val)
        if current.left:
            current.left.distance = current.distance + 1
            breadth.append(current.left)
            if current.left.distance > max_distance:
                max_distance = current.left.distance
        if current.right:
            current.right.distance = current.distance + 1
            breadth.append(current.right)
            if current.right.distance > max_distance:
                max_distance = current.right.distance
    return max_distance


# pytest.main()

def test_tree2():
#    A
#  B   C

    A = TreeNode('A')
    B = TreeNode('B')
    C = TreeNode('C')

    A.left = B
    A.right = C


def test_tree4():
#    A
#  B   C
# D E   F 
#        G
#         
    A = TreeNode('A')
    B = TreeNode('B')
    C = TreeNode('C')
    D = TreeNode('D')
    E = TreeNode('E')
    F = TreeNode('F')
    G = TreeNode('G')

    A.left = B
    A.right = C
    B.right = E
    B.left = D
    C.right = F
    F.right = G

    assert maxDepth(A) == 4

def test_tree5():
#    A
#  B   C
# D E   F 
#        G
#       H
    A = TreeNode('A')
    B = TreeNode('B')
    C = TreeNode('C')
    D = TreeNode('D')
    E = TreeNode('E')
    F = TreeNode('F')
    G = TreeNode('G')
    H = TreeNode('H')

    A.left = B
    A.right = C
    B.right = E
    B.left = D
    C.right = F
    F.right = G
    G.left = H

    assert maxDepth(A) == 5