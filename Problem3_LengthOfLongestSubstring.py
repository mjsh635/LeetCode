"""3. Longest Substring Without Repeating Characters
Medium
Topics
Companies
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
"""
# solution one, avg of 67ms, provides the substring and the length
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substring = []
        for char in list(s): #iterate through a list of characters that are in the string
            if substring.count(char) == 0: # if char is not in the list add it
                substring.append(char) 
                longest = max(len(substring,longest)) #update the longest seen substring
            else:                    
                #if the char exist in the string, delete from the start of substring until
                #the first occurance of the character, then add the char to the end of the
                #substring.
                del substring[0:substring.index(char) + 1] 
                substring.append(char)
                pass          
        return longest 
    

