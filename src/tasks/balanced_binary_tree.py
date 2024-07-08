'''
Leetcode #110 https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is height-balanced

Note: A height-balanced binary tree is a binary tree in which the depth 
of the two subtrees of every node never differs by more than one.
'''

'''
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
    
Example 3:

Input: root = []
Output: true
'''

'''
Constraints:

The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
'''

import time
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getHeight(node):
    if not node:
        return 0
    left_height = getHeight(node.left)
    right_height = getHeight(node.right)
    if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        return -1
    return 1 + max(left_height, right_height)

def solve(root: Optional[TreeNode]) -> bool:
    return getHeight(root) != -1

    
print('Start.')
run_start_time = time.time()
print("End. \trun() executed in %s seconds" % (time.time() - run_start_time))