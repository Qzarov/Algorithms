'''
Leetcode #20 https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

'''
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

'''
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
'''

import time

def solve(s: str) -> bool:
    stack = []
    for b in s:
        if b in ['(', '[', '{']:
            stack.append(b)
        else:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if opening_bracket == '(' and b != ')':
                return False
            elif opening_bracket == '[' and b != ']':
                return False
            elif opening_bracket == '{' and b != '}':
                return False
    if stack:
        return False  # unbalanced parentheses
    return True
            
def run():
    start_time = time.time()
    res = solve("()")
    print('1. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == True
    
    start_time = time.time()
    res = solve("()[]{}")
    print('2. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    assert res == True
    
    start_time = time.time()
    res = solve("(]")
    assert res == False
    print('3. res:', res, 'executed in %s seconds' % (time.time() - start_time))
    
print('Start.')
start_time = time.time()
run()
print("End. run() executed in %s seconds" % (time.time() - start_time))