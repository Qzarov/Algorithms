'''
Leetcode #1 https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

'''
Leetcode #1 https://leetcode.com/problems/two-sum/

Дан массив целых чисел и целочисленная цель target.
Вернуть индексы двух чисел массива таких, чтобы их сумма была равна target

Предполагается, что каждый набор входных данных имеет ровно одно решение,
один и тот же элемент нельзя использовать дважды.

Продолжение: Можете ли вы предложить алгоритм, который был бы менее 
сложным по времени, чем O(n2)?
'''

'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-10^9 <= nums[i] <= 10^9
-10^9 <= target  <= 10^9
Only one valid answer exists.
'''

import time

# Using the Brude force, complexity is O(n^2)
def solve_slow(arr: list, target: int): # 35 ms in leetcode
    for i in range(len(arr)):
        el = arr[i]
        if target - el in arr:
            if not i == arr.index(target - el):
                return [i, arr.index(target - el)]
    return []

# Using HashMap, complexity is O(n)
def solve(arr: list, target: int): # 43 ms in leetcode
    numbers = {} # value: index
    for i in range(len(arr)):
        delta = target - arr[i]
        if delta.get(numbers):
            return [numbers[delta], i]
        else:
            numbers[arr[i]] = i
        

def run():
    start_time = time.time()
    res = solve([2,7,11,15], 9)
    assert 0 in res and 1 in res
    print('1. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    
    start_time = time.time()
    res = solve([3,2,4], 6)
    assert 1 in res and 2 in res
    print('2. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    
    start_time = time.time()
    res = solve([3,3], 6)
    assert 0 in res and 1 in res
    print('3. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    
    start_time = time.time()
    res = solve(range(1, 10000000), 10000000)
    assert 4999998 in res and 5000000 in res
    print('4. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    
print('Start.')
start_time = time.time()
run()
print("End. run() executed in %s seconds" % (time.time() - start_time))