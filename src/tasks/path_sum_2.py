'''
Leetcode #113 https://leetcode.com/problems/path-sum-ii/

Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node values 
in the path equals targetSum. Each path should be returned as a list 
of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending 
at any leaf node. A leaf is a node with no children.
'''

'''
Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
'''

import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    def dfs(node, targetSum, current_path, result):
        if not node:
            return

        current_path.append(node.val)

        if targetSum == node.val and not node.left and not node.right:
            result.append(current_path[:])
            return

        if node.left:
            l_current_path = current_path.copy()
            dfs(node.left, targetSum - node.val, l_current_path, result)
        if node.right:
            r_current_path = current_path.copy()
            dfs(node.right, targetSum - node.val, r_current_path, result)

    result = []
    dfs(root, targetSum, [], result)
    return result
    
print('Start.')
run_start_time = time.time()
print("End. \trun() executed in %s seconds" % (time.time() - run_start_time))
