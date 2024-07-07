'''
Leetcode #33 https://leetcode.com/problems/search-in-rotated-sorted-array/description/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated 
at an unknown pivot index k (1 <= k < nums.length) such that 
the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
(0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 
and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

'''
Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4

'''

'''
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1
'''

import time
from typing import List

def solve(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
            
def run():
    start_time = time.time()
    res = solve(nums = [4,5,6,7,0,1,2], target = 0)
    print('1. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == 4
    
    start_time = time.time()
    res = solve(nums = [4,5,6,7,0,1,2], target = 3)
    print('2. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == -1
    
    start_time = time.time()
    res = solve(nums = [1], target = 0)
    print('3. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == -1
    
    start_time = time.time()
    res = solve(nums = [3, 1], target = 1)
    print('4. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == 1
    
    start_time = time.time()
    res = solve(nums = [1, 3], target = 1)
    print('5. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == 0
    
    start_time = time.time()
    res = solve(nums = [5, 1, 3], target = 1)
    print('6. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == 1

    start_time = time.time()
    res = solve(nums = [1, 3], target = 3)
    print('7. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == 1

    
print('Start.')
run_start_time = time.time()
run()
print("End. run() executed in %s seconds" % (time.time() - run_start_time))