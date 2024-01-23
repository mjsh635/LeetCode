"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        

"""

class Solution:
    def isValid(self, s: str) -> bool:
        # take s and split it into a char array
        # iterate over the array and when i see an open bracket add it to the stack
        # when i see a close bracket compare it to the top of stack,
            # if they match pop that element
            # if they dont match return false
        # after iterating over all values, if len(stack) != 0, return false, else return true
        stack = []
        openB = {'(' : ')', 
                 '[' : ']', 
                 '{' : '}'}
        closeB = {
                 ')' : '(',
                 ']' : '[',
                 '}' : '{'
                 }
        for bracket in list(s):
            if bracket in openB:
                stack.append(bracket)
            else:
                if stack and stack[-1] == closeB.get(bracket):
                    stack.pop()
                else:
                    return False
        return not bool(stack)


s = Solution()


assert(s.isValid("]") == False)