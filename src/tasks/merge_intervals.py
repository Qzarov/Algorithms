'''
Leetcode #56  https://leetcode.com/problems/merge-intervals/
Given an array of intervals where intervals[i] = [start_i, end_i], 
merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.
'''

'''
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= start_i <= end_i <= 10^4
'''

'''
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

import time
from typing import List

def solve(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    
    result = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result

            
def run():
    start_time = time.time()
    res = solve(intervals = [[1,3], [2,6], [8,10], [15,18]])
    print('1. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == [[1,6],[8,10],[15,18]]

    start_time = time.time()
    res = solve(intervals = [[1,4], [4,5]])
    print('2. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == [[1,5]]
    
    start_time = time.time()
    res = solve(intervals = [[15,18], [1,3], [8,10], [2,6]])
    print('3. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == [[1,6],[8,10],[15,18]]

    
print('Start.')
run_start_time = time.time()
run()
print("End. run() executed in %s seconds" % (time.time() - run_start_time))