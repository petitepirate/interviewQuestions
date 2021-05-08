# This problem was asked by Facebook.

# Given a binary tree, return the level of the tree with minimum sum.

#_______________________________________________________________________________________________
# Solution
# A binary tree is a data structure in which each node has at most two children (left and right), 
# and a level is how many parents a node has until it reaches the root.

# To better explain this question, let's see this example:

#        1      (Level 0 = 1)
#       / \
#      2   3    (Level 1 = 2 + 3)
#         / \
#        4   5  (Level 2 = 4 + 5)
# One possible way to solve this problem is iterate level by level on the tree's nodes, so we 
# can get theirs respective sum. Like this code:

from Queue import Queue
from collections import defaultdict

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def minimum_level_sum(root):
    queue = Queue()
    queue.put((root, 0))
    level_to_sum = defaultdict(int) # Maps level to its sum


    while not queue.empty():
        node, level = queue.get()
        level_to_sum[level] += node.val

        if node.right:
            queue.put((node.right, level + 1))

        if node.left:
            queue.put((node.left, level + 1))

    return min(level_to_sum, key=level_to_sum.get)
# The complexity of this function is O(N), and works both with positive or negative values. It works 
# by doing a breadth first search and keeping track of the sum in each level.

# You can try yourself with these examples:

# """
#          1
#        /  \
#      -2   -3            (level 1 is the minimum)
#          /  \
#         4   -5
# """
root = Node(
    value=1,
    left=Node(-2),
    right=Node(-3, Node(4), Node(-5))
)
print(minimum_level_sum(root))
# """
#           1
#       /       \
#     2          3
#   /  \          \
#  4    5          6
#        \       /   \
#        -1   -7     -8   (level 3 is the minimum)

# """
root = Node(
    value=1,
    left=Node(2, Node(4), Node(5, Node(-1))),
    right=Node(
        value=3,
        right=Node(6, Node(-7), Node(-8))
    )
)
print(minimum_level_sum(root))
