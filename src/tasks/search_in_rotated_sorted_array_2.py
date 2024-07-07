'''
Leetcode #81 https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

There is an integer array nums sorted in non-decreasing order 
(not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown 
pivot index k (0 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
(0-indexed). 

For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and 
become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, 
return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Follow up: This problem is similar to Search in Rotated Sorted Array, 
but nums may contain duplicates. Would this affect the runtime complexity? 
How and why?
'''

'''
Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
'''

'''
Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
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

def solve_slow(nums: List[int], target: int) -> bool:
    nums.sort()
    return binary_search(nums, target)

def solve(nums: List[int], target: int) -> bool:
    for n in nums:
        if n == target:
            return True 
    return False

def run():
    start_time = time.time()
    res = solve(nums = [2,5,6,0,0,1,2], target = 0)
    print('1. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == True

    start_time = time.time()
    res = solve(nums = [2,5,6,0,0,1,2], target = 3)
    print('2. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == False
    
print('Start.')
run_start_time = time.time()
run()
print("End. run() executed in %s seconds" % (time.time() - run_start_time))