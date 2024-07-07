'''
Leetcode #18 https://leetcode.com/problems/4sum/description/

Given an array nums of n integers, return an array of all 
the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
'''

import time
from typing import List

def solve_slow(nums: List[int], target: int) -> List[List[int]]:
    if len(nums) < 3:
        return
    
    nums.sort()
    result = []
    
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            right = len(nums) - 1
            for k in range(j + 1, len(nums) - 1):
                if right < k:
                    break
                ls = [nums[i], nums[j], nums[k]]
                sum3 = nums[i] + nums[j] + nums[k]
                while nums[right] + sum3 >= target and right > k:             
                    if sum3 + nums[right] == target:
                        ls.append(nums[right])
                        if ls not in result:
                            result.append(ls)
                        break
                    right -= 1 
                     
    return result
        
def solve(nums: List[int], target: int) -> List[List[int]]:
    if len(nums) < 4:
        return []

    nums.sort()
    result = []

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if cur_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left <= right and nums[left - 1] == nums[left]:
                        left += 1
                    while left <= right and nums[right + 1] == nums[right]:
                        right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1

    return result


def run():
    start_time = time.time()
    res = solve([1, 0, -1, 0, -2, 2], 0)
    print('1. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]] == res


    start_time = time.time()
    res = solve([2,2,2,2,2], 8)
    print('2. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert [[2,2,2,2]] == res
    
print('Start.')
start_time = time.time()
run()
print("End. run() executed in %s seconds" % (time.time() - start_time))