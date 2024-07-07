'''
Leetcode #74 https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix matrix with the following two properties:

1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer 
    of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

'''
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
'''

'''
Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

import time
from typing import List

def binary_search(array: List[int], target: int):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def solve(matrix: List[List[int]], target: int) -> bool:
    for arr in matrix:
        if binary_search(arr, target):
            return True
    return False
    
            
def run():
    start_time = time.time()
    res = solve(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
    print('1. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == True

    start_time = time.time()
    res = solve(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
    print('2. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == False

    
print('Start.')
run_start_time = time.time()
run()
print("End. run() executed in %s seconds" % (time.time() - run_start_time))