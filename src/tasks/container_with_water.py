'''
Leetcode #11 https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical 
lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that 
the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant (наклонять) the container.
'''

'''
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.


Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
'''

import time

def solve(height):
    max_area = 0
    left, right = 0, len(height) - 1
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

def run():
    start_time = time.time()
    res = solve([1,8,6,2,5,4,8,3,7])
    assert 49 == res
    print('1. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    
    start_time = time.time()
    res = solve([1,1])
    assert 1 == res
    print('2. res:', res, 'executed in %s seconds' % (time.time() - start_time))

print('Start.')
start_time = time.time()
run()
print("End. run() executed in %s seconds" % (time.time() - start_time))