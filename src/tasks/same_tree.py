'''
Leetcode #100 https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check 
if they are the same or not.

Two binary trees are considered the same if they are 
structurally identical, and the nodes have the same value.
'''

'''
Constraints:

The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4
'''

'''
Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false
'''

import time
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Successfully go through the local tests, but don't pass Leetcode's tests
def solve_strange(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if isinstance(p, list):
        p = TreeNode(p[0], p[1], p[2])
    if isinstance(q, list):
        q = TreeNode(q[0], q[1], q[2])
    
    if isinstance(p, TreeNode) and isinstance(q, TreeNode):
       return p.val == q.val and solve_strange(p.left, q.left) and solve_strange(p.right, q.right)
    elif isinstance(p, int) and isinstance(q, int):
        return p == q
    else:
        return False

# Leetcode get it
def solve(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False

    if p.val == q.val:
        return solve(p.left, q.left) and solve(p.right, q.right)
    else:
        return False

def run():
    start_time = time.time()
    res = solve(p = [1,2,3], q = [1,2,3])
    print('1. res:', res, '\texecuted in %s seconds' % (time.time() - start_time))
    assert res == True

    start_time = time.time()
    res = solve(TreeNode(1, 2), TreeNode(1, None, 2))
    print('2. res:', res, '\texecuted in %s seconds' % (time.time() - start_time))
    assert res == False

    start_time = time.time()
    res = solve(TreeNode(1, 2, 1), TreeNode(1,1,2))
    print('3. res:', res, '\texecuted in %s seconds' % (time.time() - start_time))
    assert res == False
    
print('Start.')
run_start_time = time.time()
run()
print("End. \trun() executed in %s seconds" % (time.time() - run_start_time))